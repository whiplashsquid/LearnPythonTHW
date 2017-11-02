def numlist(start, numbers, stop, increment):
    i = start
    incr = increment
    while i < stop:
        print(f"At the top index value is {i}")
        numbers.append(i)

        i += incr

        print("Numbers now: ", numbers)
        print(f"At the bottom index value is is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

print("Give me a stopping value from 1-100:")
end = int(input("> "))
print("Give me an increment to apply from 1-10:")
value = int(input("> "))
numlist(0, [], end, value)
