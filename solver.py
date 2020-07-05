#Sudoku-Solver
import random
import copy

def generateBoard(remainingNums):
	newBoard=[
		["", "", "", "", "", "", "", "", ""],
		["", "", "", "", "", "", "", "", ""],
		["", "", "", "", "", "", "", "", ""],
		["", "", "", "", "", "", "", "", ""],
		["", "", "", "", "", "", "", "", ""],
		["", "", "", "", "", "", "", "", ""],
		["", "", "", "", "", "", "", "", ""],
		["", "", "", "", "", "", "", "", ""],
		["", "", "", "", "", "", "", "", ""]
	]

	solve(newBoard)
	#remove all but remainingNums numbers
	for i in range(81-remainingNums):
		row = random.randint(0, 8)
		col = random.randint(0, 8)
		while newBoard[row][col] == "":
			row = random.randint(0, 8)
			col = random.randint(0, 8)
		newBoard[row][col] = ""
	return newBoard

def generateVeryHard():
	return generateBoard(17)

def generateHard():
	return generateBoard(44)

def generateMedium():
	return generateBoard(53)

def generateEasy():
	return generateBoard(66)

def solve(bd):
	#Solves a board by trying random numbers in backtracking algorithm, as opposed to counting up from 1
	pos = findNextEmpty(bd)
	if pos == None:
		return True
	else:
		row = pos[0]
		col = pos[1]
		possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		random.shuffle(possible)
		for i in possible:
			if isvalid(bd, i, pos):
				#modify board
				bd[row][col] = i
				#follow this version of board to completion.
				if solve(bd):
					return True 
				#if that version of board can't create a valid solution, undo our modification of board.
				else:
					bd[row][col] = ""
		#If no number 1 through 9 can be validly placed in pos, return False. This version of board is invalid.
		return False

def canBeSolved(bd):
	bdcpy = copy.deepcopy(bd)
	if isValidBoard(bdcpy) == False: #if it's not a valid board, false
		return False
	solve(bdcpy) #if it is a valid board, see if it's solvable
	if findNextEmpty(bdcpy) == None:
		return True
	else:
		return False

#Find next empty spot
def findNextEmpty(bd):
	for i in range(len(bd)):
		for j in range(len(bd[i])):
			if bd[i][j] == "":
				return (i,j) #row, column

#Checks whether the board is valid - note that a board can be valid yet not be solvable
def isValidBoard(bd):
	bdcpy = copy.deepcopy(bd)
	for i in range(len(bdcpy)):
		for j in range(len(bdcpy)):
			if bdcpy[i][j] != "":
				temp=bdcpy[i][j]
				bdcpy[i][j]=""
				if isvalid(bdcpy, temp, (i, j)) == False:
					return False
				bdcpy[i][j]=temp
	return True



def isvalid(bd, num, pos):
	#checks whether placing a certain number in a certain position is a valid move.
	col = pos[1]
	row = pos[0]
	#check row and column
	for i in range(len(bd[0])):
		if bd[row][i] == num:
			return False
		if bd[i][col] == num:
			return False
	for k in range(col - (col % 3), col - (col % 3) +3):
		for m in range(row - (row % 3), row - (row % 3) +3):
			if bd[m][k] == num:
				return False
	return True

#Print the argument board in the command line
def printBoard(bd):
	for i in range(len(bd)):
		if (i%3 == 0) and (i != 0):
			print("- - - - - - - - - - - - - - - - -")
		for j in range(len(bd[i])):

			if (j%3 == 0) and (j != 0):
				print(" | ", end="")
			if bd[i][j] == "":
				print("   ", end="")
			else:
				print(" "+str(bd[i][j])+" ", end="")
		print('\n')

#To show the solver used from the command line
def main(bd):
	print('\n')
	print('Board: ')
	print('\n')
	printBoard(bd)
	print('\n')
	print('Solution: ')
	print('\n')
	if canBeSolved(bd):
		solve(bd)
		printBoard(bd)
	else:
		print("Board cannot be solved.")


#Below code generates and prints a hard board, and prints solution.

# bd = generateHard()
# main(bd)

