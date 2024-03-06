import random

def main():
    op = getoperator()
    lev = get_level()
    generate_integer(lev, op)

def getoperator():
    while True:
        operator = input("Operator: ")
        if operator in ['+', '-', '*', '/', '^', '**']:
            return operator
        else:
            print("Invalid operator")
            continue

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            print("Not an integer")
            continue
        else:
            if level < 1 or level > 3:
                print("Enter a valid level (1-3)")
                continue
            else:
                return level

def levelact(min, max, op):
    m = 10
    for i in range(10):
        num = random.randint(min, max)
        num2 = random.randint(min, max)
        s = 0
        while True:
            if op == '+':
                r = num + num2
            elif op == '-':
                r = num - num2
            elif op == '*':
                r = num * num2
            elif op == '/':
                r = num / num2
            elif op == '^' or op == '**':
                r = num ** num2
            r = str(r)
            user = input(f"{num} {op} {num2} = ")
            if user != r:
                print("EEE")
                s += 1
                if s == 3:
                    m -= 1
                    print(f"{num} {op} {num2} = {r}")
                    break
                else:
                    continue
            else:
                break
    print(f"you got {m}/10")


def generate_integer(level, op):
    if level == 1:
        levelact(1, 10, op)
    elif level == 2:
        levelact(1, 100, op)
    elif level == 3:
        levelact(1, 1000, op)

if __name__ == "__main__":
    main()