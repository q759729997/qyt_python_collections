def get_d(e, phi_n):
    """计算d"""
    print('de=1(modφ(n))')
    print('=====d的计算过程,k系数为1时，另d=1，d系数为1时，另k=0倒序代入======')
    print('{}d-{}k=1'.format(e, phi_n))
    arg1 = e
    arg2 = phi_n
    while arg1 != 1 and arg2 != 1:
        if arg2 > arg1:
            arg2 = arg2 % arg1
            print('{}d-{}k=1'.format(arg1, arg2))
        else:
            arg1 = arg1 % arg2
            print('{}d-{}k=1'.format(arg1, arg2))
    print('====计算机求d===')
    for i in range(1, 10000):
        if (phi_n * i + 1) % e == 0:
            break
    print('{}d-{}×{}=1'.format(e, phi_n, i))
    return (1 + phi_n * i) / e



if __name__ == "__main__":
    """计算RSA"""
    p = 3
    q = 11
    e = 7
    M = 5
    p = 5
    q = 11
    e = 3
    M = 9
    n = p * q
    print('n=pq={}×{}={}'.format(p, q, n))
    phi_n = (p - 1) * (q - 1)
    print('φ(n)=(p-1)(q-1)={}×{}={}'.format(p-1, q-1, phi_n))
    d = get_d(e, phi_n)
    print('d={}'.format(d))