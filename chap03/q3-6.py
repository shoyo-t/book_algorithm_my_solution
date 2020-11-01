def main(K, N):
    cnt = 0
    for x in range(min(K, N) + 1):
        for y in range(min(K, N) + 1):
            z = N-x-y
            if (z >= 0 and z <= K):
                print(x,y,z)
                cnt += 1
    return cnt


if __name__ == '__main__':
    K = 3
    N = 4
    print(main(K, N))
