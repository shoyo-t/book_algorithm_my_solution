def func(M: int, list_a: list) -> int:
    N = len(list_a)
    sorted_a = sorted(list_a, key=lambda x:x[0])

    ans = 0
    bi_total = 0
    for ai, bi in sorted_a:
        if bi_total > M:
            break

        if bi + bi_total <= M:
            ans += ai * bi
        else:
            ans += ai * (M - bi_total)
        
        bi_total += bi
    
    return ans



if __name__ == '__main__':
    # 公式ページ：入力例1
    M = 5
    list_a = [(4,9), (2,4)]
    print(func(M, list_a))

    # 公式ページ：入力例2
    M = 30
    list_a = [(6,18), (2,5), (3,10), (7,9)]
    print(func(M, list_a))

    # 公式ページ：入力例3
    M = 100000
    list_a = [(1000000000,100000)]
    print(func(M, list_a))