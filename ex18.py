# this one is like your scripts with argv; args is unpacked on the following line as a variable name that takes two arguments so that when the function is used (line 19) we must pass it two arguments to take an action on. The next line is the action, in this case printing a formatted string including the two arguments that we pass on line 19.
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this one takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
# don't forget colon(:) at end of function definition, otherwise code is not complete and every following line will be included
# def is the function define which we use to define our own functions. Follow def with a short name for the function which says what it does and then all the parameters we want attahced to this name in brackets.
