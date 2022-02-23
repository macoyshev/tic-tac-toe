import os
import pickle


class Field:
    __height: int
    __width: int
    __moves: list
    __savePath = "save.pickle"
    
    @staticmethod
    def init(width: int, height: int):
        Field.__width = width
        Field.__height = height
        Field.__moves = []
        
    @staticmethod 
    def saveGame():
        with open(Field.__savePath, "wb") as save:
            pickle.dump(Field.__moves, save)
        
    @staticmethod
    def loadSave():
        with open(Field.__savePath, "rb") as save:
            pickle.load(Field.__moves, save)
        
        Field.eraseSave()
        
    @staticmethod
    def isThereSave():
        res = os.path.getsize(Field.__savePath)
        return res != 0
        
    @staticmethod 
    def erase():
        save = open(Field.__savePath, "w")
        save.close()