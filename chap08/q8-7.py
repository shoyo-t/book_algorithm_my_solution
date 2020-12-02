def func(list_a, list_b, N, K):
    # 数列に負の数があると動作しない。
    # 正負で2次元配列にすればできる？
    tmp = [-1]*20
    
    for a in list_a:
        tmp[a] = 1
    
    for b in list_b:
        if K - b < 0:
            continue
        if tmp[K-b] == 1:
            return True
    return False

if __name__ == '__main__':
    list_a = [6,3,7,5,8]
    list_b = [1,6,4,7,2]
    N = len(list_a)
    print(func(list_a, list_b, N, 3))
    print(func(list_a, list_b, N, 13))
