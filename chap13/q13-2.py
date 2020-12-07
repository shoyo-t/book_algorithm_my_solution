def bfs(graph: list, v: int) -> None:
    seen[v] = True

    que_list = [v]
    while que_list:
        v = que_list.pop(0)

        for next_v in graph[v]:
            if seen[next_v]:
                continue
            seen[next_v] = True
            que_list.append(next_v)

def get_graph(edges: list, N: int, is_directed: bool=False) -> list:
    graph = [[] * i for i in range(N)]
    for e in edges:
        a, b = e
        graph[a].append(b)
        if not is_directed:
            graph[b].append(a)
    return graph

def main(edges: list, N: int, s: int, t: int) -> bool:

    # edgesからグラフを作成
    graph = get_graph(edges, N)
    
    # 頂点sをスタートとして探索
    bfs(graph, s)

    return seen[t]


if __name__ == '__main__':
    # p164のグラフ 答え0
    N = 12
    edges = [(4, 1),(4, 2),(4, 6),(1, 3),(1, 6),
             (2, 5),(2, 7),(6, 7),(3, 0),(3, 7),
             (7, 0),(0, 5),(9,10),(10,11)]
    seen = [False] * N
    print(main(edges, N, 4, 5))
    print(main(edges, N, 4, 9))
    print(main(edges, N, 11, 9))
