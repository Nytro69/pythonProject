def reduce(list, func):
    if len(list) == 0:
        raise Exception("Empty list")

    accumulator = list[0]
    for i in range(1, len(list)):
        accumulator = func(accumulator, list[i])

    return accumulator


def eval_expr(expr: str):
    expr = expr.replace(" ", "")
    return eval_add_expr(expr)

def eval_add_expr(expr: str):
    return eval_generic_expr(expr, '+', eval_minus_expr, lambda x, y: x + y)

    # args = expr.split('+')
    # args = list(map(lambda arg: eval_minus_expr(arg), args))
    #
    # if len(args) == 0:
    #     raise Exception("Expected number")
    #
    # return reduce(args, lambda x, y: x + y)

def eval_minus_expr(expr: str):
    return eval_generic_expr(expr, '-', eval_mult_expr, lambda x, y: x - y)

    # args = expr.split('-')
    # args = list(map(lambda arg: eval_mult_expr(arg), args))
    #
    # if len(args) == 0:
    #     raise Exception("Expected number")
    #
    # return reduce(args, lambda x, y: x - y)

def eval_mult_expr(expr: str):
    return eval_generic_expr(expr, '*', eval_div_expr, lambda x, y: x * y)

    # args = expr.split('*')
    # args = list(map(lambda arg: eval_div_expr(arg), args))
    #
    # if len(args) == 0:
    #     raise Exception("Expected number")
    #
    # return reduce(args, lambda x, y: x * y)

def eval_div_expr(expr: str):
    return eval_generic_expr(expr, '/', eval_pow_expr, lambda x, y: x / y)

    # args = expr.split('/')
    # args = list(map(lambda arg: eval_pow_expr(arg), args))
    #
    # if len(args) == 0:
    #     raise Exception("Expected number")
    #
    # return reduce(args, lambda x, y: x / y)

def eval_pow_expr(expr: str):
    return eval_generic_expr(expr, '^', eval_number, lambda x, y: x ** y)

    # args = expr.split('^')
    # args = list(map(lambda arg: eval_number(arg), args))
    #
    # if len(args) == 0:
    #     raise Exception("Expected number")
    #
    # return reduce(args, lambda x, y: x ** y)


def eval_number(expr: str):
    return float(expr)


def eval_generic_expr(expr: str, op: str, next_fn, reducer):
    args = expr.split(op)
    args = list(map(next_fn, args))

    if len(args) == 0:
        raise Exception("Expected number")

    return reduce(args, reducer)


def parse_number(s: str, i: int) -> str:
    j = i + 1

    while s[j].isdigit():
        j += 1

    return s[i: (j - i)]

def parse(s: str):
    s = s.replace(" ", "")

    tokens = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            token = parse_number(s, i)
        elif s[i] in "+-*/":
            token = s[i]
        else:
            raise Exception(f'Invalid token {s[i]}')

        i += len(token)
        tokens.append(token)

    return tokens


print(eval_expr("1 + 2 * 3 ^ 2 + 1 + 40 / 2 ^ 2 - 10 + 22"))