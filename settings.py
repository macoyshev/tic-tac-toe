class Settings:
    colums: int
    rows: int
    
    @staticmethod
    def rows(rows: int):
        Settings.rows = rows

    @staticmethod
    def colums(colums: int):
        Settings.colums = colums
