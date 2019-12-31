"""
在一条街上有n所房子，$H[i](1\leq i\leq n)$ 是第i所房子离街道起点处的距离（以米为单位），假设 $H[1]< H[2]<\cdots  < H[n]$ 。目前该街道上还没有一所邮局，现计划新建若干所邮局，使得每所房子到最近的邮局距离在100米以内。试设计一个时间复杂度为O(n)的算法，计算出新建邮局的位置，即每所新建邮局离街道起点处的距离 $P[j](1\leq j\leq m)$ ,同时确保新建邮局个数m最小。
"""
import random


if __name__ == "__main__":
    # 随机生成房子的位置
    H = random.sample(list(range(1, 2019)), k=10)
    H.sort()
    P = list()
    # 距离第一个房子100米的地方，设置第一个邮局
    P.append(H[0]+100)
    for i in range(1, len(H)):
        # 若当前房子距离最新的邮局距离超过100米，则添加一个邮局
        if H[i] > (P[-1] + 100):
            P.append(H[i]+100)
    print('房子位置：{}'.format(H))
    print('邮局位置：{}'.format(P))
    print('邮局个数：{}'.format(len(P)))
