import sympy

m = input("Number: ")
m = int(m)
final = []
while True:
    if sympy.isprime(m):
        print("Number is prime")
        quit()
    else:
        primes = list(sympy.primerange(0, m + 1))
        for i in primes:
            if m == i:
                print("Number is prime")
                print(final)
                quit()
            k = m / i
            if k.is_integer():
                final.append(i)
                print(k)
                m = k
                break
        continue