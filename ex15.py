# imports argv from sys module so that you can take user data from the command line
from sys import argv

# assigns what you pass to python in command line to two variable names in order
script, filename = argv

# assigns contents of your file (bound to filename) to variable name txt using open function (takes parameter filename and returns a file object)
txt = open(filename)

# prints formatted string
print(f"Here's your file {filename}:")
# print contents of file bound to variable name txt using read function to access (commends txt file to be read with no parameter)
print(txt.read())

# prints formatted string
print("Type the filename again:")
# prints a prompt string and then uses input function to take data from user and assign it to variable name file_again
file_again = input("> ")

# uses open function to open the file the user inputted which is assigned to variable name file_again and assigns its contents to txt_again
txt_again = open(file_again)

# prints contents of file bound to variable name txt_again using read function to access
print(txt_again.read())

# close files again
txt.close()
txt_again.close()
