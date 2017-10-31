the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list by assigning each element of the list to variable number with each iteration of the loop
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can create a numerical list with a range
elements = range(0,6)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

print("I can sort elements of a list:")
fruits.sort(key=None, reverse=False)

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

print("Or insert new elements:")
the_count.insert(2, 2.5)

for number in the_count:
    print(f"This is count {number}")

print("I can also remove values:")
change.remove('dimes')

for i in change:
    print(f"I got {i}")

print("And append elements to a list, even whole lists:")
change.append(fruits)

for i in change:
    print(f"I got {i}")
