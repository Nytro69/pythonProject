import random


def main(z):
    b = [0, 0, 0, 0, 0, 3, 6, 12, 25, 50, 100]
    x = 0
    for i in range(z):
        a = random.randint(1, 6)
        a = a + random.randint(1, 6)

        x += b[a-2]

    return x - 12*z


for i in range(1, 1000):
    r = 0
    for j in range(1000):
        k = main(i)
        if k > 0:
            r += 1

    if r/1000 < 0.1:
        print(i)

