# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/8/2 22:35
# @Software: PyCharm

# There are n non-negative integers,
# which are concatenated into an integer in the way of string concatenation,
# so that the integer is the largest.
from functools import cmp_to_key

lst = [32, 94, 128, 1286, 6, 71]

def xy_cmp(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0

def number_join(lst):
    lst = list(map(str,lst))
    lst.sort(key=cmp_to_key(xy_cmp))
    return "".join(lst)

if __name__ == '__main__':
    print(number_join(lst))