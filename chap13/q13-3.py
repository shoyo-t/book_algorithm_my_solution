def bfs(graph: list, v: int) -> bool:
    color[v] = 0

    que_list = [v]
    while que_list:
        v = que_list.pop(0)
        cur = color[v]
        for next_v in graph[v]:
            if color[next_v] != -1:
                if color[next_v] == cur:
                    return False
                continue
            color[next_v] = 1 - cur
            que_list.append(next_v)
    return True

def get_graph(edges: list, N: int, is_directed: bool=False) -> list:
    graph = [[] * i for i in range(N)]
    for e in edges:
        a, b = e
        graph[a].append(b)
        if not is_directed:
            graph[b].append(a)
    return graph

def main(edges: list, N: int) -> bool:

    # edgesからグラフを作成
    graph = get_graph(edges, N)
    
    for v in range(N):
        if color[v] != -1:
            continue
        if not bfs(graph, v):
            return False

    return True


if __name__ == '__main__':
    # p232のグラフ 答えTrue
    N = 5
    edges = [(0, 1),(0, 3),(1, 2),(1, 4),(3, 4)]
    color = [-1] * N
    print(main(edges, N))

    # p232のグラフに辺を追加 答えTrue
    N = 5
    edges = [(0, 1),(0, 3),(1, 2),(1, 4),(3, 4),(0,4)]
    color = [-1] * N
    print(main(edges, N))
