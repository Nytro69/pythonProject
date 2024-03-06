camel = input("CamelCase: ")
print("snake_case: ", end="")
for c in camel:
    if 65 <= ord(c) and ord(c) <= 90:
        c = c.lower()
        print(f"_{c}", end="")
    else:
        print(c, end="")