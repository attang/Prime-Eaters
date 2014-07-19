class Sudoku:

    from random import randrange
    num_rows = 9
    num_columns = 9

    def __init__(self):
        self.board = [] #board[row][col]
        self.count_list = [0,0,0,0,0,0,0,0,0]
        for i in range(self.num_rows):
            self.board.append([' '] * self.num_columns)

    def printBoard(self):
        """Prints the formatted Sudoku board."""
        line = "---------------------"
        for i, row in enumerate(self.board):
            rowString = ""
            for j, col in enumerate(row):
                if (j == 3 or j == 6):
                    rowString += "| "
                rowString += row[j] + " "
            print rowString
            if (i == 2 or i == 5):
                print line

    def get_board(self):
        return self.board

    def check_empty_space(self, row, column):
        """Return true iff position (row, column) of the board is empty."""
        return self.board[row][column] == ' '

    def check_full_board(self): #rows then columns
        """Returns true iff the board is filled."""
        for row in self.board:
            for column_of_row in row:
                if column_of_row == ' ':
                    return False
        return True

    def return_row(self, num_row):
        """Returns row #NUM of the board as a list."""
        result = []
        for i in range(num_columns):
            result.append(self.board[num_row][i])
        return result

    def return_col(self, num_col):
        """Returns column #NUM of the board as a list."""
        result = []
        for i in range(num_rows):
            result.append(self.board[i][num_col])
        return result

    def return_box(self, num):
      """
        Returns a 3x3 subgrid of the board as a list.
        Board indexed as:
                            1 2 3
                            4 5 6
                            7 8 9,
        where each index represents a 3x3 subgrid.
      """
        result = []
        three = [0, 1, 2]
        for a in three:
            for b in three:
                result += self.board[a+((num-1)//3*3)][b+(num%3-1)*3]
        return result


    def check_3x3(self, box):
      """Returns true iff the 3x3 subgrid BOX contains NUM."""

    def place_num(self, num, row, column):
        self.board[row][column] = num

    def generate_random_board(self):
        # while min(count_list) > 9: #checks if there's a number not used 9 times
        #   num_to_add = randrange(9) + 1
        #   if self.count_list[num_to_add-1] !> 10:
        #       if check_3x3(self.board):
                    #put number in a place on the board


#make some way to add numbers to the board

# board = Sudoku()
# print(board.board)
# board.get_board()


class Solver(Sudoku):


    def solve(board):
        for i in len(count_list):
            while max(count_list) < 9:
