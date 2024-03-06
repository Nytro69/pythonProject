map = [
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1],
]

def run():
    visited = []

    print(f"Islands: {count_islands(map, visited)}")
    print(f"Ground spaces: {', '.join(visited)}")

def islands(x, y, map, visited):

    if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]) or map[y][x] == 0:
        return False

    visited.append(f"{x, y}")

    map[y][x] = 0

    islands(x, y + 1, map, visited)
    islands(x, y - 1, map, visited)
    islands(x + 1, y, map, visited)
    islands(x - 1, y, map, visited)

    return True

def count_islands(map, visited):
    counter = 0
    for j in range(len(map)):
        for i in range(len(map[0])):
            if islands(i, j, map, visited):
                counter += 1

    return counter

def guess(x, y, map):
    counter = 0
    while True:
        counter = 0
        if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]):
            print("outside the map")
            k()
            return

        if map[y][x] == 1:
            print("Correct!")
            return
        else:
            if island_check(x - 1, y, map, counter):
                counter += 1
            if island_check(x + 1, y, map, counter):
                counter += 1
            if island_check(x, y - 1, map, counter):
                counter += 1
            if island_check(x, y + 1, map, counter):
                counter += 1
            print(f"there are {counter} ground spaces adjacent to ({x}, {y})")
            k()
            return

def island_check(x, y, map, counter):
    if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]):
        return
    if map[y][x] == 1:
        return True


choice = input("choose mode:\n1, calculate islands\n2, guessing game\n3, quit\n")

if choice == "1":
    run()
elif choice == "2":
    def k():
        x = input("guess coordinate (x, y): ")

        x, y = x.split(", ")
        x = int(x)
        y = int(y)
        guess(x, y, map)
    k()

else:
    quit()