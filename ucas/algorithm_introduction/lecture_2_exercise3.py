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


def calculate_domino(l_list, r_list, first, last, w_list):
    """计算多米诺之和.

    Args:
        l_list: 每个位置的左侧数列.
        r_list: 每个位置的右侧数列.
        first: 起始位置.
        last: 末尾位置.
        w_list: 状态列表

    Returns:
        多米诺计算之和.
    """
    if last - first < 2:  # 牌的个数需要大于1
        return -1

    def get_domino_max(l_list, r_list, first, last):
        if last - first == 1:
            print('last==first:{},{}, r-num:{},l-num:{}'.format(last, first, r_list[first], l_list[last]))
            max = r_list[first] * l_list[last]
        else:
            middle = int((first + last) / 2)
            print('middle:{}'.format(middle))
            print('1 get_domino_max==first==middle:{},{}'.format(first, middle))
            max_l1 = get_domino_max(l_list, r_list, first, middle)
            print('1 get_domino_max==last==middle:{},{}'.format(last, middle))
            max_r1 = get_domino_max(l_list, r_list, middle, last)
            max1 = max_l1 + max_r1
            # 交换
            temp = l_list[middle]
            l_list[middle] = r_list[middle]
            r_list[middle] = temp
            print('2 get_domino_max==first==middle:{},{}'.format(first, middle))
            max_l2 = get_domino_max(l_list, r_list, first, middle)
            print('2 get_domino_max==last==middle:{},{}'.format(last, middle))
            max_r2 = get_domino_max(l_list, r_list, middle, last)
            max2 = max_l2 + max_r2
            if max1 > max2:
                max = max1
                w_list[middle] = 1
            else:
                max = max2
                w_list[middle] = 0
        return max
    return get_domino_max(l_list, r_list, first, last)


if __name__ == "__main__":
    s = [[5, 8], [4, 2], [9, 6], [7, 7], [3, 9], [11, 10]]
    n = len(s)
    r_list = [0]
    l_list = list()
    for l, r in s:
        l_list.append(l)
        r_list.append(r)
    l_list.append(0)
    first = 0
    last = n
    w_list = [0] * n
    print('l_list:{}'.format(l_list))
    print('r_list:{}'.format(r_list))
    max = calculate_domino(l_list, r_list, first, last, w_list)
    print('l_list:{}'.format(l_list))
    print('r_list:{}'.format(r_list))
    print(max)
    print(w_list)
