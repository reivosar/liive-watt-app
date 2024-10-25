import os
import shutil
from app.jobs.electricity_data_import.const import RAW_DIR, PROCESSED_DIR

class ProcessedFileHandler:
    
    def move_to_processed(self, filename):
        source = os.path.join(RAW_DIR, filename)
        destination = os.path.join(PROCESSED_DIR, filename)

        try:
            shutil.move(source, destination)
            print(f"Moved {filename} to {PROCESSED_DIR}")
            return True
        except Exception as e:
            print(f"Error moving {filename} to {PROCESSED_DIR}: {e}")
            return False
