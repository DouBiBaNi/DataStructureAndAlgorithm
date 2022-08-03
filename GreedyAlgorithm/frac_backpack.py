# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/8/2 22:10
# @Software: PyCharm

goods = [(60, 10), (100, 20), (120,30)] #each tuple is (price, weight)

def frac_backpack(goods, w):
    goods.sort(key=lambda x:x[0]/x[1], reverse=True)
    m = [0]*(len(goods))
    for i, (price, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            w -= weight
        else:
            m[i] = w / weight
            # w = 0
            break
    return m

if __name__ == '__main__':
    print(frac_backpack(goods, 50))