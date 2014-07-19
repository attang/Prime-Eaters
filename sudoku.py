class Sudoku:

	from random import randrange
	num_rows = 9
	num_columns = 9

	def __init__(self):
		self.board = [] #board[row][col]
		self.count_list = [0,0,0,0,0,0,0,0,0]
		for i in range(self.num_rows):
			self.board.append([' '] * self.num_columns)

	def get_board(self):
		return self.board

	def check_empty_space(self, row, column):
		return self.board[row][column] == ' '

	def check_full_board(self): #rows then columns
		for row in self.board:
			for column_of_row in row:
				if column_of_row == ' ':
					return False
		return True

	def return_row(self, num_row):
		result = []
		for i in range(num_columns):
			result.append(self.board[num_row][i])
		return result

	def return_col(self, num_col):
		result = []
		for i in range(num_rows):
			result.append(self.board[i][num_col])
		return result

	def return_box(self, num):
		'''boxes go 1, 2, 3
					4, 5, 6
					7, 8, 9'''
		result = []
		three = [0, 1, 2]
		for a in three:
			for b in three:
				result += self.board[a+((num-1)//3*3)][b+(num%3-1)*3]
		return result

    def check_box(self, num, box_num):
    # this method checks if a specific box already has a specific number
    # @self is the board object
    # @num is the specific number being checked
    # @box_num is the box number of the board in row major order, starting from 1
    # @return returns true if the box already has the number, false otherwise
        
        box = self.return_box(self, box_num):
        

	def check_3x3(self, box):
		'''checks whether the 3x3 grid (box) has the number in it
			returns True or False'''


	def place_num(self, num, row, column):
		self.board[row][column] = num

	def generate_random_board(self):
		# while min(count_list) > 9: #checks if there's a number not used 9 times
		# 	num_to_add = randrange(9) + 1
		# 	if self.count_list[num_to_add-1] !> 10:
		# 		if check_3x3(self.board):
					#put number in a place on the board


#make some way to add numbers to the board

# board = Sudoku()
# print(board.board)
# board.get_board()


class Solver(Sudoku):


	def solve(board):
		for i in len(count_list):
			while max(count_list) < 9:
