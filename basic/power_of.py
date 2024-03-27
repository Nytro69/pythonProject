def square(n, power):
    if isinstance(power, (float)):
        return "no decimal powers"
    result = 0
    if power == 0:
        return 1
    for x in range(power):
        if result == 0:
            result = n
            continue

        result = result * n
    return result


print(square(int(input("base: ")), int(input(("power: ")))))

