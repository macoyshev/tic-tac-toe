import os


class Settings:
    colums: int
    rows: int

    @staticmethod
    def setColums(cols) -> None:
        if cols < Settings.get_max_columns_count():
            Settings.colums = cols
        else:
            raise AttributeError(
                f"colums count must be less than {Settings.get_max_columns_count()}, according your console size"
            )

    @staticmethod
    def setRows(rows) -> None:
        if rows < Settings.get_max_rows_count():
            Settings.rows = rows
        else:
            raise AttributeError(
                f"rows count must be less than {Settings.get_max_rows_count()}, according your console size"
            )

    @staticmethod
    def getWidth() -> int:
        return Settings.colums * 2 + 1

    @staticmethod
    def getHeight() -> int:
        return Settings.rows

    @staticmethod
    def get_max_columns_count() -> int:
        return os.get_terminal_size().columns // 2

    def get_max_rows_count() -> int:
        return os.get_terminal_size().lines - 3
