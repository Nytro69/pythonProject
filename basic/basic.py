# for workshop as school activity
print("hello, world")

# following program helps with explaining: lists, values (as x in this case), functions, printf.
while True:
    name = input("Name: ")
    # Let us say that you can only choose between a list of names
    names = [""] # names of something, Don't know what in this example.
    if name not in names:
        print(f"hello, {name}")
        break
    else:
        continue

x = input("Number: ")
y = input("Number: ")

# differance between int and str.

print(x + y)

x = int(x)
y = int(y)

print(x / y)

def hypiothenuse():
    ...


def guess(a: int, b: int, c: int):
    a = c
    c = b
    b = a

    print(b + c)

guess(1, 3, 5)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
num = int(input("Enter a number to calculate its factorial: "))
print("Factorial of", num, "is", factorial(num)

def square(n, power):
    if not power.isdigit():
        return "no decimal powers"




"""
Variables and data types (integers, floats, strings)
Basic arithmetic operations
Print statements
Input from users (using input())

Introduce conditionals (if, elif, else).
Explain loops (for and while).

Explain what functions are and why they’re essential.
Teach students how to define and call functions.

Create simple functions (e.g., a function to calculate the area of a rectangle).

Cover lists (arrays) and their manipulation.
Show how to iterate through lists using loops.

Creating ASCII art.

csv files? (if good enough)
"""
# 1- primitives
# 2- means of combination
# 3- means of abstraction


# Sequence (one instruction after the other)
# selection (make decision, take different paths based on conditions) (if)
# iteration (ability to repeat) (while, for)