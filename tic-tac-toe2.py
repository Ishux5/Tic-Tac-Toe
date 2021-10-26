#imports:
import os

#game Variables
gameActive = True
activePlayer = 1
gameBuffer = 0
spaces = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
rowcoldia = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3", "a1", "b1", "c1", "a1", "b1", "c1", "a2", "b2", "c2", "a3", "b3", "c3", "a1", "b2", "c3", "c1", "b2", "a3"]
gameWonX = "XXX"
gameWonO = "OOO"

#functions:
def syntax(player):
	print(
"Player" + str(player) + "!"
"""
The Correct Input is RowCol!
e.g. A2.
The Row must be a letter from a-c or A-C.
The Col must be a number from 1-3.
""")

def displayGame(gameOld):
	game = gameOld.copy()
	player = "XO"
	for x in game:
		if x not in player:
			index = game.index(x)
			game[index] = " "

	print("	    1	    2	    3")
	print("	        │       │")
	print("A	    " + game[0] + "	│   " + game[1] + "	│   " + game[2])
	print("	────────┼───────┼────────")
	print("B	    " + game[3] + "	│   " + game[4] + "	│   " + game[5])
	print("	────────┼───────┼────────")
	print("C	    " + game[6] + "	│   " + game[7] + "	│   " + game[8])
	print("	        │       │")

def gameStatus():
	condition1 = rowcoldia[0] + rowcoldia[1] + rowcoldia[2]
	condition2 = rowcoldia[3] + rowcoldia[4] + rowcoldia[5]
	condition3 = rowcoldia[6] + rowcoldia[7] + rowcoldia[8]
	condition4 = rowcoldia[0] + rowcoldia[3] + rowcoldia[6]
	condition5 = rowcoldia[1] + rowcoldia[4] + rowcoldia[6]
	condition6 = rowcoldia[2] + rowcoldia[5] + rowcoldia[8]
	condition7 = rowcoldia[0] + rowcoldia[4] + rowcoldia[8]
	condition8 = rowcoldia[6] + rowcoldia[4] + rowcoldia[2]
	totalConditions = [condition1, condition2, condition3, condition4, condition5, condition6, condition7, condition8]
	for x in totalConditions:
		if x == gameWonX:
			return True
		elif x == gameWonO:
			return True
	gameStatus = 0
	for x in rowcoldia:
		if x in spaces:
			gameStatus += 1
	if gameStatus == 0:
		return False

def clearConsole():
	command = "clear"
	if os.name in ("nt", "dos"):
		command = "cls"
	os.system(command)
#game
while gameActive:	#while the game is active run this while loop
	if activePlayer == 1:
		askInput = input("Player" + str(activePlayer) + " Enter a valid Space: ")
		while not askInput.lower() in rowcoldia:	#runs only if the input is incorrect
			syntax(activePlayer)
			askInput = input("Player" + str(activePlayer) + " Enter a valid Space: ")
		for x in rowcoldia:
			if askInput.lower() in rowcoldia:
				index = rowcoldia.index(askInput)
				rowcoldia[index] = "X"
		clearConsole()
		displayGame(rowcoldia)
		if gameStatus() == True:
			print("Player" + str(activePlayer) + " has WON!")
			gameActive = False
			break
		elif gameStatus() == False:
			print("Draw!")
			gameActive = False
			break
		activePlayer = 2

	if activePlayer == 2:
		askInput = input("Player" + str(activePlayer) + " Enter a valid Space: ")
		while not askInput.lower() in rowcoldia:	#runs only if the input is incorrect
			syntax(activePlayer)
			askInput = input("Player" + str(activePlayer) + " Enter a valid Space: ")
		for x in rowcoldia:
			if askInput.lower() in rowcoldia:
				index = rowcoldia.index(askInput)
				rowcoldia[index] = "O"
		clearConsole()
		displayGame(rowcoldia)
		if gameStatus() == True:
			print("Player" + str(activePlayer) + " has WON!")
			gameActive = False
			break
		elif gameStatus() == False:
			print("Draw!")
			gameActive = False
			break
		activePlayer = 1

while not gameActive:
	close = input("Do you want to close this Window now? (Y): ")
	if close.lower() == "y":
		break
