def binary_search(sorted_nums, val):
    left, right = 0, len(sorted_nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_nums[mid] == val:
            return mid
        elif sorted_nums[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def func(not_sorted_nums):
    sorted_nums = sorted(not_sorted_nums)
    ans = []
    for num in not_sorted_nums:
        ans.append(binary_search(sorted_nums, num))
    return ans

if __name__ == '__main__':
    a = [12, 43, 7, 15, 9]
    print(func(a))
