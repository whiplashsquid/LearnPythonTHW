def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some maths with just functions!")

age = add(24, 34)
height = subtract(100, 1023)

print("Here is a puzzle.")

what = divide(age, height)
print("That becomes: ", what, "Can you do it by hand?")
