# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/25 18:25
# @Software: PyCharm

class Node:
    def __init__(self, name, type="dir"):
        self.name = name
        self.type = type  # "dir" or "file"
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


class FileSystemTree:

    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mk_dir(self, name):
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name[-1] != "/":
            name += "/"
        if name == "../":
            self.now = self.now.parent

        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise ValueError("invalid dir")


if __name__ == '__main__':
    tree = FileSystemTree()
    tree.mk_dir("var/")
    tree.mk_dir("bin/")
    tree.mk_dir("usr/")

    tree.cd("bin/")
    tree.mk_dir("python/")

    print(tree.ls())
