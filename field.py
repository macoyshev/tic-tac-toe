from settings import Settings


class Field:
    def __init__(self):
        self.rows = Settings.rows
        self.columns = Settings.colums
        self.body = [[None] * self.columns for _ in range(self.rows)]
        self.emptyCells = self.rows * self.columns
        self.lastMove = None

    def addUserMove(self, row: int, col: int):
        self.emptyCells -= 1
        self.body[row][col] = "x"
        self.lastMove = "user"

    def addBotMove(self, row: int, col: int):
        self.emptyCells -= 1
        self.body[row][col] = "o"
        self.lastMove = "bot"

    def isFull(self):
        return self.emptyCells == 0

    def isFree(self, row, col):
        return self.body[row][col] == None
