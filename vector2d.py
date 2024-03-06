import math


class Vector2d:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def add(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return f"({self.x}, {self.y})"