def prime(a):
    x = []
    for i in range(2, a + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            x.append(i)
    return x

numbers = input("(a, b, ...): ").split(", ")
numbers = list(map(int, numbers))

prime_numbers = prime(max(*numbers))

ground = []
for number in numbers:
    x = int(number)
    z = []
    restart = False
    while True:
        if restart:
            break
        for prime in prime_numbers:
            if x == 1:
                ground.append(z)
                restart = True
                break
            if x % prime == 0:
                z.append(prime)
                x = x / prime
                break
        else:
            break

main = []
for g in ground:
    if len(g) > 0:
        if len(main) == 0:
            main = g
            continue
        if g in main:
            continue
        x = main[:]

        for i in g:
            if i in x:
                x.remove(i)
                continue
            main.append(i)

a = 1
for i in main:
    a *= i
print(a)

