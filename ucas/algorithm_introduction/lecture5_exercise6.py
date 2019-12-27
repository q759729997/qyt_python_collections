# -*- coding: utf-8 -*-
"""
现有n 块“多米诺骨牌” $s_1,s_2,…,s_n$ 水平放成一排，每块骨牌 $s_i$ 包含左右两个部分，每个部分赋予一个非负整数值，如下图所示为包含6 块骨牌的序列。骨牌可做180 度旋转，使得原来在左边的值变到右边，而原来在右边的值移到左边，假设不论 $s_i$ 如何旋转，L[i] 总是存储 $s_i$ 左边的值，R[i] 总是存储 $s_i$ 右边的值，W[i] 用于存储 $s_i$ 的状态：当L[i] $\le$ R[i] 时记为0，否则记为1，试设计**<u>时间复杂度为O(n)的动态规划算法</u>**，求 $\sum_{i=1}^{n-1}R[i]\cdot L[i+1]$ 的最大值，以及当取得最大值时每个骨牌的状态。
"""
if __name__ == "__main__":
    dominno_cards = [[5, 8], [4, 2], [9, 6], [7, 7], [3, 9], [11, 10]]
    dp_items = list()
    # 构建每个位置0,1的状态元素值
    for i, temp in enumerate(dominno_cards):
        dp_item0 = None
        dp_item1 = None
        dp_item = list()
        if temp[0] > temp[1]:
            dp_item.append((temp[1], temp[0]))
            dp_item.append((temp[0], temp[1]))
        else:
            dp_item.append((temp[0], temp[1]))
            dp_item.append((temp[1], temp[0]))
        dp_items.append(dp_item)
    print(dp_items)
    # [[(5, 8), (8, 5)], [(2, 4), (4, 2)], [(6, 9), (9, 6)], [(7, 7), (7, 7)], [(3, 9), (9, 3)], [(10, 11), (11, 10)]]
    # 构建状态空间
    dominno_status = []
    dp_space = [[0, 0]]
    for i in range(1, len(dominno_cards)):
        # 状态0位置判断
        space_item_0_1 = dp_space[i-1][0] + dp_items[i][0][0] * dp_items[i-1][0][1]
        space_item_0_2 = dp_space[i-1][1] + dp_items[i][0][0] * dp_items[i-1][1][1]
        if space_item_0_1 >= space_item_0_2:
            space_item_0 = space_item_0_1
            status_item_0 = (0, 0)
        else:
            space_item_0 = space_item_0_2
            status_item_0 = (1, 0)
        # 状态1位置判断
        space_item_1_1 = dp_space[i-1][0] + dp_items[i][1][0] * dp_items[i-1][0][1]
        space_item_1_2 = dp_space[i-1][1] + dp_items[i][1][0] * dp_items[i-1][1][1]
        if space_item_1_1 >= space_item_1_2:
            space_item_1 = space_item_1_1
            status_item_1 = (0, 1)
        else:
            space_item_1 = space_item_1_2
            status_item_1 = (1, 1)
        dp_space.append([space_item_0, space_item_1])
        dominno_status.append([status_item_0, status_item_1])
    print(dp_space)
    # [[0, 0], [16, 32], [44, 52], [107, 107], [128, 170], [218, 227]]
    print(dominno_status)
    # [[(0, 0), (0, 1)], [(1, 0), (0, 1)], [(0, 0), (0, 1)], [(0, 0), (0, 1)], [(0, 0), (0, 1)]]
    # 计算最终结果
    if space_item_0 >= space_item_1:
        dominno_max_sum = space_item_0
        dominno_max_status = [0]
        for status_temp in reversed(dominno_status):
            dominno_max_status.append(status_temp[dominno_max_status[-1]][0])
    else:
        dominno_max_sum = space_item_1
        dominno_max_status = [1]
        for status_temp in reversed(dominno_status):
            dominno_max_status.append(status_temp[dominno_max_status[-1]][0])
    print('计算结果：{}'.format(dominno_max_sum))
    dominno_max_status.reverse()
    print('状态：{}'.format(dominno_max_status))
