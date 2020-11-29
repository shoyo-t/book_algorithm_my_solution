def func(a, N, W):
    # dpの初期化
    dp = [[False] * (W + 1) for i in range(N+1)]
    dp[0][0] = True

    for i in range(N):
        for w in range(W + 1):
            if(dp[i][w]):
                dp[i+1][w] = True
            elif(w >= a[i] and dp[i][w-a[i]]):
                dp[i+1][w] = True
    # print(dp)
    return dp[N][W]

if __name__ == '__main__':
    a1 = [3, 2, 4] # True: 2,3,4,5,6,7,9
    N1 = len(a1)
    print(func(a1, N1, 10))
