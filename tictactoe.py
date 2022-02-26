import random
import os
import pickle
from cursor import Cursor
from settings import Settings
from field import Field


class TicTacToe:
    def __init__(self):
        self.gameSavePath = "saves/gameSave.pickle"
        self.wasSaveLoad = False
        self.field = Field()
        self.cursor = Cursor()
        self.winner = None

    def displayField(self, screen):
        screen.clear()
        for y in range(Settings.getHeight()):
            for x in range(Settings.getWidth()):
                if x % 2 == 0:
                    screen.addstr(y, x, "|")

        if self.wasSaveLoad:
            for ri, row in enumerate(self.field.body):
                for ei, el in enumerate(row):
                    if el:
                        screen.addstr(ri, ei * 2 + 1, el)

    def displayMenu(self, screen):
        screen.addstr(Settings.getHeight(), 0, "press 'x' to move")
        screen.addstr(Settings.getHeight() + 1, 0, "press 'q' to quit")
        screen.addstr(Settings.getHeight() + 2, 0, "press 's' to save")

    def userMove(self, screen):
        x = self.cursor.x
        y = self.cursor.y

        row, col = self.getRowAndColumnFromCoordinates(y, x)

        if self.field.isFree(row, col):
            self.field.addUserMove(row, col)
            screen.addstr(y, x, Settings.userSign)

    def botMove(self, screen):
        if self.field.isFull() or self.field.lastMove == "bot":
            return
        row, col = 0, 0
        while not self.field.isFree(row, col):
            rand = random.randint(0, 1)
            if rand == 1:
                row = (row + 1) % Settings.rows
            else:
                col = (col + 1) % Settings.colums

        y, x = self.getCordinatesFromRowsAndColums(row, col)
        self.field.addBotMove(row, col)
        screen.addstr(y, x, Settings.botSign)
        

    def saveGame(self):
        with open(self.gameSavePath, "wb") as file:
            pickle.dump(self.field, file)

    def loadSave(self):
        with open(self.gameSavePath, "rb") as save:
            self.field = pickle.load(save)
            self.wasSaveLoad = True

    def eraseSave(self):
        save = open(self.gameSavePath, "w")
        save.close()

    def hasSave(self):
        s = os.getcwd()
        res = os.path.getsize(self.gameSavePath)
        return res != 0

    def saveSuccessMessage(self, screen):
        screen.addstr(Settings.getHeight() + 4, 0, "Game saved!")

    def getRowAndColumnFromCoordinates(self, y, x):
        return [y, x - x // 2 - 1]

    def getCordinatesFromRowsAndColums(self, row, col):
        return [row, col * 2 + 1]
