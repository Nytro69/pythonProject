"""
def parse_number(s: str, i: int) -> str:
    j = i + 1

    while s[j].isdigit():
        j += 1

    return s[i: (j - i)] # (j - i) is the problem
"""


def op(expression):
    operators = "+-*/^"
    for i in expression:
        if i in operators:
            return True
    return False


def parse_number(s: str, i: int) -> str:
    j = i + 1

    while j < len(s) and s[j].isdigit():
        j += 1

    return s[i: j]


def parse(s: str):
    expression = []
    s = s.replace(" ", "")
    i = 0

    while i < len(s):
        if s[i].isdigit():
            token = parse_number(s, i)
        elif s[i] in "+-*/^":
            token = s[i]
        else:
            raise Exception(f"Unknown token: {s[i]}")

        expression.append(token)
        i += len(token)
    return eval(expression)


def eval(expression):
    h = 2
    while op(expression):
        for x in range(len(expression)):

            if any(v in "^" for v in expression):
                ...
            else:
                h = 1
            if any(v in "/*" for v in expression) and h == 1:
                ...
            elif h == 1:
                h = 0

            if expression[x] == "^":
                expression[x - 1: x + 2] = [str(float(expression[x - 1]) ** float(expression[x + 1]))]
                break
            if expression[x] in "*/" and h == 1:
                if expression[x] == "*":
                    expression[x - 1: x + 2] = [str(float(expression[x - 1]) * float(expression[x + 1]))]
                    break
                if expression[x] == "/":
                    expression[x - 1: x + 2] = [str(float(expression[x - 1]) / float(expression[x + 1]))]
                    break


            if expression[x] in "+-" and h == 0:
                if expression[x] == "+":
                    expression[x - 1: x + 2] = [str(float(expression[x - 1]) + float(expression[x + 1]))]
                    break
                if expression[x] == "-":
                    expression[x - 1: x + 2] = [str(float(expression[x - 1]) - float(expression[x + 1]))]
                    break

    return float("".join(expression))

print(parse(input("Expression: ")))
