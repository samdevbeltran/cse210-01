from GameMethods import *

gameMethods = GameMethods([1,2,3,4,5,6,7,8,9])

def main():
    
    startGame = True
    gamePlayer = "X"
    gameMethods.displayGameBoard()

    while startGame:
        if gamePlayer == "X":
            gameMethods.ask(gamePlayer)
            gameMethods.displayGameBoard()
            if gameMethods.checkIfWinner(gamePlayer):
                print("Good game "+gamePlayer+". Thanks for playing!")
                gameMethods.endGameWinner()
            gamePlayer = "O"
            
        else:
            gameMethods.ask(gamePlayer) 
            gameMethods.displayGameBoard()
            if gameMethods.checkIfWinner(gamePlayer):
                print("Good game "+gamePlayer+". Thanks for playing!")
                gameMethods.endGameWinner()
            gamePlayer = "X"
            
    
main()