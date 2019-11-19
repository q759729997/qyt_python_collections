"""
已知一个长度为n 的数组和一个正整数k，并且最多只能使用一个用
于交换数组元素的附加空间单元，试设计算法得到原数组循环右移k
次的结果并分析算法的时间复杂度。
参考：https://segmentfault.com/a/1190000020745639
"""


def reverse(start, end, B):  # 逆置函数
    i = start
    j = end
    temp = 0  # 附加空间
    counter = 0
    while (i < j):
        temp = B[i]
        B[i] = B[j]
        B[j] = temp
        j -= 1
        i += 1
        counter += 1
    return counter


def exchange(Num, k, B):  # 生成函数
    k = k % Num
    counter = 0
    counter += reverse(0, Num - k - 1, B)  # 注意传参时一维数组下标由0开始
    print(counter)
    counter += reverse(Num - k, Num - 1, B)
    print(counter)
    counter += reverse(0, Num - 1, B)
    print(counter)


if __name__ == "__main__":
    # 1.输入n和k
    # input_n = input("请输入数组长度：")
    # input_k = input("请输入右移位数：")
    input_n = 33
    input_k = 9

    n = input_n
    k = input_k

    # 2.初始化数组
    arr = [i for i in range(1, n + 1)]
    print("生成数组")
    print(arr)

    # 3.移动数组
    exchange(input_n, input_k, arr)

    # 4.打印结果
    print("交换最终结果")
    print(arr)
