def func(N, a, b):
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    cnt = 0
    i, j = 0, 0
    while j < N:
        if sorted_a[i] < sorted_b[j]:
            cnt += 1
            i += 1
        j += 1
    return cnt
        
if __name__ == '__main__':
    a = [9, 5, 8, 3]
    b = [4, 7, 2, 6]
    N = len(a)
    print(func(N, a, b))
        