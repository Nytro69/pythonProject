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


num = Operation("+",
                Number(2),
                Operation("*",
                          Number(3),
                          Number(4)))


print(num.eval())