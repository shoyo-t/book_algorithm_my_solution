'''
・q13-4と考え方は同じ
'''
import sys

def bfs(y: int, x: int) -> int:

    score = [[sys.maxsize] * W for i in range(H)]  
    score[y][x] = 0
    move = [(1,0),(0,1),(-1,0),(0,-1)]
    que_list = [(y, x)]
    while que_list:
        y, x = que_list.pop(0)
        for i, j in move:
            next_y, next_x = y + i, x + j
            if (next_y > H-1 or next_y < 0 or
                next_x > W-1 or next_x < 0):
                continue
            next_area = maze[next_y][next_x]
            # 壁かつ最短経路だったら更新
            if (next_area == '#' and
                score[next_y][next_x] > score[y][x] + 1):
                score[next_y][next_x] = score[y][x] + 1
                que_list.append((next_y, next_x))
            # 壁じゃないかつ最短経路だったら更新
            if (next_area != '#' and
                score[next_y][next_x] > score[y][x]):
                score[next_y][next_x] = score[y][x]
                que_list.append((next_y, next_x))
    # print(*score, sep='\n')
    return score[gy][gx]

def set_start_goal() -> None:
    for i in range(H):
        for j in range(W):
            if maze[i][j] == 's':
                sy, sx = i, j
            if maze[i][j] == 'g':
                gy, gx = i, j
    return sy, sx, gy, gx

if __name__ == '__main__':
    # 入力例1 答え1
    maze = [
        ['s','#','#','#','#'],
        ['.','.','.','.','#'],
        ['#','#','#','#','#'],
        ['#','.','.','.','g'],
    ]
    H, W = len(maze), len(maze[0])
    sy, sx, gy, gx = set_start_goal()
    print('answer: ', bfs(sy, sx))

    # 入力例2 答え0
    maze = [
        ['.','.','.','s'],
        ['.','.','.','.'],
        ['.','.','.','.'],
        ['.','g','.','.'],
    ]
    H, W = len(maze), len(maze[0])
    sy, sx, gy, gx = set_start_goal()
    print('answer: ', bfs(sy, sx))

    # 入力例3 答え2
    maze = [
        ['s','.','.','.','.','.','.','.','.','.'],
        ['#','#','#','#','#','#','#','#','#','.'],
        ['#','.','.','.','.','.','.','.','#','.'],
        ['#','.','.','#','#','#','#','.','#','.'],
        ['#','#','.','.','.','.','#','.','#','.'],
        ['#','#','#','#','#','.','#','.','#','.'],
        ['g','#','#','.','#','.','#','.','#','.'],
        ['#','#','#','.','#','.','#','.','#','.'],
        ['#','#','#','.','#','.','#','.','#','.'],
        ['#','.','.','.','.','.','#','.','.','.'],
    ]
    H, W = len(maze), len(maze[0])
    sy, sx, gy, gx = set_start_goal()
    print('answer: ', bfs(sy, sx))

    # 入力例4 答え2
    maze = [
        ['.','.','.','.','.','s'],
        ['#','#','#','.','.','.'],
        ['#','#','#','.','.','.'],
        ['#','#','#','#','#','#'],
        ['.','.','.','#','#','#'],
        ['g','.','#','#','#','#'],
    ]
    H, W = len(maze), len(maze[0])
    sy, sx, gy, gx = set_start_goal()
    print('answer: ', bfs(sy, sx))

    # 入力例5 答え4
    maze = [
        ['s','.','.','#','#','#','#','.','.','g'],
    ]
    H, W = len(maze), len(maze[0])
    sy, sx, gy, gx = set_start_goal()
    print('answer: ', bfs(sy, sx))
