def func(list_a, list_b):
    tmp = [0]*100
    cnt = 0
    
    for a in list_a:
        tmp[a] += 1
    
    for b in list_b:
        cnt += tmp[b]
    
    return cnt

if __name__ == '__main__':
    list_a = [6,3,7,5,4,4]
    list_b = [1,6,4,7,7]
    print(func(list_a, list_b))
