class Sudoku:

	from random import randrange
	num_rows = 9
	num_columns = 9

	def __init__(self):
		self.board = []
		self.count_list = [0,0,0,0,0,0,0,0,0]
		for i in range(self.num_rows):
			self.board.append([' '] * self.num_columns)

	def get_board(self):
		return self.board

	def check_3x3(board):
		'''checks whether the 3x3 grid has the number in it
			returns True or False'''

	def generate_random_board(self):
		while min(count_list) > 9: #checks if there's a number not used 9 times
			num_to_add = randrange(9) + 1
			if self.count_list[num_to_add-1] !> 10:
				if check_3x3(self.board):
					#put number in a place on the board


#make some way to add numbers to the board

board = Sudoku()
print(board.board)
board.get_board()


class Solver(Sudoku):


	def solve(board):
		for i in len(count_list):
			while max(count_list) < 9:
