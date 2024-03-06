def main():
    gre = input("Greeting: ").strip().lower()
    value(gre)


def value(gre):
    gre = gre.lower().strip()
    if gre and len(gre) >= 5 and gre[0: 5] == "hello":
        return 100
    elif gre and len(gre) >= 1 and gre[0] == "h":
        return 20
    else:
        return 0

if __name__ == "__main__":
    main()