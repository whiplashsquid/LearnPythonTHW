def numlist(begRange, endRange, incRange):
    numbers = [range(begRange, endRange[incRange])]
    begRange = numbers[0]
    for num in numbers:
        print(num)

print("Where would you like to start?", end=' ')
start = int(input("Number: "))
print("Where would you like to stop?", end=' ')
stop = int(input("Number: "))
print("How much would you like to increment by?", end=' ')
step = int(input("Number: "))
numlist(start, stop, step)
