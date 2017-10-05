# prints string and continues to next line without placing newline character
print("How old are you?", end=' ')
# assigns whatever you type in as input to variable name age
age = input()
# prints string and continues to next line without placing newline character
print("How tall are you?", end=' ')
# assigns whatever you type in as input to variable name height
height = input()
# prints string and continues to next line without placing newline character
print("How much do you weigh?", end=' ')
# assigns whatever you type in as input to variable name weight
weight = input()

# prints formatted string with embedded variables age, height and weight
print(f"So, you're {age} years old, {height} tall and {weight} heavy.")
