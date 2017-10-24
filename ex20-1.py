from sys import argv

script, input_file = argv

# defines the print_all function as printing the file which is a parameter of the function and assigned to variable name f
def print_all(f):
    print(f.read())

# defines rewind function which seeks the 0 byte position of the file assigned to f
def rewind(f):
    f.seek(0)

# defines print_a_line function as one which takes the variable parameters line_count and f and returns a print of the data assigned to variable line_count and then prints a line of the file assigned to f according the position in the current position within the file. After each call of the function the position in the file is set at the next line by use of the readline function rather than read which gives the whole file. end = "" stops the \n written into the file f being included in the print.
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

# opens file imported from command line and assigned to variable input_file and assigns contents as string to current_file variable name
current_file = open(input_file)

# prints a string and moves to the next line
print("First let's print the whole file:\n")
# calls print_all function on parameter current_file
print_all(current_file)
# prints a string
print("Now let's rewind, kind of like a tape.")
# calls rewind function on parameter current_file
rewind(current_file)
# prints a string
print("Let's print three lines:")

# assigns character 1 to variable name current_line
current_line = 1
# calls print_a_line function with the parameters current_line and current_file: first iteration returns a print 1 then the first line of the file assigned to f
print_a_line(current_line, current_file)
# assigns the result of a maths function to the variable current_line (i.e. changes the state of the variable within the script). Maths function is binary function 'add' using parameters current_line and 1 so that whatever the current state of the variable current_line is, it's state is changed by +1 everytime this line is run through
current_line += 1
# calls print_a_line function: second iteration returns result of 1 + 1 (i.e. 2) then next line of the file assigned to f
print_a_line(current_line, current_file)
# assigns next state change to current_line
current_line += 1
# calls print_a_line function: third iteration returns result of 2 + 1 (i.e. 3) then next line of the file assigned to f
print_a_line(current_line, current_file)
