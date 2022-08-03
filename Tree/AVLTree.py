# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/29 13:38
# @Software: PyCharm
class AVLNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0
        # self.bf = 0


class AVLTree():

    def __init__(self, lst=None):
        self.root = None
        if lst:
            for num in lst:
                self.insert(num)

    def find(self, val):
        if not self.root:
            return None
        else:
            return self._find(val, self.root)

    def _find(self, val, node):
        if not node:
            return None
        elif val < node.data:
            return self._find(val, node.left)
        elif val > node.data:
            return self._find(val, node.right)
        else:
            return node

    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)

    def _findMin(self, node):
        if node.left:
            return self._findMin(node.left)
        else:
            return node

    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)

    def _findMax(self, node):
        if node.right:
            return self._findMax(node.right)
        else:
            return node

    # def balancefactor(self, node):
    #     if node is None:
    #         return -1
    #     else:
    #         return node.bf

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def left_left_rotate(self, node):
        k1 = node.left
        node.left = k1.right
        k1.right = node

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        # node.bf = self.height(node.right)-self.height(node.left)

        k1.height = max(self.height(k1.left), node.height) + 1

        return k1

    def right_right_rotate(self, node):
        k1 = node.right
        node.right = k1.left
        k1.left = node

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.right), node.height) + 1

        return k1

    def right_left_rotate(self, node):
        node.right = self.left_left_rotate(node.right)

        return self.right_right_rotate(node)

    def left_right_rotate(self, node):
        node.left = self.right_right_rotate(node.left)

        return self.left_left_rotate(node)

    def insert(self, val):
        if not self.root:
            self.root = AVLNode(val)

        else:
            self.root = self._insert(val, self.root)

    def _insert(self, val, node):
        if node is None:
            node = AVLNode(val)

        elif val < node.data:
            node.left = self._insert(val, node.left)

            if (self.height(node.left) - self.height(node.right)) == 2:
                if val < node.left.data:
                    node = self.left_left_rotate(node)
                else:
                    node = self.left_right_rotate(node)

        elif val > node.data:

            node.right = self._insert(val, node.right)

            if (self.height(node.right) - self.height(node.left)) == 2:
                if val > node.right.data:
                    node = self.right_right_rotate(node)
                else:
                    node = self.left_right_rotate(node)

        node.height = max(self.height(node.left), self.height(node.right)) + 1

        return node

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.data, end=",")
            self.in_order(node.right)


if __name__ == '__main__':
    # lst = [1, 9, 5, 7, 6, 3, 2, 4, 8]
    lst = list(map(int, input().split()))
    avl = AVLTree(lst)
    avl.in_order(avl.root)

# https://blog.csdn.net/Wang_Runlin/article/details/104770922
