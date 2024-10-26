import os
import requests

from app.jobs.electricity_data_import.const import RAW_DIR, PROCESSED_DIR

from app.utils.local_file_reader import LocalFileReader
from app.utils.local_file_access import LocalFileAccess

class DataDownloader:
    def __init__(self, urls_file=None, request_handler=None, file_reader=None, file_access=None):
        self.file_reader = file_reader or LocalFileReader()
        self.file_access = file_access or LocalFileAccess()
        _urls_file = urls_file or self.file_access.join_path(os.path.dirname(__file__), 'urls.txt')
        self.urls = self.load_urls_from_file(_urls_file)
        self.request_handler = request_handler or requests

    def load_urls_from_file(self, urls_file):
        urls_file_path = self.file_access.get_abspath(urls_file)
        
        if not self.file_reader.file_exists(urls_file_path):
            raise FileNotFoundError(f"{urls_file_path} does not exist.")
        
        return self.file_reader.read_file(urls_file_path)

    def download_data(self):
        downloaded_file_names = []
        for url in self.urls:
            filename = self.file_access.get_basename(url)
            raw_filepath = self.file_access.join_path(RAW_DIR, filename)
            processed_filepath = self.file_access.join_path(PROCESSED_DIR, filename)

            if self.file_reader.file_exists(processed_filepath):
                print(f"File already processed: {processed_filepath}, skipping download.")
                continue

            try:
                response = self.request_handler.get(url)
                response.raise_for_status()

                self.file_access.write_file(raw_filepath, response.content)
                print(f"Downloaded: {raw_filepath}")

                downloaded_file_names.append(filename)

            except Exception as e:
                print(f"Error downloading {url}: {e}")

        return downloaded_file_names
