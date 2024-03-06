


def main():
    full = input("input: ")
    full = str_conversion(full)
    print(f"output: {full}")

def str_conversion(i):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for s in vowels:
        if s in i:
            i = i.replace(s, "")
        else:
            continue
    return i

if __name__ == "__main__":
    main()
