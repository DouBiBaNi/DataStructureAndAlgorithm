# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/25 20:58
# @Software: PyCharm
from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

def pre_order(root):
    print("---pre_order---")
    def _pre_order(root):
        if root:
            print(root.data, end=",")
            _pre_order(root.lchild)
            _pre_order(root.rchild)
    _pre_order(root)
    print()

def in_order(root):
    print("---in_order---")
    def _in_order(root):
        if root:
            _in_order(root.lchild)
            print(root.data, end=",")
            _in_order(root.rchild)
    _in_order(root)
    print()

def post_order(root):
    def _post_order(root):
        if root:
            _post_order(root.lchild)
            _post_order(root.rchild)
            print(root.data, end=",")
    print("---post_order---")
    _post_order(root)
    print()


def level_order(root):
    print("---level_order---")
    q = deque()
    q.append(root)
    while q:
        cur = q.popleft()
        print(cur.data, end=',')
        if cur.lchild:
            q.append(cur.lchild)
        if cur.rchild:
            q.append(cur.rchild)


def create_tree(root, trees):
    if len(trees) == 0:
        return root

    if trees[0] != None:
        root = BiTreeNode(trees[0])
        trees.pop(0)
        root.lchild = create_tree(root.lchild, trees)
        root.rchild = create_tree(root.rchild, trees)
        return root
    else:
        trees.pop(0)
        return root


if __name__ == '__main__':
    strs = "EA##CBDG###F##"
    trees = list(strs)
    for i in range(len(trees)):
        if trees[i] == "#":
            trees[i] = None

    root = None
    roots = create_tree(root, trees)

    for serchTree in [pre_order, in_order, post_order, level_order]:
        serchTree(roots)

    # result:
    # ---pre_order---
    # E,A,C,B,D,G,F,
    # ---in_order---
    # A,E,G,D,B,F,C,
    # ---post_order---
    # A,G,D,F,B,C,E,
    # ---level_order---
    # E,A,C,B,D,F,G,
