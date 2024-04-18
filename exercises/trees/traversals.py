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

"""
1- Visit the current node (in the figure: position red).
2- Recursively traverse the current node's left subtree.
3- Recursively traverse the current node's right subtree.
"""


from tree import Tree
def pre_order_traverse(tree: Tree):
    print(tree.value)
    if tree.left is not None:
        pre_order_traverse(tree.left)
    if tree.right is not None:
        pre_order_traverse(tree.right)


def post_order_traverse(tree: Tree):
    if tree is None:
        return

    post_order_traverse(tree.left)

    post_order_traverse(tree.right)

    print(tree.value)

def in_order_traverse(tree: Tree):
    if tree is None:
        return
    in_order_traverse(tree.left)
    print(tree.value)
    in_order_traverse(tree.right)



def by_level_traverse(tree: Tree):
    que = Queue()
    que.enqueue(tree)
    while not que.is_empty():
        node = que.dequeue()
        print(node.value)

        if node.left is not None:
            que.enqueue(node.left)

        if node.right is not None:
            que.enqueue(node.right)

tree = Tree(3,
            Tree(5,
                 Tree(15),
                 Tree(25)),
            Tree(7,
                 Tree(17),
                 Tree(27,
                      Tree(217),
                      Tree(228)))
            )

by_level_traverse(tree)
"""
in order
pre order
post order
by level
"""