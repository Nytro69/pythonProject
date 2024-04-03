class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def height(self) -> int:
        left_height = 0 if self.left is None else self.left.height()
        right_height = 0 if self.right is None else self.right.height()
        return 1 + max(left_height, right_height)

