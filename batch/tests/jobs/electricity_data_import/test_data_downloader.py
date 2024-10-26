import unittest

from unittest.mock import MagicMock
from app.jobs.electricity_data_import.data_downloader import DataDownloader

class TestDataDownloader(unittest.TestCase):

    def setUp(self):
        self.mock_file_reader = MagicMock()
        self.mock_file_access = MagicMock()
        self.mock_requests = MagicMock()

        self.mock_file_reader.read_file.return_value = ["https://example.com/test.xlsx"]

        self.mock_file_access.join_path.side_effect = lambda *args: '/'.join(args)
        self.mock_file_access.get_basename.side_effect = lambda path: path.split('/')[-1]
        self.mock_file_access.get_abspath.side_effect = lambda path: f"/absolute/{path}"

        self.downloader = DataDownloader(
            file_reader=self.mock_file_reader, 
            file_access=self.mock_file_access, 
            request_handler=self.mock_requests
        )

    def test_download_data_when_file_already_processed_then_skip_download(self):
        # Given
        self.mock_file_reader.file_exists.side_effect = [True, True] 
        self.mock_requests.get.return_value.status_code = 200
        self.mock_requests.get.return_value.content = b"file content"
        
        # When
        result = self.downloader.download_data()

        # Then
        self.assertEqual(result, []) 

    def test_download_data_when_file_not_processed_then_download(self):
        # Given
        self.mock_file_reader.file_exists.side_effect = [False, False] 
        self.mock_requests.get.return_value.status_code = 200
        self.mock_requests.get.return_value.content = b"file content"

        # When
        result = self.downloader.download_data()

        # Then
        self.assertEqual(result, ['test.xlsx']) 

    def test_download_data_file_not_found_error(self):
        # Given
        self.mock_file_reader.file_exists.side_effect = [True, False]
        self.mock_requests.get.side_effect = Exception("File not found")

        # When
        result = self.downloader.download_data()

        # Then
        self.assertEqual(result, [])
