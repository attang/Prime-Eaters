class Sudoku

num_rows = 9
num_columns = 9

def __init__(self):
	self.board = []
	for i in range(num_rows):
		self.board.append([' '] * num_columns)
