class Jar:
    def __init__(self, capacity=12):
        if capacity > 0 and isinstance(capacity, int):
            self._capacity = capacity
        else:
            raise ValueError(f"capacity need to be a non-negative int, what you typed: {capacity} ")
        self._size = 0

    def __str__(self):
        return "🍪" * self._size
    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError(f"Exceeded capacity. capacity: {self.capacity} cookies: {self._size + n}")
        return self._size + n
    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError(f"Not enough cookies to withdraw: {self._size - n}")
        return self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

class_jar = Jar(10)