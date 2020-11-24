# 最初の回答
# def main(K):
#     tgt_nums = ['7', '5', '3']
#     cnt = 0
#     for i in range(K+1):
#         str_i = str(i)
#         if all(tgt in str_i for tgt in tgt_nums):
#             cnt += 1
#     return cnt

# 答えを見て回答
def main(N, cur, use, cnt):
    if(cur > N):
        return cnt
    if(use == 0b111):
        cnt += 1
    
    cnt = main(N, cur * 10 + 7, use | 0b001, cnt)
    cnt = main(N, cur * 10 + 5, use | 0b010, cnt)
    cnt = main(N, cur * 10 + 3, use | 0b100, cnt)

    return cnt


if __name__ == '__main__':
    print(main(1000, 0, 0, 0))