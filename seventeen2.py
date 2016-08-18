import random

def input_file(filename):
	move_lst = []
	move_dict = {}
	with open(filename, 'r') as file:
		move_lst = file.readlines()
	for index, item in enumerate(move_lst):
		item = item.strip().split(',')
		item = [int(x) for x in item]
		move_dict.setdefault(index, item)
	return move_dict

def player1(game_n, turn, marbles):
	# The program reads from an input file with sequence of moves made by Player 1.
	p1_moves = input_file('i206_placein_input_0.txt')
	# Player 1 removes all the remaining marbles if marbles left is fewer 
	if p1_moves[game_n][turn-1] > marbles:
		return marbles
	else:
		return p1_moves[game_n][turn-1]


def player2(marbles):
	# Random number not greater than the number of marbles remaining
	if marbles == 0:
		return 0
	elif marbles >= 3:
		p2_input = random.randint(1,3)
	else:
		p2_input = random.randint(1, marbles)
	return p2_input	

def check_winner(marbles, turn, file, p1, p2):
	if marbles != 0:
		file.write('{}-{}-'.format(p1, p2))
	else:
		if p2 == 0:
			file.write("{}. Winner: P2\n".format(p1))
			return False
		else:
			file.write("{}-{}. Winner: P1\n".format(p1, p2))
			return True

def play_game():
	game_n = 0
	output = open('Output.txt', 'w')
	p1_win = 0
	p2_win = 0
	while game_n < 10:
		marbles = 17
		output.write("Game #{}. Play sequence: ".format(game_n+1))
		turn = 0
		while marbles > 0:
			turn += 1
			p1 = player1(game_n, turn, marbles)
			marbles = marbles - p1
			p2 = player2(marbles)
			marbles = marbles - p2
			check_winner(marbles, turn, output, p1, p2)
		# Counts number of wins by player
		if p2 == 0:
		 	p2_win += 1
		else:
		 	p1_win += 1
		game_n += 1
	output.write("Player 1 won {} times; Player 2 won {} times.".format(p1_win, p2_win))
	output.close()



def main():
	play_game()


if __name__ == '__main__':
    main()

