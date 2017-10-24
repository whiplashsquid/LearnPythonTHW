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
print("How old are you?", end=' ')
age = float(input())
print("How tall are you?", end=' ')
height = float(input())
print("How much do you weigh?", end=' ')
weight = float(input())
print("What is your IQ?", end=' ')
iq = float(input())

print(f"What can we do with your age: {age}, height: {height}, weight: {weight} & IQ: {iq}?")
print("Here is a puzzle.")

what = round(add(age, subtract(height, multiply (weight, divide(iq, 2)))))

print("That becomes: ", what, "(rounded). Can you do it by hand?")
