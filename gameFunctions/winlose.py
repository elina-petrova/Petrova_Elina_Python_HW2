from random import randint
from gameFunctions import gameVars

def winorlose(status): 
	
	print("called win or lose")
	print("************************")
	print("You", status + "! Would you like to play again?")

	choice = input("Y / N: ")
	print(choice)

	if (choice is "N") or (choice is "n"):
		print("You chose to quit.")
		exit()

	elif (choice is "Y") or (choice is "y"):
		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0,2)]
	
	else:
		print("make a valid choice, Y or N")
		winorlose(status)