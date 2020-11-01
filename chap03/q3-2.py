def main(num_list, search_num):
    cnt = 0
    for num in num_list:
        if num == search_num:
            cnt += 1
    return cnt


if __name__ == '__main__':
    num_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]
    print(main(num_list, 3))
    print(main(num_list, 1))
    print(main(num_list, 4))