import pandas as pd

class ExcelFileWrapper:
    def __init__(self, file_path):
        """Initialize the wrapper with an Excel file."""
        self.excel_file = pd.ExcelFile(file_path)

    def get_sheet_names(self):
        """Return the list of sheet names."""
        return self.excel_file.sheet_names

    def get_sheet(self, sheet_name):
        """Return the sheet data wrapped in ExcelSheet."""
        data_frame = pd.read_excel(self.excel_file, sheet_name=sheet_name, header=None)
        return ExcelSheet(data_frame)

class ExcelSheet:
    def __init__(self, data_frame):
        """Initialize with a pandas DataFrame."""
        self.data_frame = data_frame

    def iter_rows(self):
        """Yield each row in the DataFrame."""
        for idx, row in self.data_frame.iterrows():
            yield idx, row

    def get_row(self, idx):
        """Get a specific row by index."""
        return self.data_frame.iloc[idx]

class ExcelReader:
    def load_excel_file(self, file_path):
        """Load and return the Excel file wrapped in a custom interface."""
        return ExcelFileWrapper(file_path)
