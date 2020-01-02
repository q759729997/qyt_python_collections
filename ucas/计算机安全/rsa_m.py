def get_d(e, phi_n):
    """计算d"""
    print('de 三等号 1(mod φ(n))')
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
    d = int((1 + phi_n * i) / e)
    return d


def get_mod(a, b, a_pow=1):
    """取模"""
    print('{} = {} (mod {})'.format(a, a % b, b))
    if a_pow > 1:
        print('{}**{} = {} (mod {})'.format(a, 2, a**2 % b, b))
    if a_pow > 3:
        print('{}**{} = {} (mod {})'.format(a, 4, a**4 % b, b))
    return a**a_pow % b


if __name__ == "__main__":
    """计算RSA
    3, 11, 7, 5
    5, 11, 3, 9
    7, 11, 17, 8
    """
    e, phi_n = 5, 24
    n, C = 35, 10
    print('=========求d==============')
    d = get_d(e=e, phi_n=phi_n)
    print('d={}'.format(d))
    print('=========求M==============')
    M = get_mod(C, n, a_pow=d)
    print('M={}'.format(M))
    print('M=C**d mod n={}**{} mod {}'.format(C, d, n))
