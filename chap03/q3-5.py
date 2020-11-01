def main(num_list):
    min_cnt = 999999
    for num in num_list:
        tmp_cnt = 0
        while num % 2 == 0:
            num = num / 2
            tmp_cnt += 1
        if(tmp_cnt < min_cnt):
            min_cnt = tmp_cnt
    return min_cnt


if __name__ == '__main__':
    #num_list = [5,6,7,3,4]
    num_list = [12,4,8]
    print(main(num_list))
