def dfs(graph: list, v: int) -> None:
    seen[v] = True

    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(graph, next_v)

def get_graph(edges: list, N: int, is_directed: bool=False) -> list:
    graph = [[] * i for i in range(N)]
    for e in edges:
        a, b = e
        graph[a].append(b)
        if not is_directed:
            graph[b].append(a)
    return graph

def main(edges: list, N: int) -> int:

    # edgesからグラフを作成
    graph = get_graph(edges, N)
    
    ans = 0
    for v in range(N):
        if seen[v]:
            continue
        dfs(graph, v)
        # 未探索のノードに来た時にインクリメントする
        ans += 1
    return ans


if __name__ == '__main__':
    # p164のグラフ 答え0
    N = 12
    edges = [(4, 1),(4, 2),(4, 6),(1, 3),(1, 6),
             (2, 5),(2, 7),(6, 7),(3, 0),(3, 7),
             (7, 0),(0, 5),(9,10),(10,11)]
    seen = [False] * N
    print('answer: ', main(edges, N))
