menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
total = 0


def main():
    global total
    while True:
        if in_menu(menu):
            total = price(item, menu) + total
            print(total)
        if item == "":
            print(f"total: {total}")
            quit()


def in_menu(menu):
    global item
    while True:
        try:
            item = input("order: ").lower()
        except Exception:
            pass
        if item == "":
            return item
        if item not in menu:
            return False
        else:
            return True, item



def price(variable, add):
    if variable in add:
        return add[variable]
    else:
        return None


main()