name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = round(height * 2.54) # conversion to cm using round function to curtail floating point number
weight = 180 # lbs
weight_kg = round(weight * (1 / 2.2)) # conversion to kg using round function to curtail floating point number
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# print formatted string with embedded variable
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall which is {height_cm} centimetres (rounded to the nearest cm).")
print(f"He's {weight} pounds heavy which is {weight_kg} kilograms (rounded to the nearest kg).")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usuallly {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
