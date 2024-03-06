item_list = []

def main():
    duplicates = duplicate()

    for i in duplicates:
        print(f"{duplicates[i]}  {i}")

def duplicate():
    items = inpuk()
    items.sort()
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    duplicates = {item: count for item, count in counts.items()}
    return duplicates


def inpuk():
    item_list = []
    while True:

        try:
            item = input().upper().strip()
        except EOFError:
            return item_list
        else:
            item_list.append(item)

if __name__ == '__main__':
    main()