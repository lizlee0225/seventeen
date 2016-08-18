import random

def human_input(marbles):
	human = input("Your turn: How many marbles will you remove (1-3)? ")
	# If the human enters incorrect input (anything other than 1, 2, 3, 
	# or a number larger than the number of marbles remaining in the jar), 
	# an error message should be displayed, and the human is prompted to try again.
	try:
		human = int(human)
	except:
		print("Sorry, that is not a valid option. Try again!")
		return 0
	if human < 1 or human > 3 or human > marbles:
		print("Sorry, that is not a valid option. Try again!")
		return 0
	else:
		# At the end of each turn, the program should print out the 
		# number of marbles removed in the previous turn
		print("You removed {} marbles.".format(human))
	return human

def computer_input(marbles):
	print("Computer's turn...")
	if marbles > 3:
		computer = random.randint(1,3)
	else:
		computer = random.randint(1, marbles)
	print("Computer removed {} marbles.".format(computer))
	return computer

def check_winner(marbles, winner):
	if marbles == 0:
		print("There are no marbles left. {} wins!".format(winner))
		quit()

def interactive_mode():
	print("Let's play the game of Seventeen!")
	marbles = 17
	while marbles > 0:
		human = 0
		while human == 0:
			human = human_input(marbles)
			marbles -= human
			print("Number of marbles left in jar: {}\n".format(marbles))
			check_winner(marbles, 'Computer')
		# Computer chooses random number
		computer = computer_input(marbles)
		marbles -= computer
		print("Number of marbles left in jar: {}\n".format(marbles))
		check_winner(marbles, 'You')
		



def main():  
	print(interactive_mode())


if __name__ == '__main__':
    main()
