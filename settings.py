class Settings:
    userSign = "x"
    botSign = "o"
    colums: int
    rows: int

    @staticmethod
    def getWidth() -> int:
        return Settings.colums * 2 + 1

    @staticmethod
    def getHeight() -> int:
        return Settings.rows
