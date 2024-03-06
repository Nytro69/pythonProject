numbers = [1, 4, 3, 6, 18, 6]
length = len(numbers)
# Ex 1: Given a list of numbers, print the maximum.

high = max(numbers)

print(high)

# Ex 2: Given a list of numbers, print the minimum.

small = min(numbers)

print(small)

# Ex 3: Given a list of numbers, print the average.

total = 0

for i in numbers:
    total += i

average = total / length

print(average)

# Ex 4: sort the numbers and print them.

sorteds = []

for i in range(length):
    g = min(numbers)
    sorteds.append(g)
    numbers.remove(g)

print(sorteds)