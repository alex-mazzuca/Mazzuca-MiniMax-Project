

# Initites the Tic Tac Toe Game
#Wriiten for Assignment 4 CMPUT 355 University of ALberta
# Written by Alex Mazzuca
def main():

    ticTacToeGame()

    return

# Runs Tic Tac Toe Game. Only the Human player can player X and plays against the ai O player
# Written by Alex Mazzuca
def ticTacToeGame():

    gameBoard = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    
    gameBoardpositions = [" 1 ", " 2 ", " 3 ", " 4 " , " 5 ", " 6 ", " 7 ", " 8 ", " 9" ]

    acceptableInputs = ["1","2","3","4","5","6","7","8","9"]

    player = "X"
    computer = "O"

    turn = player
    turnNumber = 0

    print("Welcome to Tic Tac Toe. The player will go first and will be X.")
    print("The Player will input wich position they will go based on this board.")
    showBoard(gameBoardpositions)

    while (turnNumber < 9):
            #X Turn
            if (turn == "X"):
                print("It is your turn")

                playerInput = checkInput(acceptableInputs, gameBoardpositions)
                
                emptyPosition = checkPostion(playerInput, gameBoard)

                while (emptyPosition == False):
                    print("Position Occupied")
        
                    playerInput = checkInput(acceptableInputs, gameBoardpositions)
                    emptyPosition = checkPostion(playerInput, gameBoard)
                
            
                gameBoard[playerInput - 1] = " X "

                showBoard(gameBoard)
                
                winner = checkWin(gameBoard, turn)
                if winner == "X":
                    print("X has won. Game Over!")
                    return
                elif winner == "Tie":
                    print("Tie. Game Over!")
                    return
                
                turnNumber += 1
                turn = "O"
                if turnNumber == 9:
                    break
            
            #O Turn
            elif (turn == "O"):
                
                oPlaced = False
                scoreBoard = gameBoard.copy()

                for i in range(9):
                    minimaxGameBoard = gameBoard.copy()
                    if minimaxGameBoard[i] == "   ":
                        minimaxGameBoard[i] = " O "
                        score = minimax(minimaxGameBoard, "O")
                        scoreBoard[i] = score
            
                for i in range(9):
                    if (scoreBoard[i] == 1 and oPlaced == False):
                        gameBoard[i] = " O "
                        oPlaced = True
                
                if oPlaced == False:
                    for i in range(9):
                        if (scoreBoard[i] == 0 and oPlaced == False):
                            gameBoard[i] = " O "
                            oPlaced = True
                
                if oPlaced == False:
                    for i in range(9):
                        if (scoreBoard[i] == -1 and oPlaced == False):
                            gameBoard[i] = " O "
                            oPlaced = True
                
                print("\n O's Move")
                showBoard(gameBoard)
                winner = checkWin(gameBoard, turn)

                if winner == "O":
                    print("O has won. Game Over!")
                    return
                elif winner == "Tie":
                    print("Tie. Game Over!")
                    return
                
                turnNumber += 1
                turn = "X"
                if turnNumber == 9:
                    break
                

        



    return

# Shows the current gameboard will all the current moves
# Written by Alex Mazzuca
def showBoard(gameBoard):

    print(gameBoard[0] + '|' + gameBoard[1] + "|" + gameBoard[2])
    print("---+---+---")
    print(gameBoard[3] + '|' + gameBoard[4] + "|" + gameBoard[5])
    print("---+---+---")
    print(gameBoard[6] + '|' + gameBoard[7] + "|" + gameBoard[8])

    return

# Check to see that the input is an integer from 1 to 9
# Written by Alex Mazzuca
def checkInput(acceptableInputs, gameBoardpositions):
    playerInput = None
    while (playerInput not in acceptableInputs):
        playerInput = input("Enter your position you would like to go:")
    playerInput = int(playerInput)
    
    return playerInput
    
# Checks to see if there the position on the Board is taken up
# Written by Alex Mazzuca
def checkPostion(playerInput, gameBoard):
    index = playerInput - 1
    if (gameBoard[index] != "   "):
        return False
    else:
        return True

# Checks to see if either X or O has one or checks to see is there is
# a Tie
# Written by Alex Mazzuca
def checkWin(gameBoard, turn):
    winner = None

    if gameBoard[0] == gameBoard [1] == gameBoard[2] != "   ":
        winner = turn
    elif gameBoard[0] == gameBoard [3] == gameBoard[6] != "   ":
        winner = turn
    elif gameBoard[0] == gameBoard [4] == gameBoard[8] != "   ":
        winner = turn
    elif gameBoard[6] == gameBoard [7] == gameBoard[8] != "   ":
        winner = turn
    elif gameBoard[3] == gameBoard [4] == gameBoard[5] != "   ":
        winner = turn
    elif gameBoard[1] == gameBoard [4] == gameBoard[7] != "   ":
        winner = turn
    elif gameBoard[2] == gameBoard [5] == gameBoard[8] != "   ":
        winner = turn
    elif gameBoard[2] == gameBoard [4] == gameBoard[6] != "   ":
        winner = turn

    if ("   " not in gameBoard):
        winner = "Tie"

    return winner

# Implementation of the MiniMax alogrthm that checks all the possible best moves for the AI
# Code adpated from URL: https://www.javatpoint.com/mini-max-algorithm-in-ai
# Written by Alex Mazzuca
def minimax(minigameBoard, turn):
    winner  = checkWin(minigameBoard, turn)
    

    if winner != None:
        if winner == "X":
            return -1
        elif winner == "O":
            return 1
        elif winner == "Tie":
            return 0

    if (turn == "X"):
        bestScore = -99999
        for i in range(9):
            if (minigameBoard[i] == "   "):
                minigameBoard[i] = " O "
                minimaxScore = minimax(minigameBoard, "O")
    
                minigameBoard[i] = "   "
                bestScore = max(minimaxScore, bestScore)

        return bestScore
    elif (turn == "O"):
        bestScore = 99999
        for i in range(9):
            if (minigameBoard[i] == "   "):
                minigameBoard[i] = " X "
                minimaxScore = minimax(minigameBoard, "X")

                minigameBoard[i] = "   "
                bestScore = min(minimaxScore, bestScore)

        return bestScore

if __name__ == "__main__":
    main()