coke = 50

while True:
    print(f"Amount due: {coke}")
    try:
        minus = int(input("Insert coin: "))
    except ValueError:
        print("Not an int")
        continue

    if minus != 25 and minus != 10 and minus != 5:
        print("only 25, 10 or 5 cent coins allowed")
        continue
    else:
        coke -= minus
    if coke <= 0:
        coke = coke * -1
        print(f"Change owed: {coke}")
        break