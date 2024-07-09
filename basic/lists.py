list = map(int, input("List: ").split(", "))
op = input("operator: ")
if op == "+":
    x = 0
    for i in list:
        x = x + i
if op == "*":
    x = 1
    for i in list:
        x = x * i

print(x)

def example(n):
    return n * n

print(example(3))