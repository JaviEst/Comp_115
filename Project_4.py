# Javier Esteban de Celis
# November 5th 2017 
# Project 4 -> Comp 115 
# Wheaton College Ma


# Program    : Convertion from Binary to Decimal and vice versa.

# Description: This program implements versions of the built-in int() and bin() funtions 

# Input      : Name of file
# Output     : The program outputs the convertion of the numbers. 
#              If the number is decimal it shows the binary number, 
#              If the number is binary it shows the decimal number.


# PROMPT FOR FILE NAME
def name_file():
    # Function to prompt for the name of a file
    # Pre condition: None
    # Postcondition: return the name of the file

    file = input ("Enter the name of a file: ")
    return (file)


# CONVERTS FROM BINARY TO DECIMAL
def int(decimal):
    # Function to convert from binary to decimal
    # Pre condition: code equal to 1
    # Postcondition: return the binary number of the file converted to decimal

    # Takes care of negative numbers
    negative = False
    if (decimal[0] == '-'):
        negative = True
        decimal = decimal[1:]

    # Converting from binary to decimal
    power = 0 
    total = 0
    for i in decimal[::-1]:
        if (i == '1'):
            total = total + (2**power)
            power = power + 1
        elif (i == '0'):
            power = power + 1

    # Adds negative sign if necessary
    if negative:
        total = '-' + str (total)
    return (total)
    

# CONVERTS FROM DECIMAL TO BINARY
def bin(binary):
    # Function to convert from decimal to binary
    # Pre condition: code equal to 2 
    # Postcondition: return the decimal number of the file converted to binary
    
    # Takes care of negative numbers
    negative = False
    if (binary[0] == '-'):
        negative = True
        binary = binary[1:]

    remainder = ''

    # Converting from decimal to binary
    binary = eval(binary)

    if(binary == 0):
        remainder = '0'

    while (binary != 0):
        remainder = remainder + str (binary % 2)
        binary = binary // 2

    # Adds negative sign if necessary
    if negative:
        remainder = str (remainder) + '-'

    return (remainder[::-1])
        

def main():
    # Open file
    infile = open (name_file(), "r")

    print()
    
    # Read file
    code = infile.readline()
    
    while (code != "3"):

        num = infile.readline()

        # Calling apropriare function depending on code value from file
        if (code[0] =='1'):
            print ("The decimal number is:", int(num))
            
        elif (code[0] == '2'):
            print ("The binary number is:", bin(num))
        
        code = infile.readline()

    print ("\nALL DONE")
    
    # Close file
    infile.close()

main()
