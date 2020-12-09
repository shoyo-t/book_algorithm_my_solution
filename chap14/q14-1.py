# トポロジカルソートと同じ原理。
# 一番矢印の末端にいるところから0が埋まっていく。
# 一番手前が最後に埋まり、それが最長
def rec(v: int) -> int:
    if dp[v] != -1:
        return dp[v]
    
    res = 0
    for next_v in graph[v]:
        res = max(res, rec(next_v) + 1)
    dp[v] = res
    return res

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

    res = 0
    for v in range(N):
        res = max(res, rec(v))
    return res


if __name__ == '__main__':
    dp = []
    # 入力例1 答え3
    N = 4
    edges = [(1, 2),(1, 3),(3, 2),(2, 4),(3, 4)]
    graph = get_graph(edges, N, True)
    dp = [-1] * N
    print('answer: ', main())

    # 入力例2 答え2
    N = 6
    edges = [(2, 3),(4, 5),(5, 6)]
    graph = get_graph(edges, N, True)
    dp = [-1] * N
    print('answer: ', main())

    # 入力例3 答え3
    N = 5
    edges = [(5, 3),(2, 3),(2, 4),(5, 2),(5, 1),
             (1, 4),(4, 3),(1, 3)]
    graph = get_graph(edges, N, True)
    dp = [-1] * N
    print('answer: ', main())