def main(str_num):
    total = 0
    N = len(str_num)
    for bit in range(1<<(N-1)):
        tmp = ''
        for i in range(N):
            tmp += str_num[i]
            if(bit & (1<<i)):
                total += int(tmp)
                tmp = ''
        if tmp:
            total += int(tmp)
    return total


if __name__ == '__main__':
    print(main('125'))