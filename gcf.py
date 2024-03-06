k = 1

while k != "":
    try:
        k = input("factors(a, b): ")

        a, b = k.split(", ")

        a = int(a)
        b = int(b)
    except ValueError:
        continue

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a


    print(gcd(a, b))