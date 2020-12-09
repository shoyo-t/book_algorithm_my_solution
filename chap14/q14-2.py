'''
・けんちょんさんの答えを見ながら実装
・やりたいことはわかるが、なぜN*2のイテレーションをするのかわかっていない
・V-1で本来更新が終わるのになぜN*2なんだろう。
・入力例だとN回のイテレーションでも答えは同じだった。
'''
import sys

def get_w_graph(edges: list, N: int) -> list:
    w_graph = [[] * i for i in range(N)]
    for e in edges:
        a, b, w = e
        a, b = a - 1, b - 1
        w_graph[a].append((b, -w))
    return w_graph

def main():

    # 頂点Nに関係ある不閉路判定
    negative = False
    dist[0] = 0
    
    for itr in range(N*2 + 1):
        for v in range(N):
            if dist[v] == INF:
                continue
            for e in w_graph[v]:
                if dist[e[0]] > dist[v] + e[1]:
                    dist[e[0]] = dist[v] + e[1]
                    if e[0] == N-1 and itr == N*2:
                        negative = True
    if not negative:
        return -dist[N-1]
    else:
        return 'inf'


if __name__ == '__main__':
    INF = sys.maxsize
    # 入力例1 答え7
    N = 3
    edges = [(1, 2, 4),(2, 3, 3),(1, 3, 5)]
    w_graph = get_w_graph(edges, N)
    dist = [INF] * N
    print('answer: ', main())

    # 入力例2 答えinf
    N = 2
    edges = [(1, 2, 1),(2, 1, 1)]
    w_graph = get_w_graph(edges, N)
    dist = [INF] * N
    print('answer: ', main())

    # # 入力例3 答え-5000000000
    N = 6
    edges = [(1, 2, -1000000000),(2, 3, -1000000000),(3, 4, -1000000000),
             (4, 5, -1000000000),(5, 6, -1000000000)]
    w_graph = get_w_graph(edges, N)
    dist = [INF] * N
    print('answer: ', main())