def P_for_a(val1, val2):
    return val1 >= val2

def P_for_c(val1, val2):
    return val1 > val2

def binary_search(sorted_nums, val, P):
    # sorted_numsの中で関数PがTrueとなる要素数を調べる関数

    left, right = 0, len(sorted_nums) - 1

    # leftがFalse, rightがTrueでなかった場合の処理
    if not P(sorted_nums[right], val): #sorted_nums[right] < val:
        return 0
    elif P(sorted_nums[left], val): #sorted_nums[left] >= val:
        return len(sorted_nums)
    
    # Trueの最小値を探索
    while right > left + 1:
        mid = (left + right) // 2
        if P(sorted_nums[mid], val):   #sorted_nums[mid] >= val:
            right = mid
        else:
            left = mid

    return len(sorted_nums) - right

def func(a, b, c):
    sorted_a = sorted(a)
    sorted_c = sorted(c)
    ans = 0
    for b_num in b:
        ans += (len(a) - binary_search(sorted_a, b_num, P_for_a)) \
                * (binary_search(sorted_c, b_num, P_for_c))
    return ans

if __name__ == '__main__':
    a1 = [1, 5]
    b1 = [2, 4]
    c1 = [3, 6]
    print(func(a1, b1, c1))

    a2 = [1, 1, 1]
    b2 = [2, 2, 2]
    c2 = [3, 3, 3]
    print(func(a2, b2, c2))

    a3 = [3, 14, 159, 2, 6, 53]
    b3 = [58, 9, 79, 323, 84, 6]
    c3 = [2643, 383, 2, 79, 50, 288]
    print(func(a3, b3, c3))
