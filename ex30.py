people = 30
cars = 40
trucks = 15

# when the operand is true, the sttring is printed
if cars > people:
    print("We should take the cars.")
# when above operand is false and this operand is true, the string is printed (if above operand is true then this step is skipped)
elif cars < people:
    print("We should not take the cars.")
# when both preceding operands are false, the final string in the code block is printed (if either of above operands are true then this step is skipped)
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
