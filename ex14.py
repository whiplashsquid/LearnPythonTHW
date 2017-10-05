# imports from sys module and holds with argv
from sys import argv
# assigns contents of sys module to variables script and user_name. Requires 2 arguments to be passed to Python in command line
script, user_name = argv
# assigns string to variable name script
prompt = 'Type answer here: '

# prints strings and formatted strings
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
# prints prompt to user to input data which is then assigned to likes
likes = input(prompt)

# prints formatted string
print(f"Where do you live {user_name}?")
# prints prompt to user to input data which is then assigned to lives
lives = input(prompt)

# prints string
print("What kind of computer do you have?")
# prints prompt to user to input data which is then assigned to computer
computer = input(prompt)

# prints larger formatted string as paragraph
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
