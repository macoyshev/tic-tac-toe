from math import e
import re
from field import Field
import os
import pickle
from settings import Settings
from functools import reduce


class TicTacToe:
    loadSaveMessage = "There is game save, press 'y' to load,otherwise any key to start new game\n"
    
    def __init__(self):
        self.userSavePath = "saves/userMoves.pickle"
        self.botSavePath = "saves/botMoves.pickle"
        
        self.field = Field()        
    
    
    def saveGame(self):
        with open(self.userSavePath, "wb") as file:
            pickle.dump(self.field.userMoves, file)
            
        with open(self.botSavePath, "wb") as file:
            pickle.dump(self.field.botMoves, file)
    
    def loadSave(self):
        with open(self.userSavePath, "rb") as userMovesSave:
            self.field.userMoves = pickle.load(userMovesSave)
        
        with open(self.botSavePath, "rb") as botMovesSave:
            self.field.botMoves = pickle.load(botMovesSave)
        
    def eraseSaves(self):
        userMovesSave = open(self.userSavePath, "w")
        userMovesSave.close()
        
        botMovesSave = open(self.botSavePath, "w")
        botMovesSave.close()
            
    def searchSaves(self):
        res = os.path.getsize(self.userSavePath)
        return res != 0
    