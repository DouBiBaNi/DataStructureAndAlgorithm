# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/16 20:34
# @Software: PyCharm
def insertSort(lst):
    n = len(lst)
    for i in range(1, n):
        temp = lst[i]
        j = i - 1
        while lst[j] > temp and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp


if __name__ == '__main__':
    lst = [7, 5, 3, 2, 7, 8, 2, 4, 3, 1, 78, 456, 23, 1, 21, 42, 66]
    insertSort(lst)
    print(lst)

# result:
# [1, 1, 2, 2, 3, 3, 4, 5, 7, 7, 8, 21, 23, 42, 66, 78, 456]
