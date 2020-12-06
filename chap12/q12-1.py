# O(n^2)よりいいのありそうだけど、いったん回答とする
def func(list_a: list) -> list:
    n = len(list_a)
    ans = [1] * n
    for i in range(n):
        for j in range(i+1, n):
            if list_a[i] < list_a[j]:
                ans[i] += 1
            elif list_a[i] > list_a[j]:
                ans[j] += 1
    return ans


if __name__ == '__main__':
    list_a = [70, 80, 50, 70, 95]
    print(func(list_a))
