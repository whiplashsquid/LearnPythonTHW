from sys import argv
script, person1, person2, person3 = argv

print("There are three people in a room:", person1, person2 + " and", person3 + ".")
print("How old is ", person1 + "?", end=' ')
age1 = int(input())
print("How old is ", person2 + "?", end=' ')
age2 = int(input())
print("How old is ", person3 + "?", end=' ')
age3 = int(input())
total = int(age1) + int(age2) + int(age3)
print(f"So the total age of all three people is: {total} years")
