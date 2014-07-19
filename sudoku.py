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
            print(rowString)
            if (i == 2 or i == 5):
                print(line)

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
    
    def place_num(self, num, row, column):
        self.board[row][column] = num

                          
#Allan's space

    def check_box(self, num, box_num):
        """
        this method checks if a specific box already has a specific number
        @self is the board object
        @num is the specific number being checked
        @box_num is the box number of the board in row major order, starting from 1
        @return returns true if the box already has the number, false otherwise       
        """
        
        box = self.return_box(box_num)
        for board_num in box:
            if num == board_num:
                return true
        return false
        
    def check_column(self, num, num_col):
        """
        same logic as check_box, except starting at 0 
        """
        col = self.return_col(num_col)
        for board_num in col:
            if num == board_num:
                return true
        return false

    def check_row(self, num, num_row):
        """
        same logic as check
        """
        row = self.return_row(num_row)
        for board_num in row:
            if num == board_num:
                return true
        return false
        
    def what_box(self, i, j):
        if i <= 2:
            if j <= 2:
                return 1
            elif j <= 5:
                return 2
            else:
                return 3
        elif i <= 5:
            if j <= 2:
                return 4
            elif j< 5:
                return 5
            else:
                return 6
        else:
            if j <= 2:
                return 7
            elif j <= 5:
                return 8
            else:
                return 9
                
          
#end of Allan's space 

#Michelle's space

    def done(board):
        print("Solution is:")
        board.printBoard()
        return True

    def solve(board):
        """
          Backtracking algorithm for the sudoku solver. Takes in a Sudoku board;
          returns true iff algorithm successful, false otherwise.
        """
        # If board is filled, board is trivially solved
        if board.check_full_board():
            return done(board)

        # Iterate over every square in the board
        for row in range(Sudoku.num_rows):
            for col in range(Sudoku.num_columns):

                # If square is empty, begin plugging in possible values
                if board.check_empty_space(row, col):
                    for val in range(1, 10):
                        if not check_row(val, row) and \
                           not check_col(val, col) and \
                           not check_box(val, what_box(row, col)):
                            board.board[row][col] = val
                        
                            if solve(board):
                                return done(board)
                        
                            # Didn't work; undo assigment
                            board.board[row][col] = ' '

        # Bad path; backtrack
        return False;

#end of Michelle's space


#Jerry's space


























#end of Jerry's space       

