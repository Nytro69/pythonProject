import random
v = 1000

# 1 papper, 2 rock, 3 siscors
result = []
for i in range(v*10000):
    a = random.randint(1, 3)
    b = random.randint(1, 3)
    if a == b:
        result.append(0)

    elif a == 1:
        if b == 2:
            result.append(1)
        elif b == 3:
            result.append(-1)

    elif a == 2:
        if b == 3:
            result.append(1)
        elif b == 1:
            result.append(-1)

    elif a == 3:
        if b == 1:
            result.append(1)
        elif b == 2:
            result.append(-1)

wins = []
x = 0
for i in range(1, len(result)):
    x += result[i-1]
    if i % v == 0:
        if x == 0:
            wins.append(0)
        elif x >= 1:
            wins.append(1)
        elif x <= -1:
            wins.append(-1)
        x = 0


print(f"Total wins: {wins.count(0)/len(wins)}")