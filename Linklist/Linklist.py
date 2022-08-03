# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/24 22:14
# @Software: PyCharm

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linklist_head(lst):
    head = Node(lst[0])
    for val in lst[1:]:
        node = Node(val)
        node.next = head
        head = node
    return head


def create_linklist_tail(lst):
    head = Node(lst[0])
    tail = head
    for val in lst[1:]:
        node = Node(val)
        tail.next = node
        tail = node
    return head


def print_linklist(lk):
    while lk:
        print(lk.val, end=",") if lk.next else print(lk.val)
        lk = lk.next


if __name__ == '__main__':
    lst = [i for i in range(10)]
    lk = create_linklist_head(lst)
    print_linklist(lk)
    lkk = create_linklist_tail(lst)
    print_linklist(lkk)
