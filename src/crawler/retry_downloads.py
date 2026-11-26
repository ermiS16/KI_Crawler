from DocumentDownloader import DocumentDownloader

if __name__ == '__main__':
    downloader = DocumentDownloader()
    print('Imported:', downloader.import_failed())
    print(downloader.process_queue())
