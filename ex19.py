# defines function cheese_and_crackers as having two parameters, cheese_count and boxes_of_crackers, and acting by printing a series of strings
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
# passes number values directly to function as argument variables which are called by the function in the same way as previously i.e. inserted into a formatted string to be printed
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
# gives number value (characters to a string, not integers) to a variable name and passes the variables to the function as parameters
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_crackers, amount_of_cheese)


print("We can even do math inside too:")
# passes maths functions as parameters
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# passes maths functions (themselves taking variable names and integers as parameters) to the function as parameters
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
