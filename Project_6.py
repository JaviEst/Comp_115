# Javier Esteban de Celis
# December 8th 2017 
# Project 6 -> Comp 115 
# Wheaton College Ma
#
# Program    : Sudoku Validation

# Description: This program will take a file with numbers from 1 to 9. 
#              It will display the numbers in a sudoku board and check if 
#              the columns, rows, and boxes are correct.

# Input      : File name containing solved sudoku.

# Output     : The program will display the sudoku board,
#              as well as which rows, columns, or boxes are incorrect.


class Sudoku:
    def __init__(self):
        # Constructor
        # Pre condition: None
        # Postcondition: Initialize the 2 dimensional array 
        
        self.sdk = [[' ' for i in range (9)] for j in range (9)]

    def setBoard(self, val, row, col):
        # Sets sudoku board
        # Pre condition: val has to be a number between 1 and 9 including both. row is the number of the row. col is the number of the column.
        # Postcondition: Sets the numbers in the board

        self.sdk [row][col] = int (val)

    def printBoard(self):
        # Print sudoku board
        # Pre condition: the board is filled
        # Postcondition: displays the board
           
        for i in range (10):
            if (i % 3 == 0):
                    print ("+-------+-------+-------+")
            for j in range (10):
                if (j % 3 == 0 and i < 9  and j < 9):
                    print ("|", self.sdk [i][j], end=" ")
                elif (i < 9  and j < 9):
                    print (self.sdk [i][j], end=" ")
                elif (j == 9 and i < 9):
                    print("|", end=" ")
            print ()
    
    def checkRow(self, row):
        # Function to check if the rows of the sudoku are correct or incorrect
        # Pre condition: the variable row is the  number of the row and it must be a number between 0 and 8 including both
        # Postcondition: it lets the code know if the rows are correct or incorrect

        found = [False for i in range(10)]
        for i in range (9):
            val = int(self.sdk[row][i])
            if found [val]:
                return False
            found [val] = True
        return True
    
    def checkCol(self, col):
        # Function to check if the columns are correct or incorrect
        # Pre condition: the variable col is the number of the columns and it must be a number between 0 and 8 including both
        # Postcondition: it lets the code know if the columns are correct or incorrect

        found = [False for i in range(10)]
        for i in range (9):
            val = int(self.sdk[i][col])
            if found [val]:
                return False
            found [val] = True
        return True        

    def checkBox(self, row_offset, col_offset):
        # Function to check if the sudoku boxes are correct or incorrect
        # Pre condition: row_offset and col_offset determine the number of the boxes. They have to be numbers between 0 and 2 including both.
        # Postcondition: it lets the code know if the boxes are correct or incorrect

        found = [False for i in range(10)]
        for i in range (3):
            for j in range (3):
                val = self.sdk[row_offset + i] [col_offset + j]
                if found [val]:
                    return False
                found [val] = True
        return True                
    


# PROMPT FOR THE NAME OF A FILE
def name_file():
    # Function to prompt for the name of a file
    # Pre condition: None
    # Postcondition: return the name of the file

    file = input ("Enter the name of a file: ")
    return (file)

def main():
    # OPEN FILE
    infile = open (name_file(), "r")
    
    sdk = Sudoku()
    row = 0
    
    # READ THE FILE AND SET THE NUMBERS OF THE FILE INSIDE THE BOARD
    for line in infile:
        line = int(line)
        line = str(line)
        
        for val in range (9):
            sdk.setBoard(line[val],row, val)
        
        row = row + 1
    
    infile.close()

    sdk.printBoard()
    print ()
    
    # CHECK THAT THE ROWS ARE CORRECT
    for i in range (9):
        if not sdk.checkRow(i):
            print ("Row number", i+1, "is incorrect! Try again.")
    print()
    
    # CHECK THAT THE COLUMNS ARE CORRECT
    for i in range (9):
        if not sdk.checkCol(i):
            print ("Column number", i+1, "is incorrect!! Try again.")
    print()
    
    # CHECK THAT THE BOXES ARE CORRECT
    for i in range (3):
        for j in range (3):
            if not sdk.checkBox(i*3, j*3):
                print ("Box number", i+1, j+1, "is incorrect!! Try again.")
    
    
    
main()
