if __name__ == "__main__":
    """计算RSA"""
    p = 3
    q = 11
    e = 7
    M = 5
    n = p * q
    print('n=pq={}×{}={}'.format(p, q, n))
    phi_n = (p - 1) * (q - 1)
    print('φ(n)=(p-1)(q-1)={}×{}={}'.format(p-1, q-1, phi_n))