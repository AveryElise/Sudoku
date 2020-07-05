from tkinter import *
import solver
import copy

#blank board
blank = [
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
	
#Text entry boxes
boxes=[
		[],[],[],[],[],[],[],[],[],
]


def determineColor(i, j):
	#Determines what color an entrybox should be, given its location in the checkerboard pattern
	if ((i < 3 or i > 5) and (j < 3 or j > 5)) or ((i >= 3 and i <=5) and (j >= 3 and j <= 5)):
		return 'lightgrey'
	else:
		return 'white'

def fillBoard(bd):
	#Fills interface with argument board
	for i in range(9):
		for j in range(9):
			boxes[i][j].config(state='normal')
			boxes[i][j].config(bg=determineColor(i, j), disabledbackground= determineColor(i, j))				
			boxes[i][j].delete(0, END)
			boxes[i][j].insert(0, bd[i][j])
			if bd[i][j] != "": #nonblank boxes in a generated board are disabled and black font
				boxes[i][j].config(state=DISABLED, foreground = "black")
			else:
				boxes[i][j].config(foreground="light sea green")

def colorRegular():
	#return color to regular
	for i in range(9):
		for j in range(9):
			boxes[i][j].config(bg=determineColor(i, j), disabledbackground=determineColor(i, j))

def flashColor(color):
	#flashes board with argument color for quarter of second
	for i in range(9):
		for j in range(9):
			boxes[i][j].config(bg=color, disabledbackground=color)
			boxes[i][j].after(250, colorRegular)

def grade():
	bd=getBoard(boxes)
	if solver.canBeSolved(bd) == False:
		flashColor('tomato2')
		return
	elif solver.findNextEmpty(bd) != None: #not yet solved
		flashColor('yellow2')
		return
	flashColor('yellow green') #solved


def getBoard(boxlist):
	#Loads the currently displayed board to list of list format. If nonvalid input, input 0.
	possible = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	bd = copy.deepcopy(blank)
	for i in range(9):
		for j in range(9):
			if boxlist[i][j].get() not in possible:
				boxlist[i][j].delete(0, END)
				boxlist[i][j].insert(0, '')
				bd[i][j] = boxlist[i][j].get()
			else:
				try:				
					bd[i][j]=int(boxlist[i][j].get())
				except:
					bd[i][j]=boxlist[i][j].get()
	return bd


def solveBoard():
	#Fills board with solution to current board
	bd = getBoard(boxes)
	if solver.canBeSolved(bd) == False:
		flashColor('tomato2')
		return
	else:
		solver.solve(bd)
		fillBoard(bd)
		flashColor('yellow green')
		return


def customBoard():
	#Allow user to enter a custom Sudoku Board to play or solve
	customBoxes=[
		[],[],[],[],[],[],[],[],[],
	]

	#initialize new window
	window2=Tk()
	window2.title("Custom")

	#get the custom board and import it to main window game
	def done():
		customBoard = getBoard(customBoxes)
		fillBoard(customBoard)
		window2.destroy()

	#Set up boxes
	for i in range(9):
		for j in range(9):
			textentry = Entry(window2, justify = CENTER, borderwidth=2, width=3, bg=determineColor(i, j), foreground="light sea green")
			textentry.configure(font=('Courier', 14, 'bold'))
			textentry.grid(row=i, column=j, ipady=2)
			textentry.insert(0, '')
			customBoxes[i].append(textentry)

	#set up instructions
	instructions = "Enter a custom Sudoku Board, and press Done to import it to the Sudoku Game."
	msg = Message(window2, text=instructions)
	msg.config(font = ('Courier', 12))
	msg.grid(row=0, column = 15, rowspan = 4)

	#button
	Button(window2, font=('Courier', 10), text="Done", command = done) .grid(row=6,column=15)

	window2.mainloop()


def main():
	#main window
	window = Tk()
	window.title("Sudoku")

	#Set up interface
	for i in range(9):
		for j in range(9):
			textentry = Entry(window, justify = CENTER, borderwidth=2, width=3, bg=determineColor(i, j), foreground="light sea green")
			textentry.configure(font=('Courier', 14, 'bold'))
			textentry.grid(row=i, column=j, ipady=2)
			textentry.insert(0, '')
			boxes[i].append(textentry)
	#Buttons
	Button(window, font=('Courier', 10), text="Generate Easy", command= lambda: fillBoard(solver.generateEasy())) .grid(row=0,column=15)
	Button(window, font=('Courier', 10), text="Generate Medium", command= lambda: fillBoard(solver.generateMedium())) .grid(row=1,column=15,)
	Button(window, font=('Courier', 10), text="Generate Hard", command= lambda: fillBoard(solver.generateHard())) .grid(row=2,column=15)
	# Button(window, font=('Courier', 10), text="Input Custom Board", command= lambda: fillBoard(blank)) .grid(row=3,column=15)
	Button(window, font=('Courier', 10), text="Input Custom Board", command= customBoard) .grid(row=3,column=15)
	Button(window, font=('Courier', 10), text="Grade Board", command=grade) .grid(row=4,column=15)
	Button(window, font=('Courier', 10), text="Solve", command=solveBoard) .grid(row=5,column=15)

	#Default board upon start is Easy
	fillBoard(solver.generateEasy())

	#start loop
	window.mainloop()


#begin program
main()
