'''
前提：
M個の小屋をちょうど選択できる最小距離dを二分探索で求めていく
'''
def check(sorted_a, N, M, d):
    prev = sorted_a[0]
    cow = 1
    for i in range(1, N):
        if sorted_a[i] - prev >= d:
            cow += 1
            prev = sorted_a[i]
            if cow == M:
                break
    return cow == M

def func(a, M):
    sorted_a = sorted(a)
    N = len(a)
    left, right = 1, 100

    while right - left > 1:
        mid = (left + right) // 2
        if check(sorted_a, N, M, mid):
            left = mid
        else:
            right = mid
    return left

if __name__ == '__main__':
    a  = [5, 2, 20, 9, 14]
    print(func(a, 3))
