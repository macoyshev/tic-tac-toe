from field import Field
import os
import pickle


class TicTacToe:
    loadSaveMessage = "There is game save, press 'y' to load,otherwise any key to start new game\n"
    
    def __init__(self):
        self.userSavePath = "saves/userMoves.pickle"
        self.botSavePath = "saves/botMoves.pickle"
        
        self.field = Field()
    
    @property
    def winner(self):
        userRows = {y: [] for y in range(self.height)}
        botRows = {y: [] for y in range(self.height)}
        
        userColunms ={x: [] for x in range(1, self.field.width, 2)}
        botColunms ={x: [] for x in range(1, self.field.width, 2)}
        
        for move in self.userMoves:
            y, x = move
            userRows[y].append(x)
        
        for move in self.useroves:
            y, x = move
            botRows[y].append(x
        
    
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
    