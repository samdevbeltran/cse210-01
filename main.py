from GameMethods import *
'''
Tic-Tac-Toe: A Solution
Author: Samuel Beltran
'''
gameMethods = GameMethods([1,2,3,4,5,6,7,8,9])

def main():
    
    startGame = True
    gamePlayer = "X"
    gameMethods.displayGameBoard()

    while startGame:
        if gamePlayer == "X":
            gameMethods.ask(gamePlayer)
            gameMethods.displayGameBoard()
            if gameMethods.checkIfWinner():
                print("Good game "+gamePlayer+". Thanks for playing!")
                gameMethods.endGameWinner()
            elif gameMethods.checkIfWinner() == False:
                startGame = False
            gamePlayer = "O"
            
        else:
            gameMethods.ask(gamePlayer) 
            gameMethods.displayGameBoard()
            if gameMethods.checkIfWinner():
                print("Good game "+gamePlayer+". Thanks for playing!")
                gameMethods.endGameWinner()
            elif gameMethods.checkIfWinner() == False:
                startGame = False
            gamePlayer = "X"
    
    
main()