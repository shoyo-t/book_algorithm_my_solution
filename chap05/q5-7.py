def func(S, T):
    # dpの初期化
    dp = [[0] * (len(T) + 1) for i in range(len(S) + 1)]

    for i in range(len(S)):
        for j in range(len(T)):
            if(S[i] == T[j]):
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    
    # 復元
    i = len(S)
    j = len(T)
    common_sub = ''
    while i > 0 and j > 0:
        if(dp[i][j] == dp[i-1][j]):
            i -= 1
        elif(dp[i][j] == dp[i][j-1]):
            j -= 1
        else:
            common_sub = S[i-1] + common_sub
            i -= 1
            j -= 1
    return common_sub

if __name__ == '__main__':
    print(func('kodansha', 'danshari'))
    print(func('logistic', 'algorithm'))
