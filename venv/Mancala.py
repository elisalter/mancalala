"""
Program: A fun mancala game for two players in a console
Author: Ella Brownlie
Date: 20/01/2018
"""

# function that takes in a 2D array representing the board state and prints the board
def printBoard(bS):
    print("||H   1    2    3    4    5    6    H|| (Column name)")
    print("||===================================||")
    print("||" + str(bS[0][0]) + "   " + str(bS[0][1]) + "    " + str(bS[0][2]) + "    " + str(bS[0][3]) + "    " + str(bS[0][4]) + "    " + str(bS[0][5]) + "    " + str(bS[0][6]) + "     ||")
    print("||" + "    " + str(bS[1][1]) + "    " + str(bS[1][2]) + "    " + str(bS[1][3]) + "    " + str(bS[1][4]) + "    " + str(bS[1][5]) + "    " + str(bS[1][6]) + "    " + str(bS[1][7]) + "||")



# This variable represents the board state
boardState = [[0, 4, 4, 4, 4, 4, 4, None], [None, 4, 4, 4, 4, 4, 4, 0]]

# this variable represents whose turn it is
playersTurn = 1

# is the game finished or not?
finished = False

print("\n")
print("Welcome to Ella's amazing Mancala game! Please enjoy!")
print("-----------------------------------------------------")
print("\n")

printBoard(boardState)

# need to get the users input using pythons input function, take that input and pass it into a move function,
# the move function should be something like this

makeMove = raw_input('Player, what is your move?')
def makeMove (boardState, player, colummChoice):

def makeMove = raw_input(1, 2, 3, 4, 5, 6)
    print
# def makeMove(boardState, player, colummChoice) this returns a NEW boardstate
#

while finished: False
printBoard(boardState)



# learn about 'while loops': https://www.tutorialspoint.com/python/python_while_loop.htm
# user input: http://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard
# functions: https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html
# python if statements: https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html
# pythons lists (this is what our boardState variable is): https://www.digitalocean.com/community/tutorials/understanding-lists-in-python-3
# https://www.tutorialspoint.com/python/python_lists.htm
#
#
#
# GENERAL FLOW OF PROGRAM FROM  HERE ON
#
# while the game is not finished:
#      take the players move (input function)
#      calculate the new board state based on the players move (pass this into the move function)
#      check the board state to see if; a player has won, conquered, or gets another turn
#      calculate who's turn it is now based on previous step
#      print the new board state using the printBoard(boardState) work
#      update the 'finished' variable

boardState = makeMove(boardState, 1, 7)






