from app.utils.local_file_reader import LocalFileReader
from app.utils.local_file_access import LocalFileAccess
from app.utils.excel_reader import ExcelReader

from app.jobs.electricity_data_import.const import RAW_DIR, HEISEI_START_YEAR

class DataExtractor:
    def __init__(self, file_reader=None, file_access=None, excel_reader=None):
        self.file_reader = file_reader or LocalFileReader()
        self.file_access = file_access or LocalFileAccess()
        self.excel_reader = excel_reader or ExcelReader()

    def extract_energy_usage_data(self, file_name):
        data = []
        try:
            sheet_names = self.get_sheet_names(file_name)
            self.process_sheets(file_name, sheet_names, data)
        except Exception as e:
            print(f"Error processing file {file_name}: {e}")
        return data

    def get_sheet_names(self, file_name):
        filepath = self.file_access.join_path(RAW_DIR, file_name)
        excel_file = self.excel_reader.load_excel_file(filepath)
        print(f"Available sheets in {file_name}: {excel_file.get_sheet_names()}")
        return excel_file.get_sheet_names()

    def process_sheets(self, file_name, sheet_names, data):
        for sheet in sheet_names:
            if self.is_valid_sheet(file_name, sheet):
                try:
                    self.process_sheet_data(file_name, sheet, data)
                except Exception as sheet_error:
                    print(f"Error processing sheet {sheet} in file {file_name}: {sheet_error}")

    def is_valid_sheet(self, file, sheet):
        if file.startswith("3-2-H"):
            return sheet.startswith("H") and sheet.find('.') > 0
        else:
            return sheet.startswith("20") and sheet.find('.') > 0

    def process_sheet_data(self, file_name, sheet, data):
        filepath = self.file_access.join_path(RAW_DIR, file_name)
        excel_file = self.excel_reader.load_excel_file(filepath)
        excel_data = excel_file.get_sheet(sheet_name=sheet)

        start_idx, end_idx = None, None

        prefecture_column_idx = self.find_prefecture_column(excel_data)
        
        for idx, row in excel_data.iter_rows():
            if row[prefecture_column_idx] == '北海道':
                start_idx = idx
            if row[prefecture_column_idx] == '沖縄県':
                end_idx = idx
                break
        
        if start_idx is None or end_idx is None:
            raise ValueError(f"Could not find start ('北海道') or end ('沖縄県') rows in sheet {sheet}")

        for idx in range(start_idx, end_idx + 1):
            row = excel_data.get_row(idx)
            row_data = ' '.join(str(cell) for cell in row[prefecture_column_idx:]).split()

            if len(row_data) < 11: 
                print(f"Invalid row data in sheet {sheet}: {row_data}")
                continue

            year, month = self.get_year_with_month_from_sheet_name(sheet)
            data.append(self.parse_row_data(year, month, row_data))

    def find_prefecture_column(self, excel_data):
        for _, row in excel_data.iter_rows():
            for col_idx, cell in enumerate(row):
                if cell == '北海道': 
                    return col_idx
        raise ValueError("Could not find '北海道' in any column.")
    
    def get_year_with_month_from_sheet_name(self, sheet_name):
        year_str, month_str = sheet_name.split(".")
        year = int(year_str[1:]) + HEISEI_START_YEAR if sheet_name.startswith("H") else int(year_str)
        month = int(month_str)
        return year, month

    def parse_row_data(self, year, month, row_data):
        if len(row_data) < 11:
            raise ValueError("Row data is missing some fields.")
        
        return {
            'year': year,
            'month': month,
            'prefecture_name': row_data[0],
            'special_high_voltage_consumption': row_data[1],
            'special_high_voltage_retailers_count': row_data[2],
            'high_voltage_consumption': row_data[3],
            'high_voltage_retailers_count': row_data[4],
            'low_voltage_consumption': row_data[5],
            'low_voltage_special_demand': row_data[6],
            'low_voltage_free_pricing': row_data[7],
            'low_voltage_retailers_count': row_data[8],
            'total_consumption': row_data[9],
            'total_retailers_count': row_data[10],
        }
