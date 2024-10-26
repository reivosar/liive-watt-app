import unittest
from unittest.mock import MagicMock
from app.jobs.electricity_data_import.data_extractor import DataExtractor

class TestIsValidSheet(unittest.TestCase):
    def setUp(self):
        self.extractor = DataExtractor()

    def test_is_valid_sheet_for_3_2_H_file(self):
        # Given
        file_name = "3-2-H28.xlsx"
        sheet_name = "H28.4"

        # When
        is_valid = self.extractor.is_valid_sheet(file_name, sheet_name)

        # Then
        self.assertTrue(is_valid)

    def test_is_valid_sheet_for_20_file(self):
        # Given
        file_name = "2020.xlsx"
        sheet_name = "2020.4"

        # When
        is_valid = self.extractor.is_valid_sheet(file_name, sheet_name)

        # Then
        self.assertTrue(is_valid)

    def test_is_valid_sheet_invalid(self):
        # Given
        file_name = "2020.xlsx"
        sheet_name = "InvalidSheet"

        # When
        is_valid = self.extractor.is_valid_sheet(file_name, sheet_name)

        # Then
        self.assertFalse(is_valid)

class TestGetYearWithMonthFromSheetName(unittest.TestCase):
    def setUp(self):
        self.extractor = DataExtractor()

    def test_get_year_with_valid_heisei_sheet(self):
        # Given
        sheet_name = "H28.4"

        # When
        year, month = self.extractor.get_year_with_month_from_sheet_name(sheet_name)

        # Then
        self.assertEqual(year, 2016)
        self.assertEqual(month, 4)

    def test_get_year_with_valid_gregorian_sheet(self):
        # Given
        sheet_name = "2020.4"

        # When
        year, month = self.extractor.get_year_with_month_from_sheet_name(sheet_name)

        # Then
        self.assertEqual(year, 2020)
        self.assertEqual(month, 4)

    def test_get_year_with_invalid_sheet_name(self):
        # Given
        sheet_name = "InvalidSheet"

        # When/Then
        with self.assertRaises(ValueError):
            self.extractor.get_year_with_month_from_sheet_name(sheet_name)

class TestProcessSheetData(unittest.TestCase):
    def setUp(self):
        self.mock_excel_reader = MagicMock()
        self.mock_excel_file = MagicMock()
        self.mock_excel_sheet = MagicMock()
        self.extractor = DataExtractor(excel_reader=self.mock_excel_reader)

    def test_process_sheet_data_with_valid_data(self):
        # Given
        self.mock_excel_sheet.iter_rows.return_value = iter([
            (0, ['北海道', 100, 10, 200, 20, 300, 30, 400, 40, 500, 50]),
            (1, ['沖縄県', 200, 20, 400, 40, 600, 60, 800, 80, 1000, 100])
        ])
        self.mock_excel_sheet.get_row.side_effect = lambda idx: [
            ['北海道', 100, 10, 200, 20, 300, 30, 400, 40, 500, 50],
            ['沖縄県', 200, 20, 400, 40, 600, 60, 800, 80, 1000, 100]
        ][idx]

        self.mock_excel_file.get_sheet.return_value = self.mock_excel_sheet
        self.mock_excel_reader.load_excel_file.return_value = self.mock_excel_file

        data = []

        # When
        self.extractor.process_sheet_data("file.xlsx", "H28.4", data)

        # Then
        self.assertEqual(len(data), 2) 
        
    def test_process_sheet_data_with_invalid_data(self):
        # Given
        self.mock_excel_sheet.iter_rows.return_value = iter([
            (0, ['Other Prefecture', 100, 10, 200, 20, 300, 30, 400, 40, 500, 50]),
            (1, ['Somewhere Else', 200, 20, 400, 40, 600, 60, 800, 80, 1000, 100])
        ])
        self.mock_excel_file.get_sheet.return_value = self.mock_excel_sheet
        self.mock_excel_reader.load_excel_file.return_value = self.mock_excel_file

        data = []

        # When/Then
        with self.assertRaises(ValueError):
            self.extractor.process_sheet_data("file.xlsx", "H28.4", data)

class TestParseRowData(unittest.TestCase):
    def setUp(self):
        self.extractor = DataExtractor()

    def test_parse_row_data_with_valid_data(self):
        # Given
        year = 2020
        month = 4
        row_data = ['北海道', 100, 10, 200, 20, 300, 30, 400, 40, 500, 50]

        # When
        result = self.extractor.parse_row_data(year, month, row_data)

        # Then
        self.assertEqual(result['year'], 2020)
        self.assertEqual(result['month'], 4)
        self.assertEqual(result['prefecture_name'], '北海道')

    def test_parse_row_data_with_invalid_data(self):
        # Given
        year = 2020
        month = 4
        row_data = ['北海道', 100]

        # When/Then
        with self.assertRaises(ValueError):
            self.extractor.parse_row_data(year, month, row_data)
