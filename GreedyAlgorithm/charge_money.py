# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/8/2 19:58
# @Software: PyCharm

# Suppose the store owner needs to change n yuan,
# and the denominations of the coins are 100, 50, 20, and 1.
# How to make change to minimize the number of coins.

coins = [100, 50, 20, 1]

def charge_money(coins, n):
    size = len(coins)
    cnt = [0]*size
    for i, v in enumerate(coins):
        cnt[i] = n // v
        n %= v
    return cnt

if __name__ == '__main__':
    print(charge_money(coins, 521))