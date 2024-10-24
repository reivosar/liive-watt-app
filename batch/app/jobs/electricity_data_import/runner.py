from app.jobs.electricity_data_import.data_initializer import DataInitializer
from app.jobs.electricity_data_import.data_downloader import DataDownloader
from app.jobs.electricity_data_import.data_extractor import DataExtractor
from app.jobs.electricity_data_import.db_saver import DBSaver

class ElectricityDataImport:
    def __init__(self, initializer=None, downloader=None, extractor=None, saver=None):
        self.initializer = initializer or DataInitializer()
        self.downloader = downloader or DataDownloader()
        self.extractor = extractor or DataExtractor()
        self.saver = saver or DBSaver()

    def run(self):
        print("Starting the electricity import batch job.")
        try:
            self.initializer.initialize()
            self.downloader.download_data()
            extracted_data = self.extractor.extract_energy_usage_data()
            self.saver.save_to_db(extracted_data)
        finally:
            print("Finished the electricity import batch job.")