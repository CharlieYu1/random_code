import numpy as np
import itertools

ROWS = 6
COLUMNS = 7

play_sequence = '555424551003426542401004633101'

def all_equal_fixed(fixed, iterable):
	return all(i == fixed for i in iterable)

def check_board(play_sequence):
	board = np.zeros((COLUMNS, ROWS), dtype=int)
	row_height = np.zeros((COLUMNS,), dtype=int)
	msg = ''  # msg to display below the board
	
	current_player = 1  # 1st move at player 1
	def next_player():
		nonlocal current_player
		current_player = 3 - current_player
		
	for play in map(int, play_sequence):
		h = row_height[play]
		if h < 6:
			board[play][5 - h] = current_player
			row_height[play] += 1
		else:
			msg = f"Can't play at column {play}"
			return board, msg
		
		# check winner
		for i, j in itertools.product(range(COLUMNS), range(ROWS)):
			for dir_x, dir_y in [(1,0), (0,1), (1,1), (1,-1)]:
				try:
					if all_equal_fixed(current_player,
							(board[i + s * dir_x][j + s * dir_y] for s in range(4))):
						print(play)
						msg = f'Player {current_player} wins!'
						return board, msg
				except IndexError:
					pass
		next_player()
		
	msg = f'Next turn: Player {current_player}'
	return board, msg
	
def print_board(board, msg):
		
	# display board and message
	seperator = '+-+-+-+-+-+-+-+'
	print(seperator)
	for row in range(6):
		print(f'|{"|".join(map(str, board[:, row]))}|')
		print(seperator)
	print(f'Message: {msg}')
		
if __name__ == '__main__':
	print_board(*check_board(play_sequence))
