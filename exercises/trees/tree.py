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
        left = self.parse_mult_expr(tokens)

        if len(tokens) == 0:
            return left

        if not tokens[0].type in ('+', '-'):
            raise Exception("Invalid token")

        op = tokens.pop(0).value

        right = self.parse_mult_expr(tokens)
        return Operation(op, left, right)


    def parse_mult_expr(self, tokens):

        pass

    def parse_atom(self, tokens):
        if tokens[0].type == 'number':
            pass
            # return Number(int(tokens[0].value))

        pass


