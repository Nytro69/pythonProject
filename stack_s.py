# top
# empty
# push
# pop
import math


def is_empty(stack: list):
    return len(stack) == 0


def top(stack: list):
    if is_empty(stack):
        raise Exception("Stack is empty")

    return stack[-1]


def push(item, stack: list):
    stack.append(item)


def pop(stack: list):
    return stack.pop()



class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def top(self):
        if is_empty(self.items):
            raise Exception("Stack is empty")

        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()



def run():
    option = input(">> ").lower()
    if option == "type":
        print("Typing...")

    pass

run()



