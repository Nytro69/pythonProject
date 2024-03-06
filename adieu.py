names = []

def main():
    getName()
    printingName()


def getName():
    while True:
        user = input("Name: ")
        if user == "":
            break
        else:
            names.append(user)
            continue


def printingName():
    print(f"Adieu, adieu, to ", end="")
    for i in range(len(names)):
        if i == len(names) - 2:
            print(f"{names[i]} and {names[i + 1]}")
            break
        else:
            print(f"{names[i]}, ", end="")

if __name__ == '__main__':
    main()