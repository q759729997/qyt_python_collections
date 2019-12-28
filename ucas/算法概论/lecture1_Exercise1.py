"""
已知一个长度为n 的数组和一个正整数k，并且最多只能使用一个用
于交换数组元素的附加空间单元，试设计算法得到原数组循环右移k
次的结果并分析算法的时间复杂度。
参考：https://blog.csdn.net/still_night/article/details/84662311

"""


# 函数：打印数组
def printarr(arr):
    print(", ".join([str(c) for c in arr]))


# 函数：求最大公约数
def gcd(a, b):
    temp = max(a, b) % min(a, b)
    if temp == 0:
        return min(a, b)
    else:
        return gcd(min(a, b), temp)


# 函数：交换数组内两元素
def swapnum(arr, a, b):
    x = arr[a]
    arr[a] = arr[b]
    arr[b] = x


if __name__ == "__main__":
    # 1.输入n和k
    # input_n = input("请输入数组长度：")
    # input_k = input("请输入右移位数：")
    input_n = 15
    input_k = 9

    n = input_n
    k = input_k
    x = gcd(n, k)

    # 2.初始化数组
    arr = [i for i in range(1, n + 1)]
    print("生成数组")
    printarr(arr)

    # 3.移动数组
    counter = 0
    for i in range(int(len(arr) / x - 1)):
        for j in range(x):
            counter += 1
            print('=============第{}次==========='.format(counter))
            print("交换元素：" + str(j) + " ←→ " + str(((i + 1) * k + j) % len(arr)))
            swapnum(arr, j, ((i + 1) * k + j) % len(arr))
            printarr(arr)

    # 4.打印结果
    print("交换最终结果")
    printarr(arr)
