'''
Tic-Tac-Toe: A Solution
Author: Samuel Beltran
'''
from typing import Counter

class GameMethods:

    positionList = []
    
    
    def __init__(self,positionList):
        self.positionList = positionList

    def displayGameBoard(self):
        counter = 0
        boardString = ""

        for positions in self.positionList:

            if counter == 2 or counter == 5 or counter == 8:
                boardString += str(positions)  + "\n"
                
            elif counter == 3 or counter == 6:
                
                boardString += "_+_+_\n" 
                boardString += str(positions)  + "|" 

            else:
                boardString += str(positions)  + "|" 
                
            counter += 1
        
        print(boardString)    
        
    def ask(self,player):
        inputValue = input(player + "'s turn to choose a square (1-9):")

        self.changePositionByValue(player,inputValue)

    def changePositionByValue(self,player,value):
        self.positionList[int(value)-1] = player

    def endGameWinner(self):
        quit()

    def checkIfWinner(self):
        pos = self.positionList
        if(pos[0] == pos[1] == pos[2] or 
           pos[3] == pos[4] == pos[5] or 
           pos[6] == pos[7] == pos[8] or 
           pos[0] == pos[4] == pos[8] or 
           pos[0] == pos[3] == pos[6] or 
           pos[1] == pos[4] == pos[7] or 
           pos[2] == pos[5] == pos[8] or 
           pos[2] == pos[4] == pos[6]):
            return True
        elif all(isinstance(p, str) for p in pos ):
            return False
    