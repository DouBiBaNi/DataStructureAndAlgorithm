# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/24 15:50
# @Software: PyCharm

class Stack():
    """
    a list with LIFO(last-in, first-out)
    """
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def isEmpty(self):
        return self.stack == []

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None

    def get_top(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

    def __repr__(self):
        return "Stack_" + str(self.stack)

    # def __str__(self):
    #     return "Stack_" + str(self.stack)


if __name__ == '__main__':
    stack = Stack()
    for i in range(1, 4):
        stack.push(i)

    for _ in range(4):
        print(stack.get_top())
        print(stack)
        print(stack.pop())
        print("------")