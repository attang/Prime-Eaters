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
                row_string += row[j] + " "
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

    def generate_random_board(self):
        # while min(count_list) > 9: #checks if there's a number not used 9 times
        #   num_to_add = randrange(9) + 1
        #   if self.count_list[num_to_add-1] !> 10:
        #       if check_3x3(self.board):
                    #put number in a place on the board
                          
#Allan's space

     def check_box(self, num, box_num):
        # this method checks if a specific box already has a specific number
        # @self is the board object
        # @num is the specific number being checked
        # @box_num is the box number of the board in row major order, starting from 1
        # @return returns true if the box already has the number, false otherwise       
        box = self.return_box(self, box_num)
    
#end of Allan's space 

#Michelle's space



























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
                self.place_num(num, row, col)




















#end of Jerry's space       

