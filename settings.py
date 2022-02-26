from asyncio import constants
import os


class Settings:
    colums: int
    rows: int
    consoleAttrs = os.get_terminal_size()

    @staticmethod
    def setColums(cols):
        if cols < Settings.get_max_columns_count():
            Settings.colums = cols
        else:
            raise AttributeError(f"colums count must be less than {Settings.get_max_columns_count()}, according your console size")
        
    @staticmethod
    def setRows(rows):
        if rows < Settings.get_max_rows_count():
            Settings.rows = rows     
        else:
            raise  AttributeError(f"rows count must be less than {Settings.get_max_rows_count()}, according your console size")  
        
    @staticmethod
    def getWidth():
        return Settings.colums * 2 + 1

    @staticmethod
    def getHeight():
        return Settings.rows

    @staticmethod
    def get_max_columns_count():
        return os.get_terminal_size().columns // 2

    def get_max_rows_count():
        return os.get_terminal_size().lines - 3