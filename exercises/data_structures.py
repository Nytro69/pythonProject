from str_reverse import str_reverse

class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def front(self):
        if self.is_empty():
            return None
        return self.data[0]

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        k = self.front()
        self.data = self.data[1:]
        return k


def solve_maze(map, start, end) -> list:
    que = Queue()
    que.enqueue(start)

    parent = {}
    parent[tuple(start)] = start

    while not que.is_empty():
        now = que.dequeue()
        if now == end:
            path = []
            while now != start:
                path.append(now)
                now = parent[now]
            path.append(start)
            return path

        adjacent = [
            (now[0] - 1, now[1]),
            (now[0] + 1, now[1]),
            (now[0], now[1] - 1),
            (now[0], now[1] + 1)
        ]

        for i in adjacent:
            if i[0] < 0 or i[0] > len(map) - 1 or i[1] < 0 or i[1] > len(map[0]) - 1:
                continue

            if i not in parent:

                if map[i[0]][i[1]] == False:
                    parent[i] = now
                    que.enqueue(i)
    print("Path is impossible")

def main():
    map = [
        [False, False, True, True],
        [False, False, True, False],
        [False, False, True, False],
        [False, True, True, False],
        [False, False, False, False]
    ]

    while True:
        start1, start2 = input("start, (y, x): ").split(", ")
        end1, end2 =input("end,   (y, x): ").split(", ")

        start1 = int(start1)
        start2 = int(start2)
        end1 = int(end1)
        end2 = int(end2)

        start = (start1, start2)
        end = (end1, end2)

        if start[0] < 0 or start[0] > len(map) - 1 or start[1] < 0 or start[1] > len(map[0]) - 1 or map[start[0]][start[1]] != False or end[0] < 0 or end[0] > len(map) - 1 or end[1] < 0 or end[1] > len(map[0]) - 1 or map[end[0]][end[1]] != False:
            print("invalid position")
            continue
        else:
            print(str_reverse(solve_maze(map, start, end)))
            break

main()
