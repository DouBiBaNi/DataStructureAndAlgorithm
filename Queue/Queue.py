# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/24 16:54
# @Software: PyCharm

class Queue():
    """
    a cycle list with FIFO
    """

    def __init__(self, size):
        self.size = size
        self.queue = [0] * size
        self.rear = 0
        self.front = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def push(self, element):
        if self.isFull():
            raise IndexError("the queue is full.")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element

    def pop(self):
        if self.isEmpty():
            raise IndexError("the queue is empty.")
        else:
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]


if __name__ == '__main__':
    q = Queue(5)
    for i in range(4):
        q.push(i)
    print(q.pop())
    q.push(5)

    from collections import deque
    # dequeue is a double-end queue
    print("---collections.deque---")
    qq = deque([1, 2, 3, 4, 5], 5)
    qq.append(4)
    print(qq.popleft())

    # qq.appendleft(1)  -- push from front
    # qq.pop()  -- pop from rear

