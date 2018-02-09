"""
Program: A fun mancala game for two players in a console
Author: Ella Brownlie, Eli Salter
Date: 20/01/2018
"""

# function that takes in a 2D array representing the board state and prints the board
def printBoard(bS):
    print("\n")
    print("||H   1    2    3    4    5    6    H|| (Column name)")
    print("||===================================||")
    print("||" + str(bS[0][0]) + "   " + str(bS[0][1]) + "    " + str(bS[0][2]) + "    " + str(bS[0][3]) + "    " + str(bS[0][4]) + "    " + str(bS[0][5]) + "    " + str(bS[0][6]) + "     ||")
    print("||" + "    " + str(bS[1][1]) + "    " + str(bS[1][2]) + "    " + str(bS[1][3]) + "    " + str(bS[1][4]) + "    " + str(bS[1][5]) + "    " + str(bS[1][6]) + "    " + str(bS[1][7]) + "||")
    print("\n")


def updateBoardState(boardState, player, colummChoice):

    # side of the board that the stones are to be moved
    boardSide = player - 1
    numberOfStones = boardState[boardSide][colummChoice]

    currentColumn = colummChoice
    if (player == 1):
        direction = -1
    else:
        direction = 1

    # set number of stones at current board hole to zero
    boardState[boardSide][currentColumn] = 0

    for i in range(1, numberOfStones+1):

        currentColumn = currentColumn + direction

        # if at a home square, switch the board state
        if (currentColumn == 0 and player == 1) or (currentColumn == 7 and player == 2):

            boardState[boardSide][currentColumn] = boardState[boardSide][currentColumn] + 1

            if (boardSide == 0): # (landed at 0,0)
                boardSide = 1
                direction = 1
            else: #boardSide == 1 (landed at 1,7)
                boardSide = 0
                direction = -1
        else:
            boardState[boardSide][currentColumn] = boardState[boardSide][currentColumn] + 1

    return boardState;

# initialise boardstate, 1st array represents player 1
boardState = [[0, 4, 4, 4, 4, 4, 4, None], [None, 4, 4, 4, 4, 4, 8, 0]];
playersTurn = 1;
finished = False;

print("\n");
print("Welcome to Ella and Eli's amazing Mancala game! Please enjoy!");
print("-------------------------------------------------------------");



while(finished == False):
    printBoard(boardState);
    columnToMove = input("Player " + str(playersTurn) + " which column of stones would you like to move?\n")
    boardState = updateBoardState(boardState, playersTurn, columnToMove);
    # update players turn
    if (playersTurn == 1):
        playersTurn = 2
    else:
        playersTurn = 1












