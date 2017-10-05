# prints formatted string
print("What file would you like to open and read?")
# prints a prompt string and then uses input function to take data from user and assign it to variable name file_again
filename = input("> ")

# uses open function to open the file the user inputted which is assigned to variable name file_again and assigns its contents to txt_again
txt = open(filename)

# prints contents of file bound to variable name txt_again using read function to access
print(txt.read())

# close files again
txt.close()
