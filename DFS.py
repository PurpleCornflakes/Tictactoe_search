# This program searches all possible moves of tic tac toe via DFS
# by Chen and Ling
# 09052017

Nfirst = 0
Nsecond = 0
Tie = 0

class State: 
	'''
	state of the chess board
	'''
	def __init__(self, num=3):
		self.num = num
		self.player = {0: "X", 1: "O"}
		self.turn = 0 # turn of the next player
		self.first_move = 0
		self.moves = []
		self._state = []

	def vacancy(self):
		return [x for x in range(9) if x not in self._state]

	def update(self, pos):
		self.moves.append("{}{}".format(self.player[self.turn], pos))
		self._state.append(pos)
		self.turn = {1:0, 0:1}[self.turn]

	def cancel(self):
		if self._state:
			self._state.pop()
		if self.moves:
			self.moves.pop()
		self.turn = {1:0, 0:1}[self.turn]

	def is_final(self):

		if len(self._state) <= 4:
			return (False, -1)

		pos = self._state[-1]
		row = int(pos/self.num)
		col = pos%self.num
		win = False

		row_win = True
		for j in [(col+1)%self.num, (col+2)%self.num]:
			ind = row * self.num + j 
			if ind not in self._state:
				row_win = False
				break
			if self.turn == 1:
				if self._state.index(ind) % 2 != self.first_move % 2:
					row_win = False
			else:
				if self._state.index(ind) % 2 == self.first_move % 2:
					row_win = False

		col_win = True
		for i in [(row+1)%self.num, (row+2)%self.num]:
			ind = i * self.num + col
			if ind not in self._state:
				col_win = False
				break
			if self.turn == 1:
				if self._state.index(ind) % 2 != self.first_move % 2:
					col_win = False
			else:
				if self._state.index(ind) % 2 == self.first_move % 2:
					col_win = False

		win = win or (row_win or col_win)

		if row == col: 
			rdia_win = True
			for (i,j) in [((row+1)%self.num, (col+1)%self.num), ((row+2)%self.num, (col+2)%self.num)]:
				ind = i * self.num + j
				if ind not in self._state:
					rdia_win = False
					break
				if self.turn == 1:
					if self._state.index(ind) % 2 != self.first_move % 2:
						rdia_win = False
				else:
					if self._state.index(ind) % 2 == self.first_move % 2:
						rdia_win = False
			win = win or rdia_win
		if (row + col == self.num -1):
			ldia_win = True
			for (i,j) in [((row-1)%self.num, (col+1)%self.num), ((row-2)%self.num, (col+2)%self.num)]:
				ind = i * self.num + j
				if ind not in self._state:
					ldia_win = False
					break
				if self.turn == 1:
					if self._state.index(ind) % 2 != self.first_move % 2:
						ldia_win = False
				else:
					if self._state.index(ind) % 2 == self.first_move % 2:
						ldia_win = False
			win = win or ldia_win
		if win:
			return (True, 1 if self.turn==0 else 0)
		elif len(self._state) == self.num*self.num:
			return (True, -1)
		else:
			return (False, -1)


def search(state):
	'''
	searches all possible moves starting from current state
	'''
	global Nfirst, Nsecond, Tie
	final, winner = state.is_final()
	if final:
		# print(final, winner)
		if winner == -1:
			Tie += 1
			result="tie"
		elif winner == 0:
			Nfirst += 1
			result="{} win".format(state.player[0])
		else:
			Nsecond += 1
			result="{} win".format(state.player[1])
		print(state.moves, result)
		state.cancel()
		return 1
	for pos in state.vacancy():
		state.update(pos)
		# print("{}{} ".format(state.player[1 if state.turn == 0 else 0], pos))
		search(state)
	state.cancel()
	return 0 

state = State()
# test code
state.update(0)
state.update(1)
# state.update(2)
# state.update(3)
# state.update(4)
# state.update(5)
# state.update(6)
# print(state.is_final())
# quit()

search(state)
print("offensive move: ", Nfirst, "\ndefensivin move", Nsecond, "\ntie: ", Tie)

