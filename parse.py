import os
import xlrd


class Parse:

    @staticmethod
    def get_excel_files_in_current_dir():
        excel_files = []
        for file in os.listdir(os.curdir):
            if file.endswith(".xls") or file.endswith(".xlsx"):
                excel_files.append(file)
        return excel_files
