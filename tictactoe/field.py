from settings import Settings


class Field:
    """
    Responsible for adding bot, user moves, and containing these
    """

    def __init__(self):
        self.ROWS_COUNT = Settings.rows
        self.COLUMNS_COUNT = Settings.colums
        self.WIDTH = Settings.getWidth()
        self.HEIGHT = Settings.getHeight()
        self.empty_cells_count = self.ROWS_COUNT * self.COLUMNS_COUNT
        self.body = [[None] * self.COLUMNS_COUNT for _ in range(self.ROWS_COUNT)]

    def add_user_move(self, row: int, col: int) -> None:
        self.emptyCellsCount -= 1
        self.body[row][col] = "x"

    def add_bot_move(self, row: int, col: int) -> None:
        self.emptyCellsCount -= 1
        self.body[row][col] = "o"

    def is_full(self) -> bool:
        return self.emptyCellsCount == 0

    def is_cell_free(self, row, col) -> bool:
        return self.body[row][col] == None
