class recursiveNQueens:
	def __init__(self, N):
		self.N = N
		self.QUEENS = []
		self.solutions = []
		
	def solve(self):
		self.solutions = [] 
		self.recursive_call(1)
		return self.solutions
		
	def recursive_call(self, round):
		if round == self.N + 1:
			self.solutions.append(self.QUEENS[:])
		else:
			for possible_next in range(1, self.N + 1):
				legal = all(self.QUEENS[i] not in [possible_next, possible_next + round - (i + 1), possible_next - round + (i + 1)] for i in range(round - 1))
				if legal:
					self.QUEENS.append(possible_next)
					print(self.QUEENS)
					self.recursive_call(round + 1)
					self.QUEENS.pop()
					
print(len(recursiveNQueens(8).solve()))
