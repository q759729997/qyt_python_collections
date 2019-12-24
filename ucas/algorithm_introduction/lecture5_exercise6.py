# -*- coding: utf-8 -*-
"""
现有n 块“多米诺骨牌” $s_1,s_2,…,s_n$ 水平放成一排，每块骨牌 $s_i$ 包含左右两个部分，每个部分赋予一个非负整数值，如下图所示为包含6 块骨牌的序列。骨牌可做180 度旋转，使得原来在左边的值变到右边，而原来在右边的值移到左边，假设不论 $s_i$ 如何旋转，L[i] 总是存储 $s_i$ 左边的值，R[i] 总是存储 $s_i$ 右边的值，W[i] 用于存储 $s_i$ 的状态：当L[i] $\le$ R[i] 时记为0，否则记为1，试设计**<u>时间复杂度为O(n)的动态规划算法</u>**，求 $\sum_{i=1}^{n-1}R[i]\cdot L[i+1]$ 的最大值，以及当取得最大值时每个骨牌的状态。
"""
import math


def calculate_domino(l_list, r_list, first, last, w_reverse_flag):
    """计算多米诺之和.

    Args:
        l_list: 每个位置的左侧数列.
        r_list: 每个位置的右侧数列.
        first: 起始位置.
        last: 末尾位置.
        w_reverse_flag: 状态是否逆转列表

    Returns:
        多米诺计算之和.
    """
    if last - first < 2:  # 牌的个数需要大于1
        raise Exception('骨牌个数需要大于1')

    def get_domino_max(l_list, r_list, first, last):
        if last - first == 1:
            max_ = r_list[first] * l_list[last]
            print('first:{}/{}， last：{}/{}, max:{}'.format(first, r_list[first], last, l_list[last], max_))
        else:
            middle = math.ceil((first + last) / 2)  # 向上取整
            print('middle:{}'.format(middle))
            max_l1 = get_domino_max(l_list, r_list, first, middle)
            max_r1 = get_domino_max(l_list, r_list, middle, last)
            max1 = max_l1 + max_r1
            # 交换
            print('交换前：left:{}， right：{}'.format(l_list[middle], r_list[middle]))
            temp = l_list[middle]
            l_list[middle] = r_list[middle]
            r_list[middle] = temp
            print('交换后：left:{}， right：{}'.format(l_list[middle], r_list[middle]))
            max_l2 = get_domino_max(l_list, r_list, first, middle)
            max_r2 = get_domino_max(l_list, r_list, middle, last)
            max2 = max_l2 + max_r2
            if max1 <= max2:
                max_ = max2
                w_reverse_flag[middle - 1] = False
            else:
                max_ = max1
                w_reverse_flag[middle - 1] = True
        return max_
    return get_domino_max(l_list, r_list, first, last)


if __name__ == "__main__":
    s = [[5, 8], [4, 2], [9, 6], [7, 7], [3, 9], [11, 10]]
    dp = list()
    # 构建每个位置0,1的状态空间
    for i, temp in enumerate(s):
        dp_item0 = None
        dp_item1 = None
        dp_item = list()
        if temp[0] > temp[1]:
            dp_item.append((temp[1], temp[0]))
            dp_item.append((temp[0], temp[1]))
        else:
            dp_item.append((temp[0], temp[1]))
            dp_item.append((temp[1], temp[0]))
        dp.append(dp_item)
    print(dp)
    # [[(5, 8), (8, 5)], [(2, 4), (4, 2)], [(6, 9), (9, 6)], [(7, 7), (7, 7)], [(3, 9), (9, 3)], [(10, 11), (11, 10)]]
    # 构建