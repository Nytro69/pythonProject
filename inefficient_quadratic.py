import random

def k(b1, a1):
    if a1 < 0:
        b1 = b1 * 1
        a1 = a1 * 1
    if b1 > a1:
        return b1
    else:
        return a1


equation = input("x^2 ax b, type: a, b ")
b1, a1 = equation.split(", ")
b1 = int(b1)
a1 = int(a1)

while True:
    a = random.randint(-100, k(b1, a1))
    b = random.randint(-100, k(b1, a1))
    if b + a == b1 and b * a == a1:
        print(f"a is {a} and b {b}")
        break
    else:
        continue