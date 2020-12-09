'''
・基本的には幅優先探索で考える
・同じ店を通って調整しつつ、Tに3の倍数でいくことも可能
・そのため、各点にきた時の歩数を3で割ったとき余りのパターン分、最短距離を保持しておけばいい
・参考：https://qiita.com/vain0x/items/e2aa40d3305029f52702
'''
def get_graph(edges: list, N: int, is_directed: bool=False) -> list:
    graph = [[] * i for i in range(N)]
    for e in edges:
        a, b = e
        a, b = a - 1, b - 1
        graph[a].append(b)
        if not is_directed:
            graph[b].append(a)
    return graph

def main() -> int:

    dist = [[-1] * 3 for i in range(N)]
    dist[S][0] = 0

    que_list = []
    que_list.append((S, 0))
    while que_list:
        v, p = que_list.pop(0)
        for next_v in graph[v]:
            next_p = (p + 1) % 3
            if dist[next_v][next_p] == -1:
                dist[next_v][next_p] = dist[v][p] + 1
                que_list.append((next_v, next_p))
    
    print(dist)
    if dist[T][0] == -1:
        return -1
    else:
        return dist[T][0] / 3


if __name__ == '__main__':
    dp = []
    # 入力例1 答え2
    N = 4
    edges = [(1, 2),(2, 3),(3, 4),(4, 1)]
    S, T = 1, 3
    S, T = S - 1, T - 1
    graph = get_graph(edges, N, True)
    print('answer: ', main())

    # 入力例2 答え-1
    N = 3
    edges = [(1, 2),(2, 3),(3, 1)]
    S, T = 1, 2
    S, T = S - 1, T - 1
    graph = get_graph(edges, N, True)
    print('answer: ', main())

    # 入力例3 答え-1
    N = 2
    edges = []
    S, T = 1, 2
    S, T = S - 1, T - 1
    graph = get_graph(edges, N, True)
    print('answer: ', main())

    # 入力例4 答え2
    N = 6
    edges = [(1, 2),(2, 3),(3, 4),(4, 5),(5, 1),
             (1, 4),(1, 5),(4, 6)]
    S, T = 1, 6
    S, T = S - 1, T - 1
    graph = get_graph(edges, N, True)
    print('answer: ', main())
