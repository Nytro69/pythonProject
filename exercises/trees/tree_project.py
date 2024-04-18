def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]

        # handle space
        if char.isspace(): # if char == " "
            i += 1
            continue

        # Handle numbers
        if char.isdigit():
            char1 = char
            while i + 1 < len(expression) and expression[i + 1].isdigit():
                i += 1
                char1 += expression[i]
            tokens.append(Token('number', char1))

        # Handle operators
        elif char in '+-*/':
            tokens.append(Token(char, char))

        # Handle parentheses
        elif char in '()':
            tokens.append(Token(char, char))

        else:
            raise Exception(f"Invalid character: {char}")

        i += 1

    return tokens


class Number:
    def __init__(self, x):
        self.value = x

    def eval(self):
        return self.value



class Operation:
    def __init__(self, op, exp_l, exp_r):
        self.op = op
        self.exp_r = exp_r
        self.exp_l = exp_l

    def eval(self):
        x = self.exp_l.eval()
        y = self.exp_r.eval()

        if self.op == "+":
            return x + y

        if self.op == "-":
            return x - y

        if self.op == "*":
            return x * y

        if self.op == "/":
            return x / y

class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def height(self) -> int:
        left_height = 0 if self.left is None else self.left.height()
        right_height = 0 if self.right is None else self.right.height()
        return 1 + max(left_height, right_height)



class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __str__(self):
        return f'[{self.type}: {self.value}]'


class Parser:
    def __init__(self):
        pass

    def parse(self, tokens):
        return self.parse_expr(tokens)

    def parse_expr(self, tokens):
        left = self.parse_mult_expr(tokens)

        while len(tokens) > 0 and tokens[0].type in ('+', '-'): # type of Token is defined as THE operator or "number"
            op = tokens.pop(0).value
            right = self.parse_mult_expr(tokens)
            left = Operation(op, left, right)

        return left

    def parse_mult_expr(self, tokens):
        left = self.parse_atom(tokens)

        while len(tokens) > 0 and tokens[0].type in ('*', '/'):
            op = tokens.pop(0).value
            right = self.parse_atom(tokens)
            left = Operation(op, left, right)

        return left

    def parse_atom(self, tokens):
        token = tokens.pop(0)
        if token.type == 'number':
            return Number(int(token.value))
        elif token.type == '(':
            expr = self.parse_expr(tokens)
            if tokens.pop(0).type != ')':
                raise Exception("Expected ')'")
            return expr
        else:
            raise Exception(f"Unexpected token: {token.type}")


if __name__ == "__main__":
    expression_str = input("expression>> ")
    tokens = tokenize(expression_str)
    parser = Parser()
    expression = parser.parse(tokens)
    print(expression.eval())