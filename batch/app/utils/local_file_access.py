import os

class LocalFileAccess:
    def get_basename(self, path):
        return os.path.basename(path)

    def get_abspath(self, path):
        return os.path.abspath(path)

    def join_path(self, *paths):
        return os.path.join(*paths)

    def write_file(self, filepath, content):
        with open(filepath, 'wb') as file:
            file.write(content)
