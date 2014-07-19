import random

class Sudoku:

    
    num_rows = 9
    num_columns = 9

    def __init__(self):
        self.board = [] #board[row][col]
        self.count_list = [0,0,0,0,0,0,0,0,0]
        for i in range(self.num_rows):
            self.board.append([' '] * self.num_columns)

    def print_board(self):
        """Prints the formatted Sudoku board."""
        line = "---------------------"
        for i, row in enumerate(self.board):
            row_string = ""
            for j, col in enumerate(row):
                if j == 3 or j == 6:
                    row_string += "| "
                row_string += str(row[j]) + " "
            print(row_string)
            if i == 2 or i == 5:
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
        for i in range(self.num_columns):
            result.append(self.board[num_row][i])
        return result

    def return_col(self, num_col):
        """Returns column #NUM of the board as a list."""
        result = []
        for i in range(self.num_rows):
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
        for a in three: #row
            for b in three: #column
                result += [self.board[a+((num-1)//3)*3][b+(num%3-1)*3]]
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
                return True
        return False
        
    def check_column(self, num, num_col):
        """
        same logic as check_box, except starting at 0 
        """
        col = self.return_col(num_col)
        for board_num in col:
            if num == board_num:
                return True
        return False

    def check_row(self, num, num_row):
        """
        same logic as check
        """
        row = self.return_row(num_row)
        for board_num in row:
            if num == board_num:
                return True
        return False
        
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

    def done(self):
        print("Solution is:")
        self.print_board()
        return True

    def solve(self):
        """
          Backtracking algorithm for the sudoku solver. Takes in a Sudoku board;
          returns true iff algorithm successful, false otherwise.
        """
        # If board is filled, board is trivially solved
        if self.check_full_board():
            return self.done

        # Iterate over every square in the board
        for row in range(self.num_rows):
            for col in range(self.num_columns):

                # If square is empty, begin plugging in possible values
                if self.check_empty_space(row, col):
                    for val in range(1, 10):
                        if not self.check_row(val, row) and \
                           not self.check_column(val, col) and \
                           not self.check_box(val, self.what_box(row, col)):
                            self.board[row][col] = val
                        
                            if self.solve():
                                return self.done()
                        
                            # Didn't work; undo assigment
                            self.board[row][col] = ' '

        # Bad path; backtrack
        return False


#end of Michelle's space


#Jerry's space

    #if not enough to fill all columns, will leave rest of columns blank
    def num_to_rows(self, row):
        '''Type in a number in a row '''
        def reverse_number(number):
            num = 0
            while number > 0:
                num *= 10
                num += number%10
                number //= 10
            return num
        # row = int(input('Row number: '))
        print("Put Zeros as blanks")
        numbers = int(input('Numbers to add to ' + str(row) + ': '))
        numbers = reverse_number(numbers)
        col = 0
        while numbers > 0:
            if numbers%10 != 0:
                self.place_num(numbers%10, row, col)
            numbers //= 10
            col += 1

    def manual_fill(self):
        for i in range(self.num_rows):
            print("Row " + str(i) + ": ")
            self.num_to_rows(i)

    def random_fill(self):
        for row in range(self.num_rows):
            for col in range(self.num_columns):
                num = random.randrange(10)
                if num != 0:
                    self.place_num(num, row, col)    




















#end of Jerry's space       

