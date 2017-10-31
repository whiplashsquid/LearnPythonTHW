def numlist(start, numbers, stop):
    i = start
    while i < stop:
        print(f"At the top index value is {i}")
        numbers.append(i)

        i += 1

        print("Numbers now: ", numbers)
        print(f"At the bottom index value is is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

print("Give me a number from 1-10:")
numlist(0, [], int(input("> ")))
