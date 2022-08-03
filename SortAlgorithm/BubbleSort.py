# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/16 12:49
# @Software: PyCharm
def bubbleSort(lst):
    """
    sort list with <=
    :param lst: list
    :return:None
    """
    n = len(lst)
    for i in range(n-1):
        exchange = False
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                exchange = True
        if not exchange:
            return

if __name__ == '__main__':
    lst = [3, 4, 5, 2, 1, 5, 7, 8, 66, 43, 21, 65, 34, 11]
    bubbleSort(lst)
    print(lst)