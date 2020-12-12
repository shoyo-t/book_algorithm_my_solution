'''
・互いに素ではないカード同士で辺をつくる
・あとは二部マッチング問題に当てはめれば終わり
・参考：
　https://www.cse.kyoto-su.ac.jp/~hiraishi/ICPC/ICPC2009/Domestic/ProblemE/ICPC2009_DomE.pdf
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
            self.add_edge(e[0], e[1], e[2])
    
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

# 二部マッチングを解く。マッチング数を返却する。
def solve_bipartile_graph(N: int, M: int, edges: list) -> int:
    s = 0
    t = N + M + 1

    # s,tを追加した新たなグラフを作成
    tmp_edges = []
    # sと左列を重み1で繋ぐ
    for i in range(N):
        tmp_edges.append([s, i + 1, 1])
    # 元のedgesから右列の頂点番号を変えて追加
    for left, right in edges:
        tmp_edges.append([left, N + right, 1])
    # 右列とtを重み1で繋ぐ
    for i in range(M):
        tmp_edges.append([N + i + 1, t, 1])
    
    bi_graph = Graph(t + 1)
    bi_graph.make_graph(tmp_edges)

    ff = FordFulkerson()
    return ff.solve(bi_graph, s, t)


# 互いに素でなければTrue
def gcd(x: int, y: int) -> bool:
    if x < y:
        x, y = y, x
    
    r = x % y
    while not r == 0:
        x, y = y, r
        r = x % y
    
    return y != 1
    

def solve(N: int, M: int, left: list, right: list) -> int:

    edges = []
    # 互いに素ではないもので辺をつくる
    for i, l in enumerate(left):
        for j, r in enumerate(right):
            if gcd(l, r):
                edges.append([i + 1, j + 1])
    
    return solve_bipartile_graph(N, M, edges)



if __name__ == '__main__':
    left = [2, 6, 6, 15]
    right = [2, 3, 35]
    N, M = len(left), len(right)
    print(solve(N, M, left, right))
