from cgitb import text
import random
import os
import pickle
from cursor import Cursor
from settings import Settings
from field import Field


class TicTacToe:
    def __init__(self):
        self.__gameSavePath = "saves/gameSave.pickle"
        self.__is_save_loaded = False
        self.field = Field()
        self.cursor = Cursor()
        self.winner = None
        self.is_move_success = False
        self.move_x = None
        self.move_y = None
        self.MENU_HEIGHT = 3

    def is_winner(self):
        field = self.field.body
        sign = None

        if self.field.ROWS_COUNT >= self.field.COLUMNS_COUNT:
            for row in field:
                if len(set(row)) == 1:
                    if row[0]:
                        sign = row[0]
                        break

        if self.field.ROWS_COUNT <= self.field.COLUMNS_COUNT:
            for col in range(self.field.COLUMNS_COUNT):
                if len({field[row][col] for row in range(self.field.ROWS_COUNT)}) == 1:
                    if field[0][col]:
                        sign = field[0][col]
                        break

        if self.field.ROWS_COUNT == self.field.COLUMNS_COUNT:
            diagonal1 = {field[i][i] for i in range(self.field.ROWS_COUNT)}
            if len(diagonal1) == 1:
                if field[0][0]:
                    sign = field[0][0]

            diagonal2 = {
                field[i][self.field.ROWS_COUNT - 1 - i]
                for i in range(self.field.ROWS_COUNT)
            }
            if len(diagonal2) == 1:
                if field[0][self.field.ROWS_COUNT - 1]:
                    sign = field[0][self.field.ROWS_COUNT - 1]

        if sign != None:
            if sign == "x":
                self.winner = "user"
            else:
                self.winner = "bot"
            return True
        else:
            if self.field.isFull():
                return True
            return False

    def get_field(self):
        str_field = ""
        for y in range(self.field.HEIGHT):
            for x in range(self.field.WIDTH):
                if x % 2 == 0:
                    str_field += "|"
                else:
                    if self.__is_save_loaded:
                        row, col = self.__getRowAndColumnFromPossition(y, x)
                        if self.field.is_cell_free(row, col):
                            str_field += " "
                        else:
                            str_field += self.field.body[row][col]
                    else:
                        str_field += " "
            str_field += "\n"

        return str_field

    def get_menu(self):
        menu = ""
        menu += "press 'x' to move\n"
        menu += "press 'q' to quit\n"
        menu += "press 's' to save\n"

        return menu

    def get_saved_message(self):
        return "Games saved!"

    def get_saved_message_height(self):
        return self.field.HEIGHT + self.MENU_HEIGHT + 1

    def get_load_message(self):
        return (
            "Press 'y' to load last saved game, otherwise any key to start new game\n"
        )

    def make_user_move(self):
        y, x = self.cursor.y, self.cursor.x
        row, col = self.__getRowAndColumnFromPossition(y, x)

        if self.field.is_cell_free(row, col):
            self.field.addUserMove(row, col)

            self.is_move_success = True
            self.move_x = x
            self.move_y = y
        else:
            self.is_move_success = False

    def make_bot_move(self):
        if self.field.isFull():
            self.is_move_success = False
            return

        row, col = 0, 0
        while not self.field.is_cell_free(row, col):
            rand = random.randint(0, 1)
            if rand == 1:
                row = (row + 1) % self.field.ROWS_COUNT
            else:
                col = (col + 1) % self.field.COLUMNS_COUNT
        self.field.addBotMove(row, col)

        y, x = self.__getPossitionFromRowAndColum(row, col)
        self.is_move_success = True
        self.move_x = x
        self.move_y = y

    def save_game(self):
        with open(self.__gameSavePath, "wb") as file:
            pickle.dump(self.field, file)

    def load_save(self):
        with open(self.__gameSavePath, "rb") as save:
            self.field = pickle.load(save)
            self.__is_save_loaded = True

    def erase_save(self):
        save = open(self.__gameSavePath, "w")
        save.close()

    def has_save(self):
        return os.path.getsize(self.__gameSavePath) != 0

    def __getRowAndColumnFromPossition(self, y, x):
        return [y, x - x // 2 - 1]

    def __getPossitionFromRowAndColum(self, row, col):
        return [row, col * 2 + 1]
