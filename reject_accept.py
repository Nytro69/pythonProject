# 37% REJECT
from random import randint
x  = int(input("Numbers: ").strip())

numbers = []
for _ in range(x):
    integer = randint(-10000, 10000)
    numbers.append(integer)

for i in numbers:
    while True:
        que = input(f"{i}: ").strip().lower()
        if que == "r":
            break
        if que == "a":
            print(f"biggest number was: {max(numbers)}, Your was: {i}")
            quit()
print("you lose")