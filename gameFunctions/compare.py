from gameFunctions import gameVars

def comparison(player, computer):
	if player == "quit":
		exit()
	elif computer == player:
		print("tie! no one wins, play again")

	elif player == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "smashes", computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif player == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "covers", computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif player == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", player, "cuts", computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	else:
		print("That's not a valid choice, try again"
    )