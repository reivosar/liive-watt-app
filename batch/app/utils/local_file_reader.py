import os

class LocalFileReader:
    def file_exists(self, filepath):
        return os.path.exists(filepath)

    def read_file(self, filepath):
        with open(filepath, 'r') as file:
            return [line.strip() for line in file.readlines() if line.strip()]
