def tribonacci(N):
    if(N == 0):
        return 0
    elif(N == 1):
        return 0
    elif(N == 2):
        return 1
    return tribonacci(N-1) + tribonacci(N-2) + tribonacci(N-3)


if __name__ == '__main__':
    N = 9
    print(tribonacci(N-1))
    print(tribonacci(N))