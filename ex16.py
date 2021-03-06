# imports function argv (takes specified number of argument variables from command line and binds them to argv) from sys module
from sys import argv
# assigns data from command line (bound to argv) to variable names script and filename in the order they were passed to python by user
script, filename = argv
# prints formatted string including the data bound to filename (lines 7 & 8 print strings)
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# prompts user to input data with ? string - they should answer with either CTRL-C or RETURN as instructed above thus quitting script or running following code
input("?")
# prints string
print("Opening the file....")
# opens file bound to filename from command line in write mode and assigns contents to variable name target
target = open(filename, 'w')
# prints string
print("Truncating the file. Goodbye!")
# applies truncate function with no variable to target variable (ie. your file) thereby erasing all previous contents
target.truncate()
# prints strings
print("Now I'm going to ask you for three lines.")
# prompts for input with string, binds each input in turn to variable names line1, line2, line3
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
# prints string
print("I'm going to write these to file.")
# applies write function with variable given in () to file associated with target variable name. Nb. each \n writes to newline
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# prints string
print("And finally, we close it.")
# closes file associated with variable name target
target.close()
