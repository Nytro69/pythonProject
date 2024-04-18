def separate(string: str) -> str:
    i = 0
    h = 0
    new = []
    while i < len(string):
        if i % 50 == 0 and i != 0:
            h = 1

        if string[i].isspace() and h == 1:
            new.append("\n")
            h = 0
            i += 1
            continue
        else:
            new.append(string[i])
            i += 1

    return ''.join(new)

print(separate("jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag jag "))