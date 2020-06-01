from tkinter import *
import solver
import copy

blank = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#main window
window = Tk()
window.title("Sudoku")

def fillBoard(bd):
	#Fills current board with argument board
	for i in range(9):
		for j in range(9):
			boxes[i][j].config(state='normal')
			boxes[i][j].config(bg='white', disabledbackground= 'lightgrey')
			boxes[i][j].delete(0, END)
			boxes[i][j].insert(0, bd[i][j])
			if bd[i][j] != 0: #nonzero boxes in a generated board are disabled
				boxes[i][j].config(state=DISABLED)

def colorWhite():
	#helper func for flashColor
	for i in range(9):
		for j in range(9):
			boxes[i][j].config(bg='white', disabledbackground='lightgrey')

def flashColor(color):
	#flashes board with argument color for quarter of second
	for i in range(9):
		for j in range(9):
			boxes[i][j].config(bg=color, disabledbackground=color)
			boxes[i][j].after(250, colorWhite)

def grade():
	bd=getBoard()
	if solver.isSolvable(bd) == False: #unsolvable
		flashColor('tomato2')
		return
	elif solver.findNextEmpty(bd) != None: #not yet solved
		flashColor('yellow2')
		return
	flashColor('yellow green') #solved


def getBoard():
	#Loads the currently displayed board to list of list format. If nonvalid input, input 0.
	possible = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	bd = copy.deepcopy(blank)
	for i in range(9):
		for j in range(9):
			if boxes[i][j].get() not in possible:
				boxes[i][j].delete(0, END)
				boxes[i][j].insert(0, '0')
				bd[i][j] = int(boxes[i][j].get())
			else:				
				bd[i][j]=int(boxes[i][j].get())
	return bd

def solveBoard():
	#Fills board with solution to current board
	bd = getBoard()
	if solver.isSolvable(bd):
		solver.solve(bd)
		fillBoard(bd)
		flashColor('yellow green')
	else:
		flashColor('tomato2')
	

#Set up text entry boxes
boxes=[
		[],[],[],[],[],[],[],[],[],
]
for i in range(9):
	for j in range(9):
		textentry = Entry(window, borderwidth=2, width=3, bg='white')
		textentry.grid(row=i, column=j, ipady=2)
		textentry.insert(0, 0)
		boxes[i].append(textentry)

#Buttons
Button(window, text="Generate Hard", command= lambda: fillBoard(solver.generateHard())) .grid(row=0,column=10, sticky=W)
Button(window, text="Generate Medium", command= lambda: fillBoard(solver.generateMedium())) .grid(row=1,column=10, sticky=W)
Button(window, text="Generate Easy", command= lambda: fillBoard(solver.generateEasy())) .grid(row=2,column=10, sticky=W)
Button(window, text="Clear Board", command= lambda: fillBoard(blank)) .grid(row=3,column=10, sticky=W)
Button(window, text="Grade Board", command=grade) .grid(row=4,column=10, sticky=W)
Button(window, text="Solve", command=solveBoard) .grid(row=5,column=10, sticky=W)

window.mainloop()