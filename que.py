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

def main():
    graph = {
        "a": ["b"],
        "b": ["c", "d", "e", "a"],
        "c": ["b"],
        "d": ["i", "b", "f"],
        "e": ["b", "f", "h"],
        "f": ["d", "e", "g"],
        "g": ["f", "h", "i"],
        "h": ["e", "g"],
        "i": ["d", "g", "j"],
        "j": ["i"]
    }

    start = input("start, a-j: ").strip().lower()
    end = input("end, a-j: ").strip().lower()

    if end == start:
        print("Optimal path length:", 0)
        return

    que = Queue()
    que.enqueue(start)

    parent = {}
    path_length = {}

    while not que.is_empty():
        now = que.dequeue()
        if now == end:
            print("Found! Optimal path length:", path_length[now]) # now is the end
            # Print the path
            path = []
            while now != start:
                path.append(now)
                now = parent[now]
            path.append(start)
            print("Optimal path:", " -> ".join(path[::-1]))
            return

        # only for start node
        if now not in parent:
            parent[now] = now
            path_length[now] = 0


        adjacent = graph[now]
        for i in adjacent:
            if i not in parent:
                parent[i] = now
                path_length[i] = path_length[now] + 1
                que.enqueue(i)

    print("path is impossible")
    return 

if __name__ == '__main__':
    main()