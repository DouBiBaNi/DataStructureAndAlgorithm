# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/16 13:22
# @Software: PyCharm
def selectSort(lst):
    """
    the time cost: O(n^2)
    :param lst: lists
    :return: None
    """
    n = len(lst)
    for i in range(n - 1):
        min_loc = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_loc]:
                min_loc = j
        if min_loc != i:
            lst[i], lst[min_loc] = lst[min_loc], lst[i]


if __name__ == '__main__':
    lst = [3, 4, 2, 52, 123, 5, 87, 1, 21, 324, 53, 1, 2, 3, 42]
    selectSort(lst)
    print(lst)

# result:
# [1, 1, 2, 2, 3, 3, 4, 5, 21, 42, 52, 53, 87, 123, 324]
