def func(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x['t'])
    total_time = 0
    for task in sorted_tasks:
        total_time += task['d']
        if total_time > task['t']:
            return False
    return True

if __name__ == '__main__':
    tasks = [
        {'d': 4, 't': 10},
        {'d': 2, 't': 4},
        {'d': 3, 't': 5},
        {'d': 1, 't': 7},
    ]
    print(func(tasks))
