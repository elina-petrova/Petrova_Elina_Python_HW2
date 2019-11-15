from random import randint
from gameFunctions import winlose
from gameFunctions import compare
from gameFunctions import gameVars

while gameVars.player is False:
	print("▁ ▂ ▄ ▅ ▆ ▇ █ █ █ █ █ █ █ █ ▇ ▆ ▅ ▄ ▂ ▁", "\n")
	print(" ▀▄▀▄▀▄ Computer lives: ", gameVars.computer_lives, "/" , gameVars.total_lives, " ▄▀▄▀▄▀" ,"\n")
	print(" ▀▄▀▄▀▄ Player lives: ", gameVars.player_lives, "/",gameVars.total_lives, "▄▀▄▀▄▀" ,"\n")
	print("    Time to choose your weapon!\n")
	print("░▒▓██████████████████████████████████▓▒░")

	gameVars.player = input("choose rock, paper or scissors: ")
	gameVars.player = gameVars.player.lower()

	print("computer chose ", gameVars.computer, "\n")
	print("player chose ", gameVars.player, "\n")

	compare.comparison(gameVars.player, gameVars.computer)




	# handle all lives lost for player or AI
	if gameVars.player_lives == 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives == 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0, 2)]	