def func(a, N, W, k):
    # dpの初期化
    dp = [[INF] * (W + 1) for i in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        for w in range(W + 1):
            dp[i+1][w] = dp[i][w]
            if(w >= a[i]):
                dp[i+1][w] = min(dp[i+1][w], dp[i][w-a[i]] + 1)
    # print(dp)
    return dp[N][W] <= k

if __name__ == '__main__':
    INF = 99999
    a1 = [3, 2, 4] # 最小：[0, 99999, 1, 1, 1, 2, 2, 2, 99999, 3, 99999, ... ]
    N1 = len(a1)
    print(func(a1, N1, 10, 4))
