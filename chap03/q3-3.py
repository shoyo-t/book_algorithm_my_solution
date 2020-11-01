def main(num_list):
    min_val = 999999
    sec_val = 999999
    for num in num_list:
        if num < min_val:
            min_val = num
        elif num < sec_val:
            sec_val = num
    return sec_val


if __name__ == '__main__':
    num_list = [5,6,7,1,3,4]
    print(main(num_list))
