# KI-Crawler – Zentrale Moduldokumentation

**Geltungsbereich:** konsolidierter lokaler Python-Quellstand vom 27. November 2026. Ablage: `MODULES.md` im Repository-Hauptverzeichnis neben `README.md`.

Die [README](README.md) beschreibt Architektur, Betrieb, Installation und Roadmap. Diese Referenz beschreibt die tatsächlichen Module und ihre Schnittstellen auf Implementierungsebene. Alle eigenen Python-Dateien unter `src/crawler/` und `src/tests/` sind enthalten, auch private Methoden, Properties und lokal definierte Callbacks. Bei der Definition enthaltene Testfälle sind beschrieben, aber nicht erneut ausgeführt. Die Definitionen wurden statisch aus dem Quelltext inventarisiert; die fachlichen Beschreibungen der Produktivfunktionen wurden anhand des implementierten Verhaltens formuliert. Signaturen, Rückgabeausdrücke, explizite Exceptions, Aufrufbeispiele und Testassertionen werden direkt aus dem AST übernommen. Sie sind Navigationshilfe, keine vollständige dynamische Kontrollflussanalyse oder Typgarantie.

**Umfang:** 48 Module, 51 Klassendefinitionen, 528 Funktions-/Methodendefinitionen, darunter 195 namentlich definierte `test_*`-Funktionen (einschließlich absichtlich fehlschlagender Runner-Selbsttests). Python-Standardbibliothek und externe Abhängigkeiten werden nicht als eigene Module dokumentiert.

## Lese- und Pflegehinweise

- Die Signatur ist dem aktuellen Quellstand entnommen. `async def` kennzeichnet awaitbare Schnittstellen; Dekoratoren kennzeichnen Properties, statische Methoden oder Klassenmethoden. Nicht öffentliche Helfer sind keine stabilen externen APIs.
- Angaben unter „Rückgabe“ zeigen die im Funktionskörper gefundenen expliziten Ausdrücke (ggf. gekürzt), nicht sämtliche möglichen Laufzeitergebnisse. Ohne explizite Rückgabe erfolgt regulär `None`; Generatoren/Contextmanager werden gesondert gekennzeichnet.
- „Explizite Fehler“ nennt im Körper formulierte raise-Ausdrücke; aufgerufene Bibliotheken und I/O können weitere Ausnahmen auslösen. Verweise auf Aufrufe sind ausgewählte statische Aufrufstellen, keine vollständige Seiteneffektanalyse.
- Tests dokumentieren Prüfabsicht, Assertions und lokale Fixtures; sie sind kein Nachweis, dass die gesamte Suite gerade bestanden hat. Historische Fixtures müssen teilweise explizit bereitgestellt werden.
- Neue/änderte Module, Klassen und Funktionen werden im selben Commit nachgeführt. Normale Code-Kommentare bleiben erlaubt. Keine großen Dokumentationsblöcke im Code und keine einzelne Markdown-Datei pro Modul.
- Web Search bleibt im beschriebenen Legacy-Code vorhanden, gehört aber nicht mehr zur Zielarchitektur (Company-Policy). Historische Kosten bleiben erhalten. Die Dokumentation autorisiert keine Ausführung des Legacy-Piloten.

## Modulverzeichnis

### Produktivmodule und CLIs

- [AsyncStrategyExecutor.py](#crawler-asyncstrategyexecutor) – C-07, C-09, D-02, E-02, E-03
- [BenchmarkAnalyzer.py](#crawler-benchmarkanalyzer) – G-02, B-01
- [BrowserUse.py](#crawler-browseruse) – C-02, C-04
- [CrawlCheckpoint.py](#crawler-crawlcheckpoint) – H-01, H-03
- [DocumentDownloader.py](#crawler-documentdownloader) – E-01
- [ErrorClassifier.py](#crawler-errorclassifier) – F-01
- [ExecutionPolicy.py](#crawler-executionpolicy) – C-07, C-08, C-09
- [FullCrawl.py](#crawler-fullcrawl) – C-09, H-01, F-05
- [OpenAIClient.py](#crawler-openaiclient) – A-01, B-01, C-04, C-08
- [PaginationValidator.py](#crawler-paginationvalidator) – F-03, F-04
- [ProjectPaths.py](#crawler-projectpaths) – H-02
- [RecoveryManager.py](#crawler-recoverymanager) – C-08, F-01
- [ResumePlanner.py](#crawler-resumeplanner) – H-03
- [StrategyExecutor.py](#crawler-strategyexecutor) – C-06, D-02, E-02, C-09
- [StrategyRepair.py](#crawler-strategyrepair) – C-08
- [StrategySchema.py](#crawler-strategyschema) – C-03, C-09, D-02, E-02
- [StrategyStore.py](#crawler-strategystore) – C-05, F-02
- [StrategyValidator.py](#crawler-strategyvalidator) – F-02
- [StructureVerifier.py](#crawler-structureverifier) – C-08, F-01
- [crawler.py](#crawler-crawler) – A-01, D-01, E-01
- [main_benchmark.py](#crawler-main-benchmark) – G-02
- [main_browser.py](#crawler-main-browser) – C-02, D-01, E-02
- [main_checkpoint.py](#crawler-main-checkpoint) – H-01
- [main_discovery.py](#crawler-main-discovery) – C-04, C-05
- [main_execute.py](#crawler-main-execute) – C-06
- [main_execute_async.py](#crawler-main-execute-async) – C-07, C-09, H-01
- [main_migrate_results.py](#crawler-main-migrate-results) – H-02
- [main_recovery.py](#crawler-main-recovery) – C-08
- [main_strategy.py](#crawler-main-strategy) – F-02, F-03, H-03
- [retry_downloads.py](#crawler-retry-downloads) – E-01

### Testmodule und Runner

- [TestRunner.py](#tests-testrunner) – F-07
- [main_tests.py](#tests-main-tests) – F-07
- [test_benchmark.py](#tests-test-benchmark) – G-02
- [test_checkpoint.py](#tests-test-checkpoint) – H-01
- [test_error_classifier.py](#tests-test-error-classifier) – F-01
- [test_full_crawl.py](#tests-test-full-crawl) – C-09, H-01, F-05
- [test_legacy_paths.py](#tests-test-legacy-paths) – H-02, B-01
- [test_pagination.py](#tests-test-pagination) – C-09
- [test_pagination_links.py](#tests-test-pagination-links) – C-09
- [test_pagination_validation.py](#tests-test-pagination-validation) – F-03
- [test_project_paths.py](#tests-test-project-paths) – H-02, G-02
- [test_recovery_manager.py](#tests-test-recovery-manager) – C-08, F-01
- [test_state_menu.py](#tests-test-state-menu) – C-06, C-07
- [test_strategy_executor.py](#tests-test-strategy-executor) – C-06, D-02, E-02
- [test_strategy_store.py](#tests-test-strategy-store) – C-05
- [test_strategy_validation.py](#tests-test-strategy-validation) – F-02, H-03
- [test_test_runner.py](#tests-test-test-runner) – F-07
- [test_worker_pool.py](#tests-test-worker-pool) – C-07, E-03

## Produktivmodule

## crawler-asyncstrategyexecutor

**Modul:** [`src/crawler/AsyncStrategyExecutor.py`](src/crawler/AsyncStrategyExecutor.py)  
**Features/Storys:** C-07, C-09, D-02, E-02, E-03  
**Aufgabe und Abgrenzung:** Asynchroner deterministischer Executor auf Basis des synchronen Strategie- und Dateivertrags. Ein Browserkontext, zentrale Ergebnistab und optionale Worker-Tabs. Fehler beenden die Ausgabe neuer Jobs; laufende Jobs können noch enden. Kein LLM. Derzeit strikte Seitenidentität, Downloadpacing und konservativer Abbruch.

**Direkte Abhängigkeiten:** `import asyncio`; `import time`; `from collections import deque`; `from pathlib import Path`; `from ProjectPaths import BROWSER_TIMING_FILE`; `from urllib.parse import urljoin, urlsplit`; `from uuid import uuid4`; `from playwright.async_api import async_playwright, Error as PlaywrightError, TimeoutError as PlaywrightTimeoutError`; `from ErrorClassifier import attach_error_classification`; `from ExecutionPolicy import get_policy, has_policy`; `from BrowserUse import allowed_url, measure, write_timings`; `from StrategyExecutor import StrategyExecutor, ExecutionError, NavigationInterrupted`.

**Definitionen:** 2 Klassen, 48 Funktionen/Methoden (inkl. lokaler Definitionen).

### Klasse `ServerResponseError`

**Quellcode:** [AsyncStrategyExecutor.py:17–20](src/crawler/AsyncStrategyExecutor.py#L17-L20).

**Aufgabe:** ExecutionError mit strukturiertem 5xx-Nachweis für den aktiven Tab.

**Basisklassen:** `ExecutionError`.

#### `ServerResponseError.__init__`

**Quellcode:** [AsyncStrategyExecutor.py:18–20](src/crawler/AsyncStrategyExecutor.py#L18-L20).

```python
def __init__(self, evidence):
```

**Aufgabe:** Initialisiert ExecutionError mit Serverstatus und speichert strukturierten Nachweis in evidence.

**Parameter:** `evidence`: beobachtete Hinweise/Fehlernachweis. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.evidence`.

### Klasse `AsyncStrategyExecutor`

**Quellcode:** [AsyncStrategyExecutor.py:23–899](src/crawler/AsyncStrategyExecutor.py#L23-L899).

**Aufgabe:** Asynchrone Spezialisierung des synchronen Executors mit eigenem Browser-I/O, gemeinsamer Zugriffssperre, Worker-Pool und Ereignisdiagnostik.

**Basisklassen:** `StrategyExecutor`.

**Klassenattribute / Konfiguration:**

- `MIN_DOCUMENT_INTERVAL_SECONDS = 0.25`

#### `AsyncStrategyExecutor.__init__`

**Quellcode:** [AsyncStrategyExecutor.py:28–40](src/crawler/AsyncStrategyExecutor.py#L28-L40).

```python
def __init__(self, *args, download_timeout_ms=30000, **kwargs):
```

**Aufgabe:** Initialisiert den geerbten Strategie-/Feldvertrag, asynchronen Download-Timeout, gemeinsamen Sperrzustand, Workerstatistiken und Downloadpacing.

**Parameter:** `download_timeout_ms`: Wartebudget auf Downloadereignis in Millisekunden; `args`: weitergereichte Positionsparameter; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.access_state`, `self.failure_stage`, `self.worker_count`, `self.worker_tabs_opened`, `self.worker_jobs`, `self.worker_failures`, `self.download_timeout_ms`, `self.pool_batches`, `self.max_parallel_jobs`, `self._running_jobs`, `self._last_document_finished_at`.

#### `AsyncStrategyExecutor.blocked`

**Quellcode:** [AsyncStrategyExecutor.py:43–44](src/crawler/AsyncStrategyExecutor.py#L43-L44).

```python
@property
def blocked(self):
```

**Aufgabe:** Liest die gemeinsame Zugriffssperre aus access_state.

**Rückgabe (Ausdrücke im Code):** `self.access_state['blocked']`.

#### `AsyncStrategyExecutor.blocked.setter`

**Quellcode:** [AsyncStrategyExecutor.py:47–48](src/crawler/AsyncStrategyExecutor.py#L47-L48).

```python
@blocked.setter
def blocked(self, value):
```

**Aufgabe:** Schreibt die gemeinsame Zugriffssperre in access_state; alle Worker können den Zustand sehen.

**Parameter:** `value`: übergebener Wert gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

#### `AsyncStrategyExecutor._install_cookie_handler`

**Quellcode:** [AsyncStrategyExecutor.py:50–56](src/crawler/AsyncStrategyExecutor.py#L50-L56).

```python
async def _install_cookie_handler(self):
```

**Aufgabe:** Installiert asynchronen Locator-Handler pro Tab für konfigurierte Cookie-Behandlung.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.cookie_handler_page`.

**Relevante Aufrufe:** `self._cookie_button`, `self._cookie_locator`, `self.page.add_locator_handler`.

#### `AsyncStrategyExecutor._install_cookie_handler.handle`

**Quellcode:** [AsyncStrategyExecutor.py:53–54](src/crawler/AsyncStrategyExecutor.py#L53-L54).

```python
async def handle():
```

**Aufgabe:** Lokaler asynchroner Cookie-Callback; delegiert an _handle_cookie_dialog.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self._handle_cookie_dialog`.

#### `AsyncStrategyExecutor._page_signature`

**Quellcode:** [AsyncStrategyExecutor.py:58–59](src/crawler/AsyncStrategyExecutor.py#L58-L59).

```python
async def _page_signature(self, rows):
```

**Aufgabe:** Extrahiert geordnete Datensatzschlüssel asynchron für die gesamte Seite.

**Parameter:** `rows`: Locator/Sequenz der Ergebniszeilen. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `tuple([self._key(await self._record(rows.nth(i), keys_only=True)) for i in range(await rows.count())])`.

**Relevante Aufrufe:** `self._key`, `self._record`.

#### `AsyncStrategyExecutor._check_access`

**Quellcode:** [AsyncStrategyExecutor.py:61–71](src/crawler/AsyncStrategyExecutor.py#L61-L71).

```python
async def _check_access(self):
```

**Aufgabe:** Prüft gemeinsamen Sperrzustand, erlaubte URL und sichtbare Zugriffssignale asynchron.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ExecutionError(self.blocked)`
- `ExecutionError('Page outside allowed domain')`
- `ExecutionError('Possible security challenge; stop')`
- `ExecutionError('Possible access restriction; stop')`

**Relevante Aufrufe:** `self.page.locator`, `self.page.title`.

#### `AsyncStrategyExecutor._unique`

**Quellcode:** [AsyncStrategyExecutor.py:73–79](src/crawler/AsyncStrategyExecutor.py#L73-L79).

```python
async def _unique(self, locator, label, wait=False):
```

**Aufgabe:** Wartet optional auf Sichtbarkeit und verlangt genau einen sichtbaren Locator.

**Parameter:** `locator`: Playwright-Locator oder Locator-Regel gemäß Kontext; `label`: Bezeichnung für Diagnose/Fehlermeldung; `wait`: Wartebedingung bzw. Schalter für Sichtbarkeitsprüfung. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `locator`.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'{label}: expected one visible match, found {count}')`

**Relevante Aufrufe:** `self._wait_visible`.

#### `AsyncStrategyExecutor._wait`

**Quellcode:** [AsyncStrategyExecutor.py:81–92](src/crawler/AsyncStrategyExecutor.py#L81-L92).

```python
async def _wait(self, wait):
```

**Aufgabe:** Wartet asynchron auf die spezifizierte Postcondition und misst Dauer.

**Parameter:** `wait`: Wartebedingung bzw. Schalter für Sichtbarkeitsprüfung. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Relevante Aufrufe:** `self._check_access`, `self._wait_visible`, `self.locator`.

#### `AsyncStrategyExecutor._cookie_pending`

**Quellcode:** [AsyncStrategyExecutor.py:94–95](src/crawler/AsyncStrategyExecutor.py#L94-L95).

```python
async def _cookie_pending(self, dialog):
```

**Aufgabe:** Prüft asynchron sichtbaren Cookie-Dialog bzw. dessen Aktion.

**Parameter:** `dialog`: Cookie-Dialog-Locator. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `bool(await dialog.filter(visible=True).count() or await self._cookie_button(dialog).filter(visible=True).count())`.

**Relevante Aufrufe:** `self._cookie_button`, `self._cookie_button(dialog).filter`.

#### `AsyncStrategyExecutor._handle_cookie_dialog`

**Quellcode:** [AsyncStrategyExecutor.py:97–123](src/crawler/AsyncStrategyExecutor.py#L97-L123).

```python
async def _handle_cookie_dialog(self, from_handler=False):
```

**Aufgabe:** Behandelt nur konfigurierte notwendige Cookie-Option und prüft Abschluss; aktualisiert Diagnosezähler.

**Parameter:** `from_handler`: Aufruf durch Locator-Handler. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Cookie dialog repeatedly reappeared; stop')`
- `ExecutionError('Cookie dialog: expected exactly one matching dialog')`

**Direkt gesetzter Zustand:** `self.cookie_handler_page`, `self.cookie_dialog_count`.

**Relevante Aufrufe:** `self._check_access`, `self._cookie_button`, `self._cookie_locator`, `self._cookie_pending`, `self._install_cookie_handler`, `self._unique`, `self.page.remove_locator_handler`.

#### `AsyncStrategyExecutor._wait_visible`

**Quellcode:** [AsyncStrategyExecutor.py:125–144](src/crawler/AsyncStrategyExecutor.py#L125-L144).

```python
async def _wait_visible(self, locator):
```

**Aufgabe:** Begrenzt asynchrones Warten auf eindeutiges sichtbares Ziel unter Zugriff-/Cookie-Prüfung.

**Parameter:** `locator`: Playwright-Locator oder Locator-Regel gemäß Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'Timed out waiting for target: {locator}')`

**Relevante Aufrufe:** `self._check_access`, `self._check_navigation_context`, `self._cookie_locator`, `self._cookie_pending`, `self._handle_cookie_dialog`, `self.page.wait_for_timeout`.

#### `AsyncStrategyExecutor._cookie_diagnostics`

**Quellcode:** [AsyncStrategyExecutor.py:146–153](src/crawler/AsyncStrategyExecutor.py#L146-L153).

```python
async def _cookie_diagnostics(self):
```

**Aufgabe:** Sammelt Cookie-Status und Zähler für die Fehlerdiagnose.

**Rückgabe (Ausdrücke im Code):** `None`; `{'handled_count': self.cookie_dialog_count, 'dialog_matches': await dialog.count(), 'dialog_visible_matches': await dialog.filter(visible=True).count(), 'button_matches': await button.count…`.

**Relevante Aufrufe:** `self._cookie_button`, `self._cookie_locator`.

#### `AsyncStrategyExecutor._navigate`

**Quellcode:** [AsyncStrategyExecutor.py:155–180](src/crawler/AsyncStrategyExecutor.py#L155-L180).

```python
async def _navigate(self, start_url=None):
```

**Aufgabe:** Startet asynchrone Suchnavigation und höchstens einen Cookie-bedingten Neustart im selben Kontext.

**Parameter:** `start_url`: Start-URL der Suche. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Explizite Fehler / Abbruch:**

- `erneutes Auslösen der aktuellen Exception`
- `ExecutionError('Cookie dialog interrupted navigation again after restart; stop')`

**Direkt gesetzter Zustand:** `self.navigation_cookie_baseline`, `self.navigation_restarts`.

**Relevante Aufrufe:** `self._check_access`, `self._handle_cookie_dialog`, `self._install_cookie_handler`, `self._navigate_once`, `self.page.goto`.

#### `AsyncStrategyExecutor._menu_state`

**Quellcode:** [AsyncStrategyExecutor.py:182–187](src/crawler/AsyncStrategyExecutor.py#L182-L187).

```python
async def _menu_state(self, target, following):
```

**Aufgabe:** Liest aria-expanded und sichtbare Folgeelemente asynchron.

**Parameter:** `target`: konkretes Zielobjekt bzw. Locator; `following`: erwartetes Folgeelement. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(expanded, await following.filter(visible=True).count())`.

**Relevante Aufrufe:** `self._check_access`, `self._check_navigation_context`, `self._handle_cookie_dialog`, `target.get_attribute`.

#### `AsyncStrategyExecutor._wait_menu`

**Quellcode:** [AsyncStrategyExecutor.py:189–200](src/crawler/AsyncStrategyExecutor.py#L189-L200).

```python
async def _wait_menu(self, target, following, timeout_ms):
```

**Aufgabe:** Pollt die Menü-Postcondition bis zum Timeout.

**Parameter:** `target`: konkretes Zielobjekt bzw. Locator; `following`: erwartetes Folgeelement; `timeout_ms`: Wartebudget in Millisekunden. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(True, expanded, matches)`; `(False, expanded, matches)`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Menu postcondition is ambiguous')`

**Relevante Aufrufe:** `self._menu_state`, `self.page.wait_for_timeout`.

#### `AsyncStrategyExecutor._open_menu`

**Quellcode:** [AsyncStrategyExecutor.py:202–246](src/crawler/AsyncStrategyExecutor.py#L202-L246).

```python
async def _open_menu(self, target, following, name):
```

**Aufgabe:** Öffnet das Menü nur bei Bedarf; bestätigt Folgeelemente mit begrenztem Retry.

**Parameter:** `target`: konkretes Zielobjekt bzw. Locator; `following`: erwartetes Folgeelement; `name`: Name des Felds/Controls gemäß Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Menu postcondition is ambiguous')`
- `ExecutionError(f'Menu postcondition not met: {name}')`

**Direkt gesetzter Zustand:** `self.menu_retries`.

**Relevante Aufrufe:** `self._check_navigation_context`, `self._menu_state`, `self._unique`, `self._wait_menu`, `target.click`, `target.is_visible`.

#### `AsyncStrategyExecutor._close_state_menu`

**Quellcode:** [AsyncStrategyExecutor.py:248–287](src/crawler/AsyncStrategyExecutor.py#L248-L287).

```python
async def _close_state_menu(self, spec, selected):
```

**Aufgabe:** Schließt bekannte Bundesländer-Menüs kontrolliert und prüft gewählte Option soweit verfügbar.

**Parameter:** `spec`: Locator-, Dokument- oder Regeldefinition; `selected`: vorher ausgewählte Option. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Menu postcondition not met: Bundesländer selection before close')`
- `ExecutionError('Menu postcondition not met: Bundesländer selection lost')`
- `ExecutionError('Menu postcondition not met: Bundesländer close')`

**Relevante Aufrufe:** `self._check_access`, `self._check_navigation_context`, `self._handle_cookie_dialog`, `self._unique`, `self.locator`, `self.page.get_by_role`, `self.page.wait_for_timeout`.

#### `AsyncStrategyExecutor._navigate_once`

**Quellcode:** [AsyncStrategyExecutor.py:289–343](src/crawler/AsyncStrategyExecutor.py#L289-L343).

```python
async def _navigate_once(self):
```

**Aufgabe:** Führt die Strategieaktionen in ihrer Reihenfolge asynchron aus; prüft Navigation, Parameter und Zustände.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Download control not allowed during navigation')`
- `ExecutionError('Menu opener requires a following action')`
- `ExecutionError('Configured menu must precede a checkbox or option selection')`
- `ExecutionError('Unsupported input type')`

**Direkt gesetzter Zustand:** `self.failure_stage`, `self.step`.

**Relevante Aufrufe:** `self._check_access`, `self._check_navigation_context`, `self._close_state_menu`, `self._handle_cookie_dialog`, `self._open_menu`, `self._state_menu_to_close`, `self._unique`, `self._wait`, `self._wait_visible`, `self.locator`, `target.click`, `target.fill`, `target.get_attribute`, `target.select_option`.

#### `AsyncStrategyExecutor._rows`

**Quellcode:** [AsyncStrategyExecutor.py:345–349](src/crawler/AsyncStrategyExecutor.py#L345-L349).

```python
async def _rows(self):
```

**Aufgabe:** Liefert die Ergebniszeilen relativ zum eindeutigen Container.

**Rückgabe (Ausdrücke im Code):** `self.locator(root, self.records['row'])`.

**Relevante Aufrufe:** `self._unique`, `self.locator`.

#### `AsyncStrategyExecutor._field`

**Quellcode:** [AsyncStrategyExecutor.py:351–386](src/crawler/AsyncStrategyExecutor.py#L351-L386).

```python
async def _field(self, row, field):
```

**Aufgabe:** Asynchrone Extraktion eines Feldes mit Scope-/Regex-/Pflichtfeldregeln.

**Parameter:** `row`: Locator bzw. Datensatzzeile im aktuellen Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `value`.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'{name}: no value')`
- `ExecutionError(f'{name}: regex input too long')`
- `ExecutionError(f'{name}: regex did not produce one unambiguous value')`
- `ExecutionError(f'{name}: empty value')`

**Relevante Aufrufe:** `self._unique`, `self.locator`, `self.page.locator`, `self.patterns[name].finditer`, `target.and_`, `target.get_attribute`, `target.inner_text`.

#### `AsyncStrategyExecutor._record`

**Quellcode:** [AsyncStrategyExecutor.py:388–405](src/crawler/AsyncStrategyExecutor.py#L388-L405).

```python
async def _record(self, row, keys_only=False):
```

**Aufgabe:** Extrahiert alle Felder oder nur Schlüssel; prüft bei vollständigem Datensatz die erwarteten Filter.

**Parameter:** `row`: Locator bzw. Datensatzzeile im aktuellen Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `record`.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'Required field {name}: {exc}')`
- `ExecutionError(f'{name}: extracted value does not match requested filter')`

**Relevante Aufrufe:** `self._field`.

#### `AsyncStrategyExecutor._check_row`

**Quellcode:** [AsyncStrategyExecutor.py:407–409](src/crawler/AsyncStrategyExecutor.py#L407-L409).

```python
async def _check_row(self, row, record):
```

**Aufgabe:** Vergleicht den aktuellen Zeilenschlüssel mit dem erwarteten Datensatz.

**Parameter:** `row`: Locator bzw. Datensatzzeile im aktuellen Kontext; `record`: extrahierter Datensatz mit Schlüsselfeldern. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Row identity changed before or after document download')`

**Relevante Aufrufe:** `self._key`, `self._record`.

#### `AsyncStrategyExecutor._await_browser_download`

**Quellcode:** [AsyncStrategyExecutor.py:411–458](src/crawler/AsyncStrategyExecutor.py#L411-L458).

```python
async def _await_browser_download(self, target):
```

**Aufgabe:** Registriert Download- und Response-Listener im aktuellen Tab, klickt einmal und wartet auf Downloadereignis, Sperre, 5xx oder Timeout. Entfernt Listener im finally; kein erneuter Klick bei Ungewissheit.

**Parameter:** `target`: konkretes Zielobjekt bzw. Locator. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `received.result()`.

**Explizite Fehler / Abbruch:**

- `ExecutionError(self.blocked)`
- `ServerResponseError(server_error)`
- `erneutes Auslösen der aktuellen Exception`
- `PlaywrightTimeoutError(f'Download event not received within {self.download_timeout_ms} ms')`

**Relevante Aufrufe:** `asyncio.get_running_loop`, `asyncio.wait`, `self.page.on`, `self.page.remove_listener`, `target.click`.

#### `AsyncStrategyExecutor._await_browser_download.on_download`

**Quellcode:** [AsyncStrategyExecutor.py:418–420](src/crawler/AsyncStrategyExecutor.py#L418-L420).

```python
def on_download(download):
```

**Aufgabe:** Lokaler Listener setzt die Future auf das zuerst beobachtete Downloadobjekt.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

#### `AsyncStrategyExecutor._await_browser_download.on_response`

**Quellcode:** [AsyncStrategyExecutor.py:422–429](src/crawler/AsyncStrategyExecutor.py#L422-L429).

```python
def on_response(response):
```

**Aufgabe:** Lokaler Listener erfasst zulässige 5xx-Dokument-/XHR-/Fetch-Antworten im aktiven Wartefenster.

**Parameter:** `response`: API-/HTTP-Response-Objekt entsprechend Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self._diagnostic_url`.

#### `AsyncStrategyExecutor._download`

**Quellcode:** [AsyncStrategyExecutor.py:460–504](src/crawler/AsyncStrategyExecutor.py#L460-L504).

```python
async def _download(self, row, spec, result):
```

**Aufgabe:** Asynchroner Browser-/Linkdownload in .part; URL-/Status-/Größen-/Dateiprüfung wie synchroner Executor. Antwortbody wird aktuell vollständig gepuffert.

**Parameter:** `row`: Locator bzw. Datensatzzeile im aktuellen Kontext; `spec`: Locator-, Dokument- oder Regeldefinition; `result`: Ergebnis-/Statusobjekt. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Download URL outside allowed domains')`
- `ExecutionError('Document link has no href')`
- `ExecutionError('Document link outside allowed domains')`
- `ExecutionError(f'Document HTTP {response.status}')`
- `ExecutionError('Document size limit exceeded')`

**Relevante Aufrufe:** `response.body`, `response.dispose`, `self._await_browser_download`, `self._check_access`, `self._response`, `self._unique`, `self._validate_file`, `self.locator`, `self.output_dir.mkdir`, `target.get_attribute`, `temporary.replace`, `temporary.unlink`, `temporary.write_bytes`.

#### `AsyncStrategyExecutor._pagination_target`

**Quellcode:** [AsyncStrategyExecutor.py:506–525](src/crawler/AsyncStrategyExecutor.py#L506-L525).

```python
async def _pagination_target(self, pagination):
```

**Aufgabe:** Ermittelt Next-Control asynchron und akzeptiert nur nachweislich äquivalente doppelte Links.

**Parameter:** `pagination`: Paginierungsregel. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(None, 'missing')`; `(visible.first, states[0])`.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'Next-page control ambiguous ({count} visible matches); end of results not verified')`
- `ExecutionError(f'Next-page control ambiguous ({count} non-equivalent visible matches); end of results not verified')`

**Relevante Aufrufe:** `self._equivalent_pagination_links`, `self.locator`, `self.locator(self.page, pagination['next']).filter`.

#### `AsyncStrategyExecutor._pagination_ready`

**Quellcode:** [AsyncStrategyExecutor.py:527–542](src/crawler/AsyncStrategyExecutor.py#L527-L542).

```python
async def _pagination_ready(self):
```

**Aufgabe:** Prüft ohne Klick, ob weitergeblättert werden kann oder ein expliziter Endnachweis vorliegt.

**Rückgabe (Ausdrücke im Code):** `False`; `self._pagination_decision(pagination, next_state, marker_visible)`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Pagination end marker ambiguous; end of results not verified')`

**Direkt gesetzter Zustand:** `self.pagination_end_evidence`, `self._next_target`.

**Relevante Aufrufe:** `self._check_access`, `self._pagination_decision`, `self._pagination_target`, `self.locator`.

#### `AsyncStrategyExecutor._next_page`

**Quellcode:** [AsyncStrategyExecutor.py:544–574](src/crawler/AsyncStrategyExecutor.py#L544-L574).

```python
async def _next_page(self, previous):
```

**Aufgabe:** Klickt nach Endprüfung einmal, wartet auf stabile disjunkte neue Schlüssel; derzeit Fehler bei überlappenden Seiten.

**Parameter:** `previous`: Signatur der vorherigen Seite. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `False`; `True`.

**Explizite Fehler / Abbruch:**

- `erneutes Auslösen der aktuellen Exception`
- `ExecutionError('No verified change of page keys after pagination')`

**Direkt gesetzter Zustand:** `self.step`.

**Relevante Aufrufe:** `self._check_access`, `self._page_signature`, `self._pagination_ready`, `self._rows`, `self._wait`, `self.page.wait_for_timeout`, `self.seen.union`, `target.click`.

#### `AsyncStrategyExecutor._prepare_worker`

**Quellcode:** [AsyncStrategyExecutor.py:576–598](src/crawler/AsyncStrategyExecutor.py#L576-L598).

```python
async def _prepare_worker(self, page_url, signature):
```

**Aufgabe:** Erzeugt Tab im bestehenden Kontext, teilt Zugriffssperre und bestätigt identische Seitensignatur vor Arbeitsbeginn; schließt Tab bei Fehler.

**Parameter:** `page_url`: URL der aktuellen Ergebnisseite; `signature`: geordnete Seitensignatur aus Datensatzschlüsseln. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `worker`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Worker tab did not reproduce the result page keys; no batch started')`
- `erneutes Auslösen der aktuellen Exception`

**Direkt gesetzter Zustand:** `worker.access_state`, `worker.context`, `worker.page`, `self.worker_tabs_opened`.

**Relevante Aufrufe:** `self.context.new_page`, `worker._check_access`, `worker._handle_cookie_dialog`, `worker._install_cookie_handler`, `worker._page_signature`, `worker._rows`, `worker._wait_visible`, `worker.page.close`, `worker.page.goto`.

#### `AsyncStrategyExecutor._diagnostic_url`

**Quellcode:** [AsyncStrategyExecutor.py:601–608](src/crawler/AsyncStrategyExecutor.py#L601-L608).

```python
@staticmethod
def _diagnostic_url(url):
```

**Aufgabe:** Entfernt Query, Fragment, Zugangsdaten und Blob-ID aus Diagnose-URLs; begrenzt Länge.

**Parameter:** `url`: zu prüfende URL. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `'blob:'`; `parts.scheme + ':'`; `f"{parts.scheme}://{parts.hostname or ''}{parts.path}"[:300]`.

#### `AsyncStrategyExecutor._failure_details`

**Quellcode:** [AsyncStrategyExecutor.py:610–637](src/crawler/AsyncStrategyExecutor.py#L610-L637).

```python
async def _failure_details(self, worker, worker_id, record, step, exc, row, document_type, events):
```

**Aufgabe:** Sammelt begrenzten Fehlerkontext, Netzwerk-Ringpuffer, Zeilen-/Seiten-Snapshot und Notices noch vor Schließen des Tabs; keine neue Navigation.

**Parameter:** `worker`: Worker-Executor bzw. Testfehler; `worker_id`: Worker-Nummer; `record`: extrahierter Datensatz mit Schlüsselfeldern; `step`: Schrittnummer; `exc`: abgefangene Exception; `row`: Locator bzw. Datensatzzeile im aktuellen Kontext; `document_type`: fachlicher Dokumenttyp; `events`: Mess-/Diagnoseereignisse. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `details`.

**Relevante Aufrufe:** `self._diagnostic_url`, `self._key`, `worker.page.is_closed`, `worker.page.locator`, `worker.page.locator('body').aria_snapshot`.

#### `AsyncStrategyExecutor._before_document`

**Quellcode:** [AsyncStrategyExecutor.py:639–640](src/crawler/AsyncStrategyExecutor.py#L639-L640).

```python
def _before_document(self, record, result):
```

**Aufgabe:** Leerer Erweiterungshook vor Dokumentabruf; FullResultsExecutor überschreibt ihn für persistente Downloadabsicht.

**Parameter:** `record`: extrahierter Datensatz mit Schlüsselfeldern; `result`: Ergebnis-/Statusobjekt. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

#### `AsyncStrategyExecutor._after_document`

**Quellcode:** [AsyncStrategyExecutor.py:642–643](src/crawler/AsyncStrategyExecutor.py#L642-L643).

```python
def _after_document(self, record, result):
```

**Aufgabe:** Leerer Erweiterungshook nach Dokumentabruf; FullResultsExecutor persistiert dort das Ergebnis.

**Parameter:** `record`: extrahierter Datensatz mit Schlüsselfeldern; `result`: Ergebnis-/Statusobjekt. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

#### `AsyncStrategyExecutor._process_job`

**Quellcode:** [AsyncStrategyExecutor.py:645–743](src/crawler/AsyncStrategyExecutor.py#L645-L743).

```python
async def _process_job(self, worker, worker_id, job, stop):
```

**Aufgabe:** Verarbeitet die Dokumente eines Datensatzes sequentiell im Worker. Prüft Stop, Identität und Zugriff, hält Downloadabstand ein, sammelt Diagnose; bei Fehler keine neuen Jobs, keine automatische Wiederholung.

**Parameter:** `worker`: Worker-Executor bzw. Testfehler; `worker_id`: Worker-Nummer; `job`: Queue-Arbeitseintrag; `stop`: gemeinsames Stop-Signal. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Explizite Fehler / Abbruch:**

- `erneutes Auslösen der aktuellen Exception`

**Direkt gesetzter Zustand:** `worker.step`, `self._running_jobs`, `self.max_parallel_jobs`, `worker.download_attempts`, `worker._last_document_finished_at`.

**Relevante Aufrufe:** `asyncio.wait_for`, `self._after_document`, `self._before_document`, `self._failure_details`, `self._key`, `worker._check_access`, `worker._check_row`, `worker._download`, `worker._rows`, `worker.page.on`, `worker.page.remove_listener`.

#### `AsyncStrategyExecutor._process_job.log`

**Quellcode:** [AsyncStrategyExecutor.py:654–656](src/crawler/AsyncStrategyExecutor.py#L654-L656).

```python
def log(kind, url, **data):
```

**Aufgabe:** Lokaler Callback schreibt bereinigte Netzwerkereignisse mit relativer Zeit in begrenzten Ringpuffer.

**Parameter:** `url`: zu prüfende URL; `data`: zu verarbeitende Daten. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self._diagnostic_url`.

#### `AsyncStrategyExecutor._process_job.request_event`

**Quellcode:** [AsyncStrategyExecutor.py:658–659](src/crawler/AsyncStrategyExecutor.py#L658-L659).

```python
def request_event(request):
```

**Aufgabe:** Erfasst Request-Methode und Ressourcentyp im Ringpuffer.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

#### `AsyncStrategyExecutor._process_job.response_event`

**Quellcode:** [AsyncStrategyExecutor.py:661–663](src/crawler/AsyncStrategyExecutor.py#L661-L663).

```python
def response_event(response):
```

**Aufgabe:** Erfasst HTTP-Status, Methode und Ressourcentyp im Ringpuffer.

**Parameter:** `response`: API-/HTTP-Response-Objekt entsprechend Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

#### `AsyncStrategyExecutor._process_job.failed_event`

**Quellcode:** [AsyncStrategyExecutor.py:665–667](src/crawler/AsyncStrategyExecutor.py#L665-L667).

```python
def failed_event(request):
```

**Aufgabe:** Erfasst fehlgeschlagene Netzwerkrequests mit Fehlerhinweis.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

#### `AsyncStrategyExecutor._process_job.download_event`

**Quellcode:** [AsyncStrategyExecutor.py:669–670](src/crawler/AsyncStrategyExecutor.py#L669-L670).

```python
def download_event(download):
```

**Aufgabe:** Erfasst beobachtete Downloadereignisse für die Diagnose.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

#### `AsyncStrategyExecutor._pool`

**Quellcode:** [AsyncStrategyExecutor.py:745–784](src/crawler/AsyncStrategyExecutor.py#L745-L784).

```python
async def _pool(self, jobs, signature):
```

**Aufgabe:** Erstellt Queue und zulässige Worker-Tabs, verarbeitet Jobs und sammelt Fehler/Timings; schließt zusätzliche Tabs. Ein Fehler setzt gemeinsames Stop-Signal.

**Parameter:** `signature`: geordnete Seitensignatur aus Datensatzschlüsseln. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'Worker {worker_id}, job step {step}: {exc}')`

**Direkt gesetzter Zustand:** `self.pool_batches`, `self.step`, `self.download_attempts`.

**Relevante Aufrufe:** `asyncio.Event`, `asyncio.Queue`, `asyncio.gather`, `self._check_access`, `self._prepare_worker`, `worker.page.close`.

#### `AsyncStrategyExecutor._pool.consume`

**Quellcode:** [AsyncStrategyExecutor.py:758–770](src/crawler/AsyncStrategyExecutor.py#L758-L770).

```python
async def consume(worker, worker_id):
```

**Aufgabe:** Lokale Worker-Coroutine entnimmt Jobs bis Stop/Queue-Ende und ruft _process_job auf.

**Parameter:** `worker`: Worker-Executor bzw. Testfehler; `worker_id`: Worker-Nummer. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Relevante Aufrufe:** `self._process_job`.

#### `AsyncStrategyExecutor._collect`

**Quellcode:** [AsyncStrategyExecutor.py:786–827](src/crawler/AsyncStrategyExecutor.py#L786-L827).

```python
async def _collect(self, max_companies, max_pages, downloads):
```

**Aufgabe:** Begrenzte asynchrone Datensatzextraktion und optionaler Batchdownload mit Seitensignatur und Stop-Regeln.

**Parameter:** `max_companies`: Obergrenze für Datensätze; `max_pages`: Obergrenze für Ergebnisseiten; `downloads`: Dokumentdownload aktivieren. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `'empty_results'`; `'company_limit'`; `'page_limit'`; `self._pagination_stop_reason()`; `'limit'`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Duplicate record key; stop rather than repeat download')`
- `ExecutionError('Duplicate keys on result page; no batch started')`

**Direkt gesetzter Zustand:** `self.failure_stage`, `self.pages`, `self.step`.

**Relevante Aufrufe:** `self._check_access`, `self._key`, `self._next_page`, `self._page_signature`, `self._pagination_stop_reason`, `self._pool`, `self._record`, `self._rows`, `self._wait_visible`, `self.locator`, `self.locator(self.page, empty).first.is_visible`, `self.seen.add`.

#### `AsyncStrategyExecutor._check_run_limits`

**Quellcode:** [AsyncStrategyExecutor.py:829–831](src/crawler/AsyncStrategyExecutor.py#L829-L831).

```python
def _check_run_limits(self, max_companies, max_pages):
```

**Aufgabe:** Validiert Grenzen des normalen begrenzten Laufs; Vollmodus hat eigene Policy-Grenzen.

**Parameter:** `max_companies`: Obergrenze für Datensätze; `max_pages`: Obergrenze für Ergebnisseiten. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Invalid start URL or run limits')`

#### `AsyncStrategyExecutor.run`

**Quellcode:** [AsyncStrategyExecutor.py:833–899](src/crawler/AsyncStrategyExecutor.py#L833-L899).

```python
async def run(self, start_url, crawl_id, max_companies=1, max_pages=1, downloads=False, headless=False, timing_path=BROWSER_TIMING_FILE, executable_path=None, workers=1, parallel_authorized=False):
```

**Aufgabe:** Öffentliche asynchrone Ausführung mit Browserkontext, Workerparametern, Timing und Report; Zugriffsschutz und Cleanup. Keine KI-Aufrufe.

**Parameter:** `start_url`: Start-URL der Suche; `crawl_id`: Auftrags-/Lauf-ID; `max_companies`: Obergrenze für Datensätze; `max_pages`: Obergrenze für Ergebnisseiten; `downloads`: Dokumentdownload aktivieren; `headless`: Browser ohne sichtbares Fenster starten; `timing_path`: Pfad zum Timing-Log; `executable_path`: optionaler Chromium-Binärpfad; `workers`: Anzahl Worker; `parallel_authorized`: explizite Attestation für Parallelbetrieb; Policy bleibt bindend. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `attach_error_classification({'crawl_id': crawl_id, 'status': status, 'stop_reason': reason, 'companies': self.companies, 'access_restriction': self.blocked, 'pagination_end_verified': statu…`.

**Explizite Fehler / Abbruch:**

- `ValueError('Invalid start URL or run limits')`
- `ValueError('Worker count must be 1–4 in C.3.6')`
- `ValueError('Parallel access requires confirmed authorization for the target')`
- `erneutes Auslösen der aktuellen Exception`

**Direkt gesetzter Zustand:** `self.worker_count`, `self.context`, `self.page`.

**Relevante Aufrufe:** `browser.close`, `browser.new_context`, `self._check_run_limits`, `self._collect`, `self._cookie_diagnostics`, `self._navigate`, `self.context.new_page`, `self.context.on`, `self.context.route`, `self.page.goto`, `self.page.is_closed`, `self.page.locator`, `self.page.locator('body').aria_snapshot`.

#### `AsyncStrategyExecutor.run.route_request`

**Quellcode:** [AsyncStrategyExecutor.py:855–859](src/crawler/AsyncStrategyExecutor.py#L855-L859).

```python
async def route_request(route):
```

**Aufgabe:** Lokaler Playwright-Routing-Callback lässt nur erlaubte URLs zu und bricht andere Requests ab.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `route.abort`, `route.continue_`.

---

## crawler-benchmarkanalyzer

**Modul:** [`src/crawler/BenchmarkAnalyzer.py`](src/crawler/BenchmarkAnalyzer.py)  
**Features/Storys:** G-02, B-01  
**Aufgabe und Abgrenzung:** Offline-Auswertung von JSON-Berichten, Timing-CSV und Usage-CSV/JSONL. Historische Spaltenformate bleiben lesbar; fehlende Kosten werden nicht als null Euro interpretiert. Keine Browser- oder API-Aufrufe.

**Direkte Abhängigkeiten:** `import csv`; `import json`; `from collections import defaultdict`; `from decimal import Decimal, InvalidOperation`; `from pathlib import Path`; `from ProjectPaths import report_files`; `from statistics import median`.

**Definitionen:** 0 Klassen, 8 Funktionen/Methoden (inkl. lokaler Definitionen).

#### `number`

**Quellcode:** [BenchmarkAnalyzer.py:11–16](src/crawler/BenchmarkAnalyzer.py#L11-L16).

```python
def number(value):
```

**Aufgabe:** Wandelt in endlichen nichtnegativen Decimal-Wert um; unlesbarer oder negativer Wert ergibt None.

**Parameter:** `value`: übergebener Wert gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `result if result.is_finite() and result >= 0 else None`; `None`.

#### `read_rows`

**Quellcode:** [BenchmarkAnalyzer.py:19–41](src/crawler/BenchmarkAnalyzer.py#L19-L41).

```python
def read_rows(path):
```

**Aufgabe:** Liest JSONL oder CSV, unterstützt historisch gemischte 10-/12-Spalten-Usage-Logs; meldet andere Spaltenkonflikte.

**Parameter:** `path`: Datei-/Verzeichnispfad gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `[json.loads(line) for line in file if line.strip()]`; `[]`; `rows`.

**Explizite Fehler / Abbruch:**

- `ValueError(f'Unexpected CSV column count in {path}, line {reader.line_num}')`

**Relevante Aufrufe:** `json.loads`.

#### `aggregate_usage`

**Quellcode:** [BenchmarkAnalyzer.py:44–60](src/crawler/BenchmarkAnalyzer.py#L44-L60).

```python
def aggregate_usage(rows, expected):
```

**Aufgabe:** Summiert Token-/Kostenfelder, kennzeichnet fehlende Werte, erwartete Aufrufzahl und Kosten-Vollständigkeit. Null Kosten nur bei bestätigten null Aufrufen oder vollständigen Nullwerten.

**Parameter:** `rows`: Locator/Sequenz der Ergebniszeilen; `expected`: erwarteter Wert bzw. erwartete Felder/Anzahl je Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `dict(usage_records=len(rows), **tokens, known_cost_usd=str(known) if rows or complete else None, cost_complete=complete, cost_usd=str(known) if complete else None, unpriced_records=sum((v i…`.

#### `execution_row`

**Quellcode:** [BenchmarkAnalyzer.py:63–77](src/crawler/BenchmarkAnalyzer.py#L63-L77).

```python
def execution_row(report):
```

**Aufgabe:** Erzeugt vergleichbare Benchmark-Zeile aus Execution-Report und Dokumentstatus.

**Parameter:** `report`: strukturiertes Berichts-Dictionary. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `dict(run_id=report['crawl_id'], mode='execution', status=report['status'], duration_seconds=metrics.get('total_duration_seconds'), llm_calls=metrics.get('llm_calls'), workers=metrics.get('w…`.

#### `timing_summary`

**Quellcode:** [BenchmarkAnalyzer.py:80–89](src/crawler/BenchmarkAnalyzer.py#L80-L89).

```python
def timing_summary(rows):
```

**Aufgabe:** Aggregiert Phasenanzahl, Dauer und Fehler; Walltime nur bei eindeutigem total-Eintrag, keine Addition überlappender Phasen.

**Parameter:** `rows`: Locator/Sequenz der Ergebniszeilen. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `dict(duration_seconds=duration, phases=phases, total_rows=len(totals))`.

#### `analyze`

**Quellcode:** [BenchmarkAnalyzer.py:92–192](src/crawler/BenchmarkAnalyzer.py#L92-L192).

```python
def analyze(directory, timing_paths=(), usage_paths=(), baseline_id=None, baseline_companies=None):
```

**Aufgabe:** Verknüpft Reports, Usage und Timings per Run-ID; vermeidet doppelte Child-Runs, kann Baseline rekonstruieren; gruppiert Execution-Typen und berechnet Vergleichsmetriken. Offline.

**Parameter:** `directory`: Verzeichnis der Eingaben/Ausgaben; `timing_paths`: Liste der Timing-Dateipfade; `usage_paths`: Liste der Usage-Dateipfade; `baseline_id`: Crawl-ID eines separaten Baseline-Laufs; `baseline_companies`: bekannte Datensatzanzahl der Baseline. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `dict(benchmark_version=2, runs=list(runs.values()), execution_groups=summaries, observed_usage=observed_usage, unmatched_usage_ids=sorted(set(usage) - linked), unmatched_timing_ids=sorted(s…`.

**Explizite Fehler / Abbruch:**

- `ValueError(f'Report directory does not exist: {directory}')`
- `ValueError(f'Missing crawl_id in {path}')`
- `ValueError(f'Conflicting usage record: {key}')`
- `ValueError('Baseline must be a distinct crawl ID present in timing CSV')`

**Relevante Aufrufe:** `json.loads`, `path.name.removesuffix`, `path.read_text`.

#### `analyze.add`

**Quellcode:** [BenchmarkAnalyzer.py:115–119](src/crawler/BenchmarkAnalyzer.py#L115-L119).

```python
def add(row):
```

**Aufgabe:** Lokaler Helper registriert eindeutige Run-ID im Ergebnis und verweigert fehlende/mehrfache IDs.

**Parameter:** `row`: Locator bzw. Datensatzzeile im aktuellen Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError(f'Missing or duplicate run ID: {identifier}')`

#### `write_report`

**Quellcode:** [BenchmarkAnalyzer.py:195–205](src/crawler/BenchmarkAnalyzer.py#L195-L205).

```python
def write_report(report, output_dir):
```

**Aufgabe:** Schreibt Benchmark-JSON und flache Run-CSV in Ausgabeordner.

**Parameter:** `report`: strukturiertes Berichts-Dictionary; `output_dir`: Zielverzeichnis für Originaldateien. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `json.dumps`, `writer.writeheader`, `writer.writerows`.

---

## crawler-browseruse

**Modul:** [`src/crawler/BrowserUse.py`](src/crawler/BrowserUse.py)  
**Features/Storys:** C-02, C-04  
**Aufgabe und Abgrenzung:** Synchroner Playwright-Adapter für den KI-gesteuerten Pilot/Discovery. Tools und strukturierte DOM-Beobachtungen werden im Responses-API-Loop verwendet. Discovery deaktiviert vorgesehene Downloadaktionen; die deterministischen Executors verwenden nur ausgewählte Hilfsfunktionen.

**Direkte Abhängigkeiten:** `import csv`; `import json`; `import time`; `import warnings`; `from contextlib import contextmanager`; `from datetime import datetime, timezone`; `from pathlib import Path`; `from ProjectPaths import DOCUMENTS_DIR, BROWSER_TIMING_FILE`; `from uuid import uuid4`; `from urllib.parse import urlsplit`; `from playwright.sync_api import Error as PlaywrightError, sync_playwright`.

**Definitionen:** 1 Klassen, 10 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `INSTRUCTIONS`, `BROWSER_TOOL`, `DISCOVERY_INSTRUCTIONS`, `DISCOVERY_BROWSER_TOOL`, `INSPECT_DOM_TOOL`, `DOM_INSPECTION_JS`.

#### `measure`

**Quellcode:** [BrowserUse.py:153–163](src/crawler/BrowserUse.py#L153-L163).

```python
@contextmanager
def measure(events, phase, step=None, action=None):
```

**Aufgabe:** Contextmanager erfasst Dauer, Phase, Step, Aktion und Fehlerstatus auch bei Exception.

**Parameter:** `events`: Mess-/Diagnoseereignisse; `phase`: Bezeichnung der gemessenen Phase; `step`: Schrittnummer; `action`: Aktionsbezeichnung. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** Generator/Contextmanager; liefert .

**Explizite Fehler / Abbruch:**

- `erneutes Auslösen der aktuellen Exception`

#### `write_timings`

**Quellcode:** [BrowserUse.py:166–178](src/crawler/BrowserUse.py#L166-L178).

```python
def write_timings(path, crawl_id, events):
```

**Aufgabe:** Schreibt gemessene Phasen mit Crawl-ID in Timing-CSV.

**Parameter:** `path`: Datei-/Verzeichnispfad gemäß Funktionszweck; `crawl_id`: Auftrags-/Lauf-ID; `events`: Mess-/Diagnoseereignisse. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `path.exists`, `path.open`, `path.parent.mkdir`, `path.stat`, `writer.writeheader`, `writer.writerow`.

### Klasse `BrowserUse`

**Quellcode:** [BrowserUse.py:181–295](src/crawler/BrowserUse.py#L181-L295).

**Aufgabe:** KI-Tool-Adapter auf einer Playwright-Seite; verwaltet Discovery-Modus und Messereignisse.

#### `BrowserUse.__init__`

**Quellcode:** [BrowserUse.py:183–187](src/crawler/BrowserUse.py#L183-L187).

```python
def __init__(self, page, events=None, discovery=False):
```

**Aufgabe:** Bindet Page, Eventliste und Discovery-Flag; initialisiert Step.

**Parameter:** `page`: Browser-Page oder Seitennummer gemäß Funktionszweck; `events`: Mess-/Diagnoseereignisse. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.page`, `self.discovery`, `self.events`, `self.step`.

#### `BrowserUse.read`

**Quellcode:** [BrowserUse.py:189–196](src/crawler/BrowserUse.py#L189-L196).

```python
def read(self):
```

**Aufgabe:** Erstellt begrenzte Seitenbeobachtung aus URL und Accessibility-/DOM-Informationen.

**Rückgabe (Ausdrücke im Code):** `{'url': self.page.url, 'snapshot': snapshot[:24000], 'snapshot_truncated': len(snapshot) > 24000, 'links': links, 'links_limit': 100}`.

**Relevante Aufrufe:** `self.page.locator`, `self.page.locator('a[href]:visible').evaluate_all`, `self.page.locator('body').aria_snapshot`.

#### `BrowserUse.inspect_dom`

**Quellcode:** [BrowserUse.py:198–236](src/crawler/BrowserUse.py#L198-L236).

```python
def inspect_dom(self, selector, role, name, index, depth, relative='self'):
```

**Aufgabe:** Untersucht begrenzten sichtbaren CSS-/Rollen-Treffer oder benachbartes Element; liefert DOM-/ARIA-Snapshot, Matchanzahl und Truncation-Hinweise. Keine Interaktion.

**Parameter:** `selector`: CSS-Selektor; `role`: Accessibility-Rolle; `name`: Name des Felds/Controls gemäß Kontext; `index`: nullbasierter Index; `depth`: maximale DOM-Inspektionstiefe; `relative`: relativer Scope der DOM-Inspektion. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `{'url': self.page.url, 'match_count': count, 'error': 'No matching element at requested index'}`; `{'url': self.page.url, 'match_count': count, 'relative': relative, 'error': 'Adjacent element not found'}`; `{'url': self.page.url, 'match_count': count, 'error': 'Element is not visible'}`; `{'url': self.page.url, 'match_count': count, 'index': index, 'relative': relative, **result, 'aria': aria[:6000], 'aria_truncated': len(aria) > 6000}`.

**Explizite Fehler / Abbruch:**

- `ValueError('DOM inspection is only enabled in discovery mode')`
- `ValueError('Use one locator kind and depth 1-8')`
- `ValueError('CSS selector too long')`
- `ValueError('Unsupported relative scope')`

**Relevante Aufrufe:** `json.dumps`, `self.page.get_by_role`, `self.page.locator`, `target.aria_snapshot`, `target.evaluate`, `target.is_visible`, `target.locator`, `target.nth`.

#### `BrowserUse.execute`

**Quellcode:** [BrowserUse.py:238–255](src/crawler/BrowserUse.py#L238-L255).

```python
def execute(self, action, role, name, index, value):
```

**Aufgabe:** Dispatch für read/back und erlaubte Aktionen; misst Aktion, optional settle und erneute Beobachtung. Download im Discovery-Modus verboten.

**Parameter:** `action`: Aktionsbezeichnung; `role`: Accessibility-Rolle; `name`: Name des Felds/Controls gemäß Kontext; `index`: nullbasierter Index; `value`: übergebener Wert gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `self.read()`; `{**result, 'page': self.read()}`.

**Explizite Fehler / Abbruch:**

- `ValueError('Downloads are disabled in discovery mode')`

**Relevante Aufrufe:** `self._perform`, `self.page.go_back`, `self.page.wait_for_timeout`, `self.read`.

#### `BrowserUse._perform`

**Quellcode:** [BrowserUse.py:257–295](src/crawler/BrowserUse.py#L257-L295).

```python
def _perform(self, action, role, name, index, value):
```

**Aufgabe:** Prüft eindeutiges sichtbares Rollen-Ziel und zulässige Aktion/Parameter; klickt, füllt, wählt oder behandelt Legacy-Download, keine Passwort-/Dateiinputs.

**Parameter:** `action`: Aktionsbezeichnung; `role`: Accessibility-Rolle; `name`: Name des Felds/Controls gemäß Kontext; `index`: nullbasierter Index; `value`: übergebener Wert gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `{'status': 'downloaded', 'document_url': download.url, 'filename': filename, 'file_path': str(file_path), 'size_bytes': file_path.stat().st_size}`.

**Explizite Fehler / Abbruch:**

- `ValueError('Unsupported action or missing role/name')`
- `ValueError('Index must be non-negative')`
- `ValueError('Target not uniquely visible. Read page and use exact role/name or index.')`
- `ValueError('Downloads are disabled in discovery mode')`
- `ValueError('Check/uncheck require a discovery checkbox and no value')`
- `ValueError('Fill requires a text input and value')`
- `ValueError('Password and file inputs are not supported')`
- `ValueError('Select requires a select element and visible option label')`

**Relevante Aufrufe:** `self.page.expect_download`, `self.page.get_by_role`, `target.click`, `target.fill`, `target.get_attribute`, `target.is_visible`, `target.nth`, `target.select_option`, `target.set_checked`.

#### `allowed_url`

**Quellcode:** [BrowserUse.py:298–305](src/crawler/BrowserUse.py#L298-L305).

```python
def allowed_url(url, domains):
```

**Aufgabe:** Prüft HTTPS, Standardport, keine URL-Zugangsdaten und exakte Domain-/Subdomain-Allowlist; ungültige URL ergibt False.

**Parameter:** `url`: zu prüfende URL; `domains`: erlaubte Domainliste. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `parsed.scheme == 'https' and parsed.port in (None, 443) and (not parsed.username) and (not parsed.password) and any((host == d or host.endswith('.' + d) for d in domains))`; `False`.

#### `browser_loop`

**Quellcode:** [BrowserUse.py:308–358](src/crawler/BrowserUse.py#L308-L358).

```python
def browser_loop(client, browser, model, prompt, crawl_id, schema, max_steps, **kwargs):
```

**Aufgabe:** Begrenzter Responses-API-Function-Calling-Loop mit previous_response_id; verarbeitet Browser-/DOM-Toolaufrufe, schickt Beobachtungen als Daten zurück und verlangt finale Ausgabe. Reservierte Optionen schützen Toolvertrag.

**Parameter:** `client`: API-Client/Wrapper; `model`: Modellkennung; `prompt`: Eingabe für LLM-Aufruf; `crawl_id`: Auftrags-/Lauf-ID; `schema`: JSON-Schema-Vertrag; `max_steps`: maximale Anzahl API-Anfragen im Browser-Loop; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `response`.

**Explizite Fehler / Abbruch:**

- `ValueError(f'Reserved browser options: {sorted(reserved.intersection(options))}')`
- `RuntimeError(f'Browser response not completed: {response.status}')`
- `RuntimeError('Browser task returned no final result')`
- `RuntimeError(f'Browser step limit reached ({max_steps} API requests)')`
- `RuntimeError(f'Unexpected tool: {call.name}')`
- `RuntimeError('No final browser response')`

**Relevante Aufrufe:** `browser.execute`, `browser.inspect_dom`, `browser.read`, `client.create`, `json.dumps`, `json.loads`.

#### `run_browser`

**Quellcode:** [BrowserUse.py:361–392](src/crawler/BrowserUse.py#L361-L392).

```python
def run_browser(client, model, prompt, crawl_id, schema, domains, start_url, max_steps=20, headless=False, timing_path=BROWSER_TIMING_FILE, discovery=False, **kwargs):
```

**Aufgabe:** Validiert Auftrag, Domainliste und Step-Limit, startet Chromium mit Request-Allowlist und Discovery-Downloadregel, ruft Loop auf; schließt Browser und schreibt Timings im finally.

**Parameter:** `client`: API-Client/Wrapper; `model`: Modellkennung; `prompt`: Eingabe für LLM-Aufruf; `crawl_id`: Auftrags-/Lauf-ID; `schema`: JSON-Schema-Vertrag; `domains`: erlaubte Domainliste; `start_url`: Start-URL der Suche; `max_steps`: maximale Anzahl API-Anfragen im Browser-Loop; `headless`: Browser ohne sichtbares Fenster starten; `timing_path`: Pfad zum Timing-Log; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `browser_loop(client, BrowserUse(page, events, discovery=discovery), model, prompt, crawl_id, schema, max_steps, **kwargs)`.

**Explizite Fehler / Abbruch:**

- `ValueError('Discovery mode requires STRATEGY_SCHEMA')`
- `ValueError('Browser use requires a text prompt, start_url and a list of allowed domains')`
- `ValueError('Invalid start URL, allowed domains or max_steps')`

**Relevante Aufrufe:** `browser.close`, `browser.new_context`, `context.new_page`, `context.route`, `page.goto`.

---

## crawler-crawlcheckpoint

**Modul:** [`src/crawler/CrawlCheckpoint.py`](src/crawler/CrawlCheckpoint.py)  
**Features/Storys:** H-01, H-03  
**Aufgabe und Abgrenzung:** Ein SQLite-Checkpoint je Vollcrawl. Exklusive Neuanlage, Transaktionen und dauerhafte Downloadabsicht vor dem Abruf; Dateibytes vor finalem Datenbankstatus synchronisieren. Kein Resume aus einer bestehenden Datenbank; ein Absturz zwischen Datei und DB lässt den Zustand unklar.

**Direkte Abhängigkeiten:** `import json`; `import os`; `import sqlite3`; `import hashlib`; `from datetime import datetime, timezone`; `from pathlib import Path`.

**Definitionen:** 1 Klassen, 13 Funktionen/Methoden (inkl. lokaler Definitionen).

#### `now`

**Quellcode:** [CrawlCheckpoint.py:10–11](src/crawler/CrawlCheckpoint.py#L10-L11).

```python
def now():
```

**Aufgabe:** UTC-Zeitstempel im ISO-Format.

**Rückgabe (Ausdrücke im Code):** `datetime.now(timezone.utc).isoformat()`.

#### `encode`

**Quellcode:** [CrawlCheckpoint.py:14–15](src/crawler/CrawlCheckpoint.py#L14-L15).

```python
def encode(value):
```

**Aufgabe:** Kompakte deterministische JSON-Serialisierung ohne NaN; dient auch für Schlüssel.

**Parameter:** `value`: übergebener Wert gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'), allow_nan=False)`.

**Relevante Aufrufe:** `json.dumps`.

### Klasse `CrawlCheckpoint`

**Quellcode:** [CrawlCheckpoint.py:18–195](src/crawler/CrawlCheckpoint.py#L18-L195).

**Aufgabe:** Single-writer SQLite-Checkpoint mit Tabellen job, pages, companies, documents; keine Wiederöffnung für Schreib-Resume.

**Klassenattribute / Konfiguration:**

- `VERSION = 1`

#### `CrawlCheckpoint.__init__`

**Quellcode:** [CrawlCheckpoint.py:21–66](src/crawler/CrawlCheckpoint.py#L21-L66).

```python
def __init__(self, path, crawl_id, plan, key_fields, output_dir):
```

**Aufgabe:** Legt neue DB exklusiv an, aktiviert Foreign Keys und FULL-Synchronisation, erstellt Schema und running-Auftrag, synchronisiert Verzeichniseintrag. Existierende DB wird nicht überschrieben.

**Parameter:** `path`: Datei-/Verzeichnispfad gemäß Funktionszweck; `crawl_id`: Auftrags-/Lauf-ID; `plan`: Preflight-/Resume-Plan; `key_fields`: geordnete Liste der Datensatz-Schlüsselfelder; `output_dir`: Zielverzeichnis für Originaldateien. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `erneutes Auslösen der aktuellen Exception`

**Direkt gesetzter Zustand:** `self.path`, `self.crawl_id`, `self.key_fields`, `self.output_dir`, `self.db`.

**Relevante Aufrufe:** `os.close`, `os.open`, `self._sync_dir`, `self.db.close`, `self.db.execute`, `self.db.executescript`, `self.path.parent.mkdir`, `sqlite3.connect`.

#### `CrawlCheckpoint._sync_dir`

**Quellcode:** [CrawlCheckpoint.py:69–74](src/crawler/CrawlCheckpoint.py#L69-L74).

```python
@staticmethod
def _sync_dir(path):
```

**Aufgabe:** Synchronisiert Verzeichniseinträge über POSIX fsync und schließt den Descriptor.

**Parameter:** `path`: Datei-/Verzeichnispfad gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `os.close`, `os.fsync`, `os.open`.

#### `CrawlCheckpoint.close`

**Quellcode:** [CrawlCheckpoint.py:76–77](src/crawler/CrawlCheckpoint.py#L76-L77).

```python
def close(self):
```

**Aufgabe:** Schließt SQLite-Verbindung.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self.db.close`.

#### `CrawlCheckpoint._touch`

**Quellcode:** [CrawlCheckpoint.py:79–82](src/crawler/CrawlCheckpoint.py#L79-L82).

```python
def _touch(self):
```

**Aufgabe:** Aktualisiert Zeitstempel des laufenden Auftrags; verweigert Operationen an nicht laufendem Auftrag.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `RuntimeError('Checkpoint job is not running')`

**Relevante Aufrufe:** `self.db.execute`.

#### `CrawlCheckpoint._key`

**Quellcode:** [CrawlCheckpoint.py:84–85](src/crawler/CrawlCheckpoint.py#L84-L85).

```python
def _key(self, record):
```

**Aufgabe:** Serialisiert geordnete Schlüsselfeldwerte eines Datensatzes.

**Parameter:** `record`: extrahierter Datensatz mit Schlüsselfeldern. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `encode([record[k] for k in self.key_fields])`.

#### `CrawlCheckpoint.save_page`

**Quellcode:** [CrawlCheckpoint.py:87–108](src/crawler/CrawlCheckpoint.py#L87-L108).

```python
def save_page(self, page, records, signature, downloads):
```

**Aufgabe:** Prüft nichtleere eindeutige Signatur und lückenlose Seitenfolge. Speichert Seite, stabile Datensätze und geplante Dokumente gemeinsam in einer Transaktion; ohne Download not_requested.

**Parameter:** `page`: Browser-Page oder Seitennummer gemäß Funktionszweck; `records`: extrahierte Datensätze; `signature`: geordnete Seitensignatur aus Datensatzschlüsseln; `downloads`: Dokumentdownload aktivieren. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Invalid checkpoint page signature')`
- `ValueError('Checkpoint page sequence invalid')`
- `ValueError('New page contains previously attempted document')`

**Relevante Aufrufe:** `self._key`, `self._touch`, `self.db.execute`, `self.db.execute('SELECT page,status FROM pages ORDER BY page DESC LIMIT 1').fetchone`.

#### `CrawlCheckpoint.start_document`

**Quellcode:** [CrawlCheckpoint.py:110–117](src/crawler/CrawlCheckpoint.py#L110-L117).

```python
def start_document(self, record, doc):
```

**Aufgabe:** Wechselt genau ein noch nicht versuchtes Dokument transaktional zu in_progress vor Abruf.

**Parameter:** `record`: extrahierter Datensatz mit Schlüsselfeldern; `doc`: Dokument-Metadaten. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Checkpoint document already attempted or unknown')`

**Relevante Aufrufe:** `self._key`, `self._touch`, `self.db.execute`.

#### `CrawlCheckpoint.finish_document`

**Quellcode:** [CrawlCheckpoint.py:119–147](src/crawler/CrawlCheckpoint.py#L119-L147).

```python
def finish_document(self, record, doc):
```

**Aufgabe:** Akzeptiert nur downloaded/failed nach in_progress. Bei Erfolg Pfad, Größe, blockweisen Hash und fsync prüfen; erst dann DB aktualisieren. Kein gemeinsames atomisches Commit von Datei und DB.

**Parameter:** `record`: extrahierter Datensatz mit Schlüsselfeldern; `doc`: Dokument-Metadaten. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Invalid final document state')`
- `ValueError('Checkpoint document path outside output directory')`
- `ValueError('Checkpoint document digest or size mismatch')`
- `ValueError('Checkpoint document was not in progress')`

**Relevante Aufrufe:** `hashlib.file_digest`, `hashlib.file_digest(stream, 'sha256').hexdigest`, `os.fstat`, `os.fsync`, `path.is_file`, `path.is_relative_to`, `path.open`, `self._key`, `self._sync_dir`, `self._touch`, `self.db.execute`.

#### `CrawlCheckpoint.finish_page`

**Quellcode:** [CrawlCheckpoint.py:149–160](src/crawler/CrawlCheckpoint.py#L149-L160).

```python
def finish_page(self, page):
```

**Aufgabe:** Setzt Seite auf processed, wenn Zeilen-/Dokumentzahlen stimmen und alle Dokumente downloaded oder not_requested sind.

**Parameter:** `page`: Browser-Page oder Seitennummer gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Checkpoint page incomplete')`

**Relevante Aufrufe:** `self._touch`, `self.db.execute`.

#### `CrawlCheckpoint.finish`

**Quellcode:** [CrawlCheckpoint.py:162–169](src/crawler/CrawlCheckpoint.py#L162-L169).

```python
def finish(self, status, result):
```

**Aufgabe:** Setzt laufenden Auftrag auf completed/failed/interrupted und speichert Ergebnis; completed erfordert keine offenen Seiten.

**Parameter:** `status`: zu speichernder bzw. beobachteter Status; `result`: Ergebnis-/Statusobjekt. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Invalid checkpoint job status')`
- `ValueError('Completed job contains unfinished pages')`

**Relevante Aufrufe:** `self._touch`, `self.db.execute`, `self.db.execute("SELECT count(*) FROM pages WHERE status!='processed'").fetchone`.

#### `CrawlCheckpoint.inspect`

**Quellcode:** [CrawlCheckpoint.py:172–195](src/crawler/CrawlCheckpoint.py#L172-L195).

```python
@classmethod
def inspect(cls, path):
```

**Aufgabe:** Öffnet DB im Read-only-Modus, prüft Schemaversion, liest konsistenten Snapshot mit Auftrags-/Seiten-/Dokumentstatistik; verändert nichts.

**Parameter:** `path`: Datei-/Verzeichnispfad gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `dict(job=job, pages=pages, companies_extracted=companies, companies_documents_done=done, pages_processed=sum((p['status'] == 'processed' for p in pages)), document_counts={s: counts.get(s, …`.

**Explizite Fehler / Abbruch:**

- `ValueError('Unsupported checkpoint version')`

**Relevante Aufrufe:** `json.loads`, `sqlite3.connect`.

---

## crawler-documentdownloader

**Modul:** [`src/crawler/DocumentDownloader.py`](src/crawler/DocumentDownloader.py)  
**Features/Storys:** E-01  
**Aufgabe und Abgrenzung:** Historischer direkter HTTP-Downloader mit persistenter CSV-Queue und Wiederholungslogik. Nicht regulär einsetzen: Queue-Felder enthalten file_type nicht, obwohl _fetch dieses Feld liest; Dateinamenskonvention und Deduplizierung sind PDF-orientiert. Die Wiederholungsregeln sind nicht der aktuelle konservative Executor-Vertrag.

**Direkte Abhängigkeiten:** `import csv`; `import hashlib`; `import re`; `import time`; `from datetime import datetime, timezone`; `from pathlib import Path`; `from ProjectPaths import DOCUMENTS_DIR, DOCUMENTS_METRICS_FILE, DOWNLOAD_QUEUE_FILE`; `from urllib.parse import urlparse`; `import requests`; `from defusedxml.ElementTree import fromstring`.

**Definitionen:** 1 Klassen, 10 Funktionen/Methoden (inkl. lokaler Definitionen).

### Klasse `DocumentDownloader`

**Quellcode:** [DocumentDownloader.py:14–180](src/crawler/DocumentDownloader.py#L14-L180).

**Aufgabe:** Legacy-HTTP-Queue mit CSV-Persistenz, begrenztem Retry und binärer Duplikatprüfung. Bekannte file_type-Inkonsistenz; nicht Teil des freigegebenen neuen Crawls.

**Klassenattribute / Konfiguration:**

- `DOCUMENT_FIELDS = ('title', 'description', 'source_url', 'document_url')`
- `QUEUE_FIELDS = ('crawl_id', *DOCUMENT_FIELDS, 'attempts', 'last_error', 'last_attempt')`
- `LOG_FIELDS = ('timestamp', 'crawl_id', *DOCUMENT_FIELDS, 'final_url', 'file_path', 'sha256', 'size_bytes', 'status', 'error')`
- `RETRY_STATUS = {408, 425, 429, 500, 502, 503, 504}`

#### `DocumentDownloader.__init__`

**Quellcode:** [DocumentDownloader.py:21–31](src/crawler/DocumentDownloader.py#L21-L31).

```python
def __init__(self, output_dir=DOCUMENTS_DIR, max_size_mb=50, max_attempts=3, retry_delay=2, pause=1, log_path=DOCUMENTS_METRICS_FILE, queue_path=DOWNLOAD_QUEUE_FILE):
```

**Aufgabe:** Prüft Größen-/Retry-/Pause-Konfiguration, richtet Output und Pfade ein, setzt HTTP-Header.

**Parameter:** `output_dir`: Zielverzeichnis für Originaldateien; `max_size_mb`: maximale Dateigröße (MiB in der Implementierung); `max_attempts`: maximale Anzahl Abrufversuche im Legacy-Downloader; `retry_delay`: Basiswartezeit vor Legacy-Retry in Sekunden; `pause`: Pause zwischen Legacy-Dokumenten in Sekunden; `log_path`: Zielpfad des Logs; `queue_path`: Pfad der Legacy-CSV-Queue. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Invalid download configuration')`

**Direkt gesetzter Zustand:** `self.output_dir`, `self.log_path`, `self.queue_path`, `self.max_size`, `self.max_attempts`, `self.retry_delay`, `self.pause`, `self.headers`.

**Relevante Aufrufe:** `self.output_dir.mkdir`.

#### `DocumentDownloader._now`

**Quellcode:** [DocumentDownloader.py:34–35](src/crawler/DocumentDownloader.py#L34-L35).

```python
@staticmethod
def _now():
```

**Aufgabe:** Erzeugt UTC-Logzeitstempel.

**Rückgabe (Ausdrücke im Code):** `datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')`.

#### `DocumentDownloader._read`

**Quellcode:** [DocumentDownloader.py:38–43](src/crawler/DocumentDownloader.py#L38-L43).

```python
@staticmethod
def _read(path):
```

**Aufgabe:** Liest vorhandene CSV als Liste von Dictionaries; fehlende Datei ergibt leere Liste.

**Parameter:** `path`: Datei-/Verzeichnispfad gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `[]`; `list(csv.DictReader(file))`.

**Relevante Aufrufe:** `path.exists`, `path.open`.

#### `DocumentDownloader._save_queue`

**Quellcode:** [DocumentDownloader.py:45–52](src/crawler/DocumentDownloader.py#L45-L52).

```python
def _save_queue(self, rows):
```

**Aufgabe:** Schreibt Queue per temporärer CSV und Replace, legt Elternverzeichnis an.

**Parameter:** `rows`: Locator/Sequenz der Ergebniszeilen. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self.queue_path.parent.mkdir`, `self.queue_path.with_suffix`, `writer.writeheader`, `writer.writerows`.

#### `DocumentDownloader._key`

**Quellcode:** [DocumentDownloader.py:55–56](src/crawler/DocumentDownloader.py#L55-L56).

```python
@staticmethod
def _key(row):
```

**Aufgabe:** Identifiziert Legacy-Queue-Eintrag über crawl_id und document_url.

**Parameter:** `row`: Locator bzw. Datensatzzeile im aktuellen Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(row.get('crawl_id') or '', row['document_url'])`.

#### `DocumentDownloader.enqueue`

**Quellcode:** [DocumentDownloader.py:58–67](src/crawler/DocumentDownloader.py#L58-L67).

```python
def enqueue(self, documents, crawl_id=None):
```

**Aufgabe:** Ergänzt unbekannte Dokumente in Queue, initialisiert Attempt-/Fehlerstatus und persistiert. Heutige Queue transportiert file_type nicht.

**Parameter:** `crawl_id`: Auftrags-/Lauf-ID. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self._key`, `self._read`, `self._save_queue`.

#### `DocumentDownloader.import_failed`

**Quellcode:** [DocumentDownloader.py:69–81](src/crawler/DocumentDownloader.py#L69-L81).

```python
def import_failed(self, log_path=None):
```

**Aufgabe:** Importiert letzte fehlgeschlagene Logeinträge je Crawl/URL ohne vorhandene Queue-Metadaten zu überschreiben.

**Parameter:** `log_path`: Zielpfad des Logs. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `count`.

**Relevante Aufrufe:** `self._key`, `self._read`, `self._save_queue`.

#### `DocumentDownloader._fetch`

**Quellcode:** [DocumentDownloader.py:83–125](src/crawler/DocumentDownloader.py#L83-L125).

```python
def _fetch(self, document):
```

**Aufgabe:** Ruft Dokument via requests ab, prüft Format, Größe und Hash, speichert oder erkennt exakte Duplikate. Bekannter Fehler: document[file_type] ist nicht im Queue-Vertrag; Speicherung PDF-orientiert. Nicht als Streaming- oder neuer Sicherheitsvertrag verstehen.

**Parameter:** `document`: Dokument-Metadaten. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(existing, file_hash, len(content), final_url, 'duplicate')`; `(path, file_hash, len(content), final_url, 'success')`.

**Explizite Fehler / Abbruch:**

- `ValueError('Invalid HTTP URL')`
- `ValueError('Maximum file size exceeded')`
- `ValueError('Keine PDF-Datei')`
- `ValueError('HTML statt XML-Dokument erhalten')`
- `ValueError(f'Nicht unterstützter Dateityp: {file_type}')`

**Relevante Aufrufe:** `hashlib.sha256`, `hashlib.sha256(content).hexdigest`, `path.with_suffix`, `response.iter_content`, `response.raise_for_status`, `self.output_dir.glob`.

#### `DocumentDownloader._log`

**Quellcode:** [DocumentDownloader.py:127–139](src/crawler/DocumentDownloader.py#L127-L139).

```python
def _log(self, document, status, error='', result=None):
```

**Aufgabe:** Schreibt Abrufmetadaten, Status, Hash, Pfad, Größe und Fehler in CSV.

**Parameter:** `document`: Dokument-Metadaten; `status`: zu speichernder bzw. beobachteter Status; `error`: Fehlertext; `result`: Ergebnis-/Statusobjekt. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self._now`, `self.log_path.exists`, `self.log_path.open`, `self.log_path.parent.mkdir`, `self.log_path.stat`, `writer.writeheader`, `writer.writerow`.

#### `DocumentDownloader.process_queue`

**Quellcode:** [DocumentDownloader.py:141–180](src/crawler/DocumentDownloader.py#L141-L180).

```python
def process_queue(self, crawl_id=None):
```

**Aufgabe:** Verarbeitet ausgewählte Queue, persistiert Versuche, wiederholt nur Legacy-Fehlerklassen begrenzt mit Delay, protokolliert und entfernt abgeschlossene Einträge. Aktuelle Provider-/Recovery-Regeln sind separat.

**Parameter:** `crawl_id`: Auftrags-/Lauf-ID. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `results`.

**Relevante Aufrufe:** `self._fetch`, `self._log`, `self._now`, `self._read`, `self._save_queue`.

---

## crawler-errorclassifier

**Modul:** [`src/crawler/ErrorClassifier.py`](src/crawler/ErrorClassifier.py)  
**Features/Storys:** F-01  
**Aufgabe und Abgrenzung:** Deterministische Klassifizierung beobachtbarer Fehlerhinweise in Execution-JSONs. Explizite Zugriffssperren und Serverfehler haben Vorrang vor Strukturverdacht. Klassifikation allein erlaubt weder LLM-Reparatur noch automatischen Retry.

**Direkte Abhängigkeiten:** `import argparse`; `import json`; `import re`; `from pathlib import Path`; `from urllib.parse import urlsplit`.

**Definitionen:** 1 Klassen, 10 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `CLASSIFIER_VERSION`, `POLICIES`, `PRIORITY`, `ACCESS_STATUS`, `SERVER_STATUS`, `NETWORK`.

#### `_mapping`

**Quellcode:** [ErrorClassifier.py:39–40](src/crawler/ErrorClassifier.py#L39-L40).

```python
def _mapping(value):
```

**Aufgabe:** Behandelt Nicht-Dict-Wert defensiv als leeres Mapping.

**Parameter:** `value`: übergebener Wert gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `value if isinstance(value, dict) else {}`.

#### `_items`

**Quellcode:** [ErrorClassifier.py:43–44](src/crawler/ErrorClassifier.py#L43-L44).

```python
def _items(value):
```

**Aufgabe:** Behandelt Nicht-Listenwert defensiv als leere Sequenz.

**Parameter:** `value`: übergebener Wert gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `value if isinstance(value, list) else []`.

#### `_text`

**Quellcode:** [ErrorClassifier.py:47–48](src/crawler/ErrorClassifier.py#L47-L48).

```python
def _text(value):
```

**Aufgabe:** Normalisiert ungeeignete Eingabe zu sicher auswertbarem Text.

**Parameter:** `value`: übergebener Wert gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `value if isinstance(value, str) else ''`.

#### `_http_status`

**Quellcode:** [ErrorClassifier.py:51–52](src/crawler/ErrorClassifier.py#L51-L52).

```python
def _http_status(value):
```

**Aufgabe:** Liest HTTP-Status defensiv als numerischen Status bzw. Ersatzwert.

**Parameter:** `value`: übergebener Wert gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `value if type(value) is int and 100 <= value <= 599 else None`.

#### `_location`

**Quellcode:** [ErrorClassifier.py:55–60](src/crawler/ErrorClassifier.py#L55-L60).

```python
def _location(url):
```

**Aufgabe:** Normalisiert URL zur vergleichbaren Fehlerseitenposition ohne flüchtige Komponenten.

**Parameter:** `url`: zu prüfende URL. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(p.scheme, p.hostname, p.port, p.path) if p.scheme in ('http', 'https') and p.hostname else None`; `None`.

#### `_finding`

**Quellcode:** [ErrorClassifier.py:63–68](src/crawler/ErrorClassifier.py#L63-L68).

```python
def _finding(category, confidence, evidence, context=None):
```

**Aufgabe:** Erstellt strukturierten Befund aus Kategorie, Confidence, Evidenz und optionalem Kontext; standardmäßig keine LLM-/Retry-Erlaubnis.

**Parameter:** `category`: Fehlerkategorie; `confidence`: Evidenzstärke; `evidence`: beobachtete Hinweise/Fehlernachweis; `context`: Fehler-/Browserkontext gemäß Funktion. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `{'category': category, 'confidence': confidence, 'recommended_action': POLICIES[category], 'llm_allowed': False, 'automatic_retry_allowed': False, 'evidence': evidence, 'worker_id': context…`.

### Klasse `ErrorClassifier`

**Quellcode:** [ErrorClassifier.py:71–185](src/crawler/ErrorClassifier.py#L71-L185).

**Aufgabe:** Deterministische Klassifikationslogik für Haupt-/Workerfehler mit Evidenz, Priorität und Empfehlungen.

#### `ErrorClassifier._classify`

**Quellcode:** [ErrorClassifier.py:75–161](src/crawler/ErrorClassifier.py#L75-L161).

```python
@staticmethod
def _classify(context, report, is_worker=False):
```

**Aufgabe:** Wertet einzelne Fehlerkontexte und passende Netzwerkereignisse aus; unterscheidet Zugriff, Server, Netzwerk, Dokument, Daten, Strategie, Interaktion, Zustand und Strukturverdacht.

**Parameter:** `context`: Fehler-/Browserkontext gemäß Funktion; `report`: strukturiertes Berichts-Dictionary; `is_worker`: Kennzeichnung für Workerfehler. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `_finding('ACCESS_RESTRICTED', 'high', ['Explicit access restriction signal'], context)`; `_finding('DOMAIN_VIOLATION', 'high', ['URL violates configured domain boundary'], context)`; `_finding('ACCESS_RESTRICTED', 'high', [f'HTTP {denied} on worker failure page'], context)`; `_finding('SERVER_ERROR', 'high', [f"Explicit server error signal: HTTP {code or '5xx'}"], context)`; `_finding('SERVER_ERROR', 'high', [f'HTTP {server_code} on worker failure page', 'Original document response not established'], context)`; `_finding('NETWORK_ERROR', 'high', ['Explicit connection or DNS error'], context)`; `_finding('DOCUMENT_HTTP_ERROR', 'high', ['Explicit document HTTP failure'], context)`; `_finding('DOCUMENT_VALIDATION_ERROR', 'high', ['Document content or size validation failed'], context)`; `_finding('DATA_VALIDATION_ERROR', 'high', ['Record identity or expected filter validation failed'], context)`; `_finding('DATA_VALIDATION_ERROR', 'medium', ['Extraction rule or required field failed'], context)`; `_finding('STRATEGY_INVALID', 'medium', ['Configuration or validation exception'], context)`; `_finding('INTERACTION_BLOCKED', 'high' if 'intercepts pointer events' in msg else 'medium', evidence, context)`; `_finding('STATE_NOT_CONFIRMED', 'high', ['Expected navigation state was not confirmed'], context)`; `_finding('DOWNLOAD_TIMEOUT', 'high', ['No download event within the configured deadline', 'Underlying cause remains unknown'], context)`; `_finding('STATE_NOT_CONFIRMED', 'medium', ['Target missing during navigation after cookie handling', 'State change versus structural change not independently established'], context)`; `_finding('STRUCTURE_SUSPECTED', 'low', ['Locator or expected control unavailable or ambiguous', 'Independent verification required before strategy repair'], context)`; `_finding('BROWSER_ERROR', 'high', ['Browser lifecycle or installation error'], context)`; `_finding('UNKNOWN', 'low', ['Insufficient evidence for a specific failure class'], context)`.

#### `ErrorClassifier.classify`

**Quellcode:** [ErrorClassifier.py:164–185](src/crawler/ErrorClassifier.py#L164-L185).

```python
@classmethod
def classify(cls, report):
```

**Aufgabe:** Klassifiziert gesamten Report einschließlich Workerbefunden, wählt Hauptkategorie nach Priorität und bestimmt, ob unabhängige Strukturprüfung überhaupt zulässig ist.

**Parameter:** `report`: strukturiertes Berichts-Dictionary. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `{'classifier_version': CLASSIFIER_VERSION, 'primary': primary, 'findings': findings, 'requires_structure_verification': bool(findings) and all((f['category'] == 'STRUCTURE_SUSPECTED' for f …`.

**Explizite Fehler / Abbruch:**

- `TypeError('Execution report must be a dictionary')`

**Relevante Aufrufe:** `cls._classify`.

#### `attach_error_classification`

**Quellcode:** [ErrorClassifier.py:188–190](src/crawler/ErrorClassifier.py#L188-L190).

```python
def attach_error_classification(report):
```

**Aufgabe:** Ergänzt Klassifikation in bestehendem Execution-Report.

**Parameter:** `report`: strukturiertes Berichts-Dictionary. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `report`.

#### `main`

**Quellcode:** [ErrorClassifier.py:193–200](src/crawler/ErrorClassifier.py#L193-L200).

```python
def main():
```

**Aufgabe:** CLI liest Report und gibt deterministische Klassifikation aus; kein Browser, keine API.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `json.dumps`, `json.loads`, `path.read_text`.

---

## crawler-executionpolicy

**Modul:** [`src/crawler/ExecutionPolicy.py`](src/crawler/ExecutionPolicy.py)  
**Features/Storys:** C-07, C-08, C-09  
**Aufgabe und Abgrenzung:** Unveränderliche lokale Policy je Anbieter. Grenzen für Worker, Verifikation, KI-Reparatur und Vollcrawl. Unternehmensregister: ein Worker, Vollcrawl deaktiviert. Kein lokales Flag ersetzt eine tatsächliche Providerfreigabe.

**Direkte Abhängigkeiten:** `from dataclasses import dataclass`.

**Definitionen:** 1 Klassen, 3 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `POLICIES`.

### Klasse `ExecutionPolicy`

**Quellcode:** [ExecutionPolicy.py:6–24](src/crawler/ExecutionPolicy.py#L6-L24).

**Aufgabe:** Frozen Dataclass für Worker-, Reparatur-, Probe-, Verifikations- und Vollcrawlgrenzen. Standard ein Worker und Full-Crawl-Sperre.

**Dekoratoren:** `dataclass(frozen=True)`.

**Klassenattribute / Konfiguration:**

- `max_workers: int = 1`
- `result_path: str = ''`
- `max_repair_calls: int = 1`
- `max_output_tokens: int = 600`
- `max_probe_selectors: int = 24`
- `max_probe_rows: int = 40`
- `min_sample_rows: int = 2`
- `verification_timeout_seconds: int = 75`
- `full_crawl_enabled: bool = False`
- `full_max_pages: int = 100`
- `full_max_companies: int = 3000`
- `full_max_documents: int = 6000`
- `result_limit_marker: str = ''`

#### `ExecutionPolicy.check_workers`

**Quellcode:** [ExecutionPolicy.py:22–24](src/crawler/ExecutionPolicy.py#L22-L24).

```python
def check_workers(self, workers):
```

**Aufgabe:** Verlangt echte Ganzzahl zwischen 1 und max_workers; Flag kann Grenze nicht überschreiben.

**Parameter:** `workers`: Anzahl Worker. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError(f'Provider policy allows at most {self.max_workers} worker(s)')`

#### `get_policy`

**Quellcode:** [ExecutionPolicy.py:31–34](src/crawler/ExecutionPolicy.py#L31-L34).

```python
def get_policy(domain):
```

**Aufgabe:** Normalisiert Domain, wählt spezifischsten registrierten Domain-/Subdomain-Treffer oder konservativen Default.

**Parameter:** `domain`: Domainname. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `POLICIES[max(matches, key=len)] if matches else ExecutionPolicy()`.

#### `has_policy`

**Quellcode:** [ExecutionPolicy.py:37–39](src/crawler/ExecutionPolicy.py#L37-L39).

```python
def has_policy(domain):
```

**Aufgabe:** Prüft, ob Domain oder übergeordnete registrierte Domain explizit konfiguriert ist.

**Parameter:** `domain`: Domainname. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `any((host == key or host.endswith('.' + key) for key in POLICIES))`.

---

## crawler-fullcrawl

**Modul:** [`src/crawler/FullCrawl.py`](src/crawler/FullCrawl.py)  
**Features/Storys:** C-09, H-01, F-05  
**Aufgabe und Abgrenzung:** Vollständiger Durchlauf der angezeigten Ergebnismenge mit Preflight und Checkpoints; live durch Policy gesperrt. Verarbeitet ganze Seiten, prüft explizite Endregel und Anbieterlimit. Setzt completeness_verified weiterhin auf False; keine automatische Unterteilung von Suchanfragen.

**Direkte Abhängigkeiten:** `from pathlib import Path`; `from ProjectPaths import checkpoint_file`; `from AsyncStrategyExecutor import AsyncStrategyExecutor`; `from CrawlCheckpoint import CrawlCheckpoint`; `from BrowserUse import measure`; `from ExecutionPolicy import get_policy, has_policy`; `from StrategyExecutor import ExecutionError`; `from StrategyStore import content_digest`; `from PaginationValidator import PaginationValidator`.

**Definitionen:** 1 Klassen, 11 Funktionen/Methoden (inkl. lokaler Definitionen).

#### `full_crawl_plan`

**Quellcode:** [FullCrawl.py:15–97](src/crawler/FullCrawl.py#L15-L97).

```python
def full_crawl_plan(store, report, parameters, expected, start_url, downloads=False, authorized=False, multi_company_authorized=False):
```

**Aufgabe:** Read-only-Preflight: prüft aktive zertifizierte Strategie, passende Parameter/Filter/Hash/URL, unabhängigen Paginierungsnachweis mit Endregel und späteren Downloads, Betreiberattestation und Policy. Liefert Plan samt Blockern, Limits und ready; keine Browseraktion.

**Parameter:** `store`: StrategyStore-Instanz; `report`: strukturiertes Berichts-Dictionary; `parameters`: Such-/Auftragsparameter laut Strategie; `expected`: erwarteter Wert bzw. erwartete Felder/Anzahl je Schnittstelle; `start_url`: Start-URL der Suche; `downloads`: Dokumentdownload aktivieren; `authorized`: explizite Autorisierungsbestätigung; keine automatische Providerfreigabe; `multi_company_authorized`: explizite Attestation für mehrere Unternehmen. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `dict(mode='all_results', ready=not blockers, blockers=blockers, domain=store.domain, strategy_version=version, strategy_sha256=report.get('strategy_sha256'), activation_revision=revision, s…`.

**Explizite Fehler / Abbruch:**

- `ValueError('Reference mismatch')`

**Relevante Aufrufe:** `store.certified_active`, `store.load`.

### Klasse `FullResultsExecutor`

**Quellcode:** [FullCrawl.py:100–273](src/crawler/FullCrawl.py#L100-L273).

**Aufgabe:** Spezialisierung des AsyncStrategyExecutor für vollständige angezeigte Ergebnismenge mit Single-writer-Checkpoint und zusätzlichen Vollmodusgrenzen.

**Basisklassen:** `AsyncStrategyExecutor`.

#### `FullResultsExecutor.__init__`

**Quellcode:** [FullCrawl.py:102–111](src/crawler/FullCrawl.py#L102-L111).

```python
def __init__(self, *args, checkpoint_path=None, **kwargs):
```

**Aufgabe:** Bindet optionalen Checkpoint-Pfad, verlangt genau einen Provider, übernimmt Policy und initialisiert Seitenergebnisse sowie Fehler-/Limitzustand.

**Parameter:** `checkpoint_path`: optionaler DB-Zielpfad; `args`: weitergereichte Positionsparameter; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Full mode requires exactly one configured provider')`

**Direkt gesetzter Zustand:** `self.checkpoint_path`, `self.checkpoint`, `self.policy`, `self.result_limit_detected`, `self.page_results`, `self.server_failure`.

#### `FullResultsExecutor._before_document`

**Quellcode:** [FullCrawl.py:113–115](src/crawler/FullCrawl.py#L113-L115).

```python
def _before_document(self, record, result):
```

**Aufgabe:** Speichert Downloadabsicht vor Dokumentaktion mit Timing.

**Parameter:** `record`: extrahierter Datensatz mit Schlüsselfeldern; `result`: Ergebnis-/Statusobjekt. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self.checkpoint.start_document`.

#### `FullResultsExecutor._after_document`

**Quellcode:** [FullCrawl.py:117–119](src/crawler/FullCrawl.py#L117-L119).

```python
def _after_document(self, record, result):
```

**Aufgabe:** Persistiert Ergebnis nach Dokumentaktion mit Timing.

**Parameter:** `record`: extrahierter Datensatz mit Schlüsselfeldern; `result`: Ergebnis-/Statusobjekt. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self.checkpoint.finish_document`.

#### `FullResultsExecutor._check_run_limits`

**Quellcode:** [FullCrawl.py:121–125](src/crawler/FullCrawl.py#L121-L125).

```python
def _check_run_limits(self, max_companies, max_pages):
```

**Aufgabe:** Prüft Vollmodusgrenzen gegen Policy statt normale Kandidatengrenzen.

**Parameter:** `max_companies`: Obergrenze für Datensätze; `max_pages`: Obergrenze für Ergebnisseiten. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Full crawl must use provider safety limits')`
- `ValueError('Invalid full crawl safety limits')`

#### `FullResultsExecutor._response`

**Quellcode:** [FullCrawl.py:127–131](src/crawler/FullCrawl.py#L127-L131).

```python
def _response(self, response):
```

**Aufgabe:** Überwacht zusätzlich relevante Serverfehler zum gemeinsamen Sperrzustand.

**Parameter:** `response`: API-/HTTP-Response-Objekt entsprechend Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.server_failure`.

#### `FullResultsExecutor._check_access`

**Quellcode:** [FullCrawl.py:133–136](src/crawler/FullCrawl.py#L133-L136).

```python
async def _check_access(self):
```

**Aufgabe:** Erweitert Zugriffsschutz um erfassten Serverfehler.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'HTTP {self.server_failure}: server error during full crawl; stop')`

#### `FullResultsExecutor._inspect_result_limit`

**Quellcode:** [FullCrawl.py:138–142](src/crawler/FullCrawl.py#L138-L142).

```python
async def _inspect_result_limit(self):
```

**Aufgabe:** Sucht konfigurierten Anbieter-Hinweis auf begrenzte Ergebnismenge und protokolliert ihn.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.result_limit_detected`.

**Relevante Aufrufe:** `self.page.get_by_text`, `self.page.get_by_text(marker, exact=False).filter`.

#### `FullResultsExecutor._collect`

**Quellcode:** [FullCrawl.py:144–230](src/crawler/FullCrawl.py#L144-L230).

```python
async def _collect(self, max_companies, max_pages, downloads):
```

**Aufgabe:** Verarbeitet ganze Seiten: Signatur, Zeilen, Controls und Budget prüfen; Checkpoint vor Dokumenten schreiben; Seite erst nach allen Ergebnissen abschließen. Prüft stabilen Endzustand. Kein Aufteilen der Suche.

**Parameter:** `max_companies`: Obergrenze für Datensätze; `max_pages`: Obergrenze für Ergebnisseiten; `downloads`: Dokumentdownload aktivieren. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `'empty_results'`; `'safety_page_limit'`; `'safety_company_limit'`; `'safety_document_limit'`; `self._pagination_stop_reason()`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Unexpected or contradictory empty state during full crawl')`
- `ExecutionError('No result rows; end not verified')`
- `ExecutionError('Duplicate or unstable page keys; stop before processing page')`
- `ExecutionError('Row identity changed during page extraction')`
- `ExecutionError('Document control disabled; stop before processing page')`
- `ExecutionError('Page identity changed during extraction')`
- `ExecutionError('Page document count mismatch')`
- `ExecutionError('Page identity changed after processing')`
- `ExecutionError('Pagination state unstable')`
- `ExecutionError('Page identity changed during end verification')`
- `ExecutionError('Pagination state changed before advancing')`

**Direkt gesetzter Zustand:** `self.failure_stage`, `self.step`, `self.pages`.

**Relevante Aufrufe:** `self._check_access`, `self._inspect_result_limit`, `self._key`, `self._next_page`, `self._page_signature`, `self._pagination_ready`, `self._pagination_stop_reason`, `self._pool`, `self._record`, `self._rows`, `self._unique`, `self._wait_visible`, `self.checkpoint.finish_page`, `self.checkpoint.save_page`.

#### `FullResultsExecutor.run_full`

**Quellcode:** [FullCrawl.py:232–270](src/crawler/FullCrawl.py#L232-L270).

```python
async def run_full(self, start_url, crawl_id, plan, downloads=False, **kwargs):
```

**Aufgabe:** Verlangt eingeschaltete Provider-Policy und passenden ready-Plan, erstellt neue DB, ruft asynchronen Executor mit Vollmodusgrenzen und einem Worker auf. Erzeugt Coverage-/Checkpoint-Bericht, finalisiert oder markiert Fehler; completeness_verified bleibt false.

**Parameter:** `start_url`: Start-URL der Suche; `crawl_id`: Auftrags-/Lauf-ID; `plan`: Preflight-/Resume-Plan; `downloads`: Dokumentdownload aktivieren; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `result`.

**Explizite Fehler / Abbruch:**

- `ValueError('Full live execution disabled by provider policy')`
- `ValueError('Matching successful preflight required')`
- `ValueError('Explicit terminal condition required')`
- `erneutes Auslösen der aktuellen Exception`

**Direkt gesetzter Zustand:** `self.checkpoint`.

**Relevante Aufrufe:** `self.checkpoint.close`, `self.checkpoint.finish`.

#### `FullResultsExecutor.run`

**Quellcode:** [FullCrawl.py:272–273](src/crawler/FullCrawl.py#L272-L273).

```python
async def run(self, *args, **kwargs):
```

**Aufgabe:** Verweigert normalen run-Aufruf; erzwingt run_full mit Preflight.

**Parameter:** `args`: weitergereichte Positionsparameter; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Use run_full with preflight; ordinary runs use AsyncStrategyExecutor')`

---

## crawler-openaiclient

**Modul:** [`src/crawler/OpenAIClient.py`](src/crawler/OpenAIClient.py)  
**Features/Storys:** A-01, B-01, C-04, C-08  
**Aufgabe und Abgrenzung:** Wrapper der Responses API und Weiterleitung an BrowserUse; lokales Usage-/Kostenlogging. Web-Search-Zweig existiert noch im Quellcode, ist aber aus der Zielarchitektur ausgeschlossen und darf im Company-Betrieb nicht verwendet werden. Preistabelle lokal, nicht automatisch aktuell.

**Direkte Abhängigkeiten:** `import csv`; `import time`; `from datetime import datetime, timezone`; `from pathlib import Path`; `from ProjectPaths import USAGE_FILE`; `from openai import OpenAI`; `from uuid import uuid4`.

**Definitionen:** 1 Klassen, 3 Funktionen/Methoden (inkl. lokaler Definitionen).

### Klasse `OpenAIClient`

**Quellcode:** [OpenAIClient.py:11–129](src/crawler/OpenAIClient.py#L11-L129).

**Aufgabe:** Zustandsbehafteter SDK-Wrapper mit Logpfad und lokaler Modell-Preistabelle.

**Klassenattribute / Konfiguration:**

- `PRICES = {'gpt-6-luna': {'input': 0.1, 'cached_input': 0.01, 'output': 0.5, 'web_search': 0.01}}`

#### `OpenAIClient.__init__`

**Quellcode:** [OpenAIClient.py:18–20](src/crawler/OpenAIClient.py#L18-L20).

```python
def __init__(self, log_path=USAGE_FILE):
```

**Aufgabe:** Erstellt OpenAI-SDK-Client aus Umgebungskonfiguration und speichert Logpfad.

**Parameter:** `log_path`: Zielpfad des Logs. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.client`, `self.log_path`.

#### `OpenAIClient.create`

**Quellcode:** [OpenAIClient.py:22–65](src/crawler/OpenAIClient.py#L22-L65).

```python
def create(self, model, prompt, crawl_id=None, web_search=False, domains=None, schema=None, browser_use=False, start_url=None, max_steps=20, headless=False, **kwargs):
```

**Aufgabe:** Delegiert bei browser_use an run_browser, andernfalls Responses-API-Aufruf mit optional strengem JSON-Schema. Historischer Web-Search-Zweig und Ausschluss der Kombination mit BrowserUse sind noch implementiert, aber nicht für Zielbetrieb zulässig. Protokolliert Verbrauch und Dauer.

**Parameter:** `model`: Modellkennung; `prompt`: Eingabe für LLM-Aufruf; `crawl_id`: Auftrags-/Lauf-ID; `web_search`: historischer Tool-Schalter; im Zielbetrieb nicht zulässig; `domains`: erlaubte Domainliste; `schema`: JSON-Schema-Vertrag; `browser_use`: Browser-Loop verwenden; `start_url`: Start-URL der Suche; `max_steps`: maximale Anzahl API-Anfragen im Browser-Loop; `headless`: Browser ohne sichtbares Fenster starten; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `run_browser(self, model, prompt, crawl_id, schema, domains, start_url, max_steps=max_steps, headless=headless, **kwargs)`; `response`.

**Explizite Fehler / Abbruch:**

- `ValueError('Browser Use and Web Search cannot be combined in this pilot')`

**Relevante Aufrufe:** `self._log_usage`, `self.client.responses.create`.

#### `OpenAIClient._log_usage`

**Quellcode:** [OpenAIClient.py:67–129](src/crawler/OpenAIClient.py#L67-L129).

```python
def _log_usage(self, response, crawl_id, duration):
```

**Aufgabe:** Liest Usage, Cached Input, Output und historische Suchaufrufe; berechnet Kosten nur für bekannte Modellpreise. Schreibt CSV, legt Elternpfad bei Bedarf an; fehlende Preise bleiben leer. Bei fehlender usage kein Datensatz.

**Parameter:** `response`: API-/HTTP-Response-Objekt entsprechend Kontext; `crawl_id`: Auftrags-/Lauf-ID; `duration`: gemessene Dauer in Sekunden. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Relevante Aufrufe:** `self.log_path.exists`, `self.log_path.open`, `self.log_path.parent.mkdir`, `self.log_path.stat`, `writer.writeheader`, `writer.writerow`.

---

## crawler-paginationvalidator

**Modul:** [`src/crawler/PaginationValidator.py`](src/crawler/PaginationValidator.py)  
**Features/Storys:** F-03, F-04  
**Aufgabe und Abgrenzung:** Mehrseitige Validierung in zwei unabhängigen Browserkontexten, aktuell positions- und signaturgebunden. Technischer Modus ohne unabhängige Referenz bleibt partiell; selbst bestandene Prüfung aktiviert keine Strategie und erlaubt keinen Vollcrawl.

**Direkte Abhängigkeiten:** `import asyncio`; `import time`; `from pathlib import Path`; `from ProjectPaths import VALIDATION_DOCUMENTS_DIR, VALIDATION_TIMING_FILE`; `from uuid import uuid4`; `from AsyncStrategyExecutor import AsyncStrategyExecutor`; `from ErrorClassifier import ErrorClassifier`; `from StrategyExecutor import ExecutionError`; `from StrategyStore import content_digest`; `from StrategyValidator import StrategyValidator, compare_records, verify_file`.

**Definitionen:** 2 Klassen, 7 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `MAX_PAGES`, `MAX_ROWS`.

### Klasse `PaginationValidationExecutor`

**Quellcode:** [PaginationValidator.py:19–113](src/crawler/PaginationValidator.py#L19-L113).

**Aufgabe:** Asynchrone Validierungs-Spezialisierung mit kontrolliertem Seitenwechsel und optionalem späteren Dokumentensatz.

**Basisklassen:** `AsyncStrategyExecutor`.

#### `PaginationValidationExecutor.__init__`

**Quellcode:** [PaginationValidator.py:20–24](src/crawler/PaginationValidator.py#L20-L24).

```python
def __init__(self, *args, samples, expect_end, prefixes, prior_pages=None, **kwargs):
```

**Aufgabe:** Bindet Seitenstichproben, erwarteten Endzustand, Dokumentpräfixe und optional frühere Sitzungsseiten an den Async-Executor.

**Parameter:** `samples`: erwartete Seitenstichproben; `expect_end`: erwarteter bestätigter Endzustand; `prefixes`: erwartete Dateinamenspräfixe; `prior_pages`: Beobachtungen aus vorheriger Sitzung; `args`: weitergereichte Positionsparameter; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.samples`, `self.expect_end`, `self.prefixes`, `self.prior_pages`, `self.page_checks`.

#### `PaginationValidationExecutor._collect`

**Quellcode:** [PaginationValidator.py:26–113](src/crawler/PaginationValidator.py#L26-L113).

```python
async def _collect(self, max_companies, max_pages, downloads):
```

**Aufgabe:** Extrahiert vollständige Seiten, prüft Stichproben, Schlüssel, Controls und stabile Felder/Signaturen, optional Endnachweis und späteren Download. Vergleicht gegebenenfalls vorherige Sitzung, begrenzt Scope.

**Parameter:** `max_companies`: Obergrenze für Datensätze; `max_pages`: Obergrenze für Ergebnisseiten; `downloads`: Dokumentdownload aktivieren. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `'page_limit' if ready else self._pagination_stop_reason()`; `'end_of_results' if self.expect_end else 'page_limit'`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Validation scope mismatch')`
- `ExecutionError('Pagination validation row budget exceeded or no result rows')`
- `ExecutionError(f"Page {sample['page']}: row count differs from independent reference")`
- `ExecutionError('Duplicate record key during pagination validation')`
- `ExecutionError('Validation document control disabled')`
- `ExecutionError('Page identity changed during validation')`
- `ExecutionError('Page content differs between independent validation sessions')`
- `ExecutionError('Unexpected end before all requested validation pages')`
- `ExecutionError('Pagination state unstable on final sample page')`
- `ExecutionError('Expected final-page marker not verified')`
- `ExecutionError('Unexpected terminal state at non-final reference page')`
- `ExecutionError('Final sample page identity changed')`
- `ExecutionError('Later-page document status or identity mismatch')`
- `ExecutionError('Pagination state changed after sample download')`
- `ExecutionError('Page identity changed after sample download')`
- `ExecutionError('No validation pages processed')`

**Direkt gesetzter Zustand:** `self.failure_stage`, `self.pages`, `self.step`.

**Relevante Aufrufe:** `self._check_access`, `self._key`, `self._next_page`, `self._page_signature`, `self._pagination_ready`, `self._pagination_stop_reason`, `self._pool`, `self._record`, `self._rows`, `self._unique`, `self._wait_visible`, `self.locator`, `self.page.wait_for_timeout`, `self.seen.add`.

### Klasse `PaginationValidator`

**Quellcode:** [PaginationValidator.py:116–251](src/crawler/PaginationValidator.py#L116-L251).

**Aufgabe:** Orchestriert mehrseitige unabhängige Referenz-/Technikprüfung; erzeugt keinen StrategyStore-Freigabenachweis.

#### `PaginationValidator.__init__`

**Quellcode:** [PaginationValidator.py:117–122](src/crawler/PaginationValidator.py#L117-L122).

```python
def __init__(self, store, policy, cookie_dialog=None, open_controls=(), headless=False, executable_path=None, executor_factory=PaginationValidationExecutor, output_root=VALIDATION_DOCUMENTS_DIR, timing_path=VALIDATION_TIMING_FILE):
```

**Aufgabe:** Bindet Store, Policy, Browser-/Cookieoptionen, injizierbare Executor-Factory und Evidence-/Timing-Pfade.

**Parameter:** `store`: StrategyStore-Instanz; `policy`: ExecutionPolicy-Instanz; `cookie_dialog`: explizite Dialogkonfiguration; `open_controls`: konfigurierte Menüöffner; `headless`: Browser ohne sichtbares Fenster starten; `executable_path`: optionaler Chromium-Binärpfad; `executor_factory`: injizierbare Executor-Klasse/Factory; `output_root`: Wurzelverzeichnis für Validierungsbelege; `timing_path`: Pfad zum Timing-Log. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.store`, `self.policy`, `self.cookie_dialog`, `self.open_controls`, `self.headless`, `self.executable_path`, `self.executor_factory`, `self.output_root`, `self.timing_path`.

#### `PaginationValidator.check_reference`

**Quellcode:** [PaginationValidator.py:125–158](src/crawler/PaginationValidator.py#L125-L158).

```python
@staticmethod
def check_reference(strategy, reference):
```

**Aufgabe:** Validiert manuell bestätigte v2-Referenz, Parameter/Filter, Seitenfolge, Zeilenanzahlen, unabhängige Stichproben und End-/Dokumenterwartungen.

**Parameter:** `strategy`: Strategie-Dictionary nach StrategySchema; `reference`: unabhängige Referenzdaten. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(parameters, expected, pages, expect_end, prefixes)`.

**Explizite Fehler / Abbruch:**

- `ValueError('Manually confirmed independent pagination reference (version 2) required')`
- `ValueError('Strategy has no pagination rule')`
- `ValueError('Provide two or three consecutive reference pages and explicit expect_end')`
- `ValueError('Verified end requires a schema v3 strategy with an explicit end rule')`
- `ValueError('Each page requires its observed row count and first two or three records (one if singleton)')`
- `ValueError('Pagination validation limited to 100 result rows in total per session')`
- `ValueError('Duplicate reference keys across pages')`

#### `PaginationValidator.validate_technical`

**Quellcode:** [PaginationValidator.py:160–163](src/crawler/PaginationValidator.py#L160-L163).

```python
async def validate_technical(self, version, parameters, expected_fields, pages=2, authorized=False):
```

**Aufgabe:** Begrenzter Read-only-Check ohne unabhängige Referenz, zwei/drei Seiten; bleibt fachlich partiell und ohne Download-/Vollcrawl-Freigabe.

**Parameter:** `version`: Strategieversionsnummer; `parameters`: Such-/Auftragsparameter laut Strategie; `expected_fields`: erwartete Feldwerte/Filter; `pages`: Anzahl zu prüfender Seiten; `authorized`: explizite Autorisierungsbestätigung; keine automatische Providerfreigabe. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `await self._validate(version, None, authorized, False, technical_scope=(parameters, expected_fields, pages))`.

**Relevante Aufrufe:** `self._validate`.

#### `PaginationValidator.validate`

**Quellcode:** [PaginationValidator.py:165–166](src/crawler/PaginationValidator.py#L165-L166).

```python
async def validate(self, version, reference, authorized=False, downloads_authorized=False):
```

**Aufgabe:** Startet unabhängige referenzbasierte Paginierungsprüfung mit expliziten Autorisierungsflags.

**Parameter:** `version`: Strategieversionsnummer; `reference`: unabhängige Referenzdaten; `authorized`: explizite Autorisierungsbestätigung; keine automatische Providerfreigabe; `downloads_authorized`: explizite Bestätigung für Stichproben-Downloads. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `await self._validate(version, reference, authorized, downloads_authorized)`.

**Relevante Aufrufe:** `self._validate`.

#### `PaginationValidator._validate`

**Quellcode:** [PaginationValidator.py:168–251](src/crawler/PaginationValidator.py#L168-L251).

```python
async def _validate(self, version, reference, authorized, downloads_authorized, technical_scope=None):
```

**Aufgabe:** Gemeinsame Orchestrierung zweier frischer Sitzungen; prüft Ergebnisse, Stabilität, Endnachweis, optionale Dokumente und liefert Bericht mit missing_checks; all_results_authorized bleibt false.

**Parameter:** `version`: Strategieversionsnummer; `reference`: unabhängige Referenzdaten; `authorized`: explizite Autorisierungsbestätigung; keine automatische Providerfreigabe; `downloads_authorized`: explizite Bestätigung für Stichproben-Downloads; `technical_scope`: technischer Probeumfang ohne unabhängige Referenz. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `report`.

**Explizite Fehler / Abbruch:**

- `ValueError('Explicit authorization for bounded multi-page validation searches required')`
- `ValueError('Technical pagination validation requires two or three pages')`
- `ValueError('Strategy has no pagination rule')`
- `ValueError('Search parameters must match strategy declaration')`
- `ValueError('Expected search filters must be nonempty stable strategy fields')`
- `ValueError('Pagination validation execution failed: ' + str(result.get('error'))[:350])`
- `ValueError('Unexpected validation scope or result')`
- `ValueError('Pagination terminal state differs between independent validation sessions')`
- `ValueError('Strategy or activation revision changed during pagination validation')`

**Relevante Aufrufe:** `asyncio.wait_for`, `executor.run`, `report.update`, `self.check_reference`, `self.executor_factory`, `self.store.validation_snapshot`.

---

## crawler-projectpaths

**Modul:** [`src/crawler/ProjectPaths.py`](src/crawler/ProjectPaths.py)  
**Features/Storys:** H-02  
**Aufgabe und Abgrenzung:** Zentrale absolute Pfade aus dem Modulstandort. Lesekompatibilität für alte flache Ablagen, Konfliktkontrollen und sichere Checkpoint-Dateinamen. Import erzeugt keine Verzeichnisse.

**Direkte Abhängigkeiten:** `from pathlib import Path`; `import re`.

**Definitionen:** 0 Klassen, 4 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `ROOT_DIR`, `STRATEGIES_DIR`, `DOCUMENTS_DIR`, `VALIDATION_DOCUMENTS_DIR`, `REFERENCES_DIR`, `RESULTS_DIR`, `EXECUTIONS_DIR`, `LEGACY_EXECUTIONS_DIR`, `DISCOVERY_DIR`, `VALIDATION_DIR`, `RECOVERY_DIR`, `CHECKPOINTS_DIR`, `METRICS_DIR`, `BENCHMARK_DIR`, `USAGE_FILE`, `USAGE_JSONL_FILE`, `BROWSER_TIMING_FILE`, `VALIDATION_TIMING_FILE`, `DOCUMENTS_METRICS_FILE`, `DOWNLOAD_QUEUE_FILE`, `REPORT_FOLDERS`.

#### `report_directory`

**Quellcode:** [ProjectPaths.py:30–31](src/crawler/ProjectPaths.py#L30-L31).

```python
def report_directory(suffix, results=RESULTS_DIR):
```

**Aufgabe:** Ordnet bekannten Report-Suffix einem kanonischen Ergebnisunterordner zu; unbekannter Suffix führt zu KeyError.

**Parameter:** `suffix`: Berichts-Suffix. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `Path(results) / REPORT_FOLDERS[suffix]`.

#### `report_files`

**Quellcode:** [ProjectPaths.py:34–43](src/crawler/ProjectPaths.py#L34-L43).

```python
def report_files(results, suffix):
```

**Aufgabe:** Sammelt flache und kategorisierte Reports desselben Suffixes; gleiche Namen mit gleichen Bytes einmal, widersprüchliche Kopien Fehler.

**Parameter:** `suffix`: Berichts-Suffix. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `sorted(paths.values())`.

**Explizite Fehler / Abbruch:**

- `ValueError(f'Conflicting reports: {paths[path.name]} and {path}')`

**Relevante Aufrufe:** `path.read_bytes`.

#### `metric_inputs`

**Quellcode:** [ProjectPaths.py:46–57](src/crawler/ProjectPaths.py#L46-L57).

```python
def metric_inputs(names, root=ROOT_DIR):
```

**Aufgabe:** Sucht kanonische und alte Logpfade in vorgegebener Reihenfolge; identische Kopien nicht doppelt zählen, Konflikte melden.

**Parameter:** `names`: Liste von Dateinamen; `root`: erlaubter Wurzelpfad. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `found`.

**Explizite Fehler / Abbruch:**

- `ValueError(f'Conflicting metric logs for {name}: {paths}; specify explicit input paths')`

#### `checkpoint_file`

**Quellcode:** [ProjectPaths.py:60–63](src/crawler/ProjectPaths.py#L60-L63).

```python
def checkpoint_file(crawl_id, directory=CHECKPOINTS_DIR):
```

**Aufgabe:** Baut sicheren .sqlite3-Pfad aus Crawl-ID; erlaubt ausschließlich Buchstaben, Ziffern, Unterstrich und Bindestrich.

**Parameter:** `crawl_id`: Auftrags-/Lauf-ID; `directory`: Verzeichnis der Eingaben/Ausgaben. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `Path(directory) / f'{crawl_id}.sqlite3'`.

**Explizite Fehler / Abbruch:**

- `ValueError('Invalid crawl ID for checkpoint filename')`

---

## crawler-recoverymanager

**Modul:** [`src/crawler/RecoveryManager.py`](src/crawler/RecoveryManager.py)  
**Features/Storys:** C-08, F-01  
**Aufgabe und Abgrenzung:** Zentrale Recovery-Entscheidung nach klassifiziertem Fehler und passender Provenienz. Read-only-Strukturprüfung, lokale Sperre und reserviertes einmaliges Reparaturbudget pro Strategieversion. Speichert höchstens neuen Kandidaten, aktiviert oder resumed niemals automatisch.

**Direkte Abhängigkeiten:** `import fcntl`; `import hashlib`; `import json`; `import os`; `from uuid import uuid4`; `from ErrorClassifier import ErrorClassifier`; `from StructureVerifier import repair_target`.

**Definitionen:** 1 Klassen, 4 Funktionen/Methoden (inkl. lokaler Definitionen).

#### `strategy_digest`

**Quellcode:** [RecoveryManager.py:12–14](src/crawler/RecoveryManager.py#L12-L14).

```python
def strategy_digest(strategy):
```

**Aufgabe:** Kanonischer JSON-SHA-256 der Strategie zur Provenienzprüfung.

**Parameter:** `strategy`: Strategie-Dictionary nach StrategySchema. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `hashlib.sha256(data.encode('utf-8')).hexdigest()`.

**Relevante Aufrufe:** `hashlib.sha256`, `hashlib.sha256(data.encode('utf-8')).hexdigest`, `json.dumps`.

### Klasse `RecoveryManager`

**Quellcode:** [RecoveryManager.py:17–108](src/crawler/RecoveryManager.py#L17-L108).

**Aufgabe:** Koordiniert klassifikationsgesteuerte und lokal begrenzte Recovery.

#### `RecoveryManager.__init__`

**Quellcode:** [RecoveryManager.py:18–19](src/crawler/RecoveryManager.py#L18-L19).

```python
def __init__(self, store, policy, verifier, repair):
```

**Aufgabe:** Bindet Store, Policy, unabhängigen Verifier und Repair-Komponente.

**Parameter:** `store`: StrategyStore-Instanz; `policy`: ExecutionPolicy-Instanz; `verifier`: unabhängige Strukturprüfkomponente; `repair`: Komponente für begrenzten Reparaturvorschlag. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.store`, `self.policy`, `self.verifier`, `self.repair`.

#### `RecoveryManager._reserve`

**Quellcode:** [RecoveryManager.py:22–27](src/crawler/RecoveryManager.py#L22-L27).

```python
@staticmethod
def _reserve(path, data):
```

**Aufgabe:** Erstellt exklusiven persistenten Budgetnachweis und synchronisiert Datei vor API-Aufruf; Absturz verbraucht Versuch.

**Parameter:** `path`: Datei-/Verzeichnispfad gemäß Funktionszweck; `data`: zu verarbeitende Daten. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `file.fileno`, `file.flush`, `json.dump`, `os.fsync`, `path.open`.

#### `RecoveryManager.recover`

**Quellcode:** [RecoveryManager.py:29–108](src/crawler/RecoveryManager.py#L29-L108).

```python
async def recover(self, report, authorized=False, repair_enabled=False):
```

**Aufgabe:** Klassifiziert Report, prüft Autorisierung, Version/Hash/Parameter und Reparaturziel, erwirbt lokalen Lock. Read-only-Verifikation; nur bei bestätigter Struktur und enabled Reparaturbudget reservieren und höchstens einen Kandidaten speichern. Liefert Recovery-Report, keine Aktivierung oder Fortsetzung.

**Parameter:** `report`: strukturiertes Berichts-Dictionary; `authorized`: explizite Autorisierungsbestätigung; keine automatische Providerfreigabe; `repair_enabled`: expliziter Schalter für begrenzte KI-Reparatur. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `result`.

**Relevante Aufrufe:** `fcntl.flock`, `self._reserve`, `self.repair.propose`, `self.store.load`, `self.store.save`, `self.verifier.verify`.

---

## crawler-resumeplanner

**Modul:** [`src/crawler/ResumePlanner.py`](src/crawler/ResumePlanner.py)  
**Features/Storys:** H-03  
**Aufgabe und Abgrenzung:** Begrenzte Wiederaufnahme aus bekanntem einseitigem Execution-Report, nicht aus SQLite. Prüft Strategie, vorhandene Dateien und unveränderte Reihen-/Feldidentität; nur nie versuchte Dokumente. Unklare, gescheiterte oder server-/zugriffsbezogene Fälle werden nicht blind wiederholt.

**Direkte Abhängigkeiten:** `import copy`; `import json`; `import os`; `from pathlib import Path`; `from ProjectPaths import DOCUMENTS_DIR`; `from uuid import UUID, uuid4`; `from AsyncStrategyExecutor import AsyncStrategyExecutor`; `from ErrorClassifier import ErrorClassifier`; `from StrategyStore import content_digest`; `from StrategyValidator import compare_records, verify_file`; `from StructureVerifier import replace_locator`.

**Definitionen:** 2 Klassen, 5 Funktionen/Methoden (inkl. lokaler Definitionen).

### Klasse `ResumeExecutor`

**Quellcode:** [ResumePlanner.py:16–41](src/crawler/ResumePlanner.py#L16-L41).

**Aufgabe:** Async-Spezialisierung für bereits geplante einseitige Fortsetzung; kein allgemeiner Checkpoint-Resume.

**Basisklassen:** `AsyncStrategyExecutor`.

#### `ResumeExecutor.__init__`

**Quellcode:** [ResumePlanner.py:17–19](src/crawler/ResumePlanner.py#L17-L19).

```python
def __init__(self, *args, plan, **kwargs):
```

**Aufgabe:** Initialisiert den Async-Executor und bindet einen vorab geprüften Resume-Plan.

**Parameter:** `plan`: Preflight-/Resume-Plan; `args`: weitergereichte Positionsparameter; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.plan`.

#### `ResumeExecutor._collect`

**Quellcode:** [ResumePlanner.py:21–41](src/crawler/ResumePlanner.py#L21-L41).

```python
async def _collect(self, max_companies, max_pages, downloads):
```

**Aufgabe:** Extrahiert bekannte Stichprobe erneut, prüft vollständige Übereinstimmung, behält bestätigte Dokumente und verarbeitet nur geplante nie versuchte Dokumente.

**Parameter:** `max_companies`: Obergrenze für Datensätze; `max_pages`: Obergrenze für Ergebnisseiten; `downloads`: Dokumentdownload aktivieren. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `reason`.

**Explizite Fehler / Abbruch:**

- `ValueError('Uncertain document cannot be resumed')`

**Direkt gesetzter Zustand:** `self.failure_stage`.

**Relevante Aufrufe:** `self._check_access`, `self._check_row`, `self._pool`, `self._rows`.

### Klasse `ResumePlanner`

**Quellcode:** [ResumePlanner.py:44–168](src/crawler/ResumePlanner.py#L44-L168).

**Aufgabe:** Prüft bekannte Report-Provenienz und Dokumentzustände, erstellt konservativen Plan und kann ihn explizit ausführen.

#### `ResumePlanner.__init__`

**Quellcode:** [ResumePlanner.py:45–46](src/crawler/ResumePlanner.py#L45-L46).

```python
def __init__(self, store, document_root=DOCUMENTS_DIR):
```

**Aufgabe:** Bindet StrategyStore und erlaubten Dokumentwurzelpfad.

**Parameter:** `store`: StrategyStore-Instanz. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.store`, `self.document_root`.

#### `ResumePlanner.build`

**Quellcode:** [ResumePlanner.py:48–131](src/crawler/ResumePlanner.py#L48-L131).

```python
def build(self, report):
```

**Aufgabe:** Prüft Report, aktive zertifizierte Strategie, Fehlerkategorie, bekannte Seite, Schlüsselfelder und Datei-Hashes. Plant ausschließlich not_attempted-Dokumente; unklare oder fehlerhafte Fälle blockieren.

**Parameter:** `report`: strukturiertes Berichts-Dictionary. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `plan`.

**Explizite Fehler / Abbruch:**

- `ValueError('Only structural failure may qualify; no retry of technical or access failures')`
- `ValueError('Canonical source crawl ID required')`
- `ValueError('Source report and certified active scope do not match')`
- `ValueError('Record or document contract changed')`
- `ValueError('Active version is not a supported single-locator repair of source strategy')`
- `ValueError('No known one-page sample to resume; new explicitly authorized crawl required')`
- `ValueError('Uncertain worker state; manual review required')`
- `ValueError('Missing or duplicate record identity')`
- `ValueError('Source document inventory changed')`
- `ValueError('Failed or uncertain document; no automatic re-request')`
- `ValueError('Source attempt counters do not support safe continuation')`

**Relevante Aufrufe:** `executor._key`, `self.store.certified_active`, `self.store.load`.

#### `ResumePlanner.execute`

**Quellcode:** [ResumePlanner.py:133–168](src/crawler/ResumePlanner.py#L133-L168).

```python
async def execute(self, report, authorized=False, multi_company_authorized=False, headless=False, cookie_dialog=None, open_controls=(), executable_path=None):
```

**Aufgabe:** Baut Plan, verlangt Autorisierung und reserviert persistenten einmaligen Versuch; startet begrenzten ResumeExecutor mit passenden Parametern. Kein seitenübergreifender Resume und kein Blind-Retry.

**Parameter:** `report`: strukturiertes Berichts-Dictionary; `authorized`: explizite Autorisierungsbestätigung; keine automatische Providerfreigabe; `multi_company_authorized`: explizite Attestation für mehrere Unternehmen; `headless`: Browser ohne sichtbares Fenster starten; `cookie_dialog`: explizite Dialogkonfiguration; `open_controls`: konfigurierte Menüöffner; `executable_path`: optionaler Chromium-Binärpfad. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `result`.

**Explizite Fehler / Abbruch:**

- `ValueError('Explicit authorization for resumed document requests required')`
- `ValueError(f"Resume unavailable: {plan['reason']}")`
- `ValueError('Multi-company document authorization required')`
- `ValueError('Active strategy changed; rebuild resume plan')`

**Relevante Aufrufe:** `executor.run`, `file.fileno`, `file.flush`, `json.dump`, `os.fsync`, `self.build`, `self.store.certified_active`.

---

## crawler-strategyexecutor

**Modul:** [`src/crawler/StrategyExecutor.py`](src/crawler/StrategyExecutor.py)  
**Features/Storys:** C-06, D-02, E-02, C-09  
**Aufgabe und Abgrenzung:** Synchroner, begrenzter deterministischer Executor. Validiert Strategie und Parameter, navigiert, extrahiert Felder, prüft Identität und lädt PDF/XML. SHA-256 für Originalbytes; 20 MiB Standardlimit und vollständiges read_bytes sind aktueller Zustand, E-05 soll ihn ändern.

**Direkte Abhängigkeiten:** `import hashlib`; `import time`; `from pathlib import Path`; `from ProjectPaths import DOCUMENTS_DIR, BROWSER_TIMING_FILE`; `from urllib.parse import urljoin, urlsplit`; `from uuid import uuid4`; `import regex`; `from defusedxml import ElementTree`; `from jsonschema import Draft202012Validator`; `from playwright.sync_api import sync_playwright, Error as PlaywrightError, TimeoutError as PlaywrightTimeoutError`; `from ErrorClassifier import attach_error_classification`; `from BrowserUse import allowed_url, measure, write_timings`; `from StrategySchema import STRATEGY_SCHEMA`.

**Definitionen:** 3 Klassen, 40 Funktionen/Methoden (inkl. lokaler Definitionen).

### Klasse `ExecutionError`

**Quellcode:** [StrategyExecutor.py:20–21](src/crawler/StrategyExecutor.py#L20-L21).

**Aufgabe:** Basisklasse für kontrollierte Ausführungsfehler; erbt RuntimeError.

**Basisklassen:** `RuntimeError`.

### Klasse `NavigationInterrupted`

**Quellcode:** [StrategyExecutor.py:24–25](src/crawler/StrategyExecutor.py#L24-L25).

**Aufgabe:** Spezialisierter Ausführungsfehler bei unterbrochenem Navigationszustand.

**Basisklassen:** `ExecutionError`.

### Klasse `StrategyExecutor`

**Quellcode:** [StrategyExecutor.py:28–787](src/crawler/StrategyExecutor.py#L28-L787).

**Aufgabe:** Zustandsbehafteter synchroner Executor. Hält Strategie, Parameter, Browserzustand, Messungen, extrahierte Datensätze und bereits beobachtete Schlüssel.

#### `StrategyExecutor.__init__`

**Quellcode:** [StrategyExecutor.py:29–49](src/crawler/StrategyExecutor.py#L29-L49).

```python
def __init__(self, strategy, parameters, domains, output_dir=DOCUMENTS_DIR, timeout_ms=10000, max_file_bytes=20 * 1024 * 1024, expected_fields=None, cookie_dialog=None, open_controls=()):
```

**Aufgabe:** Validiert Schema und Kandidatenstatus; initialisiert Parameter, Ressourcenlimits, Cookie-/Menüregeln, Zähler und vorbereitete Regex-Regeln. Öffnet noch keinen Browser.

**Parameter:** `strategy`: Strategie-Dictionary nach StrategySchema; `parameters`: Such-/Auftragsparameter laut Strategie; `domains`: erlaubte Domainliste; `output_dir`: Zielverzeichnis für Originaldateien; `timeout_ms`: Wartebudget in Millisekunden; `max_file_bytes`: maximale Dateigröße in Bytes; `expected_fields`: erwartete Feldwerte/Filter; `cookie_dialog`: explizite Dialogkonfiguration; `open_controls`: konfigurierte Menüöffner. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('A complete candidate strategy is required')`

**Direkt gesetzter Zustand:** `self.strategy`, `self.records`, `self.parameters`, `self.domains`, `self.output_dir`, `self.timeout_ms`, `self.max_file_bytes`, `self.expected_fields`, `self.cookie_dialog`, `self.open_controls`, `self.navigation_checks`, `self.menu_retries`, `self.cookie_handler_page`, `self.cookie_dialog_count`, `self.navigation_restarts`, `self.navigation_cookie_baseline`, `self.events`, `self.companies`, `self.warnings`, `self.step`, `self.pages`, `self.download_attempts`, `self.page`, `self.context`, `self.blocked`, `self.seen`, `self.pagination_end_evidence`, `self.patterns`.

**Relevante Aufrufe:** `self._check_strategy`.

#### `StrategyExecutor._check_strategy`

**Quellcode:** [StrategyExecutor.py:51–100](src/crawler/StrategyExecutor.py#L51-L100).

```python
def _check_strategy(self):
```

**Aufgabe:** Prüft exakte Parameterliste, Pflicht-/Schlüsselfelder, eindeutige Dokumenttypen, Sibling-Guards, Regex mit genau einer Capture-Gruppe sowie gültige Locator- und Navigationsreferenzen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Parameters must match the strategy declaration exactly')`
- `ValueError('All parameters must be non-empty strings')`
- `ValueError('Unique field names and non-empty unique keys required')`
- `ValueError('Every key field must exist and be required')`
- `ValueError('Expected field missing from strategy')`
- `ValueError('Document types must be unique and non-empty')`
- `ValueError('Adjacent fields require a scope guard')`
- `ValueError('Unknown field parameter')`
- `ValueError('Attribute name required')`
- `ValueError(f"Exactly one capture group required: {field['name']}")`
- `ValueError('Navigation value required')`
- `ValueError('Unknown navigation parameter')`
- `ValueError('Unexpected navigation value')`

#### `StrategyExecutor._check_strategy.walk`

**Quellcode:** [StrategyExecutor.py:82–90](src/crawler/StrategyExecutor.py#L82-L90).

```python
def walk(value):
```

**Aufgabe:** Lokale rekursive Schema-Traversierung; ruft _locator_args für alle Locator-Objekte auf, damit fehlerhafte Referenzen vor Browserstart auffallen.

**Parameter:** `value`: übergebener Wert gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self._locator_args`.

#### `StrategyExecutor._locator_args`

**Quellcode:** [StrategyExecutor.py:102–119](src/crawler/StrategyExecutor.py#L102-L119).

```python
def _locator_args(self, spec):
```

**Aufgabe:** Übersetzt CSS- oder Rollen-Locator in (kind, Wert, Name); löst Parameter-Namen auf und weist inkonsistente Angaben zurück.

**Parameter:** `spec`: Locator-, Dokument- oder Regeldefinition. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `('css', spec['selector'], None)`; `('role', spec['role'], name)`.

**Explizite Fehler / Abbruch:**

- `ValueError('Invalid CSS locator')`
- `ValueError('Invalid role locator')`
- `ValueError(f'Unknown locator parameter: {name}')`
- `ValueError('Unexpected locator name')`
- `ValueError('Literal locator name required')`

#### `StrategyExecutor.locator`

**Quellcode:** [StrategyExecutor.py:121–125](src/crawler/StrategyExecutor.py#L121-L125).

```python
def locator(self, root, spec):
```

**Aufgabe:** Erzeugt Playwright-Locator relativ zu page oder row. Rollenname wird exakt abgeglichen; führt keinen Klick aus.

**Parameter:** `root`: erlaubter Wurzelpfad; `spec`: Locator-, Dokument- oder Regeldefinition. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `root.locator('css=' + value)`; `root.get_by_role(value, name=name, exact=True) if name is not None else root.get_by_role(value)`.

**Relevante Aufrufe:** `self._locator_args`.

#### `StrategyExecutor._check_access`

**Quellcode:** [StrategyExecutor.py:127–137](src/crawler/StrategyExecutor.py#L127-L137).

```python
def _check_access(self):
```

**Aufgabe:** Bricht bei gespeicherter Zugriffssperre, unerlaubter URL oder sichtbaren Challenge-Signalen ab; keine umfassende CAPTCHA-Erkennung.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ExecutionError(self.blocked)`
- `ExecutionError('Page outside allowed domain')`
- `ExecutionError('Possible security challenge; stop')`
- `ExecutionError('Possible access restriction; stop')`

**Relevante Aufrufe:** `self.page.locator`, `self.page.title`.

#### `StrategyExecutor._response`

**Quellcode:** [StrategyExecutor.py:139–141](src/crawler/StrategyExecutor.py#L139-L141).

```python
def _response(self, response):
```

**Aufgabe:** Registriert HTTP 401/403/429 als Sperre für den weiteren Lauf.

**Parameter:** `response`: API-/HTTP-Response-Objekt entsprechend Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.blocked`.

#### `StrategyExecutor._unique`

**Quellcode:** [StrategyExecutor.py:143–149](src/crawler/StrategyExecutor.py#L143-L149).

```python
def _unique(self, locator, label, wait=False):
```

**Aufgabe:** Optional auf Sichtbarkeit warten; verlangt genau einen sichtbaren Treffer, andernfalls ExecutionError.

**Parameter:** `locator`: Playwright-Locator oder Locator-Regel gemäß Kontext; `label`: Bezeichnung für Diagnose/Fehlermeldung; `wait`: Wartebedingung bzw. Schalter für Sichtbarkeitsprüfung. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `locator`.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'{label}: expected one visible match, found {count}')`

**Relevante Aufrufe:** `self._wait_visible`.

#### `StrategyExecutor._wait`

**Quellcode:** [StrategyExecutor.py:151–162](src/crawler/StrategyExecutor.py#L151-L162).

```python
def _wait(self, wait):
```

**Aufgabe:** Führt die konfigurierte sichtbare/verborgene Postcondition aus und protokolliert Timing; None bedeutet keine Wartebedingung.

**Parameter:** `wait`: Wartebedingung bzw. Schalter für Sichtbarkeitsprüfung. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Relevante Aufrufe:** `self._check_access`, `self._wait_visible`, `self.locator`.

#### `StrategyExecutor._cookie_locator`

**Quellcode:** [StrategyExecutor.py:164–167](src/crawler/StrategyExecutor.py#L164-L167).

```python
def _cookie_locator(self):
```

**Aufgabe:** Erstellt den Locator für den konfigurierten Cookie-Dialog bzw. liefert keinen, wenn nicht konfiguriert.

**Rückgabe (Ausdrücke im Code):** `None`; `self.page.get_by_role('dialog', name=self.cookie_dialog['name'], exact=True)`.

**Relevante Aufrufe:** `self.page.get_by_role`.

#### `StrategyExecutor._cookie_button`

**Quellcode:** [StrategyExecutor.py:169–170](src/crawler/StrategyExecutor.py#L169-L170).

```python
def _cookie_button(self, dialog):
```

**Aufgabe:** Sucht die konfigurierte notwendige Einwilligungsoption innerhalb des Dialogs.

**Parameter:** `dialog`: Cookie-Dialog-Locator. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `dialog.get_by_role('button', name=self.cookie_dialog['necessary_button'], exact=True)`.

#### `StrategyExecutor._cookie_pending`

**Quellcode:** [StrategyExecutor.py:172–173](src/crawler/StrategyExecutor.py#L172-L173).

```python
def _cookie_pending(self, dialog):
```

**Aufgabe:** Prüft sichtbaren Dialog beziehungsweise noch sichtbare Aktion; berücksichtigt Wrapperzustände.

**Parameter:** `dialog`: Cookie-Dialog-Locator. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `bool(dialog.filter(visible=True).count() or self._cookie_button(dialog).filter(visible=True).count())`.

**Relevante Aufrufe:** `self._cookie_button`, `self._cookie_button(dialog).filter`.

#### `StrategyExecutor._handle_cookie_dialog`

**Quellcode:** [StrategyExecutor.py:175–201](src/crawler/StrategyExecutor.py#L175-L201).

```python
def _handle_cookie_dialog(self, from_handler=False):
```

**Aufgabe:** Behandelt ausschließlich konfigurierte Cookie-Einwilligung, prüft den Abschluss und erhöht Diagnosezähler. Kein beliebiger Klick auf Consent-Elemente.

**Parameter:** `from_handler`: Aufruf durch Locator-Handler. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Cookie dialog repeatedly reappeared; stop')`
- `ExecutionError('Cookie dialog: expected exactly one matching dialog')`

**Direkt gesetzter Zustand:** `self.cookie_handler_page`, `self.cookie_dialog_count`.

**Relevante Aufrufe:** `self._check_access`, `self._cookie_button`, `self._cookie_locator`, `self._cookie_pending`, `self._install_cookie_handler`, `self._unique`, `self._unique(button, 'Necessary cookies').click`, `self.page.remove_locator_handler`.

#### `StrategyExecutor._install_cookie_handler`

**Quellcode:** [StrategyExecutor.py:203–208](src/crawler/StrategyExecutor.py#L203-L208).

```python
def _install_cookie_handler(self):
```

**Aufgabe:** Registriert einen Locator-Handler für den aktuellen Browser-Tab, sofern konfiguriert und noch nicht installiert.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.cookie_handler_page`.

**Relevante Aufrufe:** `self._cookie_button`, `self._cookie_locator`, `self.page.add_locator_handler`.

#### `StrategyExecutor._wait_visible`

**Quellcode:** [StrategyExecutor.py:210–229](src/crawler/StrategyExecutor.py#L210-L229).

```python
def _wait_visible(self, locator):
```

**Aufgabe:** Begrenzt das Warten auf Sichtbarkeit, berücksichtigt Zugriff, Cookie-Dialog und Navigationszustand.

**Parameter:** `locator`: Playwright-Locator oder Locator-Regel gemäß Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'Timed out waiting for target: {locator}')`

**Relevante Aufrufe:** `self._check_access`, `self._check_navigation_context`, `self._cookie_locator`, `self._cookie_pending`, `self._handle_cookie_dialog`, `self.page.wait_for_timeout`.

#### `StrategyExecutor._cookie_diagnostics`

**Quellcode:** [StrategyExecutor.py:231–238](src/crawler/StrategyExecutor.py#L231-L238).

```python
def _cookie_diagnostics(self):
```

**Aufgabe:** Sammelt aktuelle Cookie-Matches, Zähler und Diagnoseinformationen für den Bericht.

**Rückgabe (Ausdrücke im Code):** `None`; `{'handled_count': self.cookie_dialog_count, 'dialog_matches': dialog.count(), 'dialog_visible_matches': dialog.filter(visible=True).count(), 'button_matches': button.count(), 'button_visibl…`.

**Relevante Aufrufe:** `self._cookie_button`, `self._cookie_locator`.

#### `StrategyExecutor._check_navigation_context`

**Quellcode:** [StrategyExecutor.py:240–242](src/crawler/StrategyExecutor.py#L240-L242).

```python
def _check_navigation_context(self):
```

**Aufgabe:** Erkennt einen seit Beginn der Navigation behandelten Cookie-Dialog; löst NavigationInterrupted aus.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `NavigationInterrupted('Cookie consent changed the page state during navigation')`

#### `StrategyExecutor._navigate`

**Quellcode:** [StrategyExecutor.py:244–269](src/crawler/StrategyExecutor.py#L244-L269).

```python
def _navigate(self, start_url=None):
```

**Aufgabe:** Navigiert über _navigate_once; höchstens ein Neustart der reinen Suchnavigation bei nachgewiesener Cookie-Unterbrechung, im selben Kontext.

**Parameter:** `start_url`: Start-URL der Suche. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Explizite Fehler / Abbruch:**

- `erneutes Auslösen der aktuellen Exception`
- `ExecutionError('Cookie dialog interrupted navigation again after restart; stop')`

**Direkt gesetzter Zustand:** `self.navigation_cookie_baseline`, `self.navigation_restarts`.

**Relevante Aufrufe:** `self._check_access`, `self._handle_cookie_dialog`, `self._install_cookie_handler`, `self._navigate_once`, `self.page.goto`.

#### `StrategyExecutor._menu_state`

**Quellcode:** [StrategyExecutor.py:271–276](src/crawler/StrategyExecutor.py#L271-L276).

```python
def _menu_state(self, target, following):
```

**Aufgabe:** Liest aria-expanded und Anzahl sichtbarer Folgeelemente; prüft Zugriff, Cookie und Navigationskontext.

**Parameter:** `target`: konkretes Zielobjekt bzw. Locator; `following`: erwartetes Folgeelement. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(expanded, following.filter(visible=True).count())`.

**Relevante Aufrufe:** `self._check_access`, `self._check_navigation_context`, `self._handle_cookie_dialog`, `target.get_attribute`.

#### `StrategyExecutor._wait_menu`

**Quellcode:** [StrategyExecutor.py:278–289](src/crawler/StrategyExecutor.py#L278-L289).

```python
def _wait_menu(self, target, following, timeout_ms):
```

**Aufgabe:** Pollt begrenzt bis zur Menü-Postcondition; liefert beobachteten Zustand für _open_menu.

**Parameter:** `target`: konkretes Zielobjekt bzw. Locator; `following`: erwartetes Folgeelement; `timeout_ms`: Wartebudget in Millisekunden. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(True, expanded, matches)`; `(False, expanded, matches)`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Menu postcondition is ambiguous')`

**Relevante Aufrufe:** `self._menu_state`, `self.page.wait_for_timeout`.

#### `StrategyExecutor._open_menu`

**Quellcode:** [StrategyExecutor.py:291–335](src/crawler/StrategyExecutor.py#L291-L335).

```python
def _open_menu(self, target, following, name):
```

**Aufgabe:** Öffnet konfiguriertes Menü und bestätigt die Folgeelemente; vermeidet Schließen eines bereits offenen Menüs und begrenzt Klickwiederholung.

**Parameter:** `target`: konkretes Zielobjekt bzw. Locator; `following`: erwartetes Folgeelement; `name`: Name des Felds/Controls gemäß Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Menu postcondition is ambiguous')`
- `ExecutionError(f'Menu postcondition not met: {name}')`

**Direkt gesetzter Zustand:** `self.menu_retries`.

**Relevante Aufrufe:** `self._check_navigation_context`, `self._menu_state`, `self._unique`, `self._wait_menu`, `target.click`, `target.is_visible`.

#### `StrategyExecutor._state_menu_to_close`

**Quellcode:** [StrategyExecutor.py:337–357](src/crawler/StrategyExecutor.py#L337-L357).

```python
def _state_menu_to_close(self, actions, index):
```

**Aufgabe:** Erkennt die bekannte providerbezogene Bundesländer-Menükonstellation anhand der Navigationsschritte.

**Parameter:** `index`: nullbasierter Index. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`; `spec`.

#### `StrategyExecutor._close_state_menu`

**Quellcode:** [StrategyExecutor.py:359–398](src/crawler/StrategyExecutor.py#L359-L398).

```python
def _close_state_menu(self, spec, selected):
```

**Aufgabe:** Schließt das konfigurierte Bundesländer-Menü kontrolliert; prüft aria-expanded und die erhaltene Auswahl soweit im DOM vorhanden.

**Parameter:** `spec`: Locator-, Dokument- oder Regeldefinition; `selected`: vorher ausgewählte Option. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Menu postcondition not met: Bundesländer selection before close')`
- `ExecutionError('Menu postcondition not met: Bundesländer selection lost')`
- `ExecutionError('Menu postcondition not met: Bundesländer close')`

**Relevante Aufrufe:** `self._check_access`, `self._check_navigation_context`, `self._handle_cookie_dialog`, `self._unique`, `self.locator`, `self.page.get_by_role`, `self.page.wait_for_timeout`.

#### `StrategyExecutor._navigate_once`

**Quellcode:** [StrategyExecutor.py:400–449](src/crawler/StrategyExecutor.py#L400-L449).

```python
def _navigate_once(self):
```

**Aufgabe:** Führt die geordneten Navigationsaktionen mit Parameterauflösung, Menüregeln, Postconditions, Zugriffsschutz und Timing durch.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Download control not allowed during navigation')`
- `ExecutionError('Menu opener requires a following action')`
- `ExecutionError('Configured menu must precede a checkbox or option selection')`
- `ExecutionError('Unsupported input type')`

**Direkt gesetzter Zustand:** `self.step`.

**Relevante Aufrufe:** `self._check_access`, `self._check_navigation_context`, `self._close_state_menu`, `self._handle_cookie_dialog`, `self._open_menu`, `self._state_menu_to_close`, `self._unique`, `self._wait`, `self._wait_visible`, `self.locator`, `target.click`, `target.fill`, `target.get_attribute`, `target.select_option`.

#### `StrategyExecutor._rows`

**Quellcode:** [StrategyExecutor.py:451–455](src/crawler/StrategyExecutor.py#L451-L455).

```python
def _rows(self):
```

**Aufgabe:** Liefert den Ergebniszeilen-Locator innerhalb des optionalen eindeutig bestimmten Containers.

**Rückgabe (Ausdrücke im Code):** `self.locator(root, self.records['row'])`.

**Relevante Aufrufe:** `self._unique`, `self.locator`.

#### `StrategyExecutor._field`

**Quellcode:** [StrategyExecutor.py:457–492](src/crawler/StrategyExecutor.py#L457-L492).

```python
def _field(self, row, field):
```

**Aufgabe:** Extrahiert Text, Attribut, Parameter oder URL; bei Sibling-Scope mit Guard. Wendet Regex begrenzt an und behandelt fehlende/mehrdeutige Werte nach Pflichtfeldregel.

**Parameter:** `row`: Locator bzw. Datensatzzeile im aktuellen Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `value`.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'{name}: no value')`
- `ExecutionError(f'{name}: regex input too long')`
- `ExecutionError(f'{name}: regex did not produce one unambiguous value')`
- `ExecutionError(f'{name}: empty value')`

**Relevante Aufrufe:** `self._unique`, `self.locator`, `self.page.locator`, `self.patterns[name].finditer`, `target.and_`, `target.get_attribute`, `target.inner_text`.

#### `StrategyExecutor._record`

**Quellcode:** [StrategyExecutor.py:494–511](src/crawler/StrategyExecutor.py#L494-L511).

```python
def _record(self, row, keys_only=False):
```

**Aufgabe:** Baut einen Datensatz aus Feldregeln oder nur dessen Schlüsselfeldern; prüft erwartete Filter bei vollständiger Extraktion.

**Parameter:** `row`: Locator bzw. Datensatzzeile im aktuellen Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `record`.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'Required field {name}: {exc}')`
- `ExecutionError(f'{name}: extracted value does not match requested filter')`

**Relevante Aufrufe:** `self._field`.

#### `StrategyExecutor._key`

**Quellcode:** [StrategyExecutor.py:513–514](src/crawler/StrategyExecutor.py#L513-L514).

```python
def _key(self, record):
```

**Aufgabe:** Baut ein geordnetes Tupel aus den key_fields. Die heutige Strategie verwendet auch den Firmennamen; stabile fachliche Identität ist D-03.

**Parameter:** `record`: extrahierter Datensatz mit Schlüsselfeldern. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `tuple((record[k] for k in self.records['key_fields']))`.

#### `StrategyExecutor._check_row`

**Quellcode:** [StrategyExecutor.py:516–518](src/crawler/StrategyExecutor.py#L516-L518).

```python
def _check_row(self, row, record):
```

**Aufgabe:** Prüft, dass die aktuell adressierte Zeile noch denselben Datensatzschlüssel hat, bevor oder nachdem Dokumente verarbeitet werden.

**Parameter:** `row`: Locator bzw. Datensatzzeile im aktuellen Kontext; `record`: extrahierter Datensatz mit Schlüsselfeldern. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Row identity changed before or after document download')`

**Relevante Aufrufe:** `self._key`, `self._record`.

#### `StrategyExecutor._validate_file`

**Quellcode:** [StrategyExecutor.py:520–535](src/crawler/StrategyExecutor.py#L520-L535).

```python
def _validate_file(self, path, file_type):
```

**Aufgabe:** Prüft nichtleere Datei, max_file_bytes, PDF-Header/EOF oder sicheres XML und berechnet binären SHA-256. Liest vollständig in den Speicher; keine semantische Inhaltsprüfung.

**Parameter:** `path`: Datei-/Verzeichnispfad gemäß Funktionszweck; `file_type`: erwartetes Dateiformat. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(size, hashlib.sha256(data).hexdigest())`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Empty document or size limit exceeded')`
- `ExecutionError('Invalid PDF header or EOF')`
- `ValueError('HTML/error document')`
- `ExecutionError(f'Invalid or unsafe XML: {type(exc).__name__}')`

**Relevante Aufrufe:** `hashlib.sha256`, `hashlib.sha256(data).hexdigest`, `path.read_bytes`, `path.stat`.

#### `StrategyExecutor._download`

**Quellcode:** [StrategyExecutor.py:537–583](src/crawler/StrategyExecutor.py#L537-L583).

```python
def _download(self, row, spec, result):
```

**Aufgabe:** Löst den eindeutig sichtbaren Dokument-Control aus oder liest den direkten Link; prüft URL, Status, Größe, Format und Hash. Speichert erst nach Validierung mit generiertem Namen, entfernt .part im finally.

**Parameter:** `row`: Locator bzw. Datensatzzeile im aktuellen Kontext; `spec`: Locator-, Dokument- oder Regeldefinition; `result`: Ergebnis-/Statusobjekt. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Download URL outside allowed domains')`
- `ExecutionError('Document link has no href')`
- `ExecutionError('Document link outside allowed domains')`
- `ExecutionError(f'Document HTTP {response.status}')`
- `ExecutionError('Document size limit exceeded')`

**Relevante Aufrufe:** `response.body`, `response.dispose`, `self._check_access`, `self._response`, `self._unique`, `self._validate_file`, `self.locator`, `self.output_dir.mkdir`, `self.page.expect_download`, `target.click`, `target.get_attribute`, `temporary.replace`, `temporary.unlink`, `temporary.write_bytes`.

#### `StrategyExecutor._page_signature`

**Quellcode:** [StrategyExecutor.py:585–586](src/crawler/StrategyExecutor.py#L585-L586).

```python
def _page_signature(self, rows):
```

**Aufgabe:** Bildet geordnete Tupel der Schlüssel aller sichtbaren Ergebniszeilen; kurzfristiger Seitenzustand, aktuell auch zur strikten Duplikatkontrolle.

**Parameter:** `rows`: Locator/Sequenz der Ergebniszeilen. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `tuple((self._key(self._record(rows.nth(i), keys_only=True)) for i in range(rows.count())))`.

**Relevante Aufrufe:** `self._key`, `self._record`.

#### `StrategyExecutor._pagination_link_details`

**Quellcode:** [StrategyExecutor.py:589–591](src/crawler/StrategyExecutor.py#L589-L591).

```python
@staticmethod
def _pagination_link_details(element):
```

**Aufgabe:** Liest Tag, href, target und download-Attribut aus einem möglichen Next-Control.

**Rückgabe (Ausdrücke im Code):** `element.evaluate("el => ({tag: el.tagName, href: el.href || null,\n            target: el.target || '', download: el.hasAttribute('download')})")`.

#### `StrategyExecutor._equivalent_pagination_links`

**Quellcode:** [StrategyExecutor.py:593–600](src/crawler/StrategyExecutor.py#L593-L600).

```python
def _equivalent_pagination_links(self, details, states):
```

**Aufgabe:** Erlaubt mehrere sichtbare Next-Links nur bei gleicher zulässiger URL, gewöhnlichem Linkziel und identischem Aktivierungszustand.

**Parameter:** `details`: beobachtete Linkattribute; `states`: Aktivierungszustände der Controls. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `False`; `len(urls) == 1 and allowed_url(next(iter(urls)), self.domains)`.

#### `StrategyExecutor._pagination_target`

**Quellcode:** [StrategyExecutor.py:602–620](src/crawler/StrategyExecutor.py#L602-L620).

```python
def _pagination_target(self, pagination):
```

**Aufgabe:** Ermittelt sichtbaren Next-Control und Zustand missing/disabled/enabled. Mehrdeutige Controls werden nicht willkürlich gewählt.

**Parameter:** `pagination`: Paginierungsregel. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(None, 'missing')`; `(visible.first, states[0])`.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'Next-page control ambiguous ({count} visible matches); end of results not verified')`
- `ExecutionError(f'Next-page control ambiguous ({count} non-equivalent visible matches); end of results not verified')`

**Relevante Aufrufe:** `self._equivalent_pagination_links`, `self._pagination_link_details`, `self.locator`, `self.locator(self.page, pagination['next']).filter`.

#### `StrategyExecutor._pagination_decision`

**Quellcode:** [StrategyExecutor.py:622–637](src/crawler/StrategyExecutor.py#L622-L637).

```python
def _pagination_decision(self, pagination, next_state, marker_visible):
```

**Aufgabe:** Wertet explizite v3-Endregel und Next-Zustand aus; speichert Endnachweis bei gültiger Regel. Fehlende Navigation allein beweist kein Ende.

**Parameter:** `pagination`: Paginierungsregel; `next_state`: missing/disabled/enabled; `marker_visible`: Sichtbarkeit expliziten Endmarkers. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `False`; `True`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Pagination end marker conflicts with enabled next control')`
- `ExecutionError('Next-page control missing or hidden; end of results not verified')`

**Direkt gesetzter Zustand:** `self.pagination_end_evidence`.

#### `StrategyExecutor._pagination_stop_reason`

**Quellcode:** [StrategyExecutor.py:639–640](src/crawler/StrategyExecutor.py#L639-L640).

```python
def _pagination_stop_reason(self):
```

**Aufgabe:** Liefert end_of_results oder end_of_results_unverified abhängig vom gespeicherten Endnachweis.

**Rückgabe (Ausdrücke im Code):** `'end_of_results' if self.pagination_end_evidence else 'end_of_results_unverified'`.

#### `StrategyExecutor._next_page`

**Quellcode:** [StrategyExecutor.py:642–683](src/crawler/StrategyExecutor.py#L642-L683).

```python
def _next_page(self, previous):
```

**Aufgabe:** Prüft Ende, klickt einmal und wartet begrenzt auf zweimal beobachtete stabile, neue, nicht überlappende Schlüssel. Aktuell konservativ bei dynamischen Treffern.

**Parameter:** `previous`: Signatur der vorherigen Seite. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `False`; `True`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Pagination end marker ambiguous; end of results not verified')`
- `erneutes Auslösen der aktuellen Exception`
- `ExecutionError('No verified change of page keys after pagination')`

**Direkt gesetzter Zustand:** `self.step`.

**Relevante Aufrufe:** `self._check_access`, `self._page_signature`, `self._pagination_decision`, `self._pagination_target`, `self._rows`, `self._wait`, `self.locator`, `self.page.wait_for_timeout`, `self.seen.union`, `target.click`.

#### `StrategyExecutor._collect`

**Quellcode:** [StrategyExecutor.py:685–734](src/crawler/StrategyExecutor.py#L685-L734).

```python
def _collect(self, max_companies, max_pages, downloads):
```

**Aufgabe:** Extrahiert bis zum Unternehmens-/Seitenlimit, stoppt bei Duplikat oder Fehler; optional Dokumente je Datensatz. Limits dürfen nicht als bestätigtes Ende interpretiert werden.

**Parameter:** `max_companies`: Obergrenze für Datensätze; `max_pages`: Obergrenze für Ergebnisseiten; `downloads`: Dokumentdownload aktivieren. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `'empty_results'`; `'company_limit'`; `'page_limit'`; `self._pagination_stop_reason()`; `'limit'`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Duplicate record key; stop rather than repeat download')`
- `erneutes Auslösen der aktuellen Exception`

**Direkt gesetzter Zustand:** `self.pages`, `self.step`, `self.download_attempts`.

**Relevante Aufrufe:** `self._check_access`, `self._check_row`, `self._download`, `self._key`, `self._next_page`, `self._page_signature`, `self._pagination_stop_reason`, `self._record`, `self._rows`, `self._wait_visible`, `self.locator`, `self.locator(self.page, empty).first.is_visible`, `self.seen.add`.

#### `StrategyExecutor.run`

**Quellcode:** [StrategyExecutor.py:736–787](src/crawler/StrategyExecutor.py#L736-L787).

```python
def run(self, start_url, crawl_id, max_companies=1, max_pages=1, downloads=False, headless=False, timing_path=BROWSER_TIMING_FILE, executable_path=None):
```

**Aufgabe:** Öffentlicher begrenzter Ablauf: Browser starten, Domain-Routing, Navigation und Sammlung; Bericht, Fehlerklassifikation und Timings erzeugen, Browser schließen. Kein LLM.

**Parameter:** `start_url`: Start-URL der Suche; `crawl_id`: Auftrags-/Lauf-ID; `max_companies`: Obergrenze für Datensätze; `max_pages`: Obergrenze für Ergebnisseiten; `downloads`: Dokumentdownload aktivieren; `headless`: Browser ohne sichtbares Fenster starten; `timing_path`: Pfad zum Timing-Log; `executable_path`: optionaler Chromium-Binärpfad. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `attach_error_classification({'crawl_id': crawl_id, 'status': status, 'stop_reason': reason, 'companies': self.companies, 'access_restriction': self.blocked, 'pagination_end_verified': statu…`.

**Explizite Fehler / Abbruch:**

- `ValueError('Invalid start URL or run limits')`
- `erneutes Auslösen der aktuellen Exception`

**Direkt gesetzter Zustand:** `self.context`, `self.page`.

**Relevante Aufrufe:** `browser.close`, `browser.new_context`, `self._collect`, `self._cookie_diagnostics`, `self._navigate`, `self.context.new_page`, `self.context.on`, `self.context.route`, `self.page.goto`, `self.page.is_closed`, `self.page.locator`, `self.page.locator('body').aria_snapshot`.

---

## crawler-strategyrepair

**Modul:** [`src/crawler/StrategyRepair.py`](src/crawler/StrategyRepair.py)  
**Features/Storys:** C-08  
**Aufgabe und Abgrenzung:** Begrenzt die LLM-Reparatur auf Auswahl aus bereits unabhängig verifizierten Locator-Alternativen. Keine freie Generierung neuer Navigation und kein Browser im Reparaturaufruf.

**Direkte Abhängigkeiten:** `import json`; `from jsonschema import Draft202012Validator`; `from StrategySchema import STRATEGY_SCHEMA`; `from StructureVerifier import replace_locator`.

**Definitionen:** 1 Klassen, 2 Funktionen/Methoden (inkl. lokaler Definitionen).

### Klasse `StrategyRepair`

**Quellcode:** [StrategyRepair.py:9–52](src/crawler/StrategyRepair.py#L9-L52).

**Aufgabe:** Wählt über ein begrenztes LLM eine unabhängig beobachtete Locator-Alternative, keine eigenständige Navigation.

#### `StrategyRepair.__init__`

**Quellcode:** [StrategyRepair.py:10–11](src/crawler/StrategyRepair.py#L10-L11).

```python
def __init__(self, policy, client_factory=None, model='gpt-6-luna'):
```

**Aufgabe:** Bindet Policy, optionale injizierte Client-Factory und Modell.

**Parameter:** `policy`: ExecutionPolicy-Instanz; `client_factory`: optionale Factory zum Erzeugen eines Clients; `model`: Modellkennung. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.policy`, `self.client_factory`, `self.model`.

#### `StrategyRepair.propose`

**Quellcode:** [StrategyRepair.py:13–52](src/crawler/StrategyRepair.py#L13-L52).

```python
def propose(self, strategy, verification, crawl_id):
```

**Aufgabe:** Erfordert bestätigte Verifikation für row/container und begrenzte Alternativen. Übergibt nur Locator-Daten mit striktem Auswahl-Schema, beschränkt Prompt/Output, validiert Antwort, erzeugt gegebenenfalls Kandidat durch replace_locator. Index -1 bedeutet Ablehnung; keine Aktivierung.

**Parameter:** `strategy`: Strategie-Dictionary nach StrategySchema; `verification`: unabhängiger Verifikationsbericht; `crawl_id`: Auftrags-/Lauf-ID. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(None, selection)`; `(candidate, selection)`.

**Explizite Fehler / Abbruch:**

- `ValueError('Independent structural verification is required')`
- `ValueError('Invalid replacement set')`
- `ValueError('Repair input budget exceeded')`
- `RuntimeError('No completed repair response')`
- `ValueError('Repair selection out of range')`

**Relevante Aufrufe:** `client.create`, `json.dumps`, `json.loads`, `self.client_factory`.

---

## crawler-strategyschema

**Modul:** [`src/crawler/StrategySchema.py`](src/crawler/StrategySchema.py)  
**Features/Storys:** C-03, C-09, D-02, E-02  
**Aufgabe und Abgrenzung:** JSON-Schema-Bausteine für Locator, Navigation, Felder, Dokumente und Paginierung. Neue Discovery liefert v3; lokale Prüfung akzeptiert v2 und v3. Historische Strategien werden nicht umgeschrieben.

**Definitionen:** 0 Klassen, 5 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `STRING`, `NULLABLE_STRING`, `BOOLEAN`, `LOCATOR`, `WAIT`, `NAVIGATION_ACTION`, `FIELD`, `DOCUMENT`, `RECORDS`, `PAGINATION`, `V2_SCHEMA`, `PAGINATION_V3`, `DISCOVERY_SCHEMA`, `STRATEGY_SCHEMA`.

#### `_object`

**Quellcode:** [StrategySchema.py:4–5](src/crawler/StrategySchema.py#L4-L5).

```python
def _object(properties):
```

**Aufgabe:** Erstellt striktes Objektschema mit allen Feldern required und additionalProperties false.

**Parameter:** `properties`: Objektfelder eines JSON-Schemas. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `{'type': 'object', 'properties': properties, 'required': list(properties), 'additionalProperties': False}`.

#### `_array`

**Quellcode:** [StrategySchema.py:8–9](src/crawler/StrategySchema.py#L8-L9).

```python
def _array(items):
```

**Aufgabe:** Erzeugt Array-Schema mit übergebenem Item-Schema.

**Parameter:** `items`: Element-Schema. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `{'type': 'array', 'items': items}`.

#### `_enum`

**Quellcode:** [StrategySchema.py:12–13](src/crawler/StrategySchema.py#L12-L13).

```python
def _enum(*values):
```

**Aufgabe:** Erzeugt String-Enum-Schema aus erlaubten Werten.

**Parameter:** `values`: erlaubte Enum-Werte. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `{'type': 'string', 'enum': list(values)}`.

#### `_ref`

**Quellcode:** [StrategySchema.py:16–17](src/crawler/StrategySchema.py#L16-L17).

```python
def _ref(name):
```

**Aufgabe:** Erzeugt lokale JSON-Schema-Referenz unter $defs.

**Parameter:** `name`: Name des Felds/Controls gemäß Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `{'$ref': f'#/$defs/{name}'}`.

#### `_nullable`

**Quellcode:** [StrategySchema.py:20–21](src/crawler/StrategySchema.py#L20-L21).

```python
def _nullable(schema):
```

**Aufgabe:** Erlaubt übergebenes Schema oder JSON null.

**Parameter:** `schema`: JSON-Schema-Vertrag. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `{'anyOf': [schema, {'type': 'null'}]}`.

---

## crawler-strategystore

**Modul:** [`src/crawler/StrategyStore.py`](src/crawler/StrategyStore.py)  
**Features/Storys:** C-05, F-02  
**Aufgabe und Abgrenzung:** Lokaler versionsgebundener JSON-Speicher mit POSIX-Dateisperren und atomarem Schreiben. Kandidaten, Aktivierung, Invalidierung und hashgebundene Zertifizierung. Ältere Aktivierungs-API bleibt im Code, ist nicht der bevorzugte zertifizierte Freigabeweg.

**Direkte Abhängigkeiten:** `import json`; `import hashlib`; `import os`; `import re`; `from contextlib import contextmanager`; `from datetime import datetime, timezone`; `from pathlib import Path`; `from ProjectPaths import STRATEGIES_DIR`; `from tempfile import NamedTemporaryFile`; `from urllib.parse import urlsplit`; `import fcntl`; `from jsonschema import Draft202012Validator`; `from StrategySchema import STRATEGY_SCHEMA`.

**Definitionen:** 1 Klassen, 25 Funktionen/Methoden (inkl. lokaler Definitionen).

#### `content_digest`

**Quellcode:** [StrategyStore.py:20–22](src/crawler/StrategyStore.py#L20-L22).

```python
def content_digest(value):
```

**Aufgabe:** Berechnet SHA-256 einer kanonisch serialisierten JSON-Repräsentation (keine fachliche Normalisierung).

**Parameter:** `value`: übergebener Wert gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `hashlib.sha256(data.encode('utf-8')).hexdigest()`.

**Relevante Aufrufe:** `hashlib.sha256`, `hashlib.sha256(data.encode('utf-8')).hexdigest`, `json.dumps`.

### Klasse `StrategyStore`

**Quellcode:** [StrategyStore.py:25–337](src/crawler/StrategyStore.py#L25-L337).

**Aufgabe:** Verwaltet eine Domain/Strategie-Kombination mit Manifest, unveränderlichen Versionen, Sperrdatei und Zertifizierungsnachweisen.

#### `StrategyStore.__init__`

**Quellcode:** [StrategyStore.py:26–37](src/crawler/StrategyStore.py#L26-L37).

```python
def __init__(self, domain, strategy_name, root=STRATEGIES_DIR):
```

**Aufgabe:** Validiert Domain/Strategiename, legt Pfadobjekte für Manifest, Versionsordner und Lock an.

**Parameter:** `domain`: Domainname; `strategy_name`: Name der Strategie; `root`: erlaubter Wurzelpfad. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Invalid domain')`
- `ValueError('Invalid strategy name')`

**Direkt gesetzter Zustand:** `self.domain`, `self.strategy_name`, `self.path`, `self.versions_path`, `self.manifest_path`, `self.validator`.

#### `StrategyStore._now`

**Quellcode:** [StrategyStore.py:40–41](src/crawler/StrategyStore.py#L40-L41).

```python
@staticmethod
def _now():
```

**Aufgabe:** Erzeugt UTC-Zeitstempel für Metadaten.

**Rückgabe (Ausdrücke im Code):** `datetime.now(timezone.utc).isoformat()`.

#### `StrategyStore._read`

**Quellcode:** [StrategyStore.py:44–46](src/crawler/StrategyStore.py#L44-L46).

```python
@staticmethod
def _read(path):
```

**Aufgabe:** Liest JSON aus Datei.

**Parameter:** `path`: Datei-/Verzeichnispfad gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `json.load(file)`.

**Relevante Aufrufe:** `json.load`, `path.open`.

#### `StrategyStore._write`

**Quellcode:** [StrategyStore.py:49–62](src/crawler/StrategyStore.py#L49-L62).

```python
@staticmethod
def _write(path, data):
```

**Aufgabe:** Schreibt JSON über temporäre Datei, flush/fsync und atomaren Replace; schützt vor teilweise geschriebenem Ziel.

**Parameter:** `path`: Datei-/Verzeichnispfad gemäß Funktionszweck; `data`: zu verarbeitende Daten. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `file.fileno`, `file.flush`, `file.write`, `json.dump`, `os.fsync`, `os.replace`.

#### `StrategyStore._locked`

**Quellcode:** [StrategyStore.py:65–72](src/crawler/StrategyStore.py#L65-L72).

```python
@contextmanager
def _locked(self):
```

**Aufgabe:** Contextmanager mit exklusivem lokalem POSIX-Dateilock für Store-Operationen.

**Rückgabe:** Generator/Contextmanager; liefert .

**Relevante Aufrufe:** `fcntl.flock`, `self.versions_path.mkdir`.

#### `StrategyStore._manifest`

**Quellcode:** [StrategyStore.py:74–82](src/crawler/StrategyStore.py#L74-L82).

```python
def _manifest(self):
```

**Aufgabe:** Liest und prüft vorhandenes Manifest oder liefert initialen leeren Zustand.

**Rückgabe (Ausdrücke im Code):** `{'manifest_version': 1, 'domain': self.domain, 'strategy_name': self.strategy_name, 'active_version': None, 'versions': []}`; `manifest`.

**Explizite Fehler / Abbruch:**

- `ValueError('Manifest does not match strategy store')`

**Relevante Aufrufe:** `self._read`, `self.manifest_path.exists`.

#### `StrategyStore._entry`

**Quellcode:** [StrategyStore.py:85–91](src/crawler/StrategyStore.py#L85-L91).

```python
@staticmethod
def _entry(manifest, version):
```

**Aufgabe:** Sucht die Metadaten einer bestimmten Version im Manifest, andernfalls Fehler.

**Parameter:** `version`: Strategieversionsnummer. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `entry`.

**Explizite Fehler / Abbruch:**

- `ValueError('Version must be a positive integer')`
- `KeyError(f'Unknown strategy version: {version}')`

#### `StrategyStore._version_path`

**Quellcode:** [StrategyStore.py:93–94](src/crawler/StrategyStore.py#L93-L94).

```python
def _version_path(self, version):
```

**Aufgabe:** Bildet den versionierten Dateipfad.

**Parameter:** `version`: Strategieversionsnummer. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `self.versions_path / f'v{version:04d}.json'`.

#### `StrategyStore._check_start_url`

**Quellcode:** [StrategyStore.py:96–101](src/crawler/StrategyStore.py#L96-L101).

```python
def _check_start_url(self, start_url):
```

**Aufgabe:** Prüft, dass Start-URL im erlaubten HTTPS-Domainbereich liegt.

**Parameter:** `start_url`: Start-URL der Suche. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Start URL does not match the configured domain')`

#### `StrategyStore.save`

**Quellcode:** [StrategyStore.py:103–126](src/crawler/StrategyStore.py#L103-L126).

```python
def save(self, strategy, start_url, crawl_id=None):
```

**Aufgabe:** Validiert Kandidat und URL, reserviert neue Versionsnummer unter Lock, speichert Version und Manifest; aktiviert nicht.

**Parameter:** `strategy`: Strategie-Dictionary nach StrategySchema; `start_url`: Start-URL der Suche; `crawl_id`: Auftrags-/Lauf-ID. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `version`.

**Explizite Fehler / Abbruch:**

- `ValueError('A candidate requires a records definition')`
- `ValueError('crawl_id must be a string or None')`

**Relevante Aufrufe:** `self._check_start_url`, `self._locked`, `self._manifest`, `self._now`, `self._version_path`, `self._write`, `self.validator.validate`, `self.versions_path.glob`.

#### `StrategyStore._load_entry`

**Quellcode:** [StrategyStore.py:128–138](src/crawler/StrategyStore.py#L128-L138).

```python
def _load_entry(self, entry):
```

**Aufgabe:** Liest gespeicherte Version und prüft Integrität sowie Schema gegen Metadaten.

**Rückgabe (Ausdrücke im Code):** `{'metadata': metadata, 'strategy': strategy}`.

**Explizite Fehler / Abbruch:**

- `ValueError('Schema version does not match manifest')`
- `ValueError('Strategy content does not match manifest status')`
- `ValueError('Strategy content differs from certified version')`

**Relevante Aufrufe:** `self._read`, `self._version_path`, `self.validator.validate`.

#### `StrategyStore.load`

**Quellcode:** [StrategyStore.py:140–141](src/crawler/StrategyStore.py#L140-L141).

```python
def load(self, version):
```

**Aufgabe:** Lädt konkrete Version mitsamt Metadaten unter Lock.

**Parameter:** `version`: Strategieversionsnummer. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `self._load_entry(self._entry(self._manifest(), version))`.

**Relevante Aufrufe:** `self._entry`, `self._load_entry`, `self._manifest`.

#### `StrategyStore.load_active`

**Quellcode:** [StrategyStore.py:143–151](src/crawler/StrategyStore.py#L143-L151).

```python
def load_active(self):
```

**Aufgabe:** Lädt die im Manifest als aktiv bezeichnete Version (älterer Zugriffspfad).

**Rückgabe (Ausdrücke im Code):** `None`; `self._load_entry(entry)`.

**Explizite Fehler / Abbruch:**

- `ValueError('Inconsistent active strategy')`

**Relevante Aufrufe:** `self._entry`, `self._load_entry`, `self._manifest`.

#### `StrategyStore.exists`

**Quellcode:** [StrategyStore.py:153–161](src/crawler/StrategyStore.py#L153-L161).

```python
def exists(self, version=None):
```

**Aufgabe:** Prüft Vorhandensein des Stores bzw. einer Version.

**Parameter:** `version`: Strategieversionsnummer. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `bool(manifest['versions'])`; `True`; `False`.

**Relevante Aufrufe:** `self._entry`, `self._manifest`.

#### `StrategyStore.list_versions`

**Quellcode:** [StrategyStore.py:163–164](src/crawler/StrategyStore.py#L163-L164).

```python
def list_versions(self):
```

**Aufgabe:** Liefert Versionseinträge aus dem Manifest.

**Rückgabe (Ausdrücke im Code):** `self._manifest()['versions']`.

**Relevante Aufrufe:** `self._manifest`.

#### `StrategyStore.mark_validated`

**Quellcode:** [StrategyStore.py:166–177](src/crawler/StrategyStore.py#L166-L177).

```python
def mark_validated(self, version, validation_reference):
```

**Aufgabe:** Ältere API für externe Validierungsreferenz; führt keine unabhängige Validierung aus und ist kein Ersatz für certify.

**Parameter:** `version`: Strategieversionsnummer. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('A validation reference is required')`
- `ValueError('Only a candidate can be marked validated')`

**Relevante Aufrufe:** `self._entry`, `self._load_entry`, `self._locked`, `self._manifest`, `self._now`, `self._write`.

#### `StrategyStore.activate`

**Quellcode:** [StrategyStore.py:179–194](src/crawler/StrategyStore.py#L179-L194).

```python
def activate(self, version):
```

**Aufgabe:** Ältere Aktivierungsschnittstelle; neuer Betrieb verwendet promote_certified.

**Parameter:** `version`: Strategieversionsnummer. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Explizite Fehler / Abbruch:**

- `ValueError('Only a validated strategy can be activated')`

**Relevante Aufrufe:** `self._entry`, `self._load_entry`, `self._locked`, `self._manifest`, `self._now`, `self._write`.

#### `StrategyStore.invalidate`

**Quellcode:** [StrategyStore.py:196–208](src/crawler/StrategyStore.py#L196-L208).

```python
def invalidate(self, version, reason):
```

**Aufgabe:** Markiert Version ungültig, entfernt gegebenenfalls den aktiven Zeiger und aktualisiert Metadaten.

**Parameter:** `version`: Strategieversionsnummer; `reason`: Begründung bzw. Skip-Grund. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('An invalidation reason is required')`
- `ValueError('Only a candidate, validated or active strategy can be invalidated')`

**Relevante Aufrufe:** `self._entry`, `self._locked`, `self._manifest`, `self._now`, `self._write`.

#### `StrategyStore.validation_snapshot`

**Quellcode:** [StrategyStore.py:210–216](src/crawler/StrategyStore.py#L210-L216).

```python
def validation_snapshot(self, version):
```

**Aufgabe:** Liefert ausgewählte Strategie, aktuell aktive Version und Aktivierungsrevision als konsistenten Snapshot.

**Parameter:** `version`: Strategieversionsnummer. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(loaded, manifest['active_version'], manifest.get('activation_revision', 0))`.

**Explizite Fehler / Abbruch:**

- `ValueError('Version is not eligible for validation')`

**Relevante Aufrufe:** `self._entry`, `self._load_entry`, `self._locked`, `self._manifest`.

#### `StrategyStore.begin_validation`

**Quellcode:** [StrategyStore.py:218–235](src/crawler/StrategyStore.py#L218-L235).

```python
def begin_validation(self, version, expected_hash, expected_active, expected_revision):
```

**Aufgabe:** Entzieht vorherigen Nachweis vor Revalidierung, prüft Strategiehash und Generation und erzeugt neue Validierungsversuchs-ID.

**Parameter:** `version`: Strategieversionsnummer; `expected_hash`: erwartete SHA-256-Prüfsumme; `expected_active`: erwartete aktive Versionsnummer für CAS; `expected_revision`: erwartete Aktivierungsrevision. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `entry['validation_attempt']`.

**Explizite Fehler / Abbruch:**

- `ValueError('Strategy or active generation changed before validation')`

**Relevante Aufrufe:** `self._entry`, `self._load_entry`, `self._locked`, `self._manifest`, `self._write`.

#### `StrategyStore.certify`

**Quellcode:** [StrategyStore.py:237–274](src/crawler/StrategyStore.py#L237-L274).

```python
def certify(self, report):
```

**Aufgabe:** Prüft den erfolgreichen lokalen Validierungsbericht, Herkunft, Hash, Generation und Versuch; speichert hashgebundenen Nachweis und aktualisiert Manifest.

**Parameter:** `report`: strukturiertes Berichts-Dictionary. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `str(path)`.

**Explizite Fehler / Abbruch:**

- `ValueError('Complete successful validation evidence required')`
- `ValueError('Version is not eligible for certification')`
- `ValueError('Strategy, validation attempt or active generation changed during validation')`
- `ValueError('Document validation required before certification')`

**Relevante Aufrufe:** `path.relative_to`, `self._entry`, `self._load_entry`, `self._locked`, `self._manifest`, `self._now`, `self._write`.

#### `StrategyStore._certified_report`

**Quellcode:** [StrategyStore.py:276–290](src/crawler/StrategyStore.py#L276-L290).

```python
def _certified_report(self, entry):
```

**Aufgabe:** Liest den anhand Hash benannten Validierungsbericht und prüft unveränderten Inhalt, Version, Domain, Strategiename und Versuch.

**Rückgabe (Ausdrücke im Code):** `report`.

**Explizite Fehler / Abbruch:**

- `ValueError('C.3.9 certification required')`
- `ValueError('Certification no longer matches strategy or evidence')`

**Relevante Aufrufe:** `self._load_entry`, `self._read`.

#### `StrategyStore.certified_active`

**Quellcode:** [StrategyStore.py:292–303](src/crawler/StrategyStore.py#L292-L303).

```python
def certified_active(self):
```

**Aufgabe:** Liefert aktive Strategie mit überprüftem Zertifikat und Aktivierungsrevision; verweigert fehlende/inkonsistente Freigabe.

**Rückgabe (Ausdrücke im Code):** `(loaded, manifest.get('activation_revision', 0))`.

**Explizite Fehler / Abbruch:**

- `ValueError('No active strategy')`
- `ValueError('Inconsistent active strategy')`

**Relevante Aufrufe:** `self._certified_report`, `self._entry`, `self._load_entry`, `self._locked`, `self._manifest`.

#### `StrategyStore.promote_certified`

**Quellcode:** [StrategyStore.py:305–337](src/crawler/StrategyStore.py#L305-L337).

```python
def promote_certified(self, version, expected_active, rollback_reason=None):
```

**Aufgabe:** Atomarer Compare-and-swap-Wechsel auf zertifizierte Version; Rollback braucht ältere zuvor aktive Version, Grund und frischen Nachweis. Aktualisiert Historie und Revision.

**Parameter:** `version`: Strategieversionsnummer; `expected_active`: erwartete aktive Versionsnummer für CAS; `rollback_reason`: optional begründeter Rollback. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `manifest['activation_revision']`.

**Explizite Fehler / Abbruch:**

- `ValueError('Active version changed; no switch performed')`
- `ValueError('A different validated strategy is required')`
- `ValueError('Validation is stale; revalidate against current active generation')`
- `ValueError('Rollback requires a previously active older version and reason')`
- `ValueError('Use explicit rollback for older versions')`

**Relevante Aufrufe:** `self._certified_report`, `self._entry`, `self._locked`, `self._manifest`, `self._now`, `self._write`.

---

## crawler-strategyvalidator

**Modul:** [`src/crawler/StrategyValidator.py`](src/crawler/StrategyValidator.py)  
**Features/Storys:** F-02  
**Aufgabe und Abgrenzung:** Unabhängiger begrenzter Validierungsablauf mit manuell geprüfter Referenz und optional genehmigtem Dokumentensatz. Prüft Felder, Filter, Controls, Dateipräfix und Integrität; kein Nachweis vollständiger fachlicher PDF/XML-Inhalte.

**Direkte Abhängigkeiten:** `import asyncio`; `import time`; `from pathlib import Path`; `from ProjectPaths import VALIDATION_DOCUMENTS_DIR, VALIDATION_TIMING_FILE`; `from uuid import uuid4`; `from AsyncStrategyExecutor import AsyncStrategyExecutor`; `from StrategyExecutor import ExecutionError`; `from ErrorClassifier import ErrorClassifier`; `from StrategyStore import content_digest`.

**Definitionen:** 2 Klassen, 7 Funktionen/Methoden (inkl. lokaler Definitionen).

#### `verify_file`

**Quellcode:** [StrategyValidator.py:14–21](src/crawler/StrategyValidator.py#L14-L21).

```python
def verify_file(executor, document, root):
```

**Aufgabe:** Prüft erlaubten Evidence-Pfad, Dateityp, Größe und binären Hash gegen Dokumentmetadaten; gibt Größe und Hash zurück.

**Parameter:** `document`: Dokument-Metadaten; `root`: erlaubter Wurzelpfad. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(size, digest)`.

**Explizite Fehler / Abbruch:**

- `ValueError('Document outside permitted evidence directory')`
- `ValueError('Document integrity mismatch')`

**Relevante Aufrufe:** `executor._validate_file`, `path.is_file`, `path.is_relative_to`.

#### `compare_records`

**Quellcode:** [StrategyValidator.py:24–30](src/crawler/StrategyValidator.py#L24-L30).

```python
def compare_records(actual, expected):
```

**Aufgabe:** Vergleicht Anzahl und erwartete Feldwerte positionsgebunden; Fehler bei fehlenden/abweichenden Werten.

**Parameter:** `actual`: tatsächlich beobachtete Datensätze; `expected`: erwarteter Wert bzw. erwartete Felder/Anzahl je Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError('Sample count differs from reference')`
- `ValueError(f'Reference mismatch: row {index}, field {name}')`

### Klasse `ValidationExecutor`

**Quellcode:** [StrategyValidator.py:33–56](src/crawler/StrategyValidator.py#L33-L56).

**Aufgabe:** Begrenzte Async-Spezialisierung für unabhängige Stichprobe ohne Paginierung.

**Basisklassen:** `AsyncStrategyExecutor`.

#### `ValidationExecutor.__init__`

**Quellcode:** [StrategyValidator.py:35–37](src/crawler/StrategyValidator.py#L35-L37).

```python
def __init__(self, *args, reference, **kwargs):
```

**Aufgabe:** Initialisiert den geerbten Executor und speichert die geordnete Referenzstichprobe.

**Parameter:** `reference`: unabhängige Referenzdaten; `args`: weitergereichte Positionsparameter; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.reference`.

#### `ValidationExecutor._collect`

**Quellcode:** [StrategyValidator.py:39–56](src/crawler/StrategyValidator.py#L39-L56).

```python
async def _collect(self, max_companies, max_pages, downloads):
```

**Aufgabe:** Ruft normale Extraktion ohne Downloads auf, vergleicht Referenz, prüft eindeutige Controls; lädt nur genehmigte Stichprobe mittels Pool.

**Parameter:** `max_companies`: Obergrenze für Datensätze; `max_pages`: Obergrenze für Ergebnisseiten; `downloads`: Dokumentdownload aktivieren. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `reason`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Validation document control disabled')`

**Direkt gesetzter Zustand:** `self.failure_stage`.

**Relevante Aufrufe:** `self._check_access`, `self._check_row`, `self._pool`, `self._rows`, `self._unique`, `self.locator`, `target.is_enabled`.

### Klasse `StrategyValidator`

**Quellcode:** [StrategyValidator.py:59–164](src/crawler/StrategyValidator.py#L59-L164).

**Aufgabe:** Orchestriert zwei getrennte Browserläufe, erstellt Validierungsbericht und bei vollständigem Erfolg Zertifikat.

#### `StrategyValidator.__init__`

**Quellcode:** [StrategyValidator.py:60–64](src/crawler/StrategyValidator.py#L60-L64).

```python
def __init__(self, store, policy, cookie_dialog=None, open_controls=(), headless=False, executable_path=None, executor_factory=ValidationExecutor, output_root=VALIDATION_DOCUMENTS_DIR, timing_path=VALIDATION_TIMING_FILE):
```

**Aufgabe:** Bindet Store, Policy, Browser-/Cookieoptionen, injizierbare Executor-Factory und Evidence-/Timing-Pfade.

**Parameter:** `store`: StrategyStore-Instanz; `policy`: ExecutionPolicy-Instanz; `cookie_dialog`: explizite Dialogkonfiguration; `open_controls`: konfigurierte Menüöffner; `headless`: Browser ohne sichtbares Fenster starten; `executable_path`: optionaler Chromium-Binärpfad; `executor_factory`: injizierbare Executor-Klasse/Factory; `output_root`: Wurzelverzeichnis für Validierungsbelege; `timing_path`: Pfad zum Timing-Log. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.store`, `self.policy`, `self.cookie_dialog`, `self.open_controls`, `self.headless`, `self.executable_path`, `self.executor_factory`, `self.output_root`, `self.timing_path`.

#### `StrategyValidator.check_reference`

**Quellcode:** [StrategyValidator.py:67–97](src/crawler/StrategyValidator.py#L67-L97).

```python
@staticmethod
def check_reference(strategy, reference):
```

**Aufgabe:** Prüft manuell bestätigte v1-Referenz, Quelle, Parameter, Filter, zwei/drei geordnete Datensätze, Pflichtfelder und Schlüssel, eindeutige Keys und Dateipräfixe.

**Parameter:** `strategy`: Strategie-Dictionary nach StrategySchema; `reference`: unabhängige Referenzdaten. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `(parameters, expected, records, prefixes)`.

**Explizite Fehler / Abbruch:**

- `ValueError('Manually confirmed independent reference required')`
- `ValueError('Reference source description required')`
- `ValueError('Reference parameters differ from strategy')`
- `ValueError('Reference search filters required')`
- `ValueError('Reference must contain two or three ordered result records')`
- `ValueError('Reference must cover required stable fields, keys and requested filters')`
- `ValueError('Required reference values must be nonempty strings')`
- `ValueError('Reference record conflicts with search filters')`
- `ValueError('Reference contains duplicate keys')`
- `ValueError('Expected original filename prefixes for first record required')`

#### `StrategyValidator.validate`

**Quellcode:** [StrategyValidator.py:99–164](src/crawler/StrategyValidator.py#L99-L164).

```python
async def validate(self, version, reference, authorized=False, downloads_authorized=False):
```

**Aufgabe:** Erfordert Suchautorisierung, zieht bisherigen Nachweis zurück, startet zwei unabhängige begrenzte Läufe, prüft Metadaten, Controls und optional einen Dokumentensatz. Zertifiziert nur vollständigen Erfolg; keine automatische Aktivierung.

**Parameter:** `version`: Strategieversionsnummer; `reference`: unabhängige Referenzdaten; `authorized`: explizite Autorisierungsbestätigung; keine automatische Providerfreigabe; `downloads_authorized`: explizite Bestätigung für Stichproben-Downloads. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `report`.

**Explizite Fehler / Abbruch:**

- `ValueError('Explicit authorization for validation search required')`
- `ValueError('Validation execution failed')`
- `ValueError('Unexpected validation scope')`
- `ValueError('Document inventory mismatch')`
- `ValueError('Document status or identity mismatch')`
- `ValueError('Unexpected download in read-only check')`
- `ValueError('Unexpected download count')`

**Relevante Aufrufe:** `asyncio.wait_for`, `executor.run`, `report.setdefault`, `report.update`, `self.check_reference`, `self.executor_factory`, `self.store.begin_validation`, `self.store.certify`, `self.store.validation_snapshot`.

---

## crawler-structureverifier

**Modul:** [`src/crawler/StructureVerifier.py`](src/crawler/StructureVerifier.py)  
**Features/Storys:** C-08, F-01  
**Aufgabe und Abgrenzung:** Read-only-Replay und begrenzte DOM-Locator-Suche zur unabhängigen Bestätigung fehlender Ergebniszeilen/-container. Keine Downloads oder LLM-Aufrufe.

**Direkte Abhängigkeiten:** `import asyncio`; `import copy`; `import hashlib`; `import json`; `from urllib.parse import urlsplit`; `from playwright.async_api import async_playwright, Error as PlaywrightError`; `from AsyncStrategyExecutor import AsyncStrategyExecutor`; `from BrowserUse import allowed_url`; `from StrategyExecutor import ExecutionError`.

**Definitionen:** 1 Klassen, 12 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `OBSERVE_SELECTORS`.

#### `repair_target`

**Quellcode:** [StructureVerifier.py:14–32](src/crawler/StructureVerifier.py#L14-L32).

```python
def repair_target(strategy, report):
```

**Aufgabe:** Liefert nur bei explizit passendem Fehler den unterstützten Zielbereich row/container; andere Fehler nicht reparieren.

**Parameter:** `strategy`: Strategie-Dictionary nach StrategySchema; `report`: strukturiertes Berichts-Dictionary. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`; `name`.

#### `replace_locator`

**Quellcode:** [StructureVerifier.py:35–46](src/crawler/StructureVerifier.py#L35-L46).

```python
def replace_locator(strategy, target, new):
```

**Aufgabe:** Kopiert Strategie und ersetzt ausschließlich angegebenen Result-Locator sowie passende Wait-Referenzen, Original bleibt unverändert.

**Parameter:** `strategy`: Strategie-Dictionary nach StrategySchema; `target`: konkretes Zielobjekt bzw. Locator. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `updated`.

#### `css_spec`

**Quellcode:** [StructureVerifier.py:49–50](src/crawler/StructureVerifier.py#L49-L50).

```python
def css_spec(selector):
```

**Aufgabe:** Erzeugt CSS-Locator im Strategieformat.

**Parameter:** `selector`: CSS-Selektor. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `{'kind': 'css', 'role': None, 'name': None, 'name_source': 'none', 'selector': selector}`.

### Klasse `StructureVerifier`

**Quellcode:** [StructureVerifier.py:72–221](src/crawler/StructureVerifier.py#L72-L221).

**Aufgabe:** Unabhängige read-only-Verifikation konkreter row/container-Strukturprobleme mit begrenzter Browserprobe.

#### `StructureVerifier.__init__`

**Quellcode:** [StructureVerifier.py:73–77](src/crawler/StructureVerifier.py#L73-L77).

```python
def __init__(self, policy, domains, expected_fields, cookie_dialog=None, open_controls=(), headless=False, executable_path=None):
```

**Aufgabe:** Bindet Policy, Domains, erwartete Filter und Browser-/Cookie-/Menükonfiguration.

**Parameter:** `policy`: ExecutionPolicy-Instanz; `domains`: erlaubte Domainliste; `expected_fields`: erwartete Feldwerte/Filter; `cookie_dialog`: explizite Dialogkonfiguration; `open_controls`: konfigurierte Menüöffner; `headless`: Browser ohne sichtbares Fenster starten; `executable_path`: optionaler Chromium-Binärpfad. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.policy`, `self.domains`, `self.expected_fields`, `self.cookie_dialog`, `self.open_controls`, `self.headless`, `self.executable_path`.

#### `StructureVerifier._executor`

**Quellcode:** [StructureVerifier.py:79–81](src/crawler/StructureVerifier.py#L79-L81).

```python
def _executor(self, strategy, parameters):
```

**Aufgabe:** Erzeugt deterministischen Executor für Probe mit aktueller Strategie/Parametern.

**Parameter:** `strategy`: Strategie-Dictionary nach StrategySchema; `parameters`: Such-/Auftragsparameter laut Strategie. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `AsyncStrategyExecutor(strategy, parameters, self.domains, expected_fields=self.expected_fields, cookie_dialog=self.cookie_dialog, open_controls=self.open_controls)`.

#### `StructureVerifier._probe`

**Quellcode:** [StructureVerifier.py:83–149](src/crawler/StructureVerifier.py#L83-L149).

```python
async def _probe(self, page, strategy, parameters, target, check):
```

**Aufgabe:** Sucht begrenzte alternative Locator-Kandidaten im DOM, prüft Stichprobe, eindeutige Keys, Felder und Dokumentcontrols; keine Dokumentaktion.

**Parameter:** `page`: Browser-Page oder Seitennummer gemäß Funktionszweck; `strategy`: Strategie-Dictionary nach StrategySchema; `parameters`: Such-/Auftragsparameter laut Strategie; `target`: konkretes Zielobjekt bzw. Locator. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `{'status': 'inconclusive', 'reason': 'empty_state_present'}`; `{'status': 'inconclusive', 'reason': 'old_locator_still_present'}`; `{'status': 'inconclusive', 'reason': 'old_locator_reappeared'}`; `{'status': 'inconclusive', 'reason': 'no_observed_replacement_passed'}`; `{'status': 'inconclusive', 'reason': 'conflicting_replacements'}`; `{'status': 'confirmed', 'target': target, 'old_matches': 0, 'alternatives': alternatives, 'sample_rows': len(signatures[0]), 'downloads_attempted': 0, 'key_signature': hashlib.sha256(json.d…`.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Hidden result row')`
- `ExecutionError('Document control missing or ambiguous')`

**Relevante Aufrufe:** `hashlib.sha256`, `hashlib.sha256(json.dumps(signatures[0], ensure_ascii=False).encode()).hexdigest`, `json.dumps`, `json.dumps(signatures[0], ensure_ascii=False).encode`, `page.evaluate`, `self._executor`.

#### `StructureVerifier.verify`

**Quellcode:** [StructureVerifier.py:151–221](src/crawler/StructureVerifier.py#L151-L221).

```python
async def verify(self, strategy, parameters, start_url, report):
```

**Aufgabe:** Spielt Navigation einmal read-only unter Domain-/Zeitgrenzen nach und prüft, ob alte Struktur fehlt und beobachtete Alternativen reproduzierbar funktionieren. Liefert Verifikationsbericht, ruft kein LLM auf.

**Parameter:** `strategy`: Strategie-Dictionary nach StrategySchema; `parameters`: Such-/Auftragsparameter laut Strategie; `start_url`: Start-URL der Suche; `report`: strukturiertes Berichts-Dictionary. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `{'status': 'inconclusive', 'reason': 'unsupported_target_or_policy'}`; `{'status': 'inconclusive', 'reason': 'unexpected_result_page'}`; `first`; `{'status': 'inconclusive', 'reason': 'unstable_result_structure'}`; `second`; `{'status': 'inconclusive', 'reason': 'verification_failed', 'error_type': type(exc).__name__, 'http_status': server_errors[0] if server_errors else None, 'access_restriction': executor.bloc…`.

**Relevante Aufrufe:** `asyncio.timeout`, `browser.close`, `browser.new_context`, `context.new_page`, `context.on`, `context.route`, `executor._navigate`, `executor.page.goto`, `executor.page.wait_for_timeout`, `self._executor`, `self._probe`.

#### `StructureVerifier.verify.route_request`

**Quellcode:** [StructureVerifier.py:168–172](src/crawler/StructureVerifier.py#L168-L172).

```python
async def route_request(route):
```

**Aufgabe:** Lokaler Routing-Callback beschränkt Requests auf erlaubte Ziele.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `route.abort`, `route.continue_`.

#### `StructureVerifier.verify.response`

**Quellcode:** [StructureVerifier.py:174–177](src/crawler/StructureVerifier.py#L174-L177).

```python
def response(r):
```

**Aufgabe:** Lokaler Response-Callback beobachtet Zugriffs- und Serverfehler.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `executor._response`.

#### `StructureVerifier.verify.check`

**Quellcode:** [StructureVerifier.py:180–183](src/crawler/StructureVerifier.py#L180-L183).

```python
async def check():
```

**Aufgabe:** Lokaler Guard prüft aktuellen Browser-/Fehlerzustand während Probe.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'HTTP {server_errors[0]} during verification; stop')`

**Relevante Aufrufe:** `executor._check_access`.

#### `StructureVerifier.verify.guarded`

**Quellcode:** [StructureVerifier.py:188–191](src/crawler/StructureVerifier.py#L188-L191).

```python
async def guarded():
```

**Aufgabe:** Lokaler Wrapper führt begrenzte Prüfung unter Guard aus.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ExecutionError(f'HTTP {server_errors[0]} during verification; stop')`

#### `StructureVerifier.verify.check_probe`

**Quellcode:** [StructureVerifier.py:199–206](src/crawler/StructureVerifier.py#L199-L206).

```python
async def check_probe():
```

**Aufgabe:** Lokaler Guard für erneute Locator-Probe und Zugriffsschutz.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ExecutionError('Dialog present during structural verification')`
- `ExecutionError('Result page changed during verification')`

**Relevante Aufrufe:** `executor._cookie_locator`, `executor._cookie_pending`, `executor.page.get_by_role`, `executor.page.get_by_role('dialog').filter`.

---

## crawler-crawler

**Modul:** [`src/crawler/crawler.py`](src/crawler/crawler.py)  
**Features/Storys:** A-01, D-01, E-01  
**Aufgabe und Abgrenzung:** Historisches Skript auf Modulebene, früherer Web-Search-Pilot. Bei Import oder Start können API- und Download-Aufrufe ausgelöst werden. Aus der aktiven Zielarchitektur ausgeschlossen; nicht ausführen.

**Direkte Abhängigkeiten:** `from ProjectPaths import LEGACY_EXECUTIONS_DIR, DOCUMENTS_DIR`; `import openai`; `import json`; `from uuid import uuid4`; `from OpenAIClient import OpenAIClient`; `from DocumentDownloader import DocumentDownloader`.

**Definitionen:** 0 Klassen, 0 Funktionen/Methoden (inkl. lokaler Definitionen).

Dieses Modul enthält keine eigene Klassen- oder Funktionsdefinition; sein Verhalten liegt auf Modulebene. Die Ausführung kann reale API-/HTTP-Aktionen auslösen; nicht als Bibliothek importieren.

**Modulweite Konfiguration / Verträge:** `DOCUMENT_SCHEMA`, `EXTRACTION_SCHEMA`, `DOCUMENT_SCHEMA_COMBI`, `COMPANY_SCHEMA`.

---

## crawler-main-benchmark

**Modul:** [`src/crawler/main_benchmark.py`](src/crawler/main_benchmark.py)  
**Features/Storys:** G-02  
**Aufgabe und Abgrenzung:** Offline-CLI für BenchmarkAnalyzer; liest konfigurierbare Report-/Metrikpfade und schreibt Benchmark-JSON/CSV.

**Direkte Abhängigkeiten:** `import argparse`; `from pathlib import Path`; `from ProjectPaths import RESULTS_DIR, BENCHMARK_DIR, metric_inputs`; `from BenchmarkAnalyzer import analyze, write_report`.

**Definitionen:** 0 Klassen, 1 Funktionen/Methoden (inkl. lokaler Definitionen).

#### `main`

**Quellcode:** [main_benchmark.py:8–28](src/crawler/main_benchmark.py#L8-L28).

```python
def main():
```

**Aufgabe:** Parst Report-, Timing-, Usage- und Baseline-Optionen, ruft Offline-Analyzer und write_report auf, gibt Ergebnisstatistik aus.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

---

## crawler-main-browser

**Modul:** [`src/crawler/main_browser.py`](src/crawler/main_browser.py)  
**Features/Storys:** C-02, D-01, E-02  
**Aufgabe und Abgrenzung:** Historischer Browser-Agent-Pilot auf Modulebene mit fest hinterlegter Aufgabenbeschreibung; reale Browser-/API-Kosten möglich. Kein regulärer Produktions- oder Discovery-Einstieg.

**Direkte Abhängigkeiten:** `import json`; `from ProjectPaths import LEGACY_EXECUTIONS_DIR`; `from uuid import uuid4`; `from OpenAIClient import OpenAIClient`.

**Definitionen:** 0 Klassen, 0 Funktionen/Methoden (inkl. lokaler Definitionen).

Dieses Modul enthält keine eigene Klassen- oder Funktionsdefinition; sein Verhalten liegt auf Modulebene. Die Ausführung kann reale API-/HTTP-Aktionen auslösen; nicht als Bibliothek importieren.

**Modulweite Konfiguration / Verträge:** `EXTRACTION_SCHEMA`.

---

## crawler-main-checkpoint

**Modul:** [`src/crawler/main_checkpoint.py`](src/crawler/main_checkpoint.py)  
**Features/Storys:** H-01  
**Aufgabe und Abgrenzung:** Read-only-CLI für die Inspektion eines SQLite-Checkpoints; keine Wiederaufnahme oder Reparatur.

**Direkte Abhängigkeiten:** `import argparse`; `import json`; `import sqlite3`; `from pathlib import Path`; `from CrawlCheckpoint import CrawlCheckpoint`.

**Definitionen:** 0 Klassen, 1 Funktionen/Methoden (inkl. lokaler Definitionen).

#### `main`

**Quellcode:** [main_checkpoint.py:9–18](src/crawler/main_checkpoint.py#L9-L18).

```python
def main():
```

**Aufgabe:** Parst Checkpoint-Pfad, ruft CrawlCheckpoint.inspect auf und gibt JSON aus.

**Rückgabe (Ausdrücke im Code):** `0`.

**Relevante Aufrufe:** `json.dumps`.

---

## crawler-main-discovery

**Modul:** [`src/crawler/main_discovery.py`](src/crawler/main_discovery.py)  
**Features/Storys:** C-04, C-05  
**Aufgabe und Abgrenzung:** CLI für neue KI-Discovery oder Import eines vorhandenen Strategie-JSONs. Kandidat speichern, niemals automatisch aktivieren; aktuelle Defaults auf Unternehmensregister zugeschnitten.

**Direkte Abhängigkeiten:** `import argparse`; `import json`; `from pathlib import Path`; `from ProjectPaths import DISCOVERY_DIR`; `from uuid import uuid4`; `from StrategySchema import DISCOVERY_SCHEMA`; `from StrategyStore import StrategyStore`.

**Definitionen:** 0 Klassen, 1 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `START_URL`, `DOMAINS`, `STRATEGY_NAME`, `PARAMETERS`, `PROMPT`.

#### `main`

**Quellcode:** [main_discovery.py:64–100](src/crawler/main_discovery.py#L64-L100).

```python
def main():
```

**Aufgabe:** Parst CLI-Optionen, importiert vorhandenen JSON-Kandidaten oder startet autorisierte KI-Browser-Discovery; speichert Kandidat und Report, aktiviert nicht.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `RuntimeError(f'Keine vollständige Strategieantwort: {response.status}')`

**Relevante Aufrufe:** `client.create`, `json.dump`, `json.load`, `json.loads`, `path.open`, `store.save`.

---

## crawler-main-execute

**Modul:** [`src/crawler/main_execute.py`](src/crawler/main_execute.py)  
**Features/Storys:** C-06  
**Aufgabe und Abgrenzung:** Begrenzte synchrone CLI, historische Kompatibilität. Kandidatenmodus begrenzt, nicht der bevorzugte zertifizierte asynchrone Betrieb.

**Direkte Abhängigkeiten:** `import argparse`; `import json`; `from pathlib import Path`; `from ProjectPaths import DOCUMENTS_DIR, EXECUTIONS_DIR`; `from uuid import uuid4`; `from StrategyExecutor import StrategyExecutor`; `from StrategyStore import StrategyStore`.

**Definitionen:** 0 Klassen, 1 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `DOMAIN`, `STRATEGY_NAME`, `START_URL`, `OPEN_CONTROLS`, `COOKIE_DIALOG`.

#### `main`

**Quellcode:** [main_execute.py:18–67](src/crawler/main_execute.py#L18-L67).

```python
def main():
```

**Aufgabe:** Parst begrenzte Ausführung, lädt Strategie/Parameter, startet synchronen Executor und schreibt Report.

**Rückgabe (Ausdrücke im Code):** `0 if output['status'] == 'completed' else 1`.

**Relevante Aufrufe:** `executor.run`, `json.dumps`, `path.parent.mkdir`, `path.write_text`, `store.load`, `store.load_active`.

---

## crawler-main-execute-async

**Modul:** [`src/crawler/main_execute_async.py`](src/crawler/main_execute_async.py)  
**Features/Storys:** C-07, C-09, H-01  
**Aufgabe und Abgrenzung:** Asynchrone Ausführungs-CLI mit Kandidaten-/Aktivstrategie, Worker-Policy, Plan-only, Vollcrawl und optionaler Recovery. Keine selbstständige SQLite-Wiederaufnahme.

**Direkte Abhängigkeiten:** `import argparse`; `import asyncio`; `import json`; `from pathlib import Path`; `from ProjectPaths import DOCUMENTS_DIR, EXECUTIONS_DIR, CHECKPOINTS_DIR, RECOVERY_DIR, checkpoint_file`; `from uuid import uuid4`; `from AsyncStrategyExecutor import AsyncStrategyExecutor`; `from StrategyStore import StrategyStore, content_digest`; `from ExecutionPolicy import get_policy`; `from FullCrawl import FullResultsExecutor, full_crawl_plan`; `from RecoveryManager import RecoveryManager, strategy_digest`; `from StructureVerifier import StructureVerifier`; `from StrategyRepair import StrategyRepair`.

**Definitionen:** 0 Klassen, 1 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `DOMAIN`, `STRATEGY_NAME`, `START_URL`, `OPEN_CONTROLS`, `COOKIE_DIALOG`.

#### `main`

**Quellcode:** [main_execute_async.py:24–168](src/crawler/main_execute_async.py#L24-L168).

```python
def main():
```

**Aufgabe:** Parst Plan-/Vollmodus-, Worker-, Kandidaten-, Download- und Recovery-Optionen; prüft Freigaben, startet passende Ausführung oder gibt Blocker aus, persistiert Reports.

**Rückgabe (Ausdrücke im Code):** `0 if plan['ready'] else 2`; `0 if output['displayed_results_traversed'] and output['result_limit_detected'] is not True else 1`; `0 if output['status'] == 'completed' else 1`.

**Explizite Fehler / Abbruch:**

- `ValueError('Expected pagination validation object')`

**Relevante Aufrufe:** `asyncio.run`, `executor.run`, `executor.run_full`, `json.dumps`, `json.loads`, `path.parent.mkdir`, `path.write_text`, `store.certified_active`, `store.load`.

---

## crawler-main-migrate-results

**Modul:** [`src/crawler/main_migrate_results.py`](src/crawler/main_migrate_results.py)  
**Features/Storys:** H-02  
**Aufgabe und Abgrenzung:** Offline-Migration bekannter alter Dateinamen in zentrale Ergebnisordner; Dry-run standardmäßig. Kein Überschreiben, keine inhaltliche Änderung historischer Daten; alle Writer vorher stoppen.

**Direkte Abhängigkeiten:** `import argparse`; `import json`; `import os`; `from pathlib import Path`; `from ProjectPaths import ROOT_DIR, REPORT_FOLDERS`.

**Definitionen:** 0 Klassen, 5 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `METRICS`, `BENCHMARKS`, `REFERENCES`.

#### `migration_plan`

**Quellcode:** [main_migrate_results.py:14–39](src/crawler/main_migrate_results.py#L14-L39).

```python
def migration_plan(root, register_references=False):
```

**Aufgabe:** Ermittelt bekannte Flat-/Legacy-Dateien und Zielpfade; manuelle Referenzen nur bei expliziter Option. Keine Änderung.

**Parameter:** `root`: erlaubter Wurzelpfad; `register_references`: manuelle Referenzen explizit in Migrationsplan einbeziehen. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `moves`.

**Explizite Fehler / Abbruch:**

- `ValueError(f'Project root missing: {root}')`

#### `migration_plan.add`

**Quellcode:** [main_migrate_results.py:21–23](src/crawler/main_migrate_results.py#L21-L23).

```python
def add(source, target):
```

**Aufgabe:** Lokaler Helper nimmt vorhandene Quelldatei und Ziel in Plan auf.

**Parameter:** `target`: konkretes Zielobjekt bzw. Locator. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

#### `check_plan`

**Quellcode:** [main_migrate_results.py:42–63](src/crawler/main_migrate_results.py#L42-L63).

```python
def check_plan(root, moves):
```

**Aufgabe:** Prüft sämtliche geplanten Moves auf Konflikte, Symlinks, Zielüberschneidungen und Pfad-/Dateisystembedingungen, bevor geschrieben wird.

**Parameter:** `root`: erlaubter Wurzelpfad; `moves`: geplante Datei-Verschiebungen. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `ValueError(f'Path outside root: {path}')`
- `ValueError(f'Symlink not supported: {part}')`
- `ValueError(f'Not a regular source file: {source}')`
- `ValueError(f'Destination conflict: {target}; reconcile manually before migration')`
- `ValueError(f'Migration requires a directory on the same filesystem: {target}')`

**Relevante Aufrufe:** `path.is_relative_to`, `target.exists`.

#### `apply_plan`

**Quellcode:** [main_migrate_results.py:66–73](src/crawler/main_migrate_results.py#L66-L73).

```python
def apply_plan(root, moves):
```

**Aufgabe:** Führt geprüfte Moves ohne Überschreiben aus; Einzelmoves sind nicht gemeinsam atomar.

**Parameter:** `root`: erlaubter Wurzelpfad; `moves`: geplante Datei-Verschiebungen. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `os.link`, `target.parent.mkdir`.

#### `main`

**Quellcode:** [main_migrate_results.py:76–93](src/crawler/main_migrate_results.py#L76-L93).

```python
def main():
```

**Aufgabe:** CLI erstellt und zeigt Plan, prüft Konflikte und führt nur mit --apply aus.

**Rückgabe (Ausdrücke im Code):** `0`.

**Relevante Aufrufe:** `json.dumps`.

---

## crawler-main-recovery

**Modul:** [`src/crawler/main_recovery.py`](src/crawler/main_recovery.py)  
**Features/Storys:** C-08  
**Aufgabe und Abgrenzung:** Offline-Klassifizierung und optionale autorisierte Read-only-Verifikation/Reparatur eines Execution-Reports.

**Direkte Abhängigkeiten:** `import argparse`; `import asyncio`; `import json`; `from pathlib import Path`; `from ProjectPaths import RECOVERY_DIR`; `from ExecutionPolicy import get_policy`; `from RecoveryManager import RecoveryManager`; `from StrategyRepair import StrategyRepair`; `from StructureVerifier import StructureVerifier`; `from StrategyStore import StrategyStore`; `from main_execute_async import DOMAIN, STRATEGY_NAME, COOKIE_DIALOG, OPEN_CONTROLS`.

**Definitionen:** 0 Klassen, 1 Funktionen/Methoden (inkl. lokaler Definitionen).

#### `main`

**Quellcode:** [main_recovery.py:16–38](src/crawler/main_recovery.py#L16-L38).

```python
def main():
```

**Aufgabe:** Parst Execution-Report und Freigabeoptionen, erzeugt RecoveryManager, führt kontrollierte Offline-/Verifikationslogik aus und schreibt Report.

**Rückgabe (Ausdrücke im Code):** `int(result['status'] == 'failed')`.

**Relevante Aufrufe:** `asyncio.run`, `json.dumps`, `json.loads`, `path.parent.mkdir`, `path.write_text`.

---

## crawler-main-strategy

**Modul:** [`src/crawler/main_strategy.py`](src/crawler/main_strategy.py)  
**Features/Storys:** F-02, F-03, H-03  
**Aufgabe und Abgrenzung:** Operator-CLI für Strategie-Status, unabhängige Validierung, Paginierungsprüfung, zertifizierte Aktivierung/Rollback und begrenzten Resume.

**Direkte Abhängigkeiten:** `import argparse`; `import asyncio`; `import json`; `from pathlib import Path`; `from ProjectPaths import report_directory`; `from uuid import uuid4`; `from ExecutionPolicy import get_policy`; `from StrategyStore import StrategyStore`; `from StrategyValidator import StrategyValidator`; `from PaginationValidator import PaginationValidator`; `from ResumePlanner import ResumePlanner`; `from main_execute_async import DOMAIN, STRATEGY_NAME, COOKIE_DIALOG, OPEN_CONTROLS`.

**Definitionen:** 0 Klassen, 4 Funktionen/Methoden (inkl. lokaler Definitionen).

#### `version_or_none`

**Quellcode:** [main_strategy.py:17–23](src/crawler/main_strategy.py#L17-L23).

```python
def version_or_none(value):
```

**Aufgabe:** Parst erwartete Version bzw. none für CLI-Compare-and-swap.

**Parameter:** `value`: übergebener Wert gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`; `version`.

**Explizite Fehler / Abbruch:**

- `argparse.ArgumentTypeError('Positive version or none required')`

#### `read`

**Quellcode:** [main_strategy.py:26–27](src/crawler/main_strategy.py#L26-L27).

```python
def read(path):
```

**Aufgabe:** Liest JSON-Bericht/Referenz aus Datei.

**Parameter:** `path`: Datei-/Verzeichnispfad gemäß Funktionszweck. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `json.loads(path.read_text(encoding='utf-8'))`.

**Relevante Aufrufe:** `json.loads`, `path.read_text`.

#### `save_report`

**Quellcode:** [main_strategy.py:30–36](src/crawler/main_strategy.py#L30-L36).

```python
def save_report(report, suffix):
```

**Aufgabe:** Schreibt Report unter dem passenden zentralen Suffixpfad.

**Parameter:** `report`: strukturiertes Berichts-Dictionary; `suffix`: Berichts-Suffix. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

#### `main`

**Quellcode:** [main_strategy.py:39–141](src/crawler/main_strategy.py#L39-L141).

```python
def main():
```

**Aufgabe:** Verarbeitet Subcommands für Status, Validierung, Paginierung, Aktivierung/Rollback und begrenzte Fortsetzung; prüft Optionen und gibt Reports/Status aus.

**Rückgabe (Ausdrücke im Code):** `0`; `0 if passed else 1`; `0 if report['status'] == 'passed' else 1`; `1`; `0 if plan['status'] in ('ready', 'nothing_pending') else 1`; `0 if result['status'] == 'completed' else 1`.

**Relevante Aufrufe:** `asyncio.run`, `json.dumps`, `store._manifest`, `store.promote_certified`.

---

## crawler-retry-downloads

**Modul:** [`src/crawler/retry_downloads.py`](src/crawler/retry_downloads.py)  
**Features/Storys:** E-01  
**Aufgabe und Abgrenzung:** Historischer Modulebene-Einstieg in die direkte HTTP-Queue. Nicht mit der sicheren SQLite-Wiederaufnahme verwechseln und aufgrund bekannter Legacy-Vertragsfehler nicht regulär ausführen.

**Direkte Abhängigkeiten:** `from DocumentDownloader import DocumentDownloader`.

**Definitionen:** 0 Klassen, 0 Funktionen/Methoden (inkl. lokaler Definitionen).

Dieses Modul enthält keine eigene Klassen- oder Funktionsdefinition; sein Verhalten liegt auf Modulebene. Die Ausführung kann reale API-/HTTP-Aktionen auslösen; nicht als Bibliothek importieren.

---

## Testmodule

## tests-testrunner

**Modul:** [`src/tests/TestRunner.py`](src/tests/TestRunner.py)  
**Features/Storys:** F-07  
**Aufgabe und Abgrenzung:** Gemeinsamer unittest-Runner; konfiguriert Importpfad nur im Testprozess und erfasst genau einen abschließenden Status je Test, Fixture-Probleme separat.

**Direkte Abhängigkeiten:** `import sys`; `import unittest`; `from collections import Counter`; `from pathlib import Path`.

**Definitionen:** 2 Klassen, 13 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `CRAWLER_DIR`.

### Klasse `ProgressResult`

**Quellcode:** [TestRunner.py:16–72](src/tests/TestRunner.py#L16-L72).

**Aufgabe:** Spezialisiert unittest.TextTestResult und hält pro Test genau einen abschließenden Status sowie getrennte Fixture-Zähler.

**Basisklassen:** `unittest.TextTestResult`.

#### `ProgressResult.__init__`

**Quellcode:** [TestRunner.py:17–23](src/tests/TestRunner.py#L17-L23).

```python
def __init__(self, *args, **kwargs):
```

**Aufgabe:** Initialisiert TextTestResult, Counter, separate Fixture-Zähler und leeren aktuellen Testzustand.

**Parameter:** `args`: weitergereichte Positionsparameter; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.outcomes`, `self.fixture_errors`, `self.fixture_skips`, `self._current`, `self._outcome`.

**Relevante Aufrufe:** `Counter`, `super().__init__`.

#### `ProgressResult.startTest`

**Quellcode:** [TestRunner.py:25–27](src/tests/TestRunner.py#L25-L27).

```python
def startTest(self, test):
```

**Aufgabe:** Beginnt einen Test mit Status incomplete und delegiert Standardausgabe.

**Parameter:** `test`: unittest-Test oder Suite. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self._current`, `self._outcome`.

**Relevante Aufrufe:** `super().startTest`.

#### `ProgressResult.stopTest`

**Quellcode:** [TestRunner.py:29–32](src/tests/TestRunner.py#L29-L32).

```python
def stopTest(self, test):
```

**Aufgabe:** Zählt endgültigen Status einmal und setzt den aktuellen Test zurück.

**Parameter:** `test`: unittest-Test oder Suite. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self._current`, `self._outcome`.

**Relevante Aufrufe:** `super().stopTest`.

#### `ProgressResult._record`

**Quellcode:** [TestRunner.py:34–36](src/tests/TestRunner.py#L34-L36).

```python
def _record(self, outcome):
```

**Aufgabe:** Aktualisiert laufenden Teststatus, ohne ein bereits festgestelltes Scheitern zu überschreiben.

**Parameter:** `outcome`: abschließender Teststatus. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self._outcome`.

#### `ProgressResult.addSuccess`

**Quellcode:** [TestRunner.py:38–41](src/tests/TestRunner.py#L38-L41).

```python
def addSuccess(self, test):
```

**Aufgabe:** Registriert Erfolg nur, wenn noch kein abweichendes Ergebnis vorliegt.

**Parameter:** `test`: unittest-Test oder Suite. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self._record`, `super().addSuccess`.

#### `ProgressResult.addFailure`

**Quellcode:** [TestRunner.py:43–45](src/tests/TestRunner.py#L43-L45).

```python
def addFailure(self, test, err):
```

**Aufgabe:** Registriert fehlgeschlagenen Test.

**Parameter:** `test`: unittest-Test oder Suite; `err`: unittest-Fehlertupel. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self._record`, `super().addFailure`.

#### `ProgressResult.addError`

**Quellcode:** [TestRunner.py:47–52](src/tests/TestRunner.py#L47-L52).

```python
def addError(self, test, err):
```

**Aufgabe:** Zählt Fehler außerhalb eines Testfalls separat als Fixture-Fehler; ansonsten failed.

**Parameter:** `test`: unittest-Test oder Suite; `err`: unittest-Fehlertupel. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.fixture_errors`.

**Relevante Aufrufe:** `self._record`, `super().addError`.

#### `ProgressResult.addSubTest`

**Quellcode:** [TestRunner.py:54–57](src/tests/TestRunner.py#L54-L57).

```python
def addSubTest(self, test, subtest, err):
```

**Aufgabe:** Registriert einen fehlgeschlagenen Subtest am übergeordneten Test.

**Parameter:** `test`: unittest-Test oder Suite; `subtest`: unittest-Subtest; `err`: unittest-Fehlertupel. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self._record`, `super().addSubTest`.

#### `ProgressResult.addSkip`

**Quellcode:** [TestRunner.py:59–64](src/tests/TestRunner.py#L59-L64).

```python
def addSkip(self, test, reason):
```

**Aufgabe:** Registriert Skip eines Testfalls oder einer Fixture separat.

**Parameter:** `test`: unittest-Test oder Suite; `reason`: Begründung bzw. Skip-Grund. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.fixture_skips`.

**Relevante Aufrufe:** `self._record`, `super().addSkip`.

#### `ProgressResult.addExpectedFailure`

**Quellcode:** [TestRunner.py:66–68](src/tests/TestRunner.py#L66-L68).

```python
def addExpectedFailure(self, test, err):
```

**Aufgabe:** Registriert erwarteten Fehler separat.

**Parameter:** `test`: unittest-Test oder Suite; `err`: unittest-Fehlertupel. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self._record`, `super().addExpectedFailure`.

#### `ProgressResult.addUnexpectedSuccess`

**Quellcode:** [TestRunner.py:70–72](src/tests/TestRunner.py#L70-L72).

```python
def addUnexpectedSuccess(self, test):
```

**Aufgabe:** Wertet unerwarteten Erfolg als failed.

**Parameter:** `test`: unittest-Test oder Suite. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self._record`, `super().addUnexpectedSuccess`.

### Klasse `TestRunner`

**Quellcode:** [TestRunner.py:75–98](src/tests/TestRunner.py#L75-L98).

**Aufgabe:** Spezialisiert TextTestRunner; erzwingt standardmäßig Verbosity 2 und ProgressResult.

**Basisklassen:** `unittest.TextTestRunner`.

#### `TestRunner.__init__`

**Quellcode:** [TestRunner.py:76–79](src/tests/TestRunner.py#L76-L79).

```python
def __init__(self, *args, **kwargs):
```

**Aufgabe:** Setzt Verbosity 2 und ProgressResult, sofern der Aufrufer nichts anderes vorgibt, und initialisiert TextTestRunner.

**Parameter:** `args`: weitergereichte Positionsparameter; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `kwargs.setdefault`, `super().__init__`.

#### `TestRunner.run`

**Quellcode:** [TestRunner.py:81–98](src/tests/TestRunner.py#L81-L98).

```python
def run(self, test):
```

**Aufgabe:** Führt Suite aus, gibt zusätzliche Abschlussstatistik mit OK/NICHT OK/Skip/Expected Failure und Fixture-Status aus und liefert das Result-Objekt.

**Parameter:** `test`: unittest-Test oder Suite. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `result`.

**Relevante Aufrufe:** `result.wasSuccessful`, `self.stream.flush`, `self.stream.writeln`, `super().run`.

---

## tests-main-tests

**Modul:** [`src/tests/main_tests.py`](src/tests/main_tests.py)  
**Features/Storys:** F-07  
**Aufgabe und Abgrenzung:** Zentraler CLI-Einstieg in unittest; ohne Argumente Discovery unter tests, sonst explizite Module/Methoden. Importiert TestRunner zur Pfadkonfiguration.

**Direkte Abhängigkeiten:** `import sys`; `import unittest`; `from pathlib import Path`; `from TestRunner import TestRunner`.

**Definitionen:** 0 Klassen, 0 Funktionen/Methoden (inkl. lokaler Definitionen).

Dieses Modul enthält keine eigene Klassen- oder Funktionsdefinition; sein Verhalten liegt auf Modulebene. Es delegiert an unittest/TestRunner.

---

## tests-test-benchmark

**Modul:** [`src/tests/test_benchmark.py`](src/tests/test_benchmark.py)  
**Features/Storys:** G-02  
**Aufgabe und Abgrenzung:** Offline-Regression der Kosten- und Laufzeitaggregation, historischen CSV-Formate und Run-Deduplizierung. Temporäre Dateien.

**Direkte Abhängigkeiten:** `import csv`; `import json`; `import tempfile`; `import unittest`; `from TestRunner import TestRunner`; `from pathlib import Path`; `from BenchmarkAnalyzer import aggregate_usage, analyze, read_rows, timing_summary, write_report`.

**Definitionen:** 1 Klassen, 11 Funktionen/Methoden (inkl. lokaler Definitionen).

### Klasse `BenchmarkTests`

**Quellcode:** [test_benchmark.py:11–103](src/tests/test_benchmark.py#L11-L103).

**Aufgabe:** TestCase für Offline-Regression der Kosten- und Laufzeitaggregation, historischen CSV-Formate und Run-Deduplizierung. Temporäre Dateien.

**Basisklassen:** `unittest.TestCase`.

#### `BenchmarkTests.test_mixed_usage_csv`

**Quellcode:** [test_benchmark.py:12–22](src/tests/test_benchmark.py#L12-L22).

```python
def test_mixed_usage_csv(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(rows[1]['cost_usd'], '0.011')`
- `self.assertEqual(aggregate_usage(rows, 2)['cost_usd'], '0.021')`
- `self.assertEqual(analyze(tmp, usage_paths=[path])['observed_usage']['known_cost_usd'], '0.021')`

**Relevante Aufrufe:** `aggregate_usage`, `analyze`, `path.write_text`, `read_rows`.

#### `BenchmarkTests.test_unexpected_csv_width`

**Quellcode:** [test_benchmark.py:24–29](src/tests/test_benchmark.py#L24-L29).

```python
def test_unexpected_csv_width(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValueError)`

**Relevante Aufrufe:** `path.write_text`, `read_rows`.

#### `BenchmarkTests.test_zero_calls`

**Quellcode:** [test_benchmark.py:31–33](src/tests/test_benchmark.py#L31-L33).

```python
def test_zero_calls(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(aggregate_usage([], 0)['cost_usd'], '0')`
- `self.assertEqual(aggregate_usage([], 0)['total_tokens'], 0)`

**Relevante Aufrufe:** `aggregate_usage`.

#### `BenchmarkTests.test_missing_usage`

**Quellcode:** [test_benchmark.py:35–39](src/tests/test_benchmark.py#L35-L39).

```python
def test_missing_usage(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertIsNone(result['cost_usd'])`
- `self.assertIsNone(result['total_tokens'])`
- `self.assertTrue(result['usage_count_mismatch'])`

**Relevante Aufrufe:** `aggregate_usage`.

#### `BenchmarkTests.test_csv_cost_and_cached_tokens`

**Quellcode:** [test_benchmark.py:41–45](src/tests/test_benchmark.py#L41-L45).

```python
def test_csv_cost_and_cached_tokens(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['cached_input_tokens'], 20)`
- `self.assertEqual(result['cost_usd'], '0.0012')`

**Relevante Aufrufe:** `aggregate_usage`.

#### `BenchmarkTests.test_jsonl_unknown_pricing`

**Quellcode:** [test_benchmark.py:47–51](src/tests/test_benchmark.py#L47-L51).

```python
def test_jsonl_unknown_pricing(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertIsNone(result['cost_usd'])`
- `self.assertEqual(result['known_cost_usd'], '0.01')`
- `self.assertEqual(result['unpriced_records'], 1)`

**Relevante Aufrufe:** `aggregate_usage`.

#### `BenchmarkTests.test_missing_request`

**Quellcode:** [test_benchmark.py:53–54](src/tests/test_benchmark.py#L53-L54).

```python
def test_missing_request(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertFalse(aggregate_usage([dict(cost_usd='0.01')], 2)['cost_complete'])`

**Relevante Aufrufe:** `aggregate_usage`.

#### `BenchmarkTests.test_overlapping_phases`

**Quellcode:** [test_benchmark.py:56–60](src/tests/test_benchmark.py#L56-L60).

```python
def test_overlapping_phases(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['duration_seconds'], 10)`
- `self.assertEqual(result['phases']['download']['seconds'], 17)`

**Relevante Aufrufe:** `timing_summary`.

#### `BenchmarkTests.test_ambiguous_wall_time`

**Quellcode:** [test_benchmark.py:62–64](src/tests/test_benchmark.py#L62-L64).

```python
def test_ambiguous_wall_time(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertIsNone(result['duration_seconds'])`

**Relevante Aufrufe:** `timing_summary`.

#### `BenchmarkTests.test_report_join_and_child_deduplication`

**Quellcode:** [test_benchmark.py:66–94](src/tests/test_benchmark.py#L66-L94).

```python
def test_report_join_and_child_deduplication(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(set(runs), {'validation', 'repair', 'discovery'})`
- `self.assertEqual(runs['repair']['cost_usd'], '0.003')`
- `self.assertEqual(runs['discovery']['llm_calls'], 1)`
- `self.assertEqual(runs['validation']['documents_downloaded'], 1)`
- `self.assertEqual(runs['validation']['cost_usd'], '0')`
- `self.assertTrue((root / 'output' / 'benchmark_runs.csv').exists())`

**Relevante Aufrufe:** `(root / 'child_execution.json').write_text`, `(root / 'discovery_strategy.json').write_text`, `(root / 'output' / 'benchmark_runs.csv').exists`, `(root / 'recovery_recovery.json').write_text`, `(root / 'validation_validation.json').write_text`, `analyze`, `csv.DictWriter`, `timing.open`, `usage.write_text`, `write_report`, `writer.writeheader`, `writer.writerow`.

#### `BenchmarkTests.test_duplicate_usage_id`

**Quellcode:** [test_benchmark.py:96–103](src/tests/test_benchmark.py#L96-L103).

```python
def test_duplicate_usage_id(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(analyze(root, usage_paths=[usage])['runs'][0]['cost_usd'], '0.01')`

**Relevante Aufrufe:** `(root / 'r_recovery.json').write_text`, `analyze`, `usage.write_text`.

---

## tests-test-checkpoint

**Modul:** [`src/tests/test_checkpoint.py`](src/tests/test_checkpoint.py)  
**Features/Storys:** H-01  
**Aufgabe und Abgrenzung:** SQLite-Transaktionen, Dokumentzustände, Dateiintegrität und Prozessabbruch. Temporäre DB und Dokumente; kein Browser.

**Direkte Abhängigkeiten:** `import hashlib`; `import sqlite3`; `import subprocess`; `import sys`; `import tempfile`; `import unittest`; `from TestRunner import TestRunner`; `from pathlib import Path`; `from CrawlCheckpoint import CrawlCheckpoint`.

**Definitionen:** 1 Klassen, 12 Funktionen/Methoden (inkl. lokaler Definitionen).

#### `record`

**Quellcode:** [test_checkpoint.py:13–16](src/tests/test_checkpoint.py#L13-L16).

```python
def record(n):
```

**Aufgabe:** Erzeugt synthetischen Datensatz mit Registeridentität und geplanten CD-/SI-Dokumenten.

**Rückgabe (Ausdrücke im Code):** `dict(register_number=str(n), company_name=f'Firma {n}', source_url='https://example.test/?token=secret', documents=[dict(document_type='CD', file_type='pdf', download_status='not_attempted'…`.

### Klasse `CheckpointTests`

**Quellcode:** [test_checkpoint.py:19–125](src/tests/test_checkpoint.py#L19-L125).

**Aufgabe:** TestCase für SQLite-Transaktionen, Dokumentzustände, Dateiintegrität und Prozessabbruch. Temporäre DB und Dokumente; kein Browser.

**Basisklassen:** `unittest.TestCase`.

#### `CheckpointTests.setUp`

**Quellcode:** [test_checkpoint.py:20–29](src/tests/test_checkpoint.py#L20-L29).

```python
def setUp(self):
```

**Aufgabe:** Bereitet isolierte Test-Fixture vor; temporäre Ressourcen und Cleanup entsprechend der konkreten Einrichtung unten.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.root`, `self.path`, `self.docs`, `self.cp`, `self.r`.

**Relevante Aufrufe:** `CrawlCheckpoint`, `record`, `self.docs.mkdir`.

#### `CheckpointTests.save`

**Quellcode:** [test_checkpoint.py:31–32](src/tests/test_checkpoint.py#L31-L32).

```python
def save(self, downloads=True):
```

**Aufgabe:** Speichert Teststrategie oder Testseite in lokalem temporärem Store/Checkpoint.

**Parameter:** `downloads`: Dokumentdownload aktivieren. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self.cp.save_page`.

#### `CheckpointTests.downloaded`

**Quellcode:** [test_checkpoint.py:34–39](src/tests/test_checkpoint.py#L34-L39).

```python
def downloaded(self, doc):
```

**Aufgabe:** Erzeugt lokale synthetische Datei und Downloadmetadaten mit korrekter Größe/Hash.

**Parameter:** `doc`: Dokument-Metadaten. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `dict(doc, download_status='downloaded', file_path=str(path), filename=path.name, size_bytes=len(payload), sha256=hashlib.sha256(payload).hexdigest())`.

**Relevante Aufrufe:** `hashlib.sha256`, `hashlib.sha256(payload).hexdigest`, `path.write_bytes`.

#### `CheckpointTests.test_transaction_and_document_lifecycle`

**Quellcode:** [test_checkpoint.py:41–59](src/tests/test_checkpoint.py#L41-L59).

```python
def test_transaction_and_document_lifecycle(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(CrawlCheckpoint.inspect(self.path)['document_counts']['in_progress'], 1)`
- `self.assertRaises(ValueError)`
- `self.assertEqual(snapshot['pages_processed'], 1)`
- `self.assertEqual(snapshot['companies_documents_done'], 1)`
- `self.assertEqual(snapshot['document_counts']['downloaded'], 2)`
- `self.assertEqual(snapshot['job']['status'], 'completed')`
- `self.assertFalse(snapshot['resume_supported'])`
- `self.assertNotIn('token=secret', self.cp.db.execute('SELECT record_json FROM companies').fetchone()[0])`

**Relevante Aufrufe:** `CrawlCheckpoint.inspect`, `self.cp.db.execute`, `self.cp.db.execute('SELECT record_json FROM companies').fetchone`, `self.cp.finish`, `self.cp.finish_document`, `self.cp.finish_page`, `self.cp.start_document`, `self.downloaded`, `self.save`.

#### `CheckpointTests.test_metadata_only`

**Quellcode:** [test_checkpoint.py:61–64](src/tests/test_checkpoint.py#L61-L64).

```python
def test_metadata_only(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(CrawlCheckpoint.inspect(self.path)['document_counts']['not_requested'], 2)`

**Relevante Aufrufe:** `CrawlCheckpoint.inspect`, `self.cp.finish_page`, `self.save`.

#### `CheckpointTests.test_failed_document_blocks_page`

**Quellcode:** [test_checkpoint.py:66–76](src/tests/test_checkpoint.py#L66-L76).

```python
def test_failed_document_blocks_page(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValueError)`
- `self.assertEqual(CrawlCheckpoint.inspect(self.path)['document_counts']['failed'], 1)`

**Relevante Aufrufe:** `CrawlCheckpoint.inspect`, `self.cp.finish`, `self.cp.finish_document`, `self.cp.finish_page`, `self.cp.start_document`, `self.save`.

#### `CheckpointTests.test_duplicate_page_rolls_back`

**Quellcode:** [test_checkpoint.py:78–85](src/tests/test_checkpoint.py#L78-L85).

```python
def test_duplicate_page_rolls_back(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(sqlite3.IntegrityError)`
- `self.assertEqual(snapshot['companies_extracted'], 1)`
- `self.assertEqual(len(snapshot['pages']), 1)`

**Relevante Aufrufe:** `CrawlCheckpoint.inspect`, `record`, `self.cp.finish_page`, `self.cp.save_page`, `self.save`.

#### `CheckpointTests.test_existing_job_never_overwritten`

**Quellcode:** [test_checkpoint.py:87–90](src/tests/test_checkpoint.py#L87-L90).

```python
def test_existing_job_never_overwritten(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(FileExistsError)`
- `self.assertEqual(CrawlCheckpoint.inspect(self.path)['job']['crawl_id'], 'test')`

**Relevante Aufrufe:** `CrawlCheckpoint`, `CrawlCheckpoint.inspect`.

#### `CheckpointTests.test_wrong_file_hash_remains_uncertain`

**Quellcode:** [test_checkpoint.py:92–100](src/tests/test_checkpoint.py#L92-L100).

```python
def test_wrong_file_hash_remains_uncertain(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValueError)`
- `self.assertEqual(CrawlCheckpoint.inspect(self.path)['document_counts']['in_progress'], 1)`

**Relevante Aufrufe:** `CrawlCheckpoint.inspect`, `self.cp.finish_document`, `self.cp.start_document`, `self.downloaded`, `self.save`.

#### `CheckpointTests.test_unfinished_job_cannot_complete`

**Quellcode:** [test_checkpoint.py:102–106](src/tests/test_checkpoint.py#L102-L106).

```python
def test_unfinished_job_cannot_complete(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValueError)`
- `self.assertEqual(CrawlCheckpoint.inspect(self.path)['job']['status'], 'running')`

**Relevante Aufrufe:** `CrawlCheckpoint.inspect`, `self.cp.finish`, `self.save`.

#### `CheckpointTests.test_hard_process_exit_preserves_commits`

**Quellcode:** [test_checkpoint.py:108–125](src/tests/test_checkpoint.py#L108-L125).

```python
def test_hard_process_exit_preserves_commits(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result.returncode, 27)`
- `self.assertEqual(snapshot['job']['status'], 'running')`
- `self.assertEqual(snapshot['document_counts']['in_progress'], 1)`
- `self.assertEqual(snapshot['document_counts']['not_attempted'], 1)`

**Relevante Aufrufe:** `CrawlCheckpoint.inspect`, `Path(__file__).resolve`, `subprocess.run`.

---

## tests-test-error-classifier

**Modul:** [`src/tests/test_error_classifier.py`](src/tests/test_error_classifier.py)  
**Features/Storys:** F-01  
**Aufgabe und Abgrenzung:** Offline-Klassifikation synthetischer Reports und optional historischer JSON-Dateien; keine Reparatur/Netzwerk.

**Direkte Abhängigkeiten:** `import argparse`; `import copy`; `import json`; `import unittest`; `from TestRunner import TestRunner`; `from pathlib import Path`; `from ErrorClassifier import ErrorClassifier, attach_error_classification`.

**Definitionen:** 1 Klassen, 27 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `HISTORY`.

#### `failure`

**Quellcode:** [test_error_classifier.py:26–27](src/tests/test_error_classifier.py#L26-L27).

```python
def failure(message, kind='ExecutionError', **extra):
```

**Aufgabe:** Erzeugt minimalen fehlgeschlagenen Execution-Report für Klassifikation.

**Rückgabe (Ausdrücke im Code):** `{'status': 'failed', 'error': {'type': kind, 'message': message, 'step': 3}, **extra}`.

#### `worker`

**Quellcode:** [test_error_classifier.py:30–32](src/tests/test_error_classifier.py#L30-L32).

```python
def worker(message, **extra):
```

**Aufgabe:** Erzeugt synthetischen Workerfehler mit Dokument-/Step-Kontext.

**Rückgabe (Ausdrücke im Code):** `{'worker_id': 2, 'step': 12, 'document_type': 'CD', 'error_type': 'TimeoutError', 'error': message, **extra}`.

### Klasse `ClassifierTests`

**Quellcode:** [test_error_classifier.py:35–139](src/tests/test_error_classifier.py#L35-L139).

**Aufgabe:** TestCase für Offline-Klassifikation synthetischer Reports und optional historischer JSON-Dateien; keine Reparatur/Netzwerk.

**Basisklassen:** `unittest.TestCase`.

#### `ClassifierTests.check`

**Quellcode:** [test_error_classifier.py:36–43](src/tests/test_error_classifier.py#L36-L43).

```python
def check(self, report, category):
```

**Aufgabe:** Klassifiziert Report und prüft erwartete Kategorie sowie unveränderten Eingabereport und gesperrte LLM-Freigabe.

**Parameter:** `report`: strukturiertes Berichts-Dictionary; `category`: Fehlerkategorie. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `result`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['primary']['category'], category)`
- `self.assertEqual(report, original)`
- `self.assertFalse(result['primary']['llm_allowed'])`
- `self.assertFalse(result['primary']['automatic_retry_allowed'])`

**Relevante Aufrufe:** `ErrorClassifier.classify`, `copy.deepcopy`.

#### `ClassifierTests.test_success_with_recovered_navigation`

**Quellcode:** [test_error_classifier.py:45–46](src/tests/test_error_classifier.py#L45-L46).

```python
def test_success_with_recovered_navigation(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `self.check`.

#### `ClassifierTests.test_access_signals`

**Quellcode:** [test_error_classifier.py:48–51](src/tests/test_error_classifier.py#L48-L51).

```python
def test_access_signals(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`.

#### `ClassifierTests.test_global_access_over_worker_server`

**Quellcode:** [test_error_classifier.py:53–56](src/tests/test_error_classifier.py#L53-L56).

```python
def test_global_access_over_worker_server(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual([f['category'] for f in result['findings']], ['SERVER_ERROR', 'ACCESS_RESTRICTED'])`

**Relevante Aufrufe:** `failure`, `self.check`, `worker`.

#### `ClassifierTests.test_structured_server`

**Quellcode:** [test_error_classifier.py:58–60](src/tests/test_error_classifier.py#L58-L60).

```python
def test_structured_server(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`, `worker`.

#### `ClassifierTests.test_historical_server_page`

**Quellcode:** [test_error_classifier.py:62–67](src/tests/test_error_classifier.py#L62-L67).

```python
def test_historical_server_page(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((result['primary']['worker_id'], result['primary']['step']), (2, 12))`
- `self.assertIn('Original document response not established', result['primary']['evidence'])`

**Relevante Aufrufe:** `failure`, `self.check`, `worker`.

#### `ClassifierTests.test_unrelated_network_errors`

**Quellcode:** [test_error_classifier.py:69–74](src/tests/test_error_classifier.py#L69-L74).

```python
def test_unrelated_network_errors(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`, `worker`.

#### `ClassifierTests.test_access_after_server_in_events`

**Quellcode:** [test_error_classifier.py:76–80](src/tests/test_error_classifier.py#L76-L80).

```python
def test_access_after_server_in_events(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`, `worker`.

#### `ClassifierTests.test_network`

**Quellcode:** [test_error_classifier.py:82–83](src/tests/test_error_classifier.py#L82-L83).

```python
def test_network(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`.

#### `ClassifierTests.test_domain`

**Quellcode:** [test_error_classifier.py:85–86](src/tests/test_error_classifier.py#L85-L86).

```python
def test_domain(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`.

#### `ClassifierTests.test_cookie`

**Quellcode:** [test_error_classifier.py:88–91](src/tests/test_error_classifier.py#L88-L91).

```python
def test_cookie(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`.

#### `ClassifierTests.test_menu`

**Quellcode:** [test_error_classifier.py:93–94](src/tests/test_error_classifier.py#L93-L94).

```python
def test_menu(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`.

#### `ClassifierTests.test_download_timeout`

**Quellcode:** [test_error_classifier.py:96–97](src/tests/test_error_classifier.py#L96-L97).

```python
def test_download_timeout(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`.

#### `ClassifierTests.test_document_http`

**Quellcode:** [test_error_classifier.py:99–100](src/tests/test_error_classifier.py#L99-L100).

```python
def test_document_http(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`.

#### `ClassifierTests.test_document_validation`

**Quellcode:** [test_error_classifier.py:102–104](src/tests/test_error_classifier.py#L102-L104).

```python
def test_document_validation(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`.

#### `ClassifierTests.test_data_validation`

**Quellcode:** [test_error_classifier.py:106–109](src/tests/test_error_classifier.py#L106-L109).

```python
def test_data_validation(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`.

#### `ClassifierTests.test_strategy_invalid`

**Quellcode:** [test_error_classifier.py:111–112](src/tests/test_error_classifier.py#L111-L112).

```python
def test_strategy_invalid(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`.

#### `ClassifierTests.test_structure_suspected_not_confirmed`

**Quellcode:** [test_error_classifier.py:114–116](src/tests/test_error_classifier.py#L114-L116).

```python
def test_structure_suspected_not_confirmed(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertTrue(result['requires_structure_verification'])`

**Relevante Aufrufe:** `failure`, `self.check`.

#### `ClassifierTests.test_mixed_failures_no_structure_review`

**Quellcode:** [test_error_classifier.py:118–122](src/tests/test_error_classifier.py#L118-L122).

```python
def test_mixed_failures_no_structure_review(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertFalse(result['requires_structure_verification'])`
- `self.assertEqual(len(result['findings']), 2)`

**Relevante Aufrufe:** `failure`, `self.check`, `worker`.

#### `ClassifierTests.test_browser`

**Quellcode:** [test_error_classifier.py:124–125](src/tests/test_error_classifier.py#L124-L125).

```python
def test_browser(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`.

#### `ClassifierTests.test_unknown`

**Quellcode:** [test_error_classifier.py:127–129](src/tests/test_error_classifier.py#L127-L129).

```python
def test_unknown(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `failure`, `self.check`.

#### `ClassifierTests.test_contradictory_success`

**Quellcode:** [test_error_classifier.py:131–132](src/tests/test_error_classifier.py#L131-L132).

```python
def test_contradictory_success(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `self.check`.

#### `ClassifierTests.test_attach_preserves_existing_fields`

**Quellcode:** [test_error_classifier.py:134–139](src/tests/test_error_classifier.py#L134-L139).

```python
def test_attach_preserves_existing_fields(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertIs(attach_error_classification(report), report)`
- `self.assertEqual(report.pop('error_classification')['primary']['category'], 'SERVER_ERROR')`
- `self.assertEqual(report, original)`

**Relevante Aufrufe:** `attach_error_classification`, `copy.deepcopy`, `failure`, `report.pop`.

#### `add_history_tests`

**Quellcode:** [test_error_classifier.py:142–148](src/tests/test_error_classifier.py#L142-L148).

```python
def add_history_tests(directory):
```

**Aufgabe:** Registriert zusätzliche Regressionstests für historische Execution-Berichte mit vorgegebenen Kategorien.

**Parameter:** `directory`: Verzeichnis der Eingaben/Ausgaben. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `setattr`.

#### `add_history_tests.test`

**Quellcode:** [test_error_classifier.py:145–147](src/tests/test_error_classifier.py#L145-L147).

```python
def test(self, path=path, expected=expected):
```

**Aufgabe:** Dynamisch registrierter historischer Regressionstest; prüft vorhandene Reportdatei und erwartete Klassifikation.

**Parameter:** `path`: Datei-/Verzeichnispfad gemäß Funktionszweck; `expected`: erwarteter Wert bzw. erwartete Felder/Anzahl je Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertTrue(path.is_file(), f'Missing original execution report: {path}')`

**Relevante Aufrufe:** `json.loads`, `path.is_file`, `path.read_text`, `self.check`.

---

## tests-test-full-crawl

**Modul:** [`src/tests/test_full_crawl.py`](src/tests/test_full_crawl.py)  
**Features/Storys:** C-09, H-01, F-05  
**Aufgabe und Abgrenzung:** Vollcrawl und Checkpoints mit realem Chromium, synthetischem HTML und Downloads; testlokale Policy, keine externen Anfragen.

**Direkte Abhängigkeiten:** `import json`; `import tempfile`; `import unittest`; `from TestRunner import TestRunner`; `from dataclasses import replace`; `from pathlib import Path`; `from unittest.mock import patch`; `from playwright.async_api import Browser, Page`; `from AsyncStrategyExecutor import AsyncStrategyExecutor`; `from ExecutionPolicy import ExecutionPolicy, POLICIES`; `from FullCrawl import FullResultsExecutor, full_crawl_plan`; `from CrawlCheckpoint import CrawlCheckpoint`; `from StrategyStore import StrategyStore, content_digest`; `from test_pagination_validation import strategy, fixture`; `from test_recovery_manager import START, PARAMETERS, EXPECTED, EXECUTABLE`.

**Definitionen:** 2 Klassen, 18 Funktionen/Methoden (inkl. lokaler Definitionen).

### Klasse `FullTests`

**Quellcode:** [test_full_crawl.py:20–190](src/tests/test_full_crawl.py#L20-L190).

**Aufgabe:** TestCase für Vollcrawl und Checkpoints mit realem Chromium, synthetischem HTML und Downloads; testlokale Policy, keine externen Anfragen.

**Basisklassen:** `unittest.IsolatedAsyncioTestCase`.

#### `FullTests.asyncSetUp`

**Quellcode:** [test_full_crawl.py:21–53](src/tests/test_full_crawl.py#L21-L53).

```python
async def asyncSetUp(self):
```

**Aufgabe:** Bereitet isolierte asynchrone Test-Fixture vor; registriert Cleanup und gegebenenfalls Browser-/Netzwerk-Mocks.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.root`, `self.policy`, `self.behavior`, `self.capped`, `self.gotos`, `self.strategy`, `self.fixture_clicks`, `self.fixture_click_times`.

**Relevante Aufrufe:** `ExecutionPolicy`, `patch`, `patch.object`, `patcher.start`, `strategy`.

#### `FullTests.asyncSetUp.close`

**Quellcode:** [test_full_crawl.py:33–41](src/tests/test_full_crawl.py#L33-L41).

```python
async def close(browser, *args, **kwargs):
```

**Aufgabe:** Erfasst vor Browser-Cleanup die synthetischen Klick-/Zeitdaten und schließt Browser.

**Parameter:** `args`: weitergereichte Positionsparameter; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `original_close`, `page.evaluate`, `page.is_closed`, `self.fixture_click_times.extend`, `self.fixture_clicks.extend`.

#### `FullTests.asyncSetUp.goto`

**Quellcode:** [test_full_crawl.py:43–48](src/tests/test_full_crawl.py#L43-L48).

```python
async def goto(page, url, **kwargs):
```

**Aufgabe:** Ersetzt echte Navigation durch lokale synthetische HTML-Seite; Varianten und Zähler entsprechen der umgebenden Fixture.

**Parameter:** `page`: Browser-Page oder Seitennummer gemäß Funktionszweck; `url`: zu prüfende URL; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.gotos`.

**Relevante Aufrufe:** `fixture`, `html.replace`, `page.set_content`.

#### `FullTests.execute`

**Quellcode:** [test_full_crawl.py:55–65](src/tests/test_full_crawl.py#L55-L65).

```python
async def execute(self, downloads=False, enabled=True, download_timeout_ms=15000):
```

**Aufgabe:** Führt den im Modul vorgesehenen Testablauf mit den übergebenen Fixture-Optionen aus und liefert Ergebnis bzw. Runner-Ausgabe.

**Parameter:** `downloads`: Dokumentdownload aktivieren; `download_timeout_ms`: Wartebudget auf Downloadereignis in Millisekunden. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `await ex.run_full(START, 'fixture', plan, downloads=downloads, headless=True, executable_path=EXECUTABLE, timing_path=self.root / 'timing.csv')`.

**Relevante Aufrufe:** `FullResultsExecutor`, `content_digest`, `ex.run_full`, `patch.dict`, `replace`.

#### `FullTests.failure_summary`

**Quellcode:** [test_full_crawl.py:67–72](src/tests/test_full_crawl.py#L67-L72).

```python
def failure_summary(self, result):
```

**Aufgabe:** Serialisiert begrenzte Diagnose eines fehlgeschlagenen Vollcrawl-Tests inklusive Fixture-Klickdaten.

**Parameter:** `result`: Ergebnis-/Statusobjekt. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `json.dumps(dict(error=result.get('error'), metrics=result.get('metrics'), page_results=result.get('page_results'), worker_failures=failures, fixture_clicks=self.fixture_clicks, fixture_clic…`.

#### `FullTests.test_missing_download_event_stops_without_retry`

**Quellcode:** [test_full_crawl.py:74–89](src/tests/test_full_crawl.py#L74-L89).

```python
async def test_missing_download_event_stops_without_retry(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.behavior`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed', self.failure_summary(result))`
- `self.failure_summary(result)`
- `self.assertIn('Download event not received', result['error']['message'])`
- `self.assertEqual(result['metrics']['pages'], 1)`
- `self.assertEqual(result['metrics']['download_attempts'], 1)`
- `self.assertEqual(result['metrics']['documents_downloaded'], 0)`
- `self.assertEqual(self.fixture_clicks, [[1, 'CD']])`
- `self.assertFalse(result['displayed_results_traversed'])`
- `self.assertFalse(result['completeness_verified'])`
- `self.assertEqual(cp['job']['status'], 'failed')`
- `self.assertEqual(cp['document_counts']['failed'], 1)`
- `self.assertEqual(cp['document_counts']['not_attempted'], 5)`
- `self.assertEqual(cp['pages_processed'], 0)`

**Relevante Aufrufe:** `CrawlCheckpoint.inspect`, `self.execute`, `self.failure_summary`.

#### `FullTests.test_checkpoint_write_failure_stops_before_download`

**Quellcode:** [test_full_crawl.py:91–100](src/tests/test_full_crawl.py#L91-L100).

```python
async def test_checkpoint_write_failure_stops_before_download(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed', self.failure_summary(result))`
- `self.failure_summary(result)`
- `self.assertEqual(result['metrics']['download_attempts'], 0)`
- `self.assertEqual(self.fixture_clicks, [])`
- `self.assertEqual(cp['job']['status'], 'failed')`
- `self.assertEqual(cp['document_counts']['not_attempted'], 6)`
- `self.assertEqual(cp['pages_processed'], 0)`

**Relevante Aufrufe:** `CrawlCheckpoint.inspect`, `OSError`, `patch.object`, `self.execute`, `self.failure_summary`.

#### `FullTests.test_three_pages_and_documents`

**Quellcode:** [test_full_crawl.py:102–129](src/tests/test_full_crawl.py#L102-L129).

```python
async def test_three_pages_and_documents(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'completed', self.failure_summary(result))`
- `self.failure_summary(result)`
- `self.assertEqual(result['stop_reason'], 'end_of_results')`
- `self.assertTrue(result['displayed_results_traversed'])`
- `self.assertFalse(result['completeness_verified'])`
- `self.assertEqual([p['row_count'] for p in result['page_results']], [3, 3, 1])`
- `self.assertEqual(result['metrics']['documents_downloaded'], 14)`
- `self.assertEqual(result['metrics']['download_attempts'], 14)`
- `self.assertEqual(self.fixture_clicks, [[n, kind] for n in range(1, 8) for kind in ('CD', 'SI')])`
- `self.assertEqual(len(self.fixture_click_times), 14)`
- `self.assertGreaterEqual(min(gaps), 200, gaps)`
- `self.assertEqual(doc['filename'], f"{n}-{kind}.{doc['file_type']}")`
- `self.assertEqual(Path(doc['file_path']).read_bytes(), expected.encode())`
- `self.assertEqual(result['metrics']['llm_calls'], 0)`
- `self.assertEqual(len(list((self.root / 'docs').rglob('*.pdf'))), 7)`
- `self.assertEqual(len(list((self.root / 'docs').rglob('*.xml'))), 7)`
- `self.assertEqual(cp['job']['status'], 'completed')`
- `self.assertEqual(cp['pages_processed'], 3)`
- `self.assertEqual(cp['companies_documents_done'], 7)`
- `self.assertEqual(cp['document_counts']['downloaded'], 14)`

**Relevante Aufrufe:** `(self.root / 'docs').rglob`, `CrawlCheckpoint.inspect`, `Path(doc['file_path']).read_bytes`, `expected.encode`, `min`, `self.execute`, `self.failure_summary`, `zip`.

#### `FullTests.test_provider_limit_reported`

**Quellcode:** [test_full_crawl.py:131–137](src/tests/test_full_crawl.py#L131-L137).

```python
async def test_provider_limit_reported(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.capped`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertTrue(result['displayed_results_traversed'], result.get('error'))`
- `self.assertTrue(result['result_limit_detected'])`
- `self.assertEqual(result['coverage_status'], 'provider_result_limit')`
- `self.assertFalse(result['completeness_verified'])`

**Relevante Aufrufe:** `self.execute`.

#### `FullTests.test_page_safety_limit`

**Quellcode:** [test_full_crawl.py:139–144](src/tests/test_full_crawl.py#L139-L144).

```python
async def test_page_safety_limit(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.policy`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['stop_reason'], 'safety_page_limit', result.get('error'))`
- `self.assertEqual(result['metrics']['companies_extracted'], 6)`
- `self.assertFalse(result['displayed_results_traversed'])`

**Relevante Aufrufe:** `replace`, `self.execute`.

#### `FullTests.test_company_budget_never_splits_page`

**Quellcode:** [test_full_crawl.py:146–150](src/tests/test_full_crawl.py#L146-L150).

```python
async def test_company_budget_never_splits_page(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.policy`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['stop_reason'], 'safety_company_limit', result.get('error'))`
- `self.assertEqual(result['metrics']['companies_extracted'], 3)`

**Relevante Aufrufe:** `replace`, `self.execute`.

#### `FullTests.test_document_budget_never_splits_page`

**Quellcode:** [test_full_crawl.py:152–157](src/tests/test_full_crawl.py#L152-L157).

```python
async def test_document_budget_never_splits_page(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.policy`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['stop_reason'], 'safety_document_limit', result.get('error'))`
- `self.assertEqual(result['metrics']['documents_downloaded'], 6)`
- `self.assertFalse(result['displayed_results_traversed'])`

**Relevante Aufrufe:** `replace`, `self.execute`.

#### `FullTests.test_end_on_exact_budget`

**Quellcode:** [test_full_crawl.py:159–162](src/tests/test_full_crawl.py#L159-L162).

```python
async def test_end_on_exact_budget(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.policy`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertTrue(result['displayed_results_traversed'], result.get('error'))`

**Relevante Aufrufe:** `replace`, `self.execute`.

#### `FullTests.test_duplicate_stops`

**Quellcode:** [test_full_crawl.py:164–169](src/tests/test_full_crawl.py#L164-L169).

```python
async def test_duplicate_stops(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.behavior`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed')`
- `self.assertEqual(result['metrics']['companies_extracted'], 3)`
- `self.assertFalse(result['displayed_results_traversed'])`

**Relevante Aufrufe:** `self.execute`.

#### `FullTests.test_missing_control_stops_before_next_page_download`

**Quellcode:** [test_full_crawl.py:171–176](src/tests/test_full_crawl.py#L171-L176).

```python
async def test_missing_control_stops_before_next_page_download(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.behavior`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed')`
- `self.assertEqual(result['metrics']['companies_extracted'], 3)`
- `self.assertEqual(result['metrics']['documents_downloaded'], 6)`

**Relevante Aufrufe:** `self.execute`.

#### `FullTests.test_release_lock`

**Quellcode:** [test_full_crawl.py:178–182](src/tests/test_full_crawl.py#L178-L182).

```python
async def test_release_lock(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ValueError, 'disabled by provider policy')`
- `self.assertEqual(self.gotos, 0)`
- `self.assertFalse((self.root / 'docs' / 'checkpoint.sqlite3').exists())`

**Relevante Aufrufe:** `(self.root / 'docs' / 'checkpoint.sqlite3').exists`, `self.execute`.

#### `FullTests.test_bounded_limits_unchanged`

**Quellcode:** [test_full_crawl.py:184–190](src/tests/test_full_crawl.py#L184-L190).

```python
async def test_bounded_limits_unchanged(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ValueError, 'run limits')`
- `self.assertEqual(self.gotos, 0)`

**Relevante Aufrufe:** `AsyncStrategyExecutor`, `executor.run`.

### Klasse `PlanTests`

**Quellcode:** [test_full_crawl.py:193–215](src/tests/test_full_crawl.py#L193-L215).

**Aufgabe:** TestCase für Vollcrawl und Checkpoints mit realem Chromium, synthetischem HTML und Downloads; testlokale Policy, keine externen Anfragen.

**Basisklassen:** `unittest.TestCase`.

#### `PlanTests.test_current_technical_report_cannot_release`

**Quellcode:** [test_full_crawl.py:194–215](src/tests/test_full_crawl.py#L194-L215).

```python
def test_current_technical_report_cannot_release(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertFalse(plan['ready'])`
- `self.assertIn('certified_active_strategy_required', plan['blockers'])`
- `self.assertIn('explicit_schema_v3_end_rule_required', plan['blockers'])`
- `self.assertIn('verified_terminal_state_required', plan['blockers'])`
- `self.assertIn('later_page_document_sample_required', plan['blockers'])`
- `self.assertNotIn('pagination_report_scope_or_digest_mismatch', plan['blockers'])`
- `self.assertIn('pagination_report_scope_or_digest_mismatch', full_crawl_plan(store, report, PARAMETERS, EXPECTED, START)['blockers'])`

**Relevante Aufrufe:** `StrategyStore`, `content_digest`, `full_crawl_plan`, `store.save`, `strategy`.

---

## tests-test-legacy-paths

**Modul:** [`src/tests/test_legacy_paths.py`](src/tests/test_legacy_paths.py)  
**Features/Storys:** H-02, B-01  
**Aufgabe und Abgrenzung:** Zentrale Pfade und Overrides für Legacy-Downloader und OpenAIClient, SDK gemockt.

**Direkte Abhängigkeiten:** `import csv`; `import importlib.util`; `import inspect`; `import sys`; `import tempfile`; `import unittest`; `from pathlib import Path`; `from types import SimpleNamespace`; `from unittest.mock import Mock, patch`; `from TestRunner import TestRunner`; `import ProjectPaths as P`; `from DocumentDownloader import DocumentDownloader`.

**Definitionen:** 1 Klassen, 3 Funktionen/Methoden (inkl. lokaler Definitionen).

### Klasse `LegacyPathTests`

**Quellcode:** [test_legacy_paths.py:17–59](src/tests/test_legacy_paths.py#L17-L59).

**Aufgabe:** TestCase für Zentrale Pfade und Overrides für Legacy-Downloader und OpenAIClient, SDK gemockt.

**Basisklassen:** `unittest.TestCase`.

#### `LegacyPathTests.setUp`

**Quellcode:** [test_legacy_paths.py:18–21](src/tests/test_legacy_paths.py#L18-L21).

```python
def setUp(self):
```

**Aufgabe:** Bereitet isolierte Test-Fixture vor; temporäre Ressourcen und Cleanup entsprechend der konkreten Einrichtung unten.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.root`.

#### `LegacyPathTests.test_downloader_defaults_and_overrides`

**Quellcode:** [test_legacy_paths.py:23–37](src/tests/test_legacy_paths.py#L23-L37).

```python
def test_downloader_defaults_and_overrides(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(params[name].default, path)`
- `self.assertTrue(queue.is_file())`
- `self.assertEqual(row['crawl_id'], 'test')`
- `self.assertEqual(downloader._read(log)[0]['status'], 'failed')`

**Relevante Aufrufe:** `DocumentDownloader`, `downloader._log`, `downloader._read`, `downloader.enqueue`, `inspect.signature`, `queue.is_file`.

#### `LegacyPathTests.test_client_defaults_and_cost_logging`

**Quellcode:** [test_legacy_paths.py:39–59](src/tests/test_legacy_paths.py#L39-L59).

```python
def test_client_defaults_and_cost_logging(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(inspect.signature(client_class.__init__).parameters['log_path'].default, P.USAGE_FILE)`
- `self.assertEqual(row['crawl_id'], 'test')`
- `self.assertEqual(row['token_cost_usd'], '0.00010500')`
- `self.assertEqual(row['web_search_cost_usd'], '0.01000000')`
- `self.assertEqual(row['cost_usd'], '0.01010500')`

**Relevante Aufrufe:** `Mock`, `SimpleNamespace`, `client._log_usage`, `client_class`, `csv.DictReader`, `importlib.util.module_from_spec`, `importlib.util.spec_from_file_location`, `inspect.signature`, `next`, `patch.dict`, `path.open`, `spec.loader.exec_module`.

---

## tests-test-pagination

**Modul:** [`src/tests/test_pagination.py`](src/tests/test_pagination.py)  
**Features/Storys:** C-09  
**Aufgabe und Abgrenzung:** Schema-/Store-Kompatibilität und synchrone/asynchrone Paginierung mit synthetischem HTML in Chromium.

**Direkte Abhängigkeiten:** `import copy`; `import json`; `import shutil`; `import tempfile`; `import unittest`; `from TestRunner import TestRunner`; `from pathlib import Path`; `from unittest.mock import patch`; `from jsonschema import Draft202012Validator, ValidationError`; `from playwright.sync_api import sync_playwright`; `from playwright.async_api import Page`; `from StrategySchema import STRATEGY_SCHEMA, DISCOVERY_SCHEMA`; `from StrategyExecutor import StrategyExecutor, ExecutionError`; `from AsyncStrategyExecutor import AsyncStrategyExecutor`; `from StrategyStore import StrategyStore, content_digest`.

**Definitionen:** 3 Klassen, 26 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `STRATEGY`.

#### `css`

**Quellcode:** [test_pagination.py:20–21](src/tests/test_pagination.py#L20-L21).

```python
def css(selector):
```

**Aufgabe:** Baut CSS-Locator-Dictionary im Strategievertrag.

**Parameter:** `selector`: CSS-Selektor. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `dict(kind='css', role=None, name=None, name_source='none', selector=selector)`.

#### `strategy`

**Quellcode:** [test_pagination.py:32–41](src/tests/test_pagination.py#L32-L41).

```python
def strategy(mode='visible_marker', version=3):
```

**Aufgabe:** Erzeugt bzw. kopiert eine für dieses Testmodul angepasste Strategie; Varianten sind über die Signatur wählbar.

**Parameter:** `mode`: gewählte Variante/Modus; `version`: Strategieversionsnummer. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `result`.

**Relevante Aufrufe:** `copy.deepcopy`, `result['pagination'].pop`.

#### `fixture`

**Quellcode:** [test_pagination.py:44–64](src/tests/test_pagination.py#L44-L64).

```python
def fixture(behavior='marker'):
```

**Aufgabe:** Erzeugt das synthetische HTML bzw. die Testdaten für das im Modul beschriebene Szenario; Varianten simulieren Fehler oder Zustandsänderungen.

**Rückgabe (Ausdrücke im Code):** `'<!doctype html><html><body><div id="records"></div><button id="next" onclick="advance()">Next</button>\n    <p id="end" hidden>Last page reached</p><script>\n    (() => { const behavior = …`.

**Relevante Aufrufe:** `` '<!doctype html><html><body><div id="records"></div><button id="next" onclick="advance()">Next</button>\n    <p id="end" hidden>Last page reached</p><script>\n    (() => { const behavior = BEHAVIOR; let p=0; let ids=[[1,2],[3,4],[5]];\n    if (behavior===\'cycle\') ids=[[1,2],[3,4],[1,2]];\n    if (behavior===\'overlap\') ids=[[1,2],[3,4],[2,5]];\n    if (behavior===\'duplicate\') ids=[[1,2],[3,3],[5]];\n    if (behavior===\'unchanged\') ids=[[1,2],[1,2],[5]];\n    function render() {\n      document.querySelector(\'#records\').innerHTML=ids[p].map(n=>`<div class="record"><span class="id">${n}</span></div>`).join(\'\');\n      if(p===2){\n        if(behavior===\'disabled\') document.querySelector(\'#next\').disabled=true;\n        else if(behavior===\'aria\') document.querySelector(\'#next\').setAttribute(\'aria-disabled\',\'true\');\n        else if(behavior===\'hidden\') document.querySelector(\'#next\').hidden=true;\n        else if(behavior!==\'conflict\') document.querySelector(\'#next\').remove();\n        if([\'marker\',\'conflict\',\'ambiguous_marker\'].includes(behavior)) document.querySelector(\'#end\').hidden=false;\n        if(behavior===\'ambiguous_marker\') document.body.append(document.querySelector(\'#end\').cloneNode(true));\n      }\n    }\n    window.advance=()=>{ if(p<2){p++;setTimeout(render,80);} };\n    render(); })();</script></body></html>'.replace ``.

### Klasse `SchemaTests`

**Quellcode:** [test_pagination.py:67–101](src/tests/test_pagination.py#L67-L101).

**Aufgabe:** TestCase für Schema-/Store-Kompatibilität und synchrone/asynchrone Paginierung mit synthetischem HTML in Chromium.

**Basisklassen:** `unittest.TestCase`.

#### `SchemaTests.test_contracts`

**Quellcode:** [test_pagination.py:68–75](src/tests/test_pagination.py#L68-L75).

```python
def test_contracts(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValidationError)`

**Relevante Aufrufe:** `Draft202012Validator`, `Draft202012Validator(DISCOVERY_SCHEMA).validate`, `Draft202012Validator(STRATEGY_SCHEMA).validate`, `Draft202012Validator.check_schema`, `strategy`.

#### `SchemaTests.test_v3_requires_end_field`

**Quellcode:** [test_pagination.py:77–81](src/tests/test_pagination.py#L77-L81).

```python
def test_v3_requires_end_field(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValidationError)`

**Relevante Aufrufe:** `Draft202012Validator`, `Draft202012Validator(STRATEGY_SCHEMA).validate`, `invalid['pagination'].pop`, `strategy`.

#### `SchemaTests.test_wrong_end_mode_or_locator`

**Quellcode:** [test_pagination.py:83–90](src/tests/test_pagination.py#L83-L90).

```python
def test_wrong_end_mode_or_locator(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValidationError)`

**Relevante Aufrufe:** `Draft202012Validator`, `Draft202012Validator(STRATEGY_SCHEMA).validate`, `css`, `strategy`.

#### `SchemaTests.test_store_unchanged_legacy_hash`

**Quellcode:** [test_pagination.py:92–101](src/tests/test_pagination.py#L92-L101).

```python
def test_store_unchanged_legacy_hash(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(store.save(old, 'https://example.test'), 1)`
- `self.assertEqual(store.save(strategy(), 'https://example.test'), 2)`
- `self.assertEqual(content_digest(store.load(1)['strategy']), digest)`
- `self.assertEqual(store.load(2)['metadata']['schema_version'], 3)`
- `self.assertIsNone(store.load_active())`

**Relevante Aufrufe:** `StrategyStore`, `content_digest`, `store.load`, `store.load_active`, `store.save`, `strategy`.

### Klasse `SyncTests`

**Quellcode:** [test_pagination.py:104–169](src/tests/test_pagination.py#L104-L169).

**Aufgabe:** Synchroner TestCase für die im Modul beschriebenen Varianten.

**Basisklassen:** `unittest.TestCase`.

#### `SyncTests.setUpClass`

**Quellcode:** [test_pagination.py:106–108](src/tests/test_pagination.py#L106-L108).

```python
@classmethod
def setUpClass(cls):
```

**Aufgabe:** Initialisiert klassenweit benötigte Testressourcen bzw. absichtlich fehlerhafte Fixture im Runner-Selbsttest.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `cls.pw`, `cls.browser`.

**Relevante Aufrufe:** `cls.pw.chromium.launch`, `shutil.which`, `sync_playwright`, `sync_playwright().start`.

#### `SyncTests.tearDownClass`

**Quellcode:** [test_pagination.py:111–113](src/tests/test_pagination.py#L111-L113).

```python
@classmethod
def tearDownClass(cls):
```

**Aufgabe:** Schließt klassenweite Browser-/Playwright-Ressourcen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `cls.browser.close`, `cls.pw.stop`.

#### `SyncTests.setUp`

**Quellcode:** [test_pagination.py:115–121](src/tests/test_pagination.py#L115-L121).

```python
def setUp(self):
```

**Aufgabe:** Bereitet isolierte Test-Fixture vor; temporäre Ressourcen und Cleanup entsprechend der konkreten Einrichtung unten.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.context`, `self.page`.

**Relevante Aufrufe:** `patch`, `patcher.start`, `self.browser.new_context`, `self.context.new_page`.

#### `SyncTests.execute`

**Quellcode:** [test_pagination.py:123–127](src/tests/test_pagination.py#L123-L127).

```python
def execute(self, behavior='marker', mode='visible_marker', version=3, max_pages=5, max_companies=10):
```

**Aufgabe:** Führt den im Modul vorgesehenen Testablauf mit den übergebenen Fixture-Optionen aus und liefert Ergebnis bzw. Runner-Ausgabe.

**Parameter:** `mode`: gewählte Variante/Modus; `version`: Strategieversionsnummer; `max_pages`: Obergrenze für Ergebnisseiten; `max_companies`: Obergrenze für Datensätze. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `self.executor._collect(max_companies, max_pages, False)`.

**Direkt gesetzter Zustand:** `self.executor`.

**Relevante Aufrufe:** `StrategyExecutor`, `fixture`, `self.executor._collect`, `self.page.set_content`, `strategy`.

#### `SyncTests.test_three_pages_marker`

**Quellcode:** [test_pagination.py:129–132](src/tests/test_pagination.py#L129-L132).

```python
def test_three_pages_marker(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.execute(), 'end_of_results')`
- `self.assertEqual([c['id'] for c in self.executor.companies], ['1', '2', '3', '4', '5'])`
- `self.assertEqual(self.executor.pagination_end_evidence['page'], 3)`

**Relevante Aufrufe:** `self.execute`.

#### `SyncTests.test_disabled_native_and_aria`

**Quellcode:** [test_pagination.py:134–138](src/tests/test_pagination.py#L134-L138).

```python
def test_disabled_native_and_aria(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.execute(behavior, 'next_disabled'), 'end_of_results')`
- `self.assertEqual(self.executor.pagination_end_evidence['mode'], 'next_disabled')`

**Relevante Aufrufe:** `self.execute`.

#### `SyncTests.test_unknown_legacy_disabled`

**Quellcode:** [test_pagination.py:140–142](src/tests/test_pagination.py#L140-L142).

```python
def test_unknown_legacy_disabled(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.execute('disabled', version=2), 'end_of_results_unverified')`
- `self.assertIsNone(self.executor.pagination_end_evidence)`

**Relevante Aufrufe:** `self.execute`.

#### `SyncTests.test_unknown_v3_disabled`

**Quellcode:** [test_pagination.py:144–146](src/tests/test_pagination.py#L144-L146).

```python
def test_unknown_v3_disabled(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.execute('disabled', None), 'end_of_results_unverified')`
- `self.assertIsNone(self.executor.pagination_end_evidence)`

**Relevante Aufrufe:** `self.execute`.

#### `SyncTests.test_missing_or_hidden_next_not_end`

**Quellcode:** [test_pagination.py:148–151](src/tests/test_pagination.py#L148-L151).

```python
def test_missing_or_hidden_next_not_end(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ExecutionError, 'end of results not verified')`

**Relevante Aufrufe:** `self.execute`.

#### `SyncTests.test_marker_conflict_and_ambiguity`

**Quellcode:** [test_pagination.py:153–156](src/tests/test_pagination.py#L153-L156).

```python
def test_marker_conflict_and_ambiguity(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ExecutionError)`

**Relevante Aufrufe:** `self.execute`.

#### `SyncTests.test_cycle_overlap_duplicate_unchanged`

**Quellcode:** [test_pagination.py:158–163](src/tests/test_pagination.py#L158-L163).

```python
def test_cycle_overlap_duplicate_unchanged(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ExecutionError, 'No verified change')`
- `self.assertIsNone(self.executor.pagination_end_evidence)`
- `self.assertEqual(len(self.executor.seen), len(self.executor.companies))`

**Relevante Aufrufe:** `self.execute`.

#### `SyncTests.test_limits_do_not_certify_end`

**Quellcode:** [test_pagination.py:165–169](src/tests/test_pagination.py#L165-L169).

```python
def test_limits_do_not_certify_end(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.execute(max_pages=3), 'page_limit')`
- `self.assertIsNone(self.executor.pagination_end_evidence)`
- `self.assertEqual(self.execute(max_companies=3), 'company_limit')`

**Relevante Aufrufe:** `self.execute`.

### Klasse `AsyncTests`

**Quellcode:** [test_pagination.py:172–214](src/tests/test_pagination.py#L172-L214).

**Aufgabe:** Asynchroner TestCase für die im Modul beschriebenen Varianten.

**Basisklassen:** `unittest.IsolatedAsyncioTestCase`.

#### `AsyncTests.execute`

**Quellcode:** [test_pagination.py:173–182](src/tests/test_pagination.py#L173-L182).

```python
async def execute(self, behavior='marker', mode='visible_marker', version=3, max_pages=5, max_companies=10):
```

**Aufgabe:** Führt den im Modul vorgesehenen Testablauf mit den übergebenen Fixture-Optionen aus und liefert Ergebnis bzw. Runner-Ausgabe.

**Parameter:** `mode`: gewählte Variante/Modus; `version`: Strategieversionsnummer; `max_pages`: Obergrenze für Ergebnisseiten; `max_companies`: Obergrenze für Datensätze. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `await executor.run('https://example.test', 'test', max_companies=max_companies, max_pages=max_pages, headless=True, executable_path=shutil.which('chromium'), timing_path=Path(root) / 'timin…`.

**Relevante Aufrufe:** `AsyncStrategyExecutor`, `executor.run`, `patch`, `patch.object`, `shutil.which`, `strategy`.

#### `AsyncTests.execute.goto`

**Quellcode:** [test_pagination.py:175–176](src/tests/test_pagination.py#L175-L176).

```python
async def goto(page, url, **kwargs):
```

**Aufgabe:** Ersetzt echte Navigation durch lokale synthetische HTML-Seite; Varianten und Zähler entsprechen der umgebenden Fixture.

**Parameter:** `page`: Browser-Page oder Seitennummer gemäß Funktionszweck; `url`: zu prüfende URL; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `fixture`, `page.set_content`.

#### `AsyncTests.test_three_pages_marker_report`

**Quellcode:** [test_pagination.py:184–191](src/tests/test_pagination.py#L184-L191).

```python
async def test_three_pages_marker_report(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'completed', result)`
- `self.assertEqual(result['stop_reason'], 'end_of_results')`
- `self.assertTrue(result['pagination_end_verified'])`
- `self.assertEqual(result['metrics']['pages'], 3)`
- `self.assertEqual(result['metrics']['llm_calls'], 0)`
- `self.assertEqual([c['id'] for c in result['companies']], ['1', '2', '3', '4', '5'])`

**Relevante Aufrufe:** `self.execute`.

#### `AsyncTests.test_disabled_report`

**Quellcode:** [test_pagination.py:193–195](src/tests/test_pagination.py#L193-L195).

```python
async def test_disabled_report(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertTrue(result['pagination_end_verified'], result)`

**Relevante Aufrufe:** `self.execute`.

#### `AsyncTests.test_legacy_and_limit_report`

**Quellcode:** [test_pagination.py:197–203](src/tests/test_pagination.py#L197-L203).

```python
async def test_legacy_and_limit_report(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(legacy['stop_reason'], 'end_of_results_unverified')`
- `self.assertFalse(legacy['pagination_end_verified'])`
- `self.assertEqual(limited['stop_reason'], 'page_limit')`
- `self.assertFalse(limited['pagination_end_verified'])`

**Relevante Aufrufe:** `self.execute`.

#### `AsyncTests.test_missing_next_report`

**Quellcode:** [test_pagination.py:205–208](src/tests/test_pagination.py#L205-L208).

```python
async def test_missing_next_report(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed')`
- `self.assertFalse(result['pagination_end_verified'])`

**Relevante Aufrufe:** `self.execute`.

#### `AsyncTests.test_cycle_report`

**Quellcode:** [test_pagination.py:210–214](src/tests/test_pagination.py#L210-L214).

```python
async def test_cycle_report(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed')`
- `self.assertEqual([c['id'] for c in result['companies']], ['1', '2', '3', '4'])`
- `self.assertFalse(result['pagination_end_verified'])`

**Relevante Aufrufe:** `self.execute`.

---

## tests-test-pagination-links

**Modul:** [`src/tests/test_pagination_links.py`](src/tests/test_pagination_links.py)  
**Features/Storys:** C-09  
**Aufgabe und Abgrenzung:** Offline-Regression für äquivalente vs. mehrdeutige mehrfach sichtbare Next-Links; synchron und asynchron.

**Direkte Abhängigkeiten:** `import copy`; `import shutil`; `import unittest`; `from TestRunner import TestRunner`; `from unittest.mock import patch`; `from playwright.sync_api import sync_playwright`; `from playwright.async_api import async_playwright`; `from StrategyExecutor import StrategyExecutor, ExecutionError`; `from AsyncStrategyExecutor import AsyncStrategyExecutor`; `from test_pagination import STRATEGY, css`.

**Definitionen:** 2 Klassen, 4 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `MODES`.

#### `strategy`

**Quellcode:** [test_pagination_links.py:14–18](src/tests/test_pagination_links.py#L14-L18).

```python
def strategy():
```

**Aufgabe:** Erzeugt bzw. kopiert eine für dieses Testmodul angepasste Strategie; Varianten sind über die Signatur wählbar.

**Rückgabe (Ausdrücke im Code):** `s`.

**Relevante Aufrufe:** `copy.deepcopy`, `css`.

#### `fixture`

**Quellcode:** [test_pagination_links.py:21–41](src/tests/test_pagination_links.py#L21-L41).

```python
def fixture(mode):
```

**Aufgabe:** Erzeugt das synthetische HTML bzw. die Testdaten für das im Modul beschriebene Szenario; Varianten simulieren Fehler oder Zustandsänderungen.

**Parameter:** `mode`: gewählte Variante/Modus. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `f"""<!doctype html><html><body>{first}<div id="records">\n    <div class="record"><span class="id">1</span></div></div>{second}<script>\n    window.clicks=0; function advance(e) {{ e.preven…`.

**Relevante Aufrufe:** `first.replace`, `first.replace('class="next"', 'class="next" hidden').replace`.

### Klasse `SyncTests`

**Quellcode:** [test_pagination_links.py:47–70](src/tests/test_pagination_links.py#L47-L70).

**Aufgabe:** Synchroner TestCase für die im Modul beschriebenen Varianten.

**Basisklassen:** `unittest.TestCase`.

#### `SyncTests.test_cases`

**Quellcode:** [test_pagination_links.py:48–70](src/tests/test_pagination_links.py#L48-L70).

```python
def test_cases(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(ex._collect(10, 3, False), 'end_of_results')`
- `self.assertEqual([c['id'] for c in ex.companies], ['1', '2'])`
- `self.assertEqual(page.evaluate('window.clicks'), 1)`
- `self.assertEqual(ex.pagination_end_evidence['page'], 2)`
- `self.assertRaisesRegex(ExecutionError, 'Next-page control ambiguous')`
- `self.assertEqual(page.evaluate('window.clicks'), 0)`
- `self.assertIsNone(ex.pagination_end_evidence)`

**Relevante Aufrufe:** `StrategyExecutor`, `browser.close`, `browser.new_context`, `context.new_page`, `ex._collect`, `fixture`, `page.evaluate`, `page.set_content`, `patch.object`, `pw.chromium.launch`, `shutil.which`, `strategy`, `sync_playwright`.

### Klasse `AsyncTests`

**Quellcode:** [test_pagination_links.py:73–100](src/tests/test_pagination_links.py#L73-L100).

**Aufgabe:** Asynchroner TestCase für die im Modul beschriebenen Varianten.

**Basisklassen:** `unittest.IsolatedAsyncioTestCase`.

#### `AsyncTests.test_cases`

**Quellcode:** [test_pagination_links.py:74–100](src/tests/test_pagination_links.py#L74-L100).

```python
async def test_cases(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(await ex._collect(10, 3, False), 'end_of_results')`
- `self.assertEqual([c['id'] for c in ex.companies], ['1', '2'])`
- `self.assertEqual(await page.evaluate('window.clicks'), 1)`
- `self.assertEqual(ex.pagination_end_evidence['page'], 2)`
- `self.assertRaisesRegex(ExecutionError, 'Next-page control ambiguous')`
- `self.assertEqual(await page.evaluate('window.clicks'), 0)`
- `self.assertIsNone(ex.pagination_end_evidence)`

**Relevante Aufrufe:** `AsyncStrategyExecutor`, `async_playwright`, `browser.close`, `browser.new_context`, `context.close`, `context.new_page`, `ex._collect`, `fixture`, `page.evaluate`, `page.set_content`, `patch.object`, `pw.chromium.launch`, `shutil.which`, `strategy`.

---

## tests-test-pagination-validation

**Modul:** [`src/tests/test_pagination_validation.py`](src/tests/test_pagination_validation.py)  
**Features/Storys:** F-03  
**Aufgabe und Abgrenzung:** Mehrseitige unabhängige Validierung in synthetischen Browserläufen, technischer und Referenzmodus, Endregel und Dokumente.

**Direkte Abhängigkeiten:** `import copy`; `import json`; `import tempfile`; `import unittest`; `from TestRunner import TestRunner`; `from pathlib import Path`; `from unittest.mock import patch`; `from playwright.async_api import Page`; `from ExecutionPolicy import ExecutionPolicy`; `from PaginationValidator import PaginationValidator, PaginationValidationExecutor`; `from StrategyStore import StrategyStore, content_digest`; `from test_recovery_manager import STRATEGY, START, PARAMETERS, EXPECTED, EXECUTABLE, css_spec`.

**Definitionen:** 1 Klassen, 22 Funktionen/Methoden (inkl. lokaler Definitionen).

#### `strategy`

**Quellcode:** [test_pagination_validation.py:17–23](src/tests/test_pagination_validation.py#L17-L23).

```python
def strategy(legacy=False):
```

**Aufgabe:** Erzeugt bzw. kopiert eine für dieses Testmodul angepasste Strategie; Varianten sind über die Signatur wählbar.

**Rückgabe (Ausdrücke im Code):** `result`.

**Relevante Aufrufe:** `copy.deepcopy`, `css_spec`.

#### `reference`

**Quellcode:** [test_pagination_validation.py:26–32](src/tests/test_pagination_validation.py#L26-L32).

```python
def reference(end=True):
```

**Aufgabe:** Erzeugt unabhängige synthetische Paginierungsreferenz mit Zeilenanzahlen, Stichprobe und optionalem Endnachweis.

**Rückgabe (Ausdrücke im Code):** `dict(reference_version=2, manually_verified=True, source='Independent fixture data', parameters=PARAMETERS, expected_fields=EXPECTED, expect_end=end, pages=[dict(page=i, row_count=len(ids),…`.

#### `fixture`

**Quellcode:** [test_pagination_validation.py:35–62](src/tests/test_pagination_validation.py#L35-L62).

```python
def fixture(behavior='normal'):
```

**Aufgabe:** Erzeugt das synthetische HTML bzw. die Testdaten für das im Modul beschriebene Szenario; Varianten simulieren Fehler oder Zustandsänderungen.

**Rückgabe (Ausdrücke im Code):** `'<!doctype html><html><body><label>Query<input></label><button onclick="start()">Search</button>\n    <table hidden data-testid="old-table"><tbody></tbody></table><button id="next" hidden o…`.

**Relevante Aufrufe:** `` '<!doctype html><html><body><label>Query<input></label><button onclick="start()">Search</button>\n    <table hidden data-testid="old-table"><tbody></tbody></table><button id="next" hidden onclick="advance()">Next</button>\n    <script>\n    const behavior = BEHAVIOR; let p=0, ids=[[1,2,3],[4,5,6],[7]];\n    window.fixtureClicks=[]; window.fixtureClickTimes=[];\n    if(behavior===\'overlap\') ids[1]=[1,5,6];\n    if(behavior===\'changed\') ids[1]=[4,5,66];\n    if(behavior===\'too_many\') ids[1]=Array.from({length:98},(_,i)=>100+i);\n    if(behavior===\'early_end\') ids=ids.slice(0,2);\n    function getFile(n,kind) {\n      window.fixtureClicks.push([n,kind]); window.fixtureClickTimes.push(performance.now());\n      if(behavior===\'no_download\') return;\n      const a=document.createElement(\'a\'),ext=kind===\'CD\'?\'pdf\':\'xml\';\n      const blob=new Blob([kind===\'CD\'?\'%PDF-1.4\\n% fixture \'+n+\'\\n%%EOF\\n\':\'<register>\'+n+\'</register>\'],\n        {type:kind===\'CD\'?\'application/pdf\':\'application/xml\'});\n      const url=URL.createObjectURL(blob);\n      a.href=url; a.download=(behavior===\'wrong_file\'?999:n)+\'-\'+kind+\'.\'+ext;\n      a.hidden=true; document.body.appendChild(a); a.click(); a.remove();\n      setTimeout(()=>URL.revokeObjectURL(url),30000);\n    }\n    function render(){document.querySelector(\'table\').hidden=false;\n      let next=document.querySelector(\'#next\');next.hidden=false;next.disabled=p===ids.length-1&&behavior!==\'no_end\';\n      document.querySelector(\'tbody\').innerHTML=ids[p].map(n=>`<tr data-testid="old-row"><td class="company">Firma ${n}</td>\n      <td class="number">${n}</td><td class="type">HRB</td><td><button onclick="getFile(${n},\'CD\')">CD</button>\n      ${behavior===\'missing_control\'&&p===1?\'\':`<button onclick="getFile(${n},\'SI\')">SI</button>`}</td></tr>`).join(\'\');}\n    function start(){render();} function advance(){if(p<2){p++;setTimeout(render,60);}}\n    </script></body></html>'.replace ``.

### Klasse `Tests`

**Quellcode:** [test_pagination_validation.py:65–227](src/tests/test_pagination_validation.py#L65-L227).

**Aufgabe:** TestCase für Mehrseitige unabhängige Validierung in synthetischen Browserläufen, technischer und Referenzmodus, Endregel und Dokumente.

**Basisklassen:** `unittest.IsolatedAsyncioTestCase`.

#### `Tests.asyncSetUp`

**Quellcode:** [test_pagination_validation.py:66–83](src/tests/test_pagination_validation.py#L66-L83).

```python
async def asyncSetUp(self):
```

**Aufgabe:** Bereitet isolierte asynchrone Test-Fixture vor; registriert Cleanup und gegebenenfalls Browser-/Netzwerk-Mocks.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.root`, `self.store`, `self.gotos`, `self.behavior`, `self.second_behavior`, `self.validator`.

**Relevante Aufrufe:** `ExecutionPolicy`, `PaginationValidator`, `StrategyStore`, `patch`, `patch.object`, `patcher.start`, `self.store.save`, `strategy`.

#### `Tests.asyncSetUp.goto`

**Quellcode:** [test_pagination_validation.py:74–76](src/tests/test_pagination_validation.py#L74-L76).

```python
async def goto(page, url, **kwargs):
```

**Aufgabe:** Ersetzt echte Navigation durch lokale synthetische HTML-Seite; Varianten und Zähler entsprechen der umgebenden Fixture.

**Parameter:** `page`: Browser-Page oder Seitennummer gemäß Funktionszweck; `url`: zu prüfende URL; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.gotos`.

**Relevante Aufrufe:** `fixture`, `page.set_content`.

#### `Tests.validate`

**Quellcode:** [test_pagination_validation.py:85–86](src/tests/test_pagination_validation.py#L85-L86).

```python
async def validate(self, end=True, downloads=True, version=1):
```

**Aufgabe:** Ruft Validator mit synthetischer Referenz und expliziten Testautorisierungen auf.

**Parameter:** `downloads`: Dokumentdownload aktivieren; `version`: Strategieversionsnummer. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `await self.validator.validate(version, reference(end), authorized=True, downloads_authorized=downloads)`.

**Relevante Aufrufe:** `reference`, `self.validator.validate`.

#### `Tests.test_full_three_pages_and_no_activation`

**Quellcode:** [test_pagination_validation.py:88–100](src/tests/test_pagination_validation.py#L88-L100).

```python
async def test_full_three_pages_and_no_activation(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'passed', result)`
- `self.assertTrue(result['pagination_verified'] and result['pagination_end_verified'])`
- `self.assertTrue(result['later_page_documents_verified'])`
- `self.assertFalse(result['all_results_authorized'])`
- `self.assertEqual(self.gotos, 2)`
- `self.assertEqual([c['execution']['metrics']['download_attempts'] for c in result['checks']], [0, 2])`
- `self.assertEqual([r['register_number'] for r in records if any((d['download_status'] == 'downloaded' for d in r['documents']))], ['7'])`
- `self.assertEqual(self.store.load(1)['metadata']['status'], 'candidate')`
- `self.assertIsNone(self.store.load_active())`
- `self.assertEqual(result['strategy_sha256'], content_digest(strategy()))`

**Relevante Aufrufe:** `any`, `content_digest`, `self.store.load`, `self.store.load_active`, `self.validate`, `strategy`.

#### `Tests.test_bounded_legacy_partial`

**Quellcode:** [test_pagination_validation.py:102–109](src/tests/test_pagination_validation.py#L102-L109).

```python
async def test_bounded_legacy_partial(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'partial', result)`
- `self.assertTrue(result['pagination_verified'] and result['later_page_documents_verified'])`
- `self.assertFalse(result['pagination_end_verified'])`
- `self.assertEqual(result['checks'][1]['execution']['metrics']['pages'], 2)`
- `self.assertEqual(result['missing_checks'], ['terminal_state_not_tested'])`

**Relevante Aufrufe:** `self.store.save`, `self.validate`, `strategy`.

#### `Tests.test_read_only_partial`

**Quellcode:** [test_pagination_validation.py:111–116](src/tests/test_pagination_validation.py#L111-L116).

```python
async def test_read_only_partial(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'partial', result)`
- `self.assertTrue(result['pagination_end_verified'])`
- `self.assertFalse(result['later_page_documents_verified'])`
- `self.assertEqual(sum((c['execution']['metrics']['download_attempts'] for c in result['checks'])), 0)`

**Relevante Aufrufe:** `self.validate`.

#### `Tests.test_overlap_missing_controls_and_no_end`

**Quellcode:** [test_pagination_validation.py:118–126](src/tests/test_pagination_validation.py#L118-L126).

```python
async def test_overlap_missing_controls_and_no_end(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.behavior`, `self.gotos`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed', result)`
- `self.assertFalse(result['pagination_verified'])`
- `self.assertEqual(self.gotos, 1)`
- `self.assertEqual(result['checks'][0]['execution']['metrics']['download_attempts'], 0)`

**Relevante Aufrufe:** `self.validate`.

#### `Tests.test_unstable_second_session_before_download`

**Quellcode:** [test_pagination_validation.py:128–133](src/tests/test_pagination_validation.py#L128-L133).

```python
async def test_unstable_second_session_before_download(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.second_behavior`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed', result)`
- `self.assertIn('differs between independent', result['reason'])`
- `self.assertEqual(result['checks'][1]['execution']['metrics']['download_attempts'], 0)`

**Relevante Aufrufe:** `self.validate`.

#### `Tests.test_bad_later_filename`

**Quellcode:** [test_pagination_validation.py:135–140](src/tests/test_pagination_validation.py#L135-L140).

```python
async def test_bad_later_filename(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.behavior`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed', result)`
- `self.assertIn('identity mismatch', result['reason'])`
- `self.assertFalse(result['later_page_documents_verified'])`

**Relevante Aufrufe:** `self.validate`.

#### `Tests.test_reference_guards`

**Quellcode:** [test_pagination_validation.py:142–151](src/tests/test_pagination_validation.py#L142-L151).

```python
async def test_reference_guards(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValueError)`
- `self.assertEqual(self.gotos, 0)`

**Relevante Aufrufe:** `reference`, `self.store.save`, `self.validate`, `self.validator.validate`, `strategy`.

#### `Tests.test_wrong_reference_row_count`

**Quellcode:** [test_pagination_validation.py:153–159](src/tests/test_pagination_validation.py#L153-L159).

```python
async def test_wrong_reference_row_count(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed', result)`
- `self.assertIn('row count differs', result['reason'])`
- `self.assertEqual(self.gotos, 1)`

**Relevante Aufrufe:** `reference`, `self.validator.validate`.

#### `Tests.technical`

**Quellcode:** [test_pagination_validation.py:162–163](src/tests/test_pagination_validation.py#L162-L163).

```python
async def technical(self, pages=2, version=1, expected=EXPECTED):
```

**Aufgabe:** Ruft technischen Paginierungsvalidator mit Testparametern und expliziter Autorisierung auf.

**Parameter:** `pages`: Anzahl zu prüfender Seiten; `version`: Strategieversionsnummer; `expected`: erwarteter Wert bzw. erwartete Felder/Anzahl je Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `await self.validator.validate_technical(version, PARAMETERS, expected, pages=pages, authorized=True)`.

**Relevante Aufrufe:** `self.validator.validate_technical`.

#### `Tests.test_technical_two_pages_without_reference`

**Quellcode:** [test_pagination_validation.py:165–180](src/tests/test_pagination_validation.py#L165-L180).

```python
async def test_technical_two_pages_without_reference(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'partial', result)`
- `self.assertTrue(result['technical_validation_passed'] and result['pagination_verified'])`
- `self.assertFalse(result['independent_reference_verified'] or result['all_results_authorized'])`
- `self.assertFalse(result['pagination_end_verified'] or result['later_page_documents_verified'])`
- `self.assertIsNone(result['reference'])`
- `self.assertIsNone(result['reference_sha256'])`
- `self.assertEqual(result['validation_mode'], 'technical')`
- `self.assertEqual(self.gotos, 2)`
- `self.assertEqual([p['row_count'] for p in check['pages']], [3, 3])`
- `self.assertEqual([p['reference_rows'] for p in check['pages']], [0, 0])`
- `self.assertEqual(check['execution']['metrics']['download_attempts'], 0)`
- `self.assertIsNone(self.store.load_active())`
- `self.assertEqual(self.store.load(1)['metadata']['status'], 'candidate')`

**Relevante Aufrufe:** `self.store.load`, `self.store.load_active`, `self.technical`.

#### `Tests.test_technical_three_pages_with_end`

**Quellcode:** [test_pagination_validation.py:182–187](src/tests/test_pagination_validation.py#L182-L187).

```python
async def test_technical_three_pages_with_end(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'partial', result)`
- `self.assertTrue(result['technical_validation_passed'] and result['pagination_end_verified'])`
- `self.assertFalse(result['all_results_authorized'] or result['independent_reference_verified'])`
- `self.assertEqual([p['row_count'] for p in result['checks'][1]['pages']], [3, 3, 1])`

**Relevante Aufrufe:** `self.technical`.

#### `Tests.test_technical_legacy_without_end_rule`

**Quellcode:** [test_pagination_validation.py:189–195](src/tests/test_pagination_validation.py#L189-L195).

```python
async def test_technical_legacy_without_end_rule(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'partial', result)`
- `self.assertTrue(result['technical_validation_passed'])`
- `self.assertFalse(result['pagination_end_verified'])`
- `self.assertEqual(result['checks'][1]['execution']['stop_reason'], 'end_of_results_unverified')`

**Relevante Aufrufe:** `self.store.save`, `self.technical`, `strategy`.

#### `Tests.test_technical_changed_content`

**Quellcode:** [test_pagination_validation.py:197–202](src/tests/test_pagination_validation.py#L197-L202).

```python
async def test_technical_changed_content(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.second_behavior`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed', result)`
- `self.assertFalse(result['technical_validation_passed'])`
- `self.assertIn('differs between independent', result['reason'])`

**Relevante Aufrufe:** `self.technical`.

#### `Tests.test_technical_changed_end_state`

**Quellcode:** [test_pagination_validation.py:204–208](src/tests/test_pagination_validation.py#L204-L208).

```python
async def test_technical_changed_end_state(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.second_behavior`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed', result)`
- `self.assertIn('terminal state differs', result['reason'])`

**Relevante Aufrufe:** `self.technical`.

#### `Tests.test_technical_failures`

**Quellcode:** [test_pagination_validation.py:210–218](src/tests/test_pagination_validation.py#L210-L218).

```python
async def test_technical_failures(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.behavior`, `self.gotos`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed', result)`
- `self.assertFalse(result['technical_validation_passed'])`
- `self.assertEqual(self.gotos, 1)`
- `self.assertEqual(result['checks'][0]['execution']['metrics']['download_attempts'], 0)`

**Relevante Aufrufe:** `self.technical`.

#### `Tests.test_technical_guards_and_expected_filters`

**Quellcode:** [test_pagination_validation.py:220–227](src/tests/test_pagination_validation.py#L220-L227).

```python
async def test_technical_guards_and_expected_filters(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValueError)`
- `self.assertEqual(self.gotos, 0)`
- `self.assertEqual(result['status'], 'failed', result)`
- `self.assertIn('does not match requested filter', result['reason'])`

**Relevante Aufrufe:** `self.technical`, `self.validator.validate_technical`.

---

## tests-test-project-paths

**Modul:** [`src/tests/test_project_paths.py`](src/tests/test_project_paths.py)  
**Features/Storys:** H-02, G-02  
**Aufgabe und Abgrenzung:** Zentrale Pfade, Legacy-Migration, Konfliktkontrollen und explizite Overrides mit temporären Verzeichnissen.

**Direkte Abhängigkeiten:** `import inspect`; `import json`; `import tempfile`; `import unittest`; `from pathlib import Path`; `from unittest.mock import patch`; `from TestRunner import TestRunner`; `import ProjectPaths as P`; `from main_migrate_results import migration_plan, check_plan, apply_plan`; `from BenchmarkAnalyzer import analyze`; `from StrategyExecutor import StrategyExecutor`; `from AsyncStrategyExecutor import AsyncStrategyExecutor`; `from StrategyStore import StrategyStore`; `from StrategyValidator import StrategyValidator`; `from PaginationValidator import PaginationValidator`; `from ResumePlanner import ResumePlanner`; `from BrowserUse import write_timings`; `import main_strategy`.

**Definitionen:** 1 Klassen, 14 Funktionen/Methoden (inkl. lokaler Definitionen).

### Klasse `PathTests`

**Quellcode:** [test_project_paths.py:22–136](src/tests/test_project_paths.py#L22-L136).

**Aufgabe:** TestCase für Zentrale Pfade, Legacy-Migration, Konfliktkontrollen und explizite Overrides mit temporären Verzeichnissen.

**Basisklassen:** `unittest.TestCase`.

#### `PathTests.setUp`

**Quellcode:** [test_project_paths.py:23–26](src/tests/test_project_paths.py#L23-L26).

```python
def setUp(self):
```

**Aufgabe:** Bereitet isolierte Test-Fixture vor; temporäre Ressourcen und Cleanup entsprechend der konkreten Einrichtung unten.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.root`.

#### `PathTests.put`

**Quellcode:** [test_project_paths.py:28–32](src/tests/test_project_paths.py#L28-L32).

```python
def put(self, name, content='original bytes\n'):
```

**Aufgabe:** Schreibt Testdatei unter temporärem Root und gibt Path zurück.

**Parameter:** `name`: Name des Felds/Controls gemäß Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `path`.

**Relevante Aufrufe:** `path.parent.mkdir`, `path.write_text`.

#### `PathTests.test_central_defaults`

**Quellcode:** [test_project_paths.py:34–44](src/tests/test_project_paths.py#L34-L44).

```python
def test_central_defaults(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(P.ROOT_DIR, Path(P.__file__).resolve().parents[1])`
- `self.assertEqual(inspect.signature(func).parameters[name].default, value)`

**Relevante Aufrufe:** `Path(P.__file__).resolve`, `inspect.signature`.

#### `PathTests.test_migration_preserves_contents_and_excludes_state`

**Quellcode:** [test_project_paths.py:46–66](src/tests/test_project_paths.py#L46-L66).

```python
def test_migration_preserves_contents_and_excludes_state(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(len(moves), len(names))`
- `self.assertTrue(all((s.exists() and (not t.exists()) for s, t in moves)))`
- `self.assertFalse(source.exists())`
- `self.assertEqual(target.read_text(), str(source.relative_to(self.root)))`
- `self.assertTrue(all(((self.root / name).exists() for name in retained)))`
- `self.assertEqual(migration_plan(self.root), [])`

**Relevante Aufrufe:** `(self.root / name).exists`, `all`, `apply_plan`, `check_plan`, `migration_plan`, `s.exists`, `self.put`, `source.exists`, `source.relative_to`, `t.exists`, `target.read_text`.

#### `PathTests.test_references_explicit_scope`

**Quellcode:** [test_project_paths.py:68–73](src/tests/test_project_paths.py#L68-L73).

```python
def test_references_explicit_scope(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(migration_plan(self.root), [])`
- `self.assertEqual(moves[0][1], self.root / 'references/unternehmensregister.de/register_information/validation_reference.json')`

**Relevante Aufrufe:** `apply_plan`, `migration_plan`, `self.put`.

#### `PathTests.test_existing_destination_blocks_all`

**Quellcode:** [test_project_paths.py:75–82](src/tests/test_project_paths.py#L75-L82).

```python
def test_existing_destination_blocks_all(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ValueError, 'conflict')`
- `self.assertTrue(old.exists() and other.exists())`
- `self.assertFalse((self.root / 'results/executions/a_execution.json').exists())`

**Relevante Aufrufe:** `(self.root / 'results/executions/a_execution.json').exists`, `apply_plan`, `migration_plan`, `old.exists`, `other.exists`, `self.put`.

#### `PathTests.test_two_sources_for_one_destination`

**Quellcode:** [test_project_paths.py:84–88](src/tests/test_project_paths.py#L84-L88).

```python
def test_two_sources_for_one_destination(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ValueError, 'conflict')`

**Relevante Aufrufe:** `check_plan`, `migration_plan`, `self.put`.

#### `PathTests.test_symlink_refused`

**Quellcode:** [test_project_paths.py:90–94](src/tests/test_project_paths.py#L90-L94).

```python
def test_symlink_refused(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ValueError, 'Symlink')`

**Relevante Aufrufe:** `(self.root / 'usage.csv').symlink_to`, `check_plan`, `migration_plan`, `self.put`.

#### `PathTests.test_benchmark_categorized_and_flat`

**Quellcode:** [test_project_paths.py:96–104](src/tests/test_project_paths.py#L96-L104).

```python
def test_benchmark_categorized_and_flat(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual({r['run_id'] for r in runs}, {'v', 'r'})`
- `self.assertEqual(len(runs), 2)`

**Relevante Aufrufe:** `analyze`, `self.put`.

#### `PathTests.test_conflicting_report`

**Quellcode:** [test_project_paths.py:106–110](src/tests/test_project_paths.py#L106-L110).

```python
def test_conflicting_report(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ValueError, 'Conflicting reports')`

**Relevante Aufrufe:** `P.report_files`, `self.put`.

#### `PathTests.test_metric_locations`

**Quellcode:** [test_project_paths.py:112–119](src/tests/test_project_paths.py#L112-L119).

```python
def test_metric_locations(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(P.metric_inputs(['usage.csv'], self.root), [old])`
- `self.assertEqual(P.metric_inputs(['usage.csv'], self.root), [new])`
- `self.assertRaisesRegex(ValueError, 'Conflicting metric logs')`

**Relevante Aufrufe:** `P.metric_inputs`, `new.write_text`, `self.put`.

#### `PathTests.test_report_routing`

**Quellcode:** [test_project_paths.py:121–126](src/tests/test_project_paths.py#L121-L126).

```python
def test_report_routing(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertTrue((P.report_directory(suffix, results) / f'x_{suffix}.json').is_file())`

**Relevante Aufrufe:** `(P.report_directory(suffix, results) / f'x_{suffix}.json').is_file`, `P.report_directory`, `main_strategy.save_report`, `patch.object`.

#### `PathTests.test_checkpoint_filename`

**Quellcode:** [test_project_paths.py:128–131](src/tests/test_project_paths.py#L128-L131).

```python
def test_checkpoint_filename(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(P.checkpoint_file('fixture'), P.CHECKPOINTS_DIR / 'fixture.sqlite3')`
- `self.assertRaises(ValueError)`

**Relevante Aufrufe:** `P.checkpoint_file`.

#### `PathTests.test_explicit_timing_override`

**Quellcode:** [test_project_paths.py:133–136](src/tests/test_project_paths.py#L133-L136).

```python
def test_explicit_timing_override(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertTrue(path.exists())`

**Relevante Aufrufe:** `path.exists`, `write_timings`.

---

## tests-test-recovery-manager

**Modul:** [`src/tests/test_recovery_manager.py`](src/tests/test_recovery_manager.py)  
**Features/Storys:** C-08, F-01  
**Aufgabe und Abgrenzung:** Recovery-Orchestrierung mit echtem lokalen Store, gemocktem LLM und synthetischen Chromium-Proben; optionale Regression historischer Reports.

**Direkte Abhängigkeiten:** `import argparse`; `import copy`; `import json`; `import shutil`; `import tempfile`; `import unittest`; `from TestRunner import TestRunner`; `from pathlib import Path`; `from types import SimpleNamespace`; `from unittest.mock import AsyncMock, Mock, patch`; `from playwright.async_api import async_playwright, Page`; `from ErrorClassifier import ErrorClassifier`; `from ExecutionPolicy import ExecutionPolicy, get_policy`; `from RecoveryManager import RecoveryManager, strategy_digest`; `from StrategyRepair import StrategyRepair`; `from StrategyStore import StrategyStore`; `from StructureVerifier import StructureVerifier, css_spec`.

**Definitionen:** 3 Klassen, 29 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `START`, `PARAMETERS`, `EXPECTED`, `EXECUTABLE`, `OLD_ROW`, `OLD_CONTAINER`, `STRATEGY`.

#### `role`

**Quellcode:** [test_recovery_manager.py:27–28](src/tests/test_recovery_manager.py#L27-L28).

```python
def role(kind, name):
```

**Aufgabe:** Baut Rollen-Locator-Dictionary im Strategievertrag.

**Parameter:** `name`: Name des Felds/Controls gemäß Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `dict(kind='role', role=kind, name=name, name_source='literal', selector=None)`.

#### `field`

**Quellcode:** [test_recovery_manager.py:31–33](src/tests/test_recovery_manager.py#L31-L33).

```python
def field(name, selector):
```

**Aufgabe:** Baut Pflichtfeldregel für synthetische Zeilen.

**Parameter:** `name`: Name des Felds/Controls gemäß Kontext; `selector`: CSS-Selektor. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `dict(name=name, source='text', scope='row', scope_selector=None, locator=css_spec(selector), value=None, regex=None, required=True)`.

**Relevante Aufrufe:** `css_spec`.

#### `html`

**Quellcode:** [test_recovery_manager.py:51–58](src/tests/test_recovery_manager.py#L51-L58).

```python
def html(row='new-row', container='old-table', numbers=(1, 2, 3), missing_doc=False):
```

**Aufgabe:** Erzeugt synthetische Ergebnisseite mit konfigurierbaren Locator-/Zeilen-/Control-Varianten.

**Parameter:** `row`: Locator bzw. Datensatzzeile im aktuellen Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `'<html><body><label>Query<input></label><button onclick="document.querySelector(\'table\').hidden=false">Search</button><table hidden data-testid="' + container + '"><tbody>' + rows + '</tb…`.

**Relevante Aufrufe:** `''.join`.

#### `report`

**Quellcode:** [test_recovery_manager.py:61–66](src/tests/test_recovery_manager.py#L61-L66).

```python
def report(**extra):
```

**Aufgabe:** Erzeugt fehlgeschlagenen synthetischen Execution-Report einschließlich Strategieprovenienz; zusätzliche Felder überschreibbar.

**Rückgabe (Ausdrücke im Code):** `dict(crawl_id='source-crawl', status='failed', strategy_version=1, schema_version=2, parameters=PARAMETERS, expected_fields=EXPECTED, domain='example.test', strategy_name='search', start_ur…`.

**Relevante Aufrufe:** `strategy_digest`.

#### `confirmed`

**Quellcode:** [test_recovery_manager.py:69–72](src/tests/test_recovery_manager.py#L69-L72).

```python
def confirmed():
```

**Aufgabe:** Erzeugt bestätigten synthetischen Verifikationsbericht mit erlaubter Locator-Alternative.

**Rückgabe (Ausdrücke im Code):** `{'status': 'confirmed', 'target': 'row', 'old_matches': 0, 'sample_rows': 3, 'downloads_attempted': 0, 'alternatives': [{'locator': css_spec('tr[data-testid="new-row"]'), 'matched_rows': 3,…`.

**Relevante Aufrufe:** `css_spec`.

### Klasse `RecoveryTests`

**Quellcode:** [test_recovery_manager.py:75–166](src/tests/test_recovery_manager.py#L75-L166).

**Aufgabe:** TestCase für Recovery-Orchestrierung mit echtem lokalen Store, gemocktem LLM und synthetischen Chromium-Proben; optionale Regression historischer Reports.

**Basisklassen:** `unittest.IsolatedAsyncioTestCase`.

#### `RecoveryTests.asyncSetUp`

**Quellcode:** [test_recovery_manager.py:76–86](src/tests/test_recovery_manager.py#L76-L86).

```python
async def asyncSetUp(self):
```

**Aufgabe:** Bereitet isolierte asynchrone Test-Fixture vor; registriert Cleanup und gegebenenfalls Browser-/Netzwerk-Mocks.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.tmp`, `self.store`, `self.policy`, `self.verifier`, `self.client`, `self.manager`.

**Relevante Aufrufe:** `AsyncMock`, `ExecutionPolicy`, `Mock`, `RecoveryManager`, `SimpleNamespace`, `StrategyRepair`, `StrategyStore`, `confirmed`, `copy.deepcopy`, `self.store.save`.

#### `RecoveryTests.test_server_and_access`

**Quellcode:** [test_recovery_manager.py:88–94](src/tests/test_recovery_manager.py#L88-L94).

```python
async def test_server_and_access(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((out['category'], out['status']), (category, 'skipped'))`
- `self.verifier.verify.assert_not_called()`
- `self.client.create.assert_not_called()`

**Relevante Aufrufe:** `report`, `self.client.create.assert_not_called`, `self.manager.recover`, `self.verifier.verify.assert_not_called`.

#### `RecoveryTests.test_default_offline`

**Quellcode:** [test_recovery_manager.py:96–99](src/tests/test_recovery_manager.py#L96-L99).

```python
async def test_default_offline(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(out['reason'], 'verification_not_authorized')`
- `self.verifier.verify.assert_not_called()`

**Relevante Aufrufe:** `report`, `self.manager.recover`, `self.verifier.verify.assert_not_called`.

#### `RecoveryTests.test_verify_without_llm`

**Quellcode:** [test_recovery_manager.py:101–105](src/tests/test_recovery_manager.py#L101-L105).

```python
async def test_verify_without_llm(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(out['status'], 'verified')`
- `self.client.create.assert_not_called()`
- `self.assertEqual(len(self.store.list_versions()), 1)`

**Relevante Aufrufe:** `report`, `self.client.create.assert_not_called`, `self.manager.recover`, `self.store.list_versions`.

#### `RecoveryTests.test_unconfirmed`

**Quellcode:** [test_recovery_manager.py:107–111](src/tests/test_recovery_manager.py#L107-L111).

```python
async def test_unconfirmed(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(out['reason'], 'structure_not_confirmed')`
- `self.client.create.assert_not_called()`

**Relevante Aufrufe:** `report`, `self.client.create.assert_not_called`, `self.manager.recover`.

#### `RecoveryTests.test_success_candidate_and_budget`

**Quellcode:** [test_recovery_manager.py:113–131](src/tests/test_recovery_manager.py#L113-L131).

```python
async def test_success_candidate_and_budget(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((out['status'], out['candidate_version'], out['llm_calls']), ('candidate_saved', 2, 1))`
- `self.assertEqual(loaded['metadata']['status'], 'candidate')`
- `self.assertEqual(self.store.load_active()['metadata']['strategy_version'], 1)`
- `self.assertEqual(candidate['records']['row'], new)`
- `self.assertEqual(candidate['navigation'][-1]['wait_after']['locator'], new)`
- `self.assertEqual(candidate['pagination']['wait_after']['locator'], new)`
- `self.assertEqual(candidate['records']['documents'], STRATEGY['records']['documents'])`
- `self.assertEqual(self.store.load(1)['strategy'], STRATEGY)`
- `self.assertEqual(again['reason'], 'repair_budget_exhausted')`
- `self.client.create.assert_called_once()`
- `self.assertEqual(self.client.create.call_args.kwargs['max_output_tokens'], 600)`
- `self.assertNotIn('tools', self.client.create.call_args.kwargs)`

**Relevante Aufrufe:** `confirmed`, `report`, `self.client.create.assert_called_once`, `self.manager.recover`, `self.store.activate`, `self.store.load`, `self.store.load_active`, `self.store.mark_validated`.

#### `RecoveryTests.test_bad_model_output`

**Quellcode:** [test_recovery_manager.py:133–140](src/tests/test_recovery_manager.py#L133-L140).

```python
async def test_bad_model_output(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(out['status'], 'failed')`
- `self.assertEqual(len(self.store.list_versions()), 1)`
- `self.assertEqual(again['reason'], 'repair_budget_exhausted')`
- `self.client.create.assert_called_once()`

**Relevante Aufrufe:** `report`, `self.client.create.assert_called_once`, `self.manager.recover`, `self.store.list_versions`.

#### `RecoveryTests.test_model_declines`

**Quellcode:** [test_recovery_manager.py:142–146](src/tests/test_recovery_manager.py#L142-L146).

```python
async def test_model_declines(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(out['status'], 'declined')`
- `self.assertEqual(len(self.store.list_versions()), 1)`

**Relevante Aufrufe:** `report`, `self.manager.recover`, `self.store.list_versions`.

#### `RecoveryTests.test_report_mismatch`

**Quellcode:** [test_recovery_manager.py:148–151](src/tests/test_recovery_manager.py#L148-L151).

```python
async def test_report_mismatch(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(out['reason'], 'source_strategy_mismatch')`
- `self.verifier.verify.assert_not_called()`

**Relevante Aufrufe:** `report`, `self.manager.recover`, `self.verifier.verify.assert_not_called`.

#### `RecoveryTests.test_unsupported_navigation`

**Quellcode:** [test_recovery_manager.py:153–156](src/tests/test_recovery_manager.py#L153-L156).

```python
async def test_unsupported_navigation(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(out['reason'], 'unsupported_structure_target')`
- `self.verifier.verify.assert_not_called()`

**Relevante Aufrufe:** `report`, `self.manager.recover`, `self.verifier.verify.assert_not_called`.

#### `RecoveryTests.test_policy_limit`

**Quellcode:** [test_recovery_manager.py:158–161](src/tests/test_recovery_manager.py#L158-L161).

```python
async def test_policy_limit(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValueError)`

**Relevante Aufrufe:** `get_policy`, `get_policy('unternehmensregister.de').check_workers`.

#### `RecoveryTests.test_stage_classification`

**Quellcode:** [test_recovery_manager.py:163–166](src/tests/test_recovery_manager.py#L163-L166).

```python
async def test_stage_classification(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(ErrorClassifier.classify(report())['primary']['category'], 'STRUCTURE_SUSPECTED')`
- `self.assertEqual(ErrorClassifier.classify(report(failure_stage='navigation'))['primary']['category'], 'STATE_NOT_CONFIRMED')`

**Relevante Aufrufe:** `ErrorClassifier.classify`, `report`.

### Klasse `BrowserVerificationTests`

**Quellcode:** [test_recovery_manager.py:169–215](src/tests/test_recovery_manager.py#L169-L215).

**Aufgabe:** TestCase für Recovery-Orchestrierung mit echtem lokalen Store, gemocktem LLM und synthetischen Chromium-Proben; optionale Regression historischer Reports.

**Basisklassen:** `unittest.IsolatedAsyncioTestCase`.

#### `BrowserVerificationTests.asyncSetUp`

**Quellcode:** [test_recovery_manager.py:170–177](src/tests/test_recovery_manager.py#L170-L177).

```python
async def asyncSetUp(self):
```

**Aufgabe:** Bereitet isolierte asynchrone Test-Fixture vor; registriert Cleanup und gegebenenfalls Browser-/Netzwerk-Mocks.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.pw`, `self.browser`, `self.page`, `self.verifier`.

**Relevante Aufrufe:** `ExecutionPolicy`, `StructureVerifier`, `async_playwright`, `async_playwright().start`, `self.browser.new_page`, `self.pw.chromium.launch`.

#### `BrowserVerificationTests.probe`

**Quellcode:** [test_recovery_manager.py:179–184](src/tests/test_recovery_manager.py#L179-L184).

```python
async def probe(self, content, target='row'):
```

**Aufgabe:** Lädt synthetische Seite, startet Suche, prüft alternative Locator und verifiziert, dass kein Download-Klick erfolgt.

**Parameter:** `target`: konkretes Zielobjekt bzw. Locator. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `result`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(await self.page.evaluate('window.downloadClicks'), 0)`

**Relevante Aufrufe:** `AsyncMock`, `self.page.evaluate`, `self.page.get_by_role`, `self.page.get_by_role('button', name='Search').click`, `self.page.set_content`, `self.verifier._probe`.

#### `BrowserVerificationTests.test_changed_row`

**Quellcode:** [test_recovery_manager.py:186–189](src/tests/test_recovery_manager.py#L186-L189).

```python
async def test_changed_row(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((result['status'], result['sample_rows']), ('confirmed', 3))`
- `self.assertEqual(result['alternatives'][0]['locator'], css_spec('tr[data-testid="new-row"]'))`

**Relevante Aufrufe:** `css_spec`, `html`, `self.probe`.

#### `BrowserVerificationTests.test_changed_container`

**Quellcode:** [test_recovery_manager.py:191–194](src/tests/test_recovery_manager.py#L191-L194).

```python
async def test_changed_container(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'confirmed')`
- `self.assertEqual(result['alternatives'][0]['locator'], css_spec('table[data-testid="new-table"]'))`

**Relevante Aufrufe:** `css_spec`, `html`, `self.probe`.

#### `BrowserVerificationTests.test_old_locator_present`

**Quellcode:** [test_recovery_manager.py:196–197](src/tests/test_recovery_manager.py#L196-L197).

```python
async def test_old_locator_present(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((await self.probe(html(row='old-row')))['reason'], 'old_locator_still_present')`

**Relevante Aufrufe:** `html`, `self.probe`.

#### `BrowserVerificationTests.test_missing_document_control`

**Quellcode:** [test_recovery_manager.py:199–200](src/tests/test_recovery_manager.py#L199-L200).

```python
async def test_missing_document_control(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((await self.probe(html(missing_doc=True)))['reason'], 'no_observed_replacement_passed')`

**Relevante Aufrufe:** `html`, `self.probe`.

#### `BrowserVerificationTests.test_duplicate_keys`

**Quellcode:** [test_recovery_manager.py:202–203](src/tests/test_recovery_manager.py#L202-L203).

```python
async def test_duplicate_keys(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((await self.probe(html(numbers=(1, 1))))['status'], 'inconclusive')`

**Relevante Aufrufe:** `html`, `self.probe`.

#### `BrowserVerificationTests.test_insufficient_sample`

**Quellcode:** [test_recovery_manager.py:205–206](src/tests/test_recovery_manager.py#L205-L206).

```python
async def test_insufficient_sample(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((await self.probe(html(numbers=(1,))))['status'], 'inconclusive')`

**Relevante Aufrufe:** `html`, `self.probe`.

#### `BrowserVerificationTests.test_independent_replay`

**Quellcode:** [test_recovery_manager.py:208–215](src/tests/test_recovery_manager.py#L208-L215).

```python
async def test_independent_replay(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'confirmed', result)`
- `self.assertEqual(result['downloads_attempted'], 0)`

**Relevante Aufrufe:** `patch`, `patch.object`, `report`, `self.verifier.verify`.

#### `BrowserVerificationTests.test_independent_replay.goto`

**Quellcode:** [test_recovery_manager.py:209–210](src/tests/test_recovery_manager.py#L209-L210).

```python
async def goto(page, url, **kwargs):
```

**Aufgabe:** Ersetzt echte Navigation durch lokale synthetische HTML-Seite; Varianten und Zähler entsprechen der umgebenden Fixture.

**Parameter:** `page`: Browser-Page oder Seitennummer gemäß Funktionszweck; `url`: zu prüfende URL; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `html`, `page.set_content`.

#### `main`

**Quellcode:** [test_recovery_manager.py:218–240](src/tests/test_recovery_manager.py#L218-L240).

```python
def main():
```

**Aufgabe:** CLI für zusätzliche historische Regressionstests und unittest-Ausführung.

**Rückgabe (Ausdrücke im Code):** `not TestRunner(verbosity=2).run(suite).wasSuccessful()`.

**Relevante Aufrufe:** `TestRunner`, `TestRunner(verbosity=2).run`, `TestRunner(verbosity=2).run(suite).wasSuccessful`, `__import__`, `argparse.ArgumentParser`, `parser.add_argument`, `parser.parse_args`, `suite.addTests`, `unittest.defaultTestLoader.loadTestsFromModule`, `unittest.defaultTestLoader.loadTestsFromTestCase`.

### Klasse `main.HistoryTests`

**Quellcode:** [test_recovery_manager.py:224–238](src/tests/test_recovery_manager.py#L224-L238).

**Aufgabe:** TestCase für Recovery-Orchestrierung mit echtem lokalen Store, gemocktem LLM und synthetischen Chromium-Proben; optionale Regression historischer Reports.

**Basisklassen:** `unittest.IsolatedAsyncioTestCase`.

#### `main.HistoryTests.test_real_reports`

**Quellcode:** [test_recovery_manager.py:225–238](src/tests/test_recovery_manager.py#L225-L238).

```python
async def test_real_reports(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertTrue(paths)`
- `self.assertEqual(result['status'], 'skipped')`
- `self.assertEqual(result['llm_calls'], 0)`
- `verifier.verify.assert_not_called()`
- `repair.propose.assert_not_called()`

**Relevante Aufrufe:** `AsyncMock`, `ExecutionPolicy`, `Mock`, `RecoveryManager`, `SimpleNamespace`, `args.history_dir.glob`, `json.loads`, `manager.recover`, `path.read_text`, `repair.propose.assert_not_called`, `sorted`, `verifier.verify.assert_not_called`.

---

## tests-test-state-menu

**Modul:** [`src/tests/test_state_menu.py`](src/tests/test_state_menu.py)  
**Features/Storys:** C-06, C-07  
**Aufgabe und Abgrenzung:** Bundesländer-Menü, Overlay, bestätigte Auswahl und Folgeaktionen in synthetischem Registerformular. Synchrone und asynchrone Varianten.

**Direkte Abhängigkeiten:** `import json`; `import shutil`; `import unittest`; `from TestRunner import TestRunner`; `from unittest.mock import patch, PropertyMock`; `from playwright.async_api import async_playwright, Page as AsyncPage`; `from playwright.sync_api import sync_playwright, Page as SyncPage`; `from StrategyExecutor import StrategyExecutor, ExecutionError`; `from AsyncStrategyExecutor import AsyncStrategyExecutor`.

**Definitionen:** 2 Klassen, 17 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `URL`.

#### `role`

**Quellcode:** [test_state_menu.py:14–15](src/tests/test_state_menu.py#L14-L15).

```python
def role(role, name, source='literal'):
```

**Aufgabe:** Baut Rollen-Locator-Dictionary im Strategievertrag.

**Parameter:** `role`: Accessibility-Rolle; `name`: Name des Felds/Controls gemäß Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `dict(kind='role', role=role, name=name, name_source=source, selector=None)`.

#### `action`

**Quellcode:** [test_state_menu.py:18–19](src/tests/test_state_menu.py#L18-L19).

```python
def action(kind, locator):
```

**Aufgabe:** Baut Navigationsaktions-Dictionary für Teststrategie.

**Parameter:** `locator`: Playwright-Locator oder Locator-Regel gemäß Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `dict(action=kind, locator=locator, value_source='none', value=None, wait_after=None)`.

#### `strategy`

**Quellcode:** [test_state_menu.py:22–29](src/tests/test_state_menu.py#L22-L29).

```python
def strategy():
```

**Aufgabe:** Erzeugt bzw. kopiert eine für dieses Testmodul angepasste Strategie; Varianten sind über die Signatur wählbar.

**Rückgabe (Ausdrücke im Code):** `dict(schema_version=2, status='candidate', parameters=['federal_state'], navigation=[action('click', role('button', 'Bundesländer')), action('check', role('checkbox', 'federal_state', 'para…`.

**Relevante Aufrufe:** `action`, `role`.

#### `fixture`

**Quellcode:** [test_state_menu.py:35–52](src/tests/test_state_menu.py#L35-L52).

```python
def fixture(mode):
```

**Aufgabe:** Erzeugt das synthetische HTML bzw. die Testdaten für das im Modul beschriebene Szenario; Varianten simulieren Fehler oder Zustandsänderungen.

**Parameter:** `mode`: gewählte Variante/Modus. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `'<!doctype html><html><head><style>\n    #types {position:absolute;top:160px;left:20px;width:200px;height:40px;}\n    #overlay {position:absolute;top:160px;left:20px;width:200px;height:40px…`.

**Relevante Aufrufe:** `'<!doctype html><html><head><style>\n    #types {position:absolute;top:160px;left:20px;width:200px;height:40px;}\n    #overlay {position:absolute;top:160px;left:20px;width:200px;height:40px;z-index:2;background:white;}\n    </style></head><body><button id="states" aria-expanded="false" onclick="toggle()">Bundesländer</button>\n    <div id="choices" hidden><input type="checkbox" id="hh" aria-label="Hamburg" onchange="stateChanged()"></div>\n    <div id="overlay" class="infoButtonWrapper" hidden>Additional information</div>\n    <button id="register" aria-expanded="false" onclick="openRegister()">Registerart</button>\n    <div id="types" hidden><div role="option" onclick="window.selected=true">HRB</div></div>\n    <script>const mode=MODE;window.toggles=0;window.selected=false;\n    function toggle(){window.toggles++;let b=document.querySelector(\'#states\');let open=b.getAttribute(\'aria-expanded\')===\'true\';\n      if(open && mode===\'ignored\')return; if(open && mode===\'lost\')document.querySelector(\'#hh\').checked=false;\n      b.setAttribute(\'aria-expanded\',String(!open));document.querySelector(\'#choices\').hidden=open;\n      document.querySelector(\'#overlay\').hidden=open;}\n    function stateChanged(){if(mode===\'auto\')toggle();}\n    function openRegister(){document.querySelector(\'#register\').setAttribute(\'aria-expanded\',\'true\');\n      document.querySelector(\'#types\').hidden=false;}\n    </script></body></html>'.replace`.

#### `executor`

**Quellcode:** [test_state_menu.py:55–57](src/tests/test_state_menu.py#L55-L57).

```python
def executor(cls):
```

**Aufgabe:** Erstellt für den Menütest den angegebenen Executor mit synthetischer Strategie und Provider-Konfiguration.

**Rückgabe (Ausdrücke im Code):** `cls(strategy(), {'federal_state': 'Hamburg'}, ['unternehmensregister.de'], timeout_ms=650, open_controls=('Bundesländer', 'Registerart'))`.

**Relevante Aufrufe:** `cls`, `strategy`.

### Klasse `SyncTests`

**Quellcode:** [test_state_menu.py:60–93](src/tests/test_state_menu.py#L60-L93).

**Aufgabe:** Synchroner TestCase für die im Modul beschriebenen Varianten.

**Basisklassen:** `unittest.TestCase`.

#### `SyncTests.setUpClass`

**Quellcode:** [test_state_menu.py:62–64](src/tests/test_state_menu.py#L62-L64).

```python
@classmethod
def setUpClass(cls):
```

**Aufgabe:** Initialisiert klassenweit benötigte Testressourcen bzw. absichtlich fehlerhafte Fixture im Runner-Selbsttest.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `cls.pw`, `cls.browser`.

**Relevante Aufrufe:** `cls.pw.chromium.launch`, `shutil.which`, `sync_playwright`, `sync_playwright().start`.

#### `SyncTests.tearDownClass`

**Quellcode:** [test_state_menu.py:67–69](src/tests/test_state_menu.py#L67-L69).

```python
@classmethod
def tearDownClass(cls):
```

**Aufgabe:** Schließt klassenweite Browser-/Playwright-Ressourcen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `cls.browser.close`, `cls.pw.stop`.

#### `SyncTests.run_case`

**Quellcode:** [test_state_menu.py:71–88](src/tests/test_state_menu.py#L71-L88).

```python
def run_case(self, mode, fails=False):
```

**Aufgabe:** Führt Menü-Szenario im synchronen oder asynchronen Executor aus und prüft erwarteten Erfolg oder Abbruch.

**Parameter:** `mode`: gewählte Variante/Modus. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ExecutionError, 'Menu postcondition not met')`
- `self.assertFalse(page.evaluate('window.selected'))`
- `self.assertTrue(page.evaluate('window.selected && document.querySelector("#hh").checked'))`
- `self.assertEqual(page.evaluate('window.toggles'), 2)`
- `self.assertEqual(item['result'], 'already_closed' if mode == 'auto' else 'confirmed')`

**Relevante Aufrufe:** `context.new_page`, `ex._navigate_once`, `executor`, `fixture`, `next`, `page.evaluate`, `page.set_content`, `patch.object`, `self.browser.new_context`.

#### `SyncTests.test_close_overlay`

**Quellcode:** [test_state_menu.py:90–90](src/tests/test_state_menu.py#L90-L90).

```python
def test_close_overlay(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `self.run_case`.

#### `SyncTests.test_already_closed`

**Quellcode:** [test_state_menu.py:91–91](src/tests/test_state_menu.py#L91-L91).

```python
def test_already_closed(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `self.run_case`.

#### `SyncTests.test_ignored_close`

**Quellcode:** [test_state_menu.py:92–92](src/tests/test_state_menu.py#L92-L92).

```python
def test_ignored_close(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `self.run_case`.

#### `SyncTests.test_lost_selection`

**Quellcode:** [test_state_menu.py:93–93](src/tests/test_state_menu.py#L93-L93).

```python
def test_lost_selection(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `self.run_case`.

### Klasse `AsyncTests`

**Quellcode:** [test_state_menu.py:96–126](src/tests/test_state_menu.py#L96-L126).

**Aufgabe:** Asynchroner TestCase für die im Modul beschriebenen Varianten.

**Basisklassen:** `unittest.IsolatedAsyncioTestCase`.

#### `AsyncTests.run_case`

**Quellcode:** [test_state_menu.py:97–121](src/tests/test_state_menu.py#L97-L121).

```python
async def run_case(self, mode, fails=False):
```

**Aufgabe:** Führt Menü-Szenario im synchronen oder asynchronen Executor aus und prüft erwarteten Erfolg oder Abbruch.

**Parameter:** `mode`: gewählte Variante/Modus. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ExecutionError, 'Menu postcondition not met')`
- `self.assertFalse(await page.evaluate('window.selected'))`
- `self.assertTrue(await page.evaluate('window.selected && document.querySelector("#hh").checked'))`
- `self.assertEqual(await page.evaluate('window.toggles'), 2)`
- `self.assertEqual(item['result'], 'already_closed' if mode == 'auto' else 'confirmed')`

**Relevante Aufrufe:** `async_playwright`, `browser.close`, `browser.new_context`, `context.new_page`, `ex._navigate_once`, `executor`, `fixture`, `next`, `page.evaluate`, `page.set_content`, `patch.object`, `patcher.start`, `pw.chromium.launch`, `shutil.which`.

#### `AsyncTests.test_close_overlay`

**Quellcode:** [test_state_menu.py:123–123](src/tests/test_state_menu.py#L123-L123).

```python
async def test_close_overlay(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `self.run_case`.

#### `AsyncTests.test_already_closed`

**Quellcode:** [test_state_menu.py:124–124](src/tests/test_state_menu.py#L124-L124).

```python
async def test_already_closed(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `self.run_case`.

#### `AsyncTests.test_ignored_close`

**Quellcode:** [test_state_menu.py:125–125](src/tests/test_state_menu.py#L125-L125).

```python
async def test_ignored_close(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `self.run_case`.

#### `AsyncTests.test_lost_selection`

**Quellcode:** [test_state_menu.py:126–126](src/tests/test_state_menu.py#L126-L126).

```python
async def test_lost_selection(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Prüfpfad:** keine direkte Assertion im Körper; Prüfung erfolgt über aufgerufene Testhelfer bzw. kontrollierte Testausführung.

**Relevante Aufrufe:** `self.run_case`.

---

## tests-test-strategy-executor

**Modul:** [`src/tests/test_strategy_executor.py`](src/tests/test_strategy_executor.py)  
**Features/Storys:** C-06, D-02, E-02  
**Aufgabe und Abgrenzung:** Synchroner Chromium-Executor, Cookie-/Menüzustand, Extraktion, Download, Paginierung und Zugriffsschutz. Benötigt explizites Strategie-JSON als CLI-Fixture.

**Direkte Abhängigkeiten:** `import copy`; `import json`; `import sys`; `import tempfile`; `import unittest`; `from TestRunner import TestRunner`; `from unittest.mock import patch`; `from pathlib import Path`; `from playwright.sync_api import sync_playwright`; `from StrategyExecutor import ExecutionError, StrategyExecutor`.

**Definitionen:** 1 Klassen, 29 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `HTML`.

### Klasse `ExecutorTests`

**Quellcode:** [test_strategy_executor.py:49–389](src/tests/test_strategy_executor.py#L49-L389).

**Aufgabe:** TestCase für Synchroner Chromium-Executor, Cookie-/Menüzustand, Extraktion, Download, Paginierung und Zugriffsschutz. Benötigt explizites Strategie-JSON als CLI-Fixture.

**Basisklassen:** `unittest.TestCase`.

#### `ExecutorTests.setUpClass`

**Quellcode:** [test_strategy_executor.py:51–56](src/tests/test_strategy_executor.py#L51-L56).

```python
@classmethod
def setUpClass(cls):
```

**Aufgabe:** Initialisiert klassenweit benötigte Testressourcen bzw. absichtlich fehlerhafte Fixture im Runner-Selbsttest.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `cls.strategy`, `cls.playwright`, `cls.browser`.

**Relevante Aufrufe:** `Path(sys.argv[1]).read_text`, `cls.playwright.chromium.launch`, `json.loads`, `sync_playwright`, `sync_playwright().start`.

#### `ExecutorTests.tearDownClass`

**Quellcode:** [test_strategy_executor.py:59–61](src/tests/test_strategy_executor.py#L59-L61).

```python
@classmethod
def tearDownClass(cls):
```

**Aufgabe:** Schließt klassenweite Browser-/Playwright-Ressourcen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `cls.browser.close`, `cls.playwright.stop`.

#### `ExecutorTests.setUp`

**Quellcode:** [test_strategy_executor.py:63–80](src/tests/test_strategy_executor.py#L63-L80).

```python
def setUp(self):
```

**Aufgabe:** Bereitet isolierte Test-Fixture vor; temporäre Ressourcen und Cleanup entsprechend der konkreten Einrichtung unten.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.temp`, `self.context`, `self.page`, `self.executor`.

**Relevante Aufrufe:** `StrategyExecutor`, `copy.deepcopy`, `patch`, `patcher.start`, `self.browser.new_context`, `self.context.new_page`, `self.executor._navigate`, `self.page.set_content`.

#### `ExecutorTests.test_cookie_dialog`

**Quellcode:** [test_strategy_executor.py:82–99](src/tests/test_strategy_executor.py#L82-L99).

```python
def test_cookie_dialog(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertTrue(self.page.evaluate('window.necessaryOnly === true && !window.allCookies'))`
- `self.assertEqual(self.executor._collect(1, 1, False), 'company_limit')`

**Relevante Aufrufe:** `self.executor._collect`, `self.executor._navigate`, `self.page.evaluate`, `self.page.set_content`.

#### `ExecutorTests.test_cookie_dialog_while_waiting_for_first_target`

**Quellcode:** [test_strategy_executor.py:101–118](src/tests/test_strategy_executor.py#L101-L118).

```python
def test_cookie_dialog_while_waiting_for_first_target(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertTrue(self.page.evaluate('window.necessaryOnly === true'))`
- `self.assertEqual(self.executor.cookie_dialog_count, 1)`
- `self.assertEqual(self.executor._collect(1, 1, False), 'company_limit')`

**Relevante Aufrufe:** `self.executor._collect`, `self.executor._navigate`, `self.page.evaluate`, `self.page.set_content`.

#### `ExecutorTests.test_cookie_dialog_during_actionability`

**Quellcode:** [test_strategy_executor.py:120–137](src/tests/test_strategy_executor.py#L120-L137).

```python
def test_cookie_dialog_during_actionability(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertTrue(self.page.evaluate('window.necessaryOnly === true'))`
- `self.assertTrue(self.page.get_by_role('checkbox', name='Hamburg').is_visible())`

**Relevante Aufrufe:** `self.executor._install_cookie_handler`, `self.executor._wait_visible`, `self.page.evaluate`, `self.page.get_by_role`, `self.page.get_by_role('checkbox', name='Hamburg').is_visible`, `self.page.set_content`, `target.click`.

#### `ExecutorTests.test_cookie_dialog_zero_sized_wrapper`

**Quellcode:** [test_strategy_executor.py:139–164](src/tests/test_strategy_executor.py#L139-L164).

```python
def test_cookie_dialog_zero_sized_wrapper(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(dialog.count(), 1)`
- `self.assertFalse(dialog.is_visible())`
- `self.assertTrue(button.is_visible())`
- `self.assertTrue(self.page.evaluate('window.necessaryOnly === true'))`
- `self.assertEqual(self.executor.cookie_dialog_count, 1)`
- `self.assertEqual(self.executor._collect(1, 1, False), 'company_limit')`

**Relevante Aufrufe:** `button.is_visible`, `button.wait_for`, `dialog.count`, `dialog.is_visible`, `self.executor._collect`, `self.executor._cookie_button`, `self.executor._cookie_locator`, `self.executor._navigate`, `self.page.evaluate`, `self.page.set_content`.

#### `ExecutorTests.test_cookie_zero_sized_wrapper_during_actionability`

**Quellcode:** [test_strategy_executor.py:166–185](src/tests/test_strategy_executor.py#L166-L185).

```python
def test_cookie_zero_sized_wrapper_during_actionability(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertFalse(self.executor._cookie_locator().is_visible())`
- `self.assertTrue(self.page.evaluate('window.necessaryOnly === true'))`
- `self.assertTrue(self.page.get_by_role('checkbox', name='Hamburg').is_visible())`

**Relevante Aufrufe:** `self.executor._cookie_locator`, `self.executor._cookie_locator().is_visible`, `self.executor._install_cookie_handler`, `self.executor._wait_visible`, `self.page.evaluate`, `self.page.get_by_role`, `self.page.get_by_role('checkbox', name='Hamburg').is_visible`, `self.page.set_content`, `target.click`.

#### `ExecutorTests._install_resetting_cookie_fixture`

**Quellcode:** [test_strategy_executor.py:187–221](src/tests/test_strategy_executor.py#L187-L221).

```python
def _install_resetting_cookie_fixture(self, repeat=False):
```

**Aufgabe:** Installiert synthetischen Cookie-Dialog, der den Navigationszustand zurücksetzt; repeat simuliert erneute Unterbrechung.

**Rückgabe (Ausdrücke im Code):** `url`.

**Relevante Aufrufe:** `"<script>\n        (() => {\n        const first = document.querySelector('button');\n        first.onclick = () => {\n            document.querySelector('#states').hidden = false;\n            if (REPEAT || !window.necessaryOnly) {\n                const dialog = document.createElement('div');\n                dialog.setAttribute('role', 'dialog');\n                dialog.setAttribute('aria-label', 'Cookie Dialog');\n                dialog.style = 'position:fixed;inset:0;background:white;z-index:100';\n                dialog.innerHTML = '<button>Nur technisch notwendige Cookies akzeptieren</button>';\n                dialog.firstChild.onclick = () => {\n                    window.necessaryOnly = true;\n                    document.querySelector('#states').hidden = true;\n                    dialog.remove();\n                };\n                document.body.append(dialog);\n            }\n        };\n        })();\n        </script>".replace`, `HTML.replace`, `goto.start`, `patch.object`, `self.page.set_content`.

#### `ExecutorTests._install_resetting_cookie_fixture.reload_fixture`

**Quellcode:** [test_strategy_executor.py:213–215](src/tests/test_strategy_executor.py#L213-L215).

```python
def reload_fixture(target, **kwargs):
```

**Aufgabe:** Simuliert Reload der lokalen Cookie-Fixture und prüft Ziel-URL.

**Parameter:** `target`: konkretes Zielobjekt bzw. Locator; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(target, url)`

**Relevante Aufrufe:** `self.page.set_content`.

#### `ExecutorTests.test_cookie_consent_resets_open_dropdown`

**Quellcode:** [test_strategy_executor.py:223–231](src/tests/test_strategy_executor.py#L223-L231).

```python
def test_cookie_consent_resets_open_dropdown(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.executor._collect(1, 1, False), 'company_limit')`
- `self.assertEqual(self.executor.cookie_dialog_count, 1)`
- `self.assertEqual(self.executor.navigation_restarts, 1)`
- `self.assertTrue(self.page.get_by_role('checkbox', name='Hamburg').is_checked())`
- `self.assertTrue(self.page.evaluate('window.necessaryOnly === true'))`

**Relevante Aufrufe:** `patch`, `self._install_resetting_cookie_fixture`, `self.executor._collect`, `self.executor._navigate`, `self.page.evaluate`, `self.page.get_by_role`, `self.page.get_by_role('checkbox', name='Hamburg').is_checked`.

#### `ExecutorTests.test_repeated_cookie_interruption_stops`

**Quellcode:** [test_strategy_executor.py:233–239](src/tests/test_strategy_executor.py#L233-L239).

```python
def test_repeated_cookie_interruption_stops(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ExecutionError, 'again after restart')`
- `self.assertEqual(self.executor.navigation_restarts, 1)`
- `self.assertEqual(self.executor.download_attempts, 0)`

**Relevante Aufrufe:** `patch`, `self._install_resetting_cookie_fixture`, `self.executor._navigate`.

#### `ExecutorTests.test_missing_target_without_cookie_is_not_replayed`

**Quellcode:** [test_strategy_executor.py:241–248](src/tests/test_strategy_executor.py#L241-L248).

```python
def test_missing_target_without_cookie_is_not_replayed(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ExecutionError, 'Timed out waiting for target')`
- `self.assertEqual(self.executor.navigation_restarts, 0)`

**Relevante Aufrufe:** `self.executor._navigate`, `self.page.get_by_role`, `self.page.get_by_role('button', name='Bundesländer').evaluate`, `self.page.set_content`.

#### `ExecutorTests._menu_fixture`

**Quellcode:** [test_strategy_executor.py:250–255](src/tests/test_strategy_executor.py#L250-L255).

```python
def _menu_fixture(self, script):
```

**Aufgabe:** Lädt Menü-HTML, konfiguriert bekannte Controls und Cookie-Dialog und führt synthetisches Testskript aus.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `frozenset`, `self.page.evaluate`, `self.page.set_content`.

#### `ExecutorTests.test_menu_ignored_first_click`

**Quellcode:** [test_strategy_executor.py:257–269](src/tests/test_strategy_executor.py#L257-L269).

```python
def test_menu_ignored_first_click(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.page.evaluate('window.menuClicks'), 2)`
- `self.assertEqual(self.executor.menu_retries, 1)`
- `self.assertEqual(self.executor._collect(1, 1, True), 'company_limit')`

**Relevante Aufrufe:** `self._menu_fixture`, `self.executor._collect`, `self.executor._navigate`, `self.page.evaluate`.

#### `ExecutorTests.test_menu_retry_after_cookie_restart`

**Quellcode:** [test_strategy_executor.py:271–293](src/tests/test_strategy_executor.py#L271-L293).

```python
def test_menu_retry_after_cookie_restart(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.executor._collect(1, 1, True), 'company_limit')`
- `self.assertEqual(self.executor.navigation_restarts, 1)`
- `self.assertEqual(self.executor.menu_retries, 1)`
- `self.assertEqual(self.executor.download_attempts, 2)`

**Relevante Aufrufe:** `frozenset`, `patch`, `self._install_resetting_cookie_fixture`, `self.executor._collect`, `self.executor._navigate`.

#### `ExecutorTests.test_menu_retry_after_cookie_restart.reload_with_ignored_click`

**Quellcode:** [test_strategy_executor.py:276–285](src/tests/test_strategy_executor.py#L276-L285).

```python
def reload_with_ignored_click(target, **kwargs):
```

**Aufgabe:** Simuliert Reload und ignorierten ersten Menüklick.

**Parameter:** `target`: konkretes Zielobjekt bzw. Locator; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `reload_fixture`, `self.page.evaluate`.

#### `ExecutorTests.test_menu_already_open_is_not_closed`

**Quellcode:** [test_strategy_executor.py:295–303](src/tests/test_strategy_executor.py#L295-L303).

```python
def test_menu_already_open_is_not_closed(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.page.evaluate('window.menuClicks'), 0)`
- `self.assertEqual(self.executor.menu_retries, 0)`

**Relevante Aufrufe:** `self._menu_fixture`, `self.executor._navigate`, `self.page.evaluate`.

#### `ExecutorTests.test_expanded_menu_waits_for_delayed_option`

**Quellcode:** [test_strategy_executor.py:305–316](src/tests/test_strategy_executor.py#L305-L316).

```python
def test_expanded_menu_waits_for_delayed_option(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.page.evaluate('window.menuClicks'), 1)`
- `self.assertEqual(self.executor.menu_retries, 0)`

**Relevante Aufrufe:** `self._menu_fixture`, `self.executor._navigate`, `self.page.evaluate`.

#### `ExecutorTests.test_menu_missing_option_stops_after_bounded_retry`

**Quellcode:** [test_strategy_executor.py:318–327](src/tests/test_strategy_executor.py#L318-L327).

```python
def test_menu_missing_option_stops_after_bounded_retry(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ExecutionError, 'Menu postcondition not met')`
- `self.assertEqual(self.page.evaluate('window.menuClicks'), 2)`
- `self.assertEqual(self.executor.menu_retries, 1)`
- `self.assertEqual(self.executor.download_attempts, 0)`

**Relevante Aufrufe:** `self._menu_fixture`, `self.executor._navigate`, `self.page.evaluate`.

#### `ExecutorTests.test_cookie_dialog_absent`

**Quellcode:** [test_strategy_executor.py:329–333](src/tests/test_strategy_executor.py#L329-L333).

```python
def test_cookie_dialog_absent(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.executor._collect(1, 1, False), 'company_limit')`

**Relevante Aufrufe:** `self.executor._collect`, `self.executor._handle_cookie_dialog`.

#### `ExecutorTests.test_cookie_dialog_without_necessary_option`

**Quellcode:** [test_strategy_executor.py:335–347](src/tests/test_strategy_executor.py#L335-L347).

```python
def test_cookie_dialog_without_necessary_option(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(Exception)`
- `self.assertFalse(self.page.evaluate('window.allCookies === true'))`

**Relevante Aufrufe:** `self.executor._handle_cookie_dialog`, `self.page.evaluate`.

#### `ExecutorTests.test_extract_and_download`

**Quellcode:** [test_strategy_executor.py:349–354](src/tests/test_strategy_executor.py#L349-L354).

```python
def test_extract_and_download(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.executor._collect(1, 1, True), 'company_limit')`
- `self.assertEqual((record['company_name'], record['register_number']), ('Firma A', '8165'))`
- `self.assertEqual([d['download_status'] for d in record['documents']], ['downloaded', 'downloaded'])`
- `self.assertTrue(all((Path(d['file_path']).exists() for d in record['documents'])))`

**Relevante Aufrufe:** `Path(d['file_path']).exists`, `all`, `self.executor._collect`.

#### `ExecutorTests.test_required_field_missing`

**Quellcode:** [test_strategy_executor.py:356–360](src/tests/test_strategy_executor.py#L356-L360).

```python
def test_required_field_missing(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ExecutionError)`
- `self.assertEqual(self.executor.companies, [])`

**Relevante Aufrufe:** `self.executor._collect`, `self.page.locator`, `self.page.locator('tbody b').first.evaluate`.

#### `ExecutorTests.test_ambiguous_field`

**Quellcode:** [test_strategy_executor.py:362–365](src/tests/test_strategy_executor.py#L362-L365).

```python
def test_ambiguous_field(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ExecutionError)`

**Relevante Aufrufe:** `self.executor._collect`, `self.page.locator`, `self.page.locator('.row_row__kw5rN').first.evaluate`.

#### `ExecutorTests.test_pagination`

**Quellcode:** [test_strategy_executor.py:367–370](src/tests/test_strategy_executor.py#L367-L370).

```python
def test_pagination(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.executor._collect(3, 2, False), 'company_limit')`
- `self.assertEqual([c['register_number'] for c in self.executor.companies], ['8165', '9999', '700'])`
- `self.assertEqual(self.executor.pages, 2)`

**Relevante Aufrufe:** `self.executor._collect`.

#### `ExecutorTests.test_invalid_xml`

**Quellcode:** [test_strategy_executor.py:372–376](src/tests/test_strategy_executor.py#L372-L376).

```python
def test_invalid_xml(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ExecutionError)`

**Relevante Aufrufe:** `path.write_text`, `self.executor._validate_file`.

#### `ExecutorTests.test_download_missing`

**Quellcode:** [test_strategy_executor.py:378–383](src/tests/test_strategy_executor.py#L378-L383).

```python
def test_download_missing(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(Exception)`
- `self.assertEqual([d['download_status'] for d in self.executor.companies[0]['documents']], ['failed', 'not_attempted'])`

**Relevante Aufrufe:** `self.executor._collect`, `self.page.get_by_role`, `self.page.get_by_role('button', name='Chronologischen Abdruck herunterladen').first.evaluate`.

#### `ExecutorTests.test_access_block`

**Quellcode:** [test_strategy_executor.py:385–389](src/tests/test_strategy_executor.py#L385-L389).

```python
def test_access_block(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ExecutionError)`
- `self.assertEqual(self.executor.download_attempts, 0)`

**Relevante Aufrufe:** `self.executor._collect`.

---

## tests-test-strategy-store

**Modul:** [`src/tests/test_strategy_store.py`](src/tests/test_strategy_store.py)  
**Features/Storys:** C-05  
**Aufgabe und Abgrenzung:** Lokaler StrategyStore mit expliziter v2-Fixture, Versionen, Lock und Legacy-Aktivierung; Discovery ohne Fixture noch nicht zuverlässig.

**Direkte Abhängigkeiten:** `import json`; `import sys`; `import unittest`; `from TestRunner import TestRunner`; `from copy import deepcopy`; `from pathlib import Path`; `from tempfile import TemporaryDirectory`; `from concurrent.futures import ThreadPoolExecutor`; `from jsonschema import ValidationError`; `from StrategyStore import StrategyStore`.

**Definitionen:** 1 Klassen, 10 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `START_URL`.

### Klasse `StrategyStoreTest`

**Quellcode:** [test_strategy_store.py:19–111](src/tests/test_strategy_store.py#L19-L111).

**Aufgabe:** TestCase für Lokaler StrategyStore mit expliziter v2-Fixture, Versionen, Lock und Legacy-Aktivierung; Discovery ohne Fixture noch nicht zuverlässig.

**Basisklassen:** `unittest.TestCase`.

#### `StrategyStoreTest.setUp`

**Quellcode:** [test_strategy_store.py:20–23](src/tests/test_strategy_store.py#L20-L23).

```python
def setUp(self):
```

**Aufgabe:** Bereitet isolierte Test-Fixture vor; temporäre Ressourcen und Cleanup entsprechend der konkreten Einrichtung unten.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.directory`, `self.store`.

**Relevante Aufrufe:** `StrategyStore`, `TemporaryDirectory`.

#### `StrategyStoreTest.save`

**Quellcode:** [test_strategy_store.py:25–26](src/tests/test_strategy_store.py#L25-L26).

```python
def save(self, strategy=None):
```

**Aufgabe:** Speichert Teststrategie oder Testseite in lokalem temporärem Store/Checkpoint.

**Parameter:** `strategy`: Strategie-Dictionary nach StrategySchema. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `self.store.save(FIXTURE if strategy is None else strategy, START_URL, 'test-crawl')`.

**Relevante Aufrufe:** `self.store.save`.

#### `StrategyStoreTest.test_empty_store`

**Quellcode:** [test_strategy_store.py:28–33](src/tests/test_strategy_store.py#L28-L33).

```python
def test_empty_store(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertFalse(self.store.exists())`
- `self.assertIsNone(self.store.load_active())`
- `self.assertEqual(self.store.list_versions(), [])`
- `self.assertRaises(KeyError)`

**Relevante Aufrufe:** `self.store.exists`, `self.store.list_versions`, `self.store.load`, `self.store.load_active`.

#### `StrategyStoreTest.test_save_and_reload`

**Quellcode:** [test_strategy_store.py:35–42](src/tests/test_strategy_store.py#L35-L42).

```python
def test_save_and_reload(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.save(), 1)`
- `self.assertEqual(self.save(), 2)`
- `self.assertTrue(reopened.exists(2))`
- `self.assertEqual(reopened.load(2)['strategy'], FIXTURE)`
- `self.assertEqual(reopened.load(2)['metadata']['crawl_id'], 'test-crawl')`
- `self.assertIsNone(reopened.load_active())`

**Relevante Aufrufe:** `StrategyStore`, `reopened.exists`, `reopened.load`, `reopened.load_active`, `self.save`.

#### `StrategyStoreTest.test_validation_and_activation`

**Quellcode:** [test_strategy_store.py:44–56](src/tests/test_strategy_store.py#L44-L56).

```python
def test_validation_and_activation(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValueError)`
- `self.assertEqual(active['metadata']['status'], 'active')`
- `self.assertEqual(active['strategy']['status'], 'candidate')`
- `self.assertEqual(active['strategy'], FIXTURE)`

**Relevante Aufrufe:** `self.save`, `self.store.activate`, `self.store.load_active`, `self.store.mark_validated`.

#### `StrategyStoreTest.test_replacement_and_invalidation`

**Quellcode:** [test_strategy_store.py:58–71](src/tests/test_strategy_store.py#L58-L71).

```python
def test_replacement_and_invalidation(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.save(), version)`
- `self.assertEqual(self.store.load(1)['metadata']['status'], 'validated')`
- `self.assertEqual(self.store.load_active()['metadata']['strategy_version'], 2)`
- `self.assertIsNone(self.store.load_active())`
- `self.assertEqual(self.store.load(2)['metadata']['invalidation_reason'], 'structure_error')`
- `self.assertRaises(ValueError)`
- `self.assertEqual(self.store.load_active()['metadata']['strategy_version'], 1)`

**Relevante Aufrufe:** `self.save`, `self.store.activate`, `self.store.invalidate`, `self.store.load`, `self.store.load_active`, `self.store.mark_validated`.

#### `StrategyStoreTest.test_unsupported_and_invalid_schema`

**Quellcode:** [test_strategy_store.py:73–89](src/tests/test_strategy_store.py#L73-L89).

```python
def test_unsupported_and_invalid_schema(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValueError)`
- `self.assertRaises(ValidationError)`
- `self.assertEqual(len(self.store.list_versions()), 1)`

**Relevante Aufrufe:** `deepcopy`, `self.save`, `self.store.activate`, `self.store.list_versions`, `self.store.mark_validated`, `unsupported.update`.

#### `StrategyStoreTest.test_domain_and_name`

**Quellcode:** [test_strategy_store.py:91–97](src/tests/test_strategy_store.py#L91-L97).

```python
def test_domain_and_name(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValueError)`

**Relevante Aufrufe:** `StrategyStore`, `self.store.save`.

#### `StrategyStoreTest.test_concurrent_saves`

**Quellcode:** [test_strategy_store.py:99–103](src/tests/test_strategy_store.py#L99-L103).

```python
def test_concurrent_saves(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(sorted(versions), list(range(1, 9)))`
- `self.assertEqual(len(self.store.list_versions()), 8)`

**Relevante Aufrufe:** `ThreadPoolExecutor`, `pool.map`, `self.store.list_versions`, `sorted`.

#### `StrategyStoreTest.test_orphan_version`

**Quellcode:** [test_strategy_store.py:105–111](src/tests/test_strategy_store.py#L105-L111).

```python
def test_orphan_version(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(self.save(), 3)`
- `self.assertFalse(self.store.exists(2))`
- `self.assertEqual(len(self.store.list_versions()), 2)`

**Relevante Aufrufe:** `orphan.write_text`, `self.save`, `self.store.exists`, `self.store.list_versions`.

---

## tests-test-strategy-validation

**Modul:** [`src/tests/test_strategy_validation.py`](src/tests/test_strategy_validation.py)  
**Features/Storys:** F-02, H-03  
**Aufgabe und Abgrenzung:** Unabhängige Validierung, zertifizierte Freigabe, Rollback und einseitiger Resume; synthetische Blob-Downloads in Chromium.

**Direkte Abhängigkeiten:** `import copy`; `import hashlib`; `import json`; `import tempfile`; `import unittest`; `from TestRunner import TestRunner`; `from pathlib import Path`; `from unittest.mock import patch`; `from uuid import uuid4`; `from playwright.async_api import Page`; `from ExecutionPolicy import ExecutionPolicy`; `from StrategyStore import StrategyStore, content_digest`; `from StrategyValidator import StrategyValidator`; `from ResumePlanner import ResumePlanner`; `from StructureVerifier import replace_locator, css_spec`; `from test_recovery_manager import STRATEGY, START, PARAMETERS, EXPECTED, EXECUTABLE`.

**Definitionen:** 1 Klassen, 19 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `REFERENCE`.

#### `fixture`

**Quellcode:** [test_strategy_validation.py:26–36](src/tests/test_strategy_validation.py#L26-L36).

```python
def fixture(row='old-row', numbers=(1, 2, 3), wrong_file=False, missing=False):
```

**Aufgabe:** Erzeugt das synthetische HTML bzw. die Testdaten für das im Modul beschriebene Szenario; Varianten simulieren Fehler oder Zustandsänderungen.

**Parameter:** `row`: Locator bzw. Datensatzzeile im aktuellen Kontext. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `'<html><body><label>Query<input></label><button onclick="document.querySelector(\'table\').hidden=false">Search</button><table hidden data-testid="old-table"><tbody>' + data + '</tbody></ta…`.

**Relevante Aufrufe:** `"<script>function getFile(n,kind) {\n        let a=document.createElement('a'), ext=kind==='CD'?'pdf':'xml';\n        a.href=URL.createObjectURL(new Blob([kind==='CD'?'%PDF-1.4\\n%%EOF':'<register>'+n+'</register>']));\n        a.download=(WRONG?999:n)+'-'+kind+'.'+ext; a.click(); }</script>".replace`, `''.join`, `str(wrong_file).lower`.

### Klasse `ValidationTests`

**Quellcode:** [test_strategy_validation.py:39–207](src/tests/test_strategy_validation.py#L39-L207).

**Aufgabe:** TestCase für Unabhängige Validierung, zertifizierte Freigabe, Rollback und einseitiger Resume; synthetische Blob-Downloads in Chromium.

**Basisklassen:** `unittest.IsolatedAsyncioTestCase`.

#### `ValidationTests.asyncSetUp`

**Quellcode:** [test_strategy_validation.py:40–55](src/tests/test_strategy_validation.py#L40-L55).

```python
async def asyncSetUp(self):
```

**Aufgabe:** Bereitet isolierte asynchrone Test-Fixture vor; registriert Cleanup und gegebenenfalls Browser-/Netzwerk-Mocks.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.root`, `self.store`, `self.policy`, `self.html`, `self.gotos`, `self.validator`.

**Relevante Aufrufe:** `ExecutionPolicy`, `StrategyStore`, `StrategyValidator`, `copy.deepcopy`, `fixture`, `patch`, `patch.object`, `patcher.start`, `self.store.save`.

#### `ValidationTests.asyncSetUp.goto`

**Quellcode:** [test_strategy_validation.py:48–50](src/tests/test_strategy_validation.py#L48-L50).

```python
async def goto(page, url, **kwargs):
```

**Aufgabe:** Ersetzt echte Navigation durch lokale synthetische HTML-Seite; Varianten und Zähler entsprechen der umgebenden Fixture.

**Parameter:** `page`: Browser-Page oder Seitennummer gemäß Funktionszweck; `url`: zu prüfende URL; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.gotos`.

**Relevante Aufrufe:** `page.set_content`.

#### `ValidationTests.validate`

**Quellcode:** [test_strategy_validation.py:57–58](src/tests/test_strategy_validation.py#L57-L58).

```python
async def validate(self, version=1, downloads=True, reference=None):
```

**Aufgabe:** Ruft Validator mit synthetischer Referenz und expliziten Testautorisierungen auf.

**Parameter:** `version`: Strategieversionsnummer; `downloads`: Dokumentdownload aktivieren; `reference`: unabhängige Referenzdaten. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `await self.validator.validate(version, reference or REFERENCE, authorized=True, downloads_authorized=downloads)`.

**Relevante Aufrufe:** `self.validator.validate`.

#### `ValidationTests.test_full_validation_and_activation`

**Quellcode:** [test_strategy_validation.py:60–69](src/tests/test_strategy_validation.py#L60-L69).

```python
async def test_full_validation_and_activation(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'passed', result)`
- `self.assertEqual(self.gotos, 2)`
- `self.assertEqual(self.store.load(1)['metadata']['status'], 'validated')`
- `self.assertIsNone(self.store.load_active())`
- `self.assertEqual((loaded['metadata']['strategy_version'], revision), (1, 1))`
- `self.assertEqual(result['checks'][1]['execution']['metrics']['documents_downloaded'], 2)`

**Relevante Aufrufe:** `self.store.certified_active`, `self.store.load`, `self.store.load_active`, `self.store.promote_certified`, `self.validate`.

#### `ValidationTests.test_partial_no_certification`

**Quellcode:** [test_strategy_validation.py:71–77](src/tests/test_strategy_validation.py#L71-L77).

```python
async def test_partial_no_certification(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'partial', result)`
- `self.assertEqual(self.store.load(1)['metadata']['status'], 'candidate')`
- `self.assertRaises(ValueError)`
- `self.assertEqual(sum((c['execution']['metrics']['download_attempts'] for c in result['checks'])), 0)`

**Relevante Aufrufe:** `self.store.load`, `self.store.promote_certified`, `self.validate`.

#### `ValidationTests.test_mismatch_before_download`

**Quellcode:** [test_strategy_validation.py:79–84](src/tests/test_strategy_validation.py#L79-L84).

```python
async def test_mismatch_before_download(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.html`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed')`
- `self.assertEqual(result['checks'][0]['execution']['metrics']['download_attempts'], 0)`
- `self.assertEqual(self.gotos, 1)`

**Relevante Aufrufe:** `fixture`, `self.validate`.

#### `ValidationTests.test_missing_document_control`

**Quellcode:** [test_strategy_validation.py:86–90](src/tests/test_strategy_validation.py#L86-L90).

```python
async def test_missing_document_control(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.html`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed')`
- `self.assertEqual(result['checks'][0]['execution']['metrics']['download_attempts'], 0)`

**Relevante Aufrufe:** `fixture`, `self.validate`.

#### `ValidationTests.test_wrong_filename`

**Quellcode:** [test_strategy_validation.py:92–97](src/tests/test_strategy_validation.py#L92-L97).

```python
async def test_wrong_filename(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.html`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed')`
- `self.assertIn('identity mismatch', result['reason'])`
- `self.assertEqual(self.store.load(1)['metadata']['status'], 'candidate')`

**Relevante Aufrufe:** `fixture`, `self.store.load`, `self.validate`.

#### `ValidationTests.test_missing_authorization_and_reference`

**Quellcode:** [test_strategy_validation.py:99–104](src/tests/test_strategy_validation.py#L99-L104).

```python
async def test_missing_authorization_and_reference(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValueError)`
- `self.assertEqual(self.gotos, 0)`

**Relevante Aufrufe:** `self.validate`, `self.validator.validate`.

#### `ValidationTests.test_rollback_and_stale_generation`

**Quellcode:** [test_strategy_validation.py:106–121](src/tests/test_strategy_validation.py#L106-L121).

```python
async def test_rollback_and_stale_generation(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((await self.validate())['status'], 'passed')`
- `self.assertEqual((await self.validate(2))['status'], 'passed')`
- `self.assertEqual((await self.validate(3))['status'], 'passed')`
- `self.assertRaises(ValueError)`
- `self.assertEqual((await self.validate(1))['status'], 'passed')`
- `self.assertEqual(self.store.load(2)['metadata']['status'], 'invalidated')`
- `self.assertEqual(self.store.certified_active()[0]['metadata']['strategy_version'], 1)`

**Relevante Aufrufe:** `self.store.certified_active`, `self.store.load`, `self.store.promote_certified`, `self.store.save`, `self.validate`.

#### `ValidationTests.test_tampered_evidence_and_strategy`

**Quellcode:** [test_strategy_validation.py:123–135](src/tests/test_strategy_validation.py#L123-L135).

```python
async def test_tampered_evidence_and_strategy(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaises(ValueError)`

**Relevante Aufrufe:** `copy.deepcopy`, `json.loads`, `path.read_text`, `path.write_text`, `self.store._version_path`, `self.store._write`, `self.store.load`, `self.store.promote_certified`, `self.validate`.

#### `ValidationTests.test_failed_revalidation_revokes_prior_approval`

**Quellcode:** [test_strategy_validation.py:137–143](src/tests/test_strategy_validation.py#L137-L143).

```python
async def test_failed_revalidation_revokes_prior_approval(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.html`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((await self.validate())['status'], 'passed')`
- `self.assertEqual((await self.validate())['status'], 'failed')`
- `self.assertEqual(self.store.load(1)['metadata']['status'], 'candidate')`
- `self.assertRaises(ValueError)`

**Relevante Aufrufe:** `fixture`, `self.store.load`, `self.store.promote_certified`, `self.validate`.

#### `ValidationTests.test_old_validation_attempt_cannot_certify`

**Quellcode:** [test_strategy_validation.py:145–152](src/tests/test_strategy_validation.py#L145-L152).

```python
async def test_old_validation_attempt_cannot_certify(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(first['status'], 'passed')`
- `self.assertRaises(ValueError)`

**Relevante Aufrufe:** `content_digest`, `self.store.begin_validation`, `self.store.certify`, `self.store.promote_certified`, `self.validate`.

#### `ValidationTests.prepare_resume`

**Quellcode:** [test_strategy_validation.py:154–176](src/tests/test_strategy_validation.py#L154-L176).

```python
async def prepare_resume(self):
```

**Aufgabe:** Erzeugt/validiert neue Teststrategie, aktiviert sie und bereitet Report/Dateien für die Wiederaufnahmeprüfung vor.

**Rückgabe (Ausdrücke im Code):** `(ResumePlanner(self.store, self.root / 'documents'), source, file)`.

**Direkt gesetzter Zustand:** `self.html`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((await self.validate(2))['status'], 'passed')`

**Relevante Aufrufe:** `ResumePlanner`, `content_digest`, `css_spec`, `file.read_bytes`, `file.stat`, `file.write_bytes`, `fixture`, `hashlib.sha256`, `hashlib.sha256(file.read_bytes()).hexdigest`, `replace_locator`, `self.store.promote_certified`, `self.store.save`, `self.validate`, `source_root.mkdir`.

#### `ValidationTests.test_resume_retains_and_downloads_only_pending`

**Quellcode:** [test_strategy_validation.py:178–188](src/tests/test_strategy_validation.py#L178-L188).

```python
async def test_resume_retains_and_downloads_only_pending(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((plan['status'], plan['retained_documents'], plan['pending_documents']), ('ready', 1, 1), plan)`
- `self.assertEqual(result['status'], 'completed', result)`
- `self.assertEqual(result['metrics']['download_attempts'], 1)`
- `self.assertEqual([d['download_status'] for d in result['companies'][0]['documents']], ['retained', 'downloaded'])`
- `self.assertTrue(file.exists())`
- `self.assertRaises(FileExistsError)`

**Relevante Aufrufe:** `file.exists`, `planner.build`, `planner.execute`, `self.prepare_resume`.

#### `ValidationTests.test_resume_blocks_corruption_and_server_error`

**Quellcode:** [test_strategy_validation.py:190–195](src/tests/test_strategy_validation.py#L190-L195).

```python
async def test_resume_blocks_corruption_and_server_error(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(planner.build(server)['status'], 'blocked')`
- `self.assertEqual(planner.build(source)['status'], 'blocked')`

**Relevante Aufrufe:** `file.write_bytes`, `planner.build`, `self.prepare_resume`.

#### `ValidationTests.test_resume_preflight_mismatch`

**Quellcode:** [test_strategy_validation.py:197–202](src/tests/test_strategy_validation.py#L197-L202).

```python
async def test_resume_preflight_mismatch(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.html`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result['status'], 'failed')`
- `self.assertEqual(result['metrics']['download_attempts'], 0)`

**Relevante Aufrufe:** `fixture`, `planner.execute`, `self.prepare_resume`.

#### `ValidationTests.test_resume_uncertain_attempt`

**Quellcode:** [test_strategy_validation.py:204–207](src/tests/test_strategy_validation.py#L204-L207).

```python
async def test_resume_uncertain_attempt(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(planner.build(source)['status'], 'blocked')`

**Relevante Aufrufe:** `planner.build`, `self.prepare_resume`.

---

## tests-test-test-runner

**Modul:** [`src/tests/test_test_runner.py`](src/tests/test_test_runner.py)  
**Features/Storys:** F-07  
**Aufgabe und Abgrenzung:** Prüft Runner selbst mit künstlichen erfolgreichen, fehlerhaften, übersprungenen und erwartbar fehlschlagenden Testfällen.

**Direkte Abhängigkeiten:** `import io`; `import unittest`; `from TestRunner import TestRunner`.

**Definitionen:** 5 Klassen, 15 Funktionen/Methoden (inkl. lokaler Definitionen).

### Klasse `ProgressTests`

**Quellcode:** [test_test_runner.py:7–79](src/tests/test_test_runner.py#L7-L79).

**Aufgabe:** TestCase für Prüft Runner selbst mit künstlichen erfolgreichen, fehlerhaften, übersprungenen und erwartbar fehlschlagenden Testfällen.

**Basisklassen:** `unittest.TestCase`.

#### `ProgressTests.execute`

**Quellcode:** [test_test_runner.py:8–12](src/tests/test_test_runner.py#L8-L12).

```python
def execute(self, case):
```

**Aufgabe:** Führt den im Modul vorgesehenen Testablauf mit den übergebenen Fixture-Optionen aus und liefert Ergebnis bzw. Runner-Ausgabe.

**Rückgabe (Ausdrücke im Code):** `(result, stream.getvalue())`.

**Relevante Aufrufe:** `TestRunner`, `TestRunner(stream=stream).run`, `io.StringIO`, `stream.getvalue`, `unittest.defaultTestLoader.loadTestsFromTestCase`.

#### `ProgressTests.test_success_failure_error_skip_expected_and_unexpected`

**Quellcode:** [test_test_runner.py:14–42](src/tests/test_test_runner.py#L14-L42).

```python
def test_success_failure_error_skip_expected_and_unexpected(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result.testsRun, 6)`
- `self.assertEqual(result.outcomes, dict(ok=1, failed=3, skipped=1, expected_failure=1))`
- `self.assertFalse(result.wasSuccessful())`
- `self.assertIn('NICHT OK         :     3', output)`
- `self.assertIn('Traceback', output)`

**Relevante Aufrufe:** `result.wasSuccessful`, `self.execute`.

### Klasse `ProgressTests.test_success_failure_error_skip_expected_and_unexpected.Cases`

**Quellcode:** [test_test_runner.py:15–35](src/tests/test_test_runner.py#L15-L35).

**Aufgabe:** Lokale unittest.TestCase-Klasse mit absichtlich erzeugten Ergebnissen; wird vom umgebenden Runner-Selbsttest ausgeführt, nicht als eigener regulärer Fachtest verwendet.

**Basisklassen:** `unittest.TestCase`.

#### `ProgressTests.test_success_failure_error_skip_expected_and_unexpected.Cases.test_ok`

**Quellcode:** [test_test_runner.py:16–17](src/tests/test_test_runner.py#L16-L17).

```python
def test_ok(self):
```

**Aufgabe:** Erzeugt gezielt den im Namen bezeichneten unittest-Zustand, damit der übergeordnete Runner-Test dessen Auswertung prüfen kann.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

#### `ProgressTests.test_success_failure_error_skip_expected_and_unexpected.Cases.test_failed`

**Quellcode:** [test_test_runner.py:19–20](src/tests/test_test_runner.py#L19-L20).

```python
def test_failed(self):
```

**Aufgabe:** Erzeugt gezielt den im Namen bezeichneten unittest-Zustand, damit der übergeordnete Runner-Test dessen Auswertung prüfen kann.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.fail('intentional')`

**Relevante Aufrufe:** `self.fail`.

#### `ProgressTests.test_success_failure_error_skip_expected_and_unexpected.Cases.test_error`

**Quellcode:** [test_test_runner.py:22–23](src/tests/test_test_runner.py#L22-L23).

```python
def test_error(self):
```

**Aufgabe:** Erzeugt gezielt den im Namen bezeichneten unittest-Zustand, damit der übergeordnete Runner-Test dessen Auswertung prüfen kann.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `RuntimeError('intentional')`

**Relevante Aufrufe:** `RuntimeError`.

#### `ProgressTests.test_success_failure_error_skip_expected_and_unexpected.Cases.test_skipped`

**Quellcode:** [test_test_runner.py:26–27](src/tests/test_test_runner.py#L26-L27).

```python
@unittest.skip('intentional')
def test_skipped(self):
```

**Aufgabe:** Erzeugt gezielt den im Namen bezeichneten unittest-Zustand, damit der übergeordnete Runner-Test dessen Auswertung prüfen kann.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `unittest.skip`.

#### `ProgressTests.test_success_failure_error_skip_expected_and_unexpected.Cases.test_expected_failure`

**Quellcode:** [test_test_runner.py:30–31](src/tests/test_test_runner.py#L30-L31).

```python
@unittest.expectedFailure
def test_expected_failure(self):
```

**Aufgabe:** Erzeugt gezielt den im Namen bezeichneten unittest-Zustand, damit der übergeordnete Runner-Test dessen Auswertung prüfen kann.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.fail('intentional')`

**Relevante Aufrufe:** `self.fail`.

#### `ProgressTests.test_success_failure_error_skip_expected_and_unexpected.Cases.test_unexpected_success`

**Quellcode:** [test_test_runner.py:34–35](src/tests/test_test_runner.py#L34-L35).

```python
@unittest.expectedFailure
def test_unexpected_success(self):
```

**Aufgabe:** Erzeugt gezielt den im Namen bezeichneten unittest-Zustand, damit der übergeordnete Runner-Test dessen Auswertung prüfen kann.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

#### `ProgressTests.test_failed_subtests_count_once`

**Quellcode:** [test_test_runner.py:44–55](src/tests/test_test_runner.py#L44-L55).

```python
def test_failed_subtests_count_once(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(len(result.failures), 3)`
- `self.assertEqual(result.testsRun, 1)`
- `self.assertEqual(result.outcomes['failed'], 1)`
- `self.assertIn('NICHT OK         :     1', output)`

**Relevante Aufrufe:** `self.execute`.

### Klasse `ProgressTests.test_failed_subtests_count_once.Cases`

**Quellcode:** [test_test_runner.py:45–49](src/tests/test_test_runner.py#L45-L49).

**Aufgabe:** Lokale unittest.TestCase-Klasse mit absichtlich erzeugten Ergebnissen; wird vom umgebenden Runner-Selbsttest ausgeführt, nicht als eigener regulärer Fachtest verwendet.

**Basisklassen:** `unittest.TestCase`.

#### `ProgressTests.test_failed_subtests_count_once.Cases.test_subtests`

**Quellcode:** [test_test_runner.py:46–49](src/tests/test_test_runner.py#L46-L49).

```python
def test_subtests(self):
```

**Aufgabe:** Erzeugt gezielt den im Namen bezeichneten unittest-Zustand, damit der übergeordnete Runner-Test dessen Auswertung prüfen kann.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(i, 3)`

#### `ProgressTests.test_fixture_error_reported_separately`

**Quellcode:** [test_test_runner.py:57–70](src/tests/test_test_runner.py#L57-L70).

```python
def test_fixture_error_reported_separately(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result.testsRun, 0)`
- `self.assertEqual(result.fixture_errors, 1)`
- `self.assertFalse(result.wasSuccessful())`
- `self.assertIn('Fixture-Fehler   :     1', output)`

**Relevante Aufrufe:** `result.wasSuccessful`, `self.execute`.

### Klasse `ProgressTests.test_fixture_error_reported_separately.Cases`

**Quellcode:** [test_test_runner.py:58–64](src/tests/test_test_runner.py#L58-L64).

**Aufgabe:** Lokale unittest.TestCase-Klasse mit absichtlich erzeugten Ergebnissen; wird vom umgebenden Runner-Selbsttest ausgeführt, nicht als eigener regulärer Fachtest verwendet.

**Basisklassen:** `unittest.TestCase`.

#### `ProgressTests.test_fixture_error_reported_separately.Cases.setUpClass`

**Quellcode:** [test_test_runner.py:60–61](src/tests/test_test_runner.py#L60-L61).

```python
@classmethod
def setUpClass(cls):
```

**Aufgabe:** Initialisiert klassenweit benötigte Testressourcen bzw. absichtlich fehlerhafte Fixture im Runner-Selbsttest.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Explizite Fehler / Abbruch:**

- `RuntimeError('intentional')`

**Relevante Aufrufe:** `RuntimeError`.

#### `ProgressTests.test_fixture_error_reported_separately.Cases.test_not_run`

**Quellcode:** [test_test_runner.py:63–64](src/tests/test_test_runner.py#L63-L64).

```python
def test_not_run(self):
```

**Aufgabe:** Erzeugt gezielt den im Namen bezeichneten unittest-Zustand, damit der übergeordnete Runner-Test dessen Auswertung prüfen kann.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

#### `ProgressTests.test_skipped_subtest_not_counted_as_passed`

**Quellcode:** [test_test_runner.py:72–79](src/tests/test_test_runner.py#L72-L79).

```python
def test_skipped_subtest_not_counted_as_passed(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(result.outcomes, dict(skipped=1))`

**Relevante Aufrufe:** `self.execute`.

### Klasse `ProgressTests.test_skipped_subtest_not_counted_as_passed.Cases`

**Quellcode:** [test_test_runner.py:73–76](src/tests/test_test_runner.py#L73-L76).

**Aufgabe:** Lokale unittest.TestCase-Klasse mit absichtlich erzeugten Ergebnissen; wird vom umgebenden Runner-Selbsttest ausgeführt, nicht als eigener regulärer Fachtest verwendet.

**Basisklassen:** `unittest.TestCase`.

#### `ProgressTests.test_skipped_subtest_not_counted_as_passed.Cases.test_subtest_skip`

**Quellcode:** [test_test_runner.py:74–76](src/tests/test_test_runner.py#L74-L76).

```python
def test_subtest_skip(self):
```

**Aufgabe:** Erzeugt gezielt den im Namen bezeichneten unittest-Zustand, damit der übergeordnete Runner-Test dessen Auswertung prüfen kann.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `self.skipTest`.

---

## tests-test-worker-pool

**Modul:** [`src/tests/test_worker_pool.py`](src/tests/test_worker_pool.py)  
**Features/Storys:** C-07, E-03  
**Aufgabe und Abgrenzung:** Async-Worker-Pool mit realem Chromium und simulierten Seiten/Blob-Downloads; explizite Strategie-Fixture, kein Live-Test.

**Direkte Abhängigkeiten:** `import json`; `import sys`; `import tempfile`; `import unittest`; `from TestRunner import TestRunner`; `from pathlib import Path`; `from unittest.mock import patch`; `from types import SimpleNamespace`; `from playwright.async_api import async_playwright`; `from AsyncStrategyExecutor import AsyncStrategyExecutor, ExecutionError, ServerResponseError`.

**Definitionen:** 1 Klassen, 17 Funktionen/Methoden (inkl. lokaler Definitionen).

**Modulweite Konfiguration / Verträge:** `START`, `RESULT`, `PARAMETERS`, `COOKIE`, `START_HTML`.

#### `result_html`

**Quellcode:** [test_worker_pool.py:32–49](src/tests/test_worker_pool.py#L32-L49).

```python
def result_html(numbers, invalid=False):
```

**Aufgabe:** Erzeugt synthetische Registerzeilen mit CD-/SI-Controls und optional ungültigen Dokumenten.

**Rückgabe (Ausdrücke im Code):** `'<html><body><table class="companyTable_companyTable__HtyK2"><tbody>' + ''.join(rows) + '</tbody></table><a href="#results2" onclick="nextPage()">Springe eine Seite weiter</a>' + script + '…`.

**Relevante Aufrufe:** `` "<script>function getFile(ext,num) { setTimeout(() => {\n        const value = ext === 'pdf' ? '%PDF-1.4\\n'+num+'\\n%%EOF' :\n          (INVALID && num===8165 ? '<html>error</html>' : '<register><number>'+num+'</number></register>');\n        const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([value]));\n        a.download=num+'.'+ext; a.click(); },300); }\n    function nextPage() { document.querySelectorAll('tbody b').forEach((e,i)=>e.textContent='Amtsgericht Hamburg HRB '+(700+i));\n    document.querySelectorAll('.row_row__kw5rN span').forEach((e,i)=>e.textContent='Firma '+(700+i));\n    document.querySelectorAll('tr[data-testid] button').forEach((e,i)=>e.setAttribute('onclick',\n      `getFile('${i%2?'xml':'pdf'}',${700+Math.floor(i/2)})`)); }</script>".replace ``, `''.join`, `str(invalid).lower`.

### Klasse `PoolTests`

**Quellcode:** [test_worker_pool.py:52–217](src/tests/test_worker_pool.py#L52-L217).

**Aufgabe:** TestCase für Async-Worker-Pool mit realem Chromium und simulierten Seiten/Blob-Downloads; explizite Strategie-Fixture, kein Live-Test.

**Basisklassen:** `unittest.IsolatedAsyncioTestCase`.

#### `PoolTests.asyncSetUp`

**Quellcode:** [test_worker_pool.py:53–124](src/tests/test_worker_pool.py#L53-L124).

```python
async def asyncSetUp(self):
```

**Aufgabe:** Bereitet isolierte asynchrone Test-Fixture vor; registriert Cleanup und gegebenenfalls Browser-/Netzwerk-Mocks.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.temp`, `self.pw`, `self.browser`, `self.context`, `self.result_requests`, `self.start_requests`, `self.mismatch`, `self.invalid`, `self.block`, `self.silent_worker`, `self.server_error`, `self.executor`.

**Relevante Aufrufe:** `AsyncStrategyExecutor`, `async_playwright`, `async_playwright().start`, `patch`, `patcher.start`, `real_new_page`, `self.browser.new_context`, `self.pw.chromium.launch`.

#### `PoolTests.asyncSetUp.fixture_start`

**Quellcode:** [test_worker_pool.py:78–84](src/tests/test_worker_pool.py#L78-L84).

```python
async def fixture_start(url, **kwargs):
```

**Aufgabe:** Simuliert Startseite und initiale Registerergebnisse; zählt Start-/Result-Requests.

**Parameter:** `url`: zu prüfende URL; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.start_requests`, `self.result_requests`.

**Relevante Aufrufe:** `START_HTML.replace`, `result_html`, `result_html((8165, 9999, 1234), self.invalid).replace`, `result_html((8165, 9999, 1234), self.invalid).replace('<html><body>', '').replace`, `self.executor.page.set_content`.

#### `PoolTests.asyncSetUp.new_worker_page`

**Quellcode:** [test_worker_pool.py:86–117](src/tests/test_worker_pool.py#L86-L117).

```python
async def new_worker_page():
```

**Aufgabe:** Erzeugt zusätzlichen Test-Worker-Tab und installiert gemockte Navigation und Ereignisse.

**Rückgabe (Ausdrücke im Code):** `page`.

**Relevante Aufrufe:** `real_new_page`.

#### `PoolTests.asyncSetUp.new_worker_page.fixture_goto`

**Quellcode:** [test_worker_pool.py:88–103](src/tests/test_worker_pool.py#L88-L103).

```python
async def fixture_goto(url, **kwargs):
```

**Aufgabe:** Simuliert Worker-Ergebnisse, zweite Seite, abweichende Treffer oder Zugriffssperre.

**Parameter:** `url`: zu prüfende URL; `kwargs`: zusätzliche Schlüsselwortparameter gemäß aufgerufener Schnittstelle. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe (Ausdrücke im Code):** `None`.

**Direkt gesetzter Zustand:** `self.result_requests`.

**Relevante Aufrufe:** `SimpleNamespace`, `html.replace`, `page.set_content`, `result_html`, `self.executor._response`, `url.endswith`.

#### `PoolTests.asyncSetUp.new_worker_page.on`

**Quellcode:** [test_worker_pool.py:107–114](src/tests/test_worker_pool.py#L107-L114).

```python
def on(event, handler):
```

**Aufgabe:** Erweitert synthetische Ereignisregistrierung um 5xx-Simulation.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `original_on`.

#### `PoolTests.asyncSetUp.new_worker_page.on.server_response`

**Quellcode:** [test_worker_pool.py:110–113](src/tests/test_worker_pool.py#L110-L113).

```python
def server_response(message):
```

**Aufgabe:** Übersetzt definierte Testdialog-Nachricht in gemockten HTTP-500-Response.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `SimpleNamespace`, `handler`.

#### `PoolTests.asyncSetUp.navigate`

**Quellcode:** [test_worker_pool.py:121–123](src/tests/test_worker_pool.py#L121-L123).

```python
async def navigate(url):
```

**Aufgabe:** Verkettet simulierte Startseitennavigation mit realer Executor-Navigationslogik.

**Parameter:** `url`: zu prüfende URL. Die vollständige Signatur oben enthält auch alle Defaults.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Relevante Aufrufe:** `fixture_start`, `original`.

#### `PoolTests.test_two_workers`

**Quellcode:** [test_worker_pool.py:126–138](src/tests/test_worker_pool.py#L126-L138).

```python
async def test_two_workers(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual(await e._collect(3, 1, True), 'company_limit')`
- `self.assertEqual(e.max_parallel_jobs, 2)`
- `self.assertEqual(e.worker_tabs_opened, 1)`
- `self.assertEqual((self.start_requests, self.result_requests, e.download_attempts), (1, 2, 6))`
- `self.assertEqual(len(self.context.pages), 1)`
- `self.assertEqual(doc['download_status'], 'downloaded')`
- `self.assertIn(company['register_number'].encode(), Path(doc['file_path']).read_bytes())`

**Relevante Aufrufe:** `Path(doc['file_path']).read_bytes`, `company['register_number'].encode`, `e._collect`, `e._navigate`.

#### `PoolTests.test_mismatch`

**Quellcode:** [test_worker_pool.py:140–147](src/tests/test_worker_pool.py#L140-L147).

```python
async def test_mismatch(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.mismatch`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ExecutionError, 'did not reproduce')`
- `self.assertEqual(self.executor.download_attempts, 0)`
- `self.assertEqual(len(self.context.pages), 1)`

**Relevante Aufrufe:** `self.executor._collect`, `self.executor._navigate`.

#### `PoolTests.test_rate_limit`

**Quellcode:** [test_worker_pool.py:149–155](src/tests/test_worker_pool.py#L149-L155).

```python
async def test_rate_limit(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.block`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ExecutionError, '429')`
- `self.assertEqual(self.executor.download_attempts, 0)`

**Relevante Aufrufe:** `self.executor._collect`, `self.executor._navigate`.

#### `PoolTests.test_invalid_xml`

**Quellcode:** [test_worker_pool.py:157–164](src/tests/test_worker_pool.py#L157-L164).

```python
async def test_invalid_xml(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.invalid`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ExecutionError, 'Invalid or unsafe XML')`
- `self.assertEqual(self.executor.companies[0]['documents'][1]['download_status'], 'failed')`
- `self.assertFalse(list(Path(self.temp.name).glob('*.part')))`

**Relevante Aufrufe:** `Path(self.temp.name).glob`, `self.executor._collect`, `self.executor._navigate`.

#### `PoolTests.test_one_worker`

**Quellcode:** [test_worker_pool.py:166–170](src/tests/test_worker_pool.py#L166-L170).

```python
async def test_one_worker(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((self.executor.worker_tabs_opened, self.executor.max_parallel_jobs), (0, 1))`
- `self.assertEqual((self.result_requests, self.executor.download_attempts), (1, 4))`

**Relevante Aufrufe:** `self.executor._collect`, `self.executor._navigate`.

#### `PoolTests.test_two_pages`

**Quellcode:** [test_worker_pool.py:172–177](src/tests/test_worker_pool.py#L172-L177).

```python
async def test_two_pages(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertEqual((self.executor.pages, self.executor.download_attempts), (2, 10))`
- `self.assertEqual([c['register_number'] for c in self.executor.companies], ['8165', '9999', '1234', '700', '701'])`

**Relevante Aufrufe:** `self.executor._collect`, `self.executor._navigate`.

#### `PoolTests.test_worker_timeout_diagnostics`

**Quellcode:** [test_worker_pool.py:179–195](src/tests/test_worker_pool.py#L179-L195).

```python
async def test_worker_timeout_diagnostics(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.silent_worker`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ExecutionError, 'Worker 2, job step')`
- `self.assertEqual(len(e.worker_failures), 1)`
- `self.assertEqual((failure['worker_id'], failure['key'][-1], failure['document_type']), (2, '9999', 'CD'))`
- `self.assertIn('Download unavailable', ' '.join(failure['notifications']))`
- `self.assertIn('Firma 9999', failure['row_snapshot'])`
- `self.assertIsNone(failure['access_restriction'])`
- `self.assertEqual(e.companies[1]['documents'][0]['download_status'], 'failed')`
- `self.assertEqual(e.companies[1]['documents'][1]['download_status'], 'not_attempted')`
- `self.assertEqual(len(self.context.pages), 1)`

**Relevante Aufrufe:** `' '.join`, `e._collect`, `e._navigate`.

#### `PoolTests.test_server_error_stops_without_timeout`

**Quellcode:** [test_worker_pool.py:197–213](src/tests/test_worker_pool.py#L197-L213).

```python
async def test_server_error_stops_without_timeout(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Direkt gesetzter Zustand:** `self.server_error`.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ExecutionError, 'HTTP 500')`
- `self.assertEqual(len(e.worker_failures), 1)`
- `self.assertEqual(failure['error_type'], 'ServerResponseError')`
- `self.assertEqual(failure['server_error']['status'], 500)`
- `self.assertEqual(failure['worker_id'], 2)`
- `self.assertLess(next((j['duration_seconds'] for j in e.worker_jobs if j['status'] == 'failed')), 10)`
- `self.assertEqual(e.companies[1]['documents'][0]['download_status'], 'failed')`
- `self.assertEqual(e.companies[1]['documents'][1]['download_status'], 'not_attempted')`
- `self.assertNotIn('downloaded', [doc['download_status'] for doc in e.companies[2]['documents']])`

**Relevante Aufrufe:** `e._collect`, `e._navigate`, `next`.

#### `PoolTests.test_requires_authorization`

**Quellcode:** [test_worker_pool.py:215–217](src/tests/test_worker_pool.py#L215-L217).

```python
async def test_requires_authorization(self):
```

**Aufgabe:** Prüft das durch den Testnamen definierte Szenario anhand der unten aufgeführten konkreten Sollbedingungen.

**Rückgabe:** regulär `None`; Ergebnis ggf. über Zustand, Ausgabe oder Exception.

**Konkrete Sollbedingungen (Assertions):**

- `self.assertRaisesRegex(ValueError, 'authorization')`

**Relevante Aufrufe:** `self.executor.run`.

---

## Vollständigkeitskontrolle und Pflege

Erfasste AST-Definitionen: 579. Alle 48 Python-Dateien aus dem konsolidierten Quellarchiv sind in der Referenz enthalten. Mehrfach definierte gleichnamige Methoden (z. B. Properties und lokale Testklassen) werden anhand der Quellposition getrennt erfasst.

Die Referenz ist auf diesen konkreten Quellstand bezogen. Nach Codeänderungen sind insbesondere Signaturen, Parameterverträge, Ausgaben, Fehlerzustände, Seiteneffekte, Abhängigkeiten, Tests und Quellverweise erneut abzugleichen. Quellcode ist die technische Wahrheit; geplante Änderungen gehören in die README-Roadmap, bis sie implementiert sind.

Keine Live-Anfrage, kein Testlauf und keine Änderung an Code, Strategien oder historischen Daten erfolgte zur Erstellung dieser Referenz. Die statische Inventarisierung garantiert die Erfassung der Definitionen, nicht die Fehlerfreiheit ihrer Implementierung.
