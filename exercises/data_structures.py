# X    0    1    Y
# 0    0    1    0
# 0    0    1    0
# 0    1    1    0
# 0    0    0    0

# True represents a wall
# X => (0, 0)
# Y => (0, 3)
# out => [(0,0), (0,1), (1,1) ... ]
# if adjacent == false, set cord in parent pointing to previous


def str_reverse(s) -> str:
    if len(s) <= 1:
        return s

    m = len(s) // 2

    half1 = str_reverse(s[:m])

    half2 = str_reverse(s[m:])


    return half2 + half1

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


def main():
    map = [
        [False, False, True, False],
        [False, False, True, False],
        [False, False, True, False],
        [False, True, True, False],
        [False, False, False, False]
    ]
    print(str_reverse(solve_maze(map, (0, 0), (0, 3))))
main()