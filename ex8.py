# assigns empty data spaces to variable name formatter
formatter = "{} {} {} {}"

# prints numbers, string, Boolean types and the data assigned to variable name formatter
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
# prints string all in one line despite being scripted across four lines as separate strings
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
