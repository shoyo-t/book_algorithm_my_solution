def func(i, w, a):
    if(i == 0):
        if(w == 0):
            return True
        else:
            return False

    if(memo[i][w] != -1):
        return memo[i][w]
    
    if(func(i-1, w, a)):
        memo[i][w] = 1
        return memo[i][w]
    
    if(func(i-1, w - a[i-1], a)):
        memo[i][w] = 1
        return memo[i][w]
    
    memo[i][w] = 0
    return memo[i][w]


if __name__ == '__main__':
    a = [3, 2, 6, 5]
    N = len(a)
    W = 12
    memo = [[-1] * (W+1) for i in range(N+1)]
    print(func(N, W, a))
