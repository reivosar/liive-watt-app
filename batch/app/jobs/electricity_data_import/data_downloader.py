import os
import requests

from app.jobs.electricity_data_import.const import RAW_DIR, PROCESSED_DIR

class DataDownloader:
    def __init__(self, urls_file=os.path.join(os.path.dirname(__file__), 'urls.txt')):
        self.urls = self.load_urls_from_file(urls_file)

    def load_urls_from_file(self, urls_file):
        urls_file_path = os.path.abspath(urls_file)
        
        if not os.path.exists(urls_file_path):
            raise FileNotFoundError(f"{urls_file_path} does not exist.")
        
        urls = []
        with open(urls_file_path, 'r') as file:
            urls = [line.strip() for line in file.readlines() if line.strip()]
        return urls

    def download_data(self):
        downloaded_file_names = []
        for url in self.urls:
            filename = os.path.basename(url)
            raw_filepath = os.path.join(RAW_DIR, filename)
            processed_filepath = os.path.join(PROCESSED_DIR, filename)

            if os.path.exists(processed_filepath):
                print(f"File already processed: {processed_filepath}, skipping download.")
                continue

            try:
                response = requests.get(url)
                response.raise_for_status()

                with open(raw_filepath, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded: {raw_filepath}")

                downloaded_file_names.append(filename)

            except Exception as e:
                print(f"Error downloading {url}: {e}")

        return downloaded_file_names
