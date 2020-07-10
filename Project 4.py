# I have abided by the Wheaton Honor Code in this work.
#
# Javier Esteban
#
# Program    : Convertion from Binary to Decimal and vice versa.
# Description: This program uses different functions to first read a file and then convert the numbers from the file to binary or decimal. One function asks you for the name of the file you want to use, while the other functions compute the convertions and ouput them.
# Input      : Input the name of a file so the program can read it and start to execute the convertions.
# Output     : The program output the convertion of the numbers. If the number is decimal it shows you its binary number, and if it is binary it shows you its decimal number.

# PROMPT FOR THE NAME OF A FILE
def name_file ():
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
    negative = False
    if (decimal[0] == '-'):
        negative = True
        decimal = decimal[1:]
    #CONVERTION FROM BINARY TO DECIMAL
    power = 0 
    total = 0
    for i in decimal[::-1]:
        if (i == '1'):
            total = total + (2**power)
            power = power + 1
        elif (i == '0'):
            power = power + 1
    if negative:
        total = '-' + str (total)
    return (total)
    
# CONVERTS FROM DECIMAL TO BINARY
def bin (binary):
    # Function to convert from decimal to binary
    # Pre condition: code equal to 2 
    # Postcondition: return the decimal number of the file converted to binary
    negative = False
    if (binary[0] == '-'):
        negative = True
        binary = binary[1:]
    remainder = ''
    #CONVERTION FROM DECIMAL TO BINARY
    binary = eval(binary)
    while (binary != 0):
        remainder = remainder + str (binary % 2)
        binary = binary // 2
    if negative:
        remainder = str (remainder) + '-'
    return (remainder[::-1])
        

def main():
    # OPEN FILE
    infile = open (name_file(), "r")
    
    # START TO READ THE FILE
    code = infile.readline()
    
    while (code != "3"):
        code = eval(code)
        code = str(code)
        num = infile.readline()
        num = eval(num)
        num = str (num)
        
        if (code == "1"):
            print ("The decimal number is:", int(num))
            
        elif (code == "2"):
            print ("The binary number is:", bin(num))
        
        code = infile.readline()
    print ("All Done")
    
    # CLOSE FILE
    infile.close()

main()