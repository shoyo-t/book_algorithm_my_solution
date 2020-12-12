'''
・既存のソースを組み合わせたので鬼汚い。
・s-t間の最短路に採用されない辺は増やしても意味ないので、最短路で使われる辺のみで考える
・最短路のみで使われる辺のうちコストが最小となるものを選ぶ。
・上記はは最短距離のみのグラフの最小カットを求めればわかる。
・参考：
　https://drken1215.hatenablog.com/entry/2019/02/15/190700
'''

import sys

class Edge():
    def __init__(self, frm: int, to: int, cap: int, rev_index: int) -> None:
        self.frm = frm
        self.to = to
        self.cap = cap
        self.rev_index = rev_index

    def add_cap(self, f: int) -> None:
        self.cap += f


class Graph():
    def __init__(self, N: int) -> None:
        self.graph = [[] for i in range(N)] # Edgeのリストを保持する
    
    def make_graph(self, edges: list) -> None:
        for e in edges:
            self.add_edge(e[0] - 1, e[1] - 1, e[2]) # q16-1からここを修正
    
    # edgeの初期追加時に使用
    # edge追加時に同時にtoからfromのedgeも容量0で追加する
    def add_edge(self, frm: int, to: int, cap: int) -> None:
        from_rev = len(self.graph[frm])
        to_rev = len(self.graph[to])
        self.graph[frm].append(Edge(frm, to, cap, to_rev))
        self.graph[to].append(Edge(to, frm, 0, from_rev))
    
    def run_flow(self, e: Edge, f: int) -> None:
        e.add_cap(-f)
        self.graph[e.to][e.rev_index].add_cap(f)


class FordFulkerson():
    
    def __init__(self) -> None:
        pass

    def fodfs(self, graph: Graph, v: int, t: int, f: int) -> int:
        # tまで到達したらreturn
        if v == t:
            return f
        
        # 深さ優先探索を実行
        self.seen[v] = True
        for e in graph.graph[v]:
            # 探索済みだったらスキップ
            if self.seen[e.to]:
                continue

            # 容量0ならスキップ
            if e.cap == 0:
                continue

            # s-tパスを探す
            flow = self.fodfs(graph, e.to, t, min(f, e.cap))

            # パスがなかったらスキップ
            if flow == 0:
                continue

            # 辺2に容量を流す
            graph.run_flow(e, flow)

            # s-tパスの最小容量を返す
            return flow
        
        # s-tパスが見つからなかった場合
        return 0

    def solve(self, graph: Graph, s: int, t: int) -> int: 
        res = 0

        # 残余グラフにs-tパスがなくなるまで反復
        while True:
            self.seen = [False] * len(graph.graph)
            flow = self.fodfs(graph, s, t, sys.maxsize)

            if flow == 0:
                return res
            
            res += flow
        
        # s-tパスなしの場合
        return 0

def get_w_graph(edges: list, N: int) -> list:
    w_graph = [[] * i for i in range(N)]
    for e in edges:
        a, b, w = e
        a, b = a - 1, b - 1
        w_graph[a].append((b, w))
    return w_graph


def dijkstra(N: int, s: int, w_graph: list) -> list:
    used = [False] * N
    dist = [sys.maxsize] * N
    dist[s] = 0
    for i in range(N):
        # 使用済み出ないもののうちdistが最小を見つける
        min_dist = sys.maxsize
        min_v = -1

        for v in range(N):
            if not used[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_v = v

        # 頂点が見つからない場合終了する
        if min_v == -1:
            break

        # min_vを始点とした各辺を緩和
        for e in w_graph[min_v]:
            dist[e[0]] = min(dist[e[0]], dist[min_v] + e[1])
        
        # min_vを使用済みにする
        used[min_v] = True
    
    return dist

def solve(N: int, s: int, t: int, edges: list):
    s, t = s - 1, t - 1
    # グラフの作成
    tmp_edges = []
    for e in edges:
        tmp_edges.append(e[0:3]) # コストはこの時点では不要なので削る
    w_graph = get_w_graph(tmp_edges, N)

    # 各頂点間の最短距離を求める
    # ダイクストラでやっちゃったが、別の方法がいいはず
    dist = []
    for v in range(N):
        dist.append(dijkstra(N, v, w_graph))

    # s-t間を最短距離で行けうる辺のみで新たなグラフを作成
    # 重みは距離ではなくコストを使う
    min_edges = []
    for i, e in enumerate(edges):
        u, v = e[0] - 1, e[1] - 1
        d_uv = e[2]
        if dist[s][u] + d_uv + dist[v][t] == dist[s][t]:
            min_edge = e[0:2]
            # 次はコストを重みとする
            min_edge.append(e[3])
            min_edges.append(min_edge)
    
    min_graph = Graph(N)
    min_graph.make_graph(min_edges)
    ff = FordFulkerson()
    
    return ff.solve(min_graph, s, t)


if __name__ == '__main__':
    N = 3
    s = 1
    t = 3
    edges = [[1, 2, 1, 1],
             [2, 3, 1, 1],
             [1, 3, 1, 1]]
    print(solve(N, s, t, edges))

    N = 8
    s = 5
    t = 7
    edges = [
        [1, 5, 2, 3],
        [3, 8, 3, 6],
        [8, 7, 1, 3],
        [2, 7, 6, 4],
        [3, 7, 5, 5],
        [8, 3, 1, 3],
        [5, 6, 3, 5],
        [1, 7, 3, 2],
        [4, 3, 2, 4],
        [5, 4, 4, 3],
        [2, 3, 2, 2],
        [2, 8, 6, 5],
        [6, 2, 1, 3],
        [4, 2, 1, 6],
        [6, 1, 4, 2]
    ]
    print(solve(N, s, t, edges))
