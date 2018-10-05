import numpy as np
np.random.seed(999999)
board = np.random.randint(1, 4, 100).reshape(10, 10)
print(board)

matched = np.zeros((10, 10), dtype=int)


for i in range(len(board)):
	for j in range(len(board[0])):
		# check horizontal
		try:
			if board[i][j] == board[i][j+1] == board[i][j+2]:
				matched[i][j] = board[i][j]
				matched[i][j+1] = board[i][j]
				matched[i][j+2] = board[i][j]
		except IndexError:
			pass
		# check vertical
		try:
			if board[i][j] == board[i+1][j] == board[i+2][j]:
				matched[i][j] = board[i][j]
				matched[i+1][j] = board[i][j]
				matched[i+2][j] = board[i][j]
		except IndexError:
			pass

print(matched)
