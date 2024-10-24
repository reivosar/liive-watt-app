import os
from app.jobs.electricity_data_import.const import RAW_DIR, PROCESSED_DIR, LOG_DIR

class DataInitializer:
    def initialize(self):

        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir) 
        print(f"Current working directory: {os.getcwd()}") 

        os.makedirs(RAW_DIR, exist_ok=True)
        os.makedirs(PROCESSED_DIR, exist_ok=True)
        os.makedirs(LOG_DIR, exist_ok=True)