import csv
import hashlib
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests
from defusedxml.ElementTree import fromstring


class DocumentDownloader:
    DOCUMENT_FIELDS = ('title', 'description', 'source_url', 'document_url')
    QUEUE_FIELDS = ('crawl_id', *DOCUMENT_FIELDS, 'attempts', 'last_error', 'last_attempt')
    LOG_FIELDS = ('timestamp', 'crawl_id', *DOCUMENT_FIELDS, 'final_url', 'file_path', 'sha256',
                  'size_bytes', 'status', 'error')
    RETRY_STATUS = {408, 425, 429, 500, 502, 503, 504}

    def __init__(self, output_dir='documents', max_size_mb=50, max_attempts=3, retry_delay=2, pause=1):
        if max_attempts < 1 or min(retry_delay, pause) < 0 or max_size_mb <= 0:
            raise ValueError('Invalid download configuration')
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.log_path = Path('documents.csv')
        self.queue_path = Path('queue.csv')
        self.max_size = max_size_mb * 1024 * 1024
        self.max_attempts, self.retry_delay, self.pause = max_attempts, retry_delay, pause
        self.headers = {'User-Agent': 'KI-Crawler/1.0', 'Accept': 'application/pdf,*/*;q=0.8'}

    @staticmethod
    def _now():
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

    @staticmethod
    def _read(path):
        path = Path(path)
        if not path.exists():
            return []
        with path.open(newline='', encoding='utf-8-sig') as file:
            return list(csv.DictReader(file))

    def _save_queue(self, rows):
        temp = self.queue_path.with_suffix('.tmp')
        with temp.open('w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.QUEUE_FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        temp.replace(self.queue_path)

    @staticmethod
    def _key(row):
        return row.get('crawl_id') or '', row['document_url']

    def enqueue(self, documents, crawl_id=None):
        rows = self._read(self.queue_path)
        keys = {self._key(row) for row in rows}
        for document in documents:
            row = {'crawl_id': crawl_id or '', **{key: document[key] for key in self.DOCUMENT_FIELDS},
                   'attempts': 0, 'last_error': '', 'last_attempt': ''}
            if self._key(row) not in keys:
                rows.append(row)
                keys.add(self._key(row))
        self._save_queue(rows)

    def import_failed(self, log_path=None):
        # Only import the latest status per crawl and URL. Existing queue metadata is preserved.
        latest = {self._key(row): row for row in self._read(Path(log_path) if log_path else self.log_path)}
        rows = self._read(self.queue_path)
        keys = {self._key(row) for row in rows}
        count = 0
        for key, row in latest.items():
            if row['status'] == 'failed' and key not in keys:
                rows.append({'crawl_id': row['crawl_id'], **{k: row[k] for k in self.DOCUMENT_FIELDS},
                             'attempts': 0, 'last_error': row['error'], 'last_attempt': row['timestamp']})
                count += 1
        self._save_queue(rows)
        return count

    def _fetch(self, document):
        url = document['document_url']
        file_type = document['file_type']

        if urlparse(url).scheme not in ('http', 'https') or not urlparse(url).hostname:
            raise ValueError('Invalid HTTP URL')

        with requests.get(url, headers=self.headers, timeout=(10, 60), stream=True) as response:
            response.raise_for_status()
            content = bytearray()
            for chunk in response.iter_content(chunk_size=65536):
                content.extend(chunk)
                if len(content) > self.max_size:
                    raise ValueError('Maximum file size exceeded')
            final_url = response.url

        if file_type == "pdf":
            if not content.startswith(b"%PDF-"):
                raise ValueError("Keine PDF-Datei")

        elif file_type == "xml":
            root = fromstring(bytes(content))

            if root.tag.split("}")[-1].lower() == "html":
                raise ValueError("HTML statt XML-Dokument erhalten")

        else:
            raise ValueError(f"Nicht unterstützter Dateityp: {file_type}")

        file_hash = hashlib.sha256(content).hexdigest()
        existing = next(self.output_dir.glob(f'*_{file_hash}.pdf'), None)
        if existing:
            return existing, file_hash, len(content), final_url, 'duplicate'
        title = re.sub(r'[^\w\- ]', '', document['title']).strip()
        title = re.sub(r'\s+', '_', title)[:80] or 'document'
        path = self.output_dir / f'{title}_{file_hash}.pdf'
        temp = path.with_suffix('.part')
        try:
            temp.write_bytes(content)
            temp.replace(path)
        finally:
            temp.unlink(missing_ok=True)
        return path, file_hash, len(content), final_url, 'success'

    def _log(self, document, status, error='', result=None):
        path, file_hash, size, final_url, _ = result or (None, None, None, None, None)
        row = {'timestamp': self._now(), 'crawl_id': document['crawl_id'],
               **{key: document[key] for key in self.DOCUMENT_FIELDS}, 'final_url': final_url,
               'file_path': str(path) if path else None, 'sha256': file_hash, 'size_bytes': size,
               'status': status, 'error': error}
        write_header = not self.log_path.exists() or self.log_path.stat().st_size == 0
        with self.log_path.open('a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.LOG_FIELDS)
            if write_header:
                writer.writeheader()
            writer.writerow(row)

    def process_queue(self, crawl_id=None):
        rows = self._read(self.queue_path)
        pending = [row for row in rows if crawl_id is None or row['crawl_id'] == crawl_id]
        results = {'success': 0, 'duplicate': 0, 'failed': 0}
        for index, row in enumerate(pending):
            if index:
                time.sleep(self.pause)
            for attempt in range(self.max_attempts):
                row['attempts'] = int(row['attempts']) + 1
                row['last_attempt'] = self._now()
                self._save_queue(rows)
                try:
                    result = self._fetch(row)
                except (requests.RequestException, ValueError, OSError) as exc:
                    row['last_error'] = str(exc)
                    self._save_queue(rows)
                    retry = isinstance(exc, (requests.ConnectionError, requests.Timeout,
                                             requests.exceptions.ChunkedEncodingError))
                    delay = self.retry_delay * 2 ** attempt
                    if isinstance(exc, requests.HTTPError) and exc.response is not None:
                        retry = exc.response.status_code in self.RETRY_STATUS
                        retry_after = exc.response.headers.get('Retry-After', '')
                        if retry_after.isdigit():
                            delay = max(delay, int(retry_after))
                        elif retry_after:
                            # Defer HTTP-date Retry-After to a later manual run.
                            retry = False
                    if retry and attempt + 1 < self.max_attempts and delay <= 60:
                        time.sleep(delay)
                        continue
                    self._log(row, 'failed', str(exc))
                    results['failed'] += 1
                    break
                else:
                    self._log(row, result[-1], result=result)
                    rows.remove(row)
                    self._save_queue(rows)
                    results[result[-1]] += 1
                    break
        return results

