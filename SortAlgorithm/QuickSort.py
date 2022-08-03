# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/16 20:57
# @Software: PyCharm

# import sys
# sys.setrecursionlimit(10**5)

def quickSort(lst, left=0, right=None):
    """
    time cost: O(nlogn)
    :param lst:list
    :return:None
    """

    def partition(lst, left, right):
        temp = lst[left]  # pick out the temp
        while left < right:
            # sort list such that the element on the left is less than temp and the right is more than temp
            while lst[right] >= temp and left < right:  # put the right on the blank
                right -= 1
            lst[left] = lst[right]
            while lst[left] <= temp and left < right:  # put the left on the blank
                left += 1
            lst[right] = lst[left]
        lst[left] = temp
        return left

    if right is None:
        right = len(lst) - 1

    if left < right:
        mid = partition(lst, left, right)
        quickSort(lst, left, mid - 1)
        quickSort(lst, mid + 1, right)


if __name__ == '__main__':
    lst = [2, 4, 5, 7, 9, 8, 5, 1, 3, 13, 54, 32, 21, 11, 11]
    quickSort(lst)
    print(lst)
