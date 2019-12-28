"""
现有n 块“多米诺骨牌” s1; s2;    ; sn 水平放成一排，每块骨牌si 包含左
右两个部分，每个部分赋予一个非负整数值，如下图所示为包含6 块骨牌的序列。骨牌可
做180 度旋转，使得原来在左边的值变到右边，而原来在右边的值移到左边，假设不论si 如
何旋转，L[i] 总是存储si 左边的值，R[i] 总是存储si 右边的值，W[i] 用于存储si 的状态：
当L[i]  R[i] 时记为0，否则记为1，试采用分治法设计算法求
Σn􀀀1
i=1 R[i]  L[i + 1] 的最大
值，以及当取得最大值时每个骨牌的状态。下面是n = 6 时的一个例子：
https://wenku.baidu.com/view/e0928f28915f804d2b16c154.html
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
    n = len(s)
    print('左右两端各加入一个为0的骨牌')
    r_list = [0]
    l_list = [0]
    for l, r in s:
        l_list.append(l)
        r_list.append(r)
    l_list.append(0)
    r_list.append(0)
    w_list = [0 if s_item[0] <= s_item[1] else 1 for s_item in s]
    print('初始化阶段')
    print('r_list:{}'.format(r_list))
    print('l_list:{}'.format(l_list))
    print('w_list:{}'.format(w_list))
    first = 0
    last = n + 1
    w_reverse_flag = [False] * n
    domino_max = calculate_domino(l_list, r_list, first, last, w_reverse_flag)
    print('重新排列计算后')
    print('domino_max:{}'.format(domino_max))
    print('w_reverse_flag:{}'.format(w_reverse_flag))
    for i in range(n):
        reverse_flag = w_reverse_flag[i]
        w = w_list[i]
        if reverse_flag:
            if w == 1:
                w_list[i] = 0
            else:
                w_list[i] = 1
    print('w_list:{}'.format(w_list))
    print('验证结果:')
    s_for_check = list()
    for i in range(n):
        s_item = s[i]
        w = w_list[i]
        if w == 0:
            s_for_check.append([min(s_item), max(s_item)])
        else:
            s_for_check.append([max(s_item), min(s_item)])
    print('s_for_check:{}'.format(s_for_check))
    domino_max_check = 0
    for i in range(1, len(s_for_check)):
        print('first:{}， next:{}'.format(s_for_check[i - 1][-1], s_for_check[i][0]))
        domino_max_check += s_for_check[i - 1][-1] * s_for_check[i][0]
    print('domino_max_check:{}'.format(domino_max_check))
