def guess(a: int, b: int, c: int):
    a = c
    c = b
    b = a

    print(b + c)

guess(1, 3, 5)