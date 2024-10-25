from app.jobs.electricity_data_import.data_initializer import DataInitializer
from app.jobs.electricity_data_import.data_downloader import DataDownloader
from app.jobs.electricity_data_import.data_extractor import DataExtractor
from app.jobs.electricity_data_import.db_saver import DBSaver
from app.jobs.electricity_data_import.processed_file_handler import ProcessedFileHandler

class ElectricityDataImport:
    def __init__(self, initializer=None, downloader=None, extractor=None, saver=None, processed_file_handler=None):
        self.initializer = initializer or DataInitializer()
        self.downloader = downloader or DataDownloader()
        self.extractor = extractor or DataExtractor()
        self.saver = saver or DBSaver()
        self.processed_file_handler = processed_file_handler or ProcessedFileHandler()

    def run(self):
        print("Starting the electricity import batch job.")
        try:
            self.initializer.initialize()
            downloaded_file_names = self.downloader.download_data()
            for file_name in downloaded_file_names:
                extracted_data = self.extractor.extract_energy_usage_data(file_name)
                if self.saver.save_to_db(extracted_data):
                    self.processed_file_handler.move_to_processed(file_name)
        finally:
            print("Finished the electricity import batch job.")