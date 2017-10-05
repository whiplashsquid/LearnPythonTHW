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

txt.close()
filename.close()
