"""
- 给定有向图 $G$ :
- (1) 证明图 $G$ 的凝聚图 $G\downarrow$ 是有向无环图。
- (2) 若图 $G$ 以邻接表的形式存储，试写出一个算法求图 $G$ 的转置图 $G^{T}$ 。
"""

if __name__ == "__main__":
    # 邻接表
    adjInfo = {
        1: [2],
        2: [3, 4],
        3: [1, 6],
        4: [2, 3],
        5: [],
        6: [4, 5, 7],
        7: [6]
    }
    print('邻接表:')
    for key, value in adjInfo.items():
        print('{} -> {}'.format(key, value))
    # 计算转置
    adjInfo_T = dict([(key, list()) for key in adjInfo])
    for key, items in adjInfo.items():
        for item in items:
            items_T = adjInfo_T.get(item)
            items_T.append(key)
            adjInfo_T[item] = items_T
    print('邻接表的转置:')
    for key, value in adjInfo_T.items():
        print('{} -> {}'.format(key, value))
