# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/27 13:22
# @Software: PyCharm
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST:
    def __init__(self, lst=None):
        self.root = None
        if lst:
            for val in lst:
                self.insert_no_rec(val)

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if not p.lchild:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
                else:
                    p = p.lchild
            elif val > p.data:
                if not p.rchild:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
                else:
                    p = p.rchild
            else:
                return

    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while True:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    def pre_order(self, root):
        print("---pre_order---")

        def _pre_order(root):
            if root:
                print(root.data, end=",")
                _pre_order(root.lchild)
                _pre_order(root.rchild)

        _pre_order(root)
        print()

    def in_order(self, root):
        print("---in_order---")

        def _in_order(root):
            if root:
                _in_order(root.lchild)
                print(root.data, end=",")
                _in_order(root.rchild)

        _in_order(root)
        print()

    def post_order(self, root):
        def _post_order(root):
            if root:
                _post_order(root.lchild)
                _post_order(root.rchild)
                print(root.data, end=",")

        print("---post_order---")
        _post_order(root)
        print()

    def __remove_node1(self, node):
        # leaf node
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:
            node.parent.lchild = None
        elif node == node.parent.rchild:
            node.parent.rchild = None

    def __remove_node21(self, node):
        # node only have a lchild
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        if node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        elif node == node.parent.rchild:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node22(self, node):
        # node only have a rchild
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None
        if node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        elif node == node.parent.rchild:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:
                self.__remove_node1(node)
            elif not node.rchild:
                self.__remove_node21(node)
            elif not node.lchild:
                self.__remove_node22(node)
            else:
                # have lchild and rchild
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                if min_node.rchild:
                    self.__remove_node22(min_node)
                else:
                    self.__remove_node1(min_node)


if __name__ == '__main__':
    tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
    tree.in_order(tree.root)
    tree.delete(4)
    tree.in_order(tree.root)
    tree.delete(1)
    tree.in_order(tree.root)
    tree.delete(8)
    tree.in_order(tree.root)

    # import random
    # lst = list(range(0, 102, 2))
    # random.shuffle(lst)
    # tree1 = BST(lst)
    # print(tree1.query(tree1.root, 100).data)
