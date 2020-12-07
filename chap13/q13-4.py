'''
・幅優先探索で実装。深さでもできるが、めんどいのでいったんやらない。
・本の通りグラフ探索を行うのではなく、ググって出てきた方法で実装。
・迷路の各セルをノードとして、迷路を用いて移動可能箇所を洗い出してグラフにすれば本の通りできるはず。
'''
import sys

def bfs(maze: list, sy: int, sx: int, gy: int, gx: int) -> int:
    h, w = len(maze), len(maze[0])
    ans = [[sys.maxsize] * w for i in range(h)]
    
    ans[sy-1][sx-1] = 0
    move = [(1,0),(0,1),(-1,0),(0,-1)]
    que_list = [(sy-1, sx-1)]
    while que_list:
        y, x = que_list.pop(0)
        for i, j in move:
            next_y, next_x = y + i, x + j
            if (next_y > h-1 or next_y < 0 or
                next_x > w-1 or next_x < 0):
                continue
            next_area = maze[next_y][next_x]
            # 壁じゃないかつ最短経路だったら更新
            if (next_area != '#' and
                ans[next_y][next_x] > ans[y][x] + 1):
                ans[next_y][next_x] = ans[y][x] + 1
                que_list.append((next_y, next_x))
    # print(*ans, sep='\n')
    return ans[gy-1][gx-1]



if __name__ == '__main__':
    maze = [
        ['.','#','.','.','.','.','#','.'],
        ['.','#','.','#','.','.','.','.'],
        ['.','.','.','#','.','#','#','.'],
        ['#','.','#','#','.','.','.','#'],
        ['.','.','.','#','#','#','.','#'],
        ['.','#','.','.','.','.','.','#'],
        ['.','.','.','#','.','#','.','.'],
        ['.','.','.','.','.','.','.','.'],
    ]
    sy, sx = 8, 1
    gy, gx = 1, 8
    print('answer: ', bfs(maze, sy, sx, gy, gx))
