import re
from settings import Settings
import random

class Field:
    def __init__(self):
        self.width = Settings.colums * 2 + 1
        self.height = Settings.rows
        self.userMoves = []
        self.botMoves = []
        self.userRows = {y: [] for y in range(self.height)}
        self.userColums = {x: [] for x in range(1, self.width, 2)}
        self.botRows = {y: [] for y in range(self.height)}
        self.botColums = {x: [] for x in range(1, self.width, 2)}

    def addUserMove(self, y, x):
        self.userMoves.append([y, x])

    def getLastUserMove(self):
        return self.userMoves[-1]

    def addBotMove(self):
        
        if self.isFull():
            return
        
        y, x = 0, 1
        while [y, x] in self.userMoves or [y, x] in self.botMoves:
            z = random.randint(0, 1)
            if z == 1:
                y = (y + 1) % self.height
            else:
                x = (x + 2) % (self.width - 1)
        
        self.botMoves.append([y, x])
    
    
    def getLastBotMove(self):
        return self.botMoves[-1]
    
    def isFull(self):
        return Settings.rows * Settings.colums == len(self.botMoves) + len(self.userMoves)
         
    def __findWinCombins(self):
        res = []
        if Settings.rows == Settings.colums:
            for y in range(self.height):
                for x in range(1, self.width, 2):
                    res.append([y,x]);
                    