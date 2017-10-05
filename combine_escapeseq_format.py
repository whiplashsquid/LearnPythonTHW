# Assigns number ten (or binary number 2) to variable name types_of_people
types_of_people = 10
# assigns escape sequence format to variable name formatted
formatted = "{} \f{}"
# Assigns formatted string containing embedded variable types_of_people to variable name x
x = f"There are \"{types_of_people}\" types of people."

# Assigns string to variable name binary
binary = "binary"
# Assigns string to variabe name do_not
do_not = "don't"
# Assigns formatted string containing embedded variables binary and do_not to variable name y
y = f"Those who know {binary} \n\t\t\tand those who {do_not}."

# prints variable x
print(x)
# prints variable y
print(y)

# prints formatted string containing embedded variable x
print(f"I said: \f{x}")
# prints formatted string containing embedded variable y
print(formatted.format("I also said:", y))

# Assigns Boolean value to variable name hilarious
hilarious = True
# Assigns string with empty embedded variable space to variable name joke_evaluation
joke_evaluation = "Isn't that joke so funny?! \t\t\t{}"

# prints variable joke_evaluation but first formats the empty embedded variable by assigning it the variable hilarious
print(joke_evaluation.format(hilarious))

# Assigns string to variable name w
w = "This is the left side of..."
# Assigns string to variable name e
e = "a string with a right side."

# prints result of operation: variable name w plus variable name e
print(w + e)
