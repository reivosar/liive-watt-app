import os
import pandas as pd
from app.jobs.electricity_data_import.const import RAW_DIR, HEISEI_START_YEAR

class DataExtractor:
    def extract_energy_usage_data(self, file_name):
        data = []
        try:
            sheet_names = self.get_sheet_names(file_name)
            self.process_sheets(file_name, sheet_names, data)
        except Exception as e:
            print(f"Error processing file {file_name}: {e}")
        return data

    def get_xlsx_files(self, directory):
        return [file for file in os.listdir(directory) if file.endswith(".xlsx")]

    def get_sheet_names(self, file):
        filepath = os.path.join(RAW_DIR, file)
        excel_file = pd.ExcelFile(filepath)
        print(f"Available sheets in {file}: {excel_file.sheet_names}")
        return excel_file.sheet_names

    def process_sheets(self, file, sheet_names, data):
        for sheet in sheet_names:
            if self.is_valid_sheet(file, sheet):
                try:
                    self.process_sheet_data(file, sheet, data)
                except Exception as sheet_error:
                    print(f"Error processing sheet {sheet} in file {file}: {sheet_error}")

    def is_valid_sheet(self, file, sheet):
        if file.startswith("3-2-H"):
            return sheet.startswith("H") and sheet.find('.') > 0
        else:
            return sheet.startswith("20") and sheet.find('.') > 0

    def process_sheet_data(self, file, sheet, data):
        filepath = os.path.join(RAW_DIR, file)
        excel_data = pd.read_excel(filepath, sheet_name=sheet, header=None)

        start_idx, end_idx = None, None

        for idx, row in excel_data.iterrows():
            if row[0] == '北海道':
                start_idx = idx
            if row[0] == '沖縄県':
                end_idx = idx
                break

        if start_idx is None or end_idx is None:
            print(f"Could not find start ('北海道') or end ('沖縄県') rows in sheet {sheet}")
            return

        for idx in range(start_idx, end_idx + 1):
            row = excel_data.iloc[idx]
            row_data = ' '.join(str(cell) for cell in row).split()

            if len(row_data) < 11: 
                print(f"Invalid row data in sheet {sheet}: {row_data}")
                continue

            year, month = self.get_year_with_month_from_sheet_name(sheet)
            data.append(self.parse_row_data(year, month, row_data))

    def get_year_with_month_from_sheet_name(self, sheet_name):
        year_str, month_str = sheet_name.split(".")
        year = int(year_str[1:]) + HEISEI_START_YEAR if sheet_name.startswith("H") else int(year_str)
        month = int(month_str)
        return year, month

    def parse_row_data(self, year, month, row_data):
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
