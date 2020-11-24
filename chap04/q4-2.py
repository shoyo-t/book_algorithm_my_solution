def tribonacci(N):
    if(N == 0):
        return 0
    elif(N == 1):
        return 0
    elif(N == 2):
        return 1
    
    if(memo[N] != -1):
        return memo[N]
    else:
        memo[N] = tribonacci(N-1) + tribonacci(N-2) + tribonacci(N-3)

    return memo[N]


if __name__ == '__main__':
    N = 9
    memo = [-1]*N
    print(tribonacci(N-1))
    print(tribonacci(N))