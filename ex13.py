# add modules to script from Python module set with import (ie. add sys module and holds it as argument with argv)
from sys import argv
# read the WYSS section for how to run this
# assigns the contents of argv to the variables given in order from left to right
script, first, second, third = argv

# prints string and whatever is held by each variable
print("The script is called", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
