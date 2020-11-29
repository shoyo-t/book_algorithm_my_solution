def func(a, b, c, N):
    # dpの初期化
    dp = [[-1] * (3) for i in range(N)]

    # i = 0 だったら初日のものを入れる
    dp[0][0] = a[0]
    dp[0][1] = b[0]
    dp[0][2] = c[0]

    # Nまでメモ化で求めていく
    for i in range(1, N):
        dp[i][0] = max(dp[i - 1][1] + a[i], dp[i - 1][2] + a[i])
        dp[i][1] = max(dp[i - 1][0] + b[i], dp[i - 1][2] + b[i])
        dp[i][2] = max(dp[i - 1][0] + c[i], dp[i - 1][1] + c[i])

    return max(dp[N-1][0], dp[N-1][1], dp[N-1][2])

if __name__ == '__main__':
    a1 = [10, 20, 30]
    b1 = [40, 50, 60]
    c1 = [70, 80, 90]
    N1 = len(a1)
    print(func(a1, b1, c1, N1))
    a2 = [100]
    b2 = [10]
    c2 = [1]
    N2 = len(a2)
    print(func(a2, b2, c2, N2))
    a3 = [6, 8, 2, 7, 4, 2, 7]
    b3 = [7, 8, 5, 8, 6, 3, 5]
    c3 = [8, 3, 2, 6, 8, 4, 1]
    N3 = len(a3)
    print(func(a3, b3, c3, N3))
