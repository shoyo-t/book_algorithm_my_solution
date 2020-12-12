'''
・p_1,...,p_G の先に頂点Nを作成
・頂点0-N間の最小カットを求めることと同義
・code_16_1.pyをほぼほぼ流用
・参考解説サイト
　https://www.slideshare.net/chokudai/abc010-35598499
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

def main():
    
    # p_1,...,p_G の先に頂点Nを作成
    for p in p_list:
        edges.append([p, N])
    # edgeの容量はオール1
    for e in edges:
        e.append(1)
    
    graph = Graph(N+1)
    graph.make_graph(edges)

    ff = FordFulkerson()
    return ff.solve(graph, 0, N)

if __name__ == '__main__':
    # 入力例1 答え1
    N = 4
    p_list = [2, 3]
    edges = [[0,1],[1,2],[1,3]]
    print(main())

    # 入力例2 答え1
    N = 4
    p_list = [3]
    edges = [[0,1],[0,2],[1,3],[2,3]]
    print(main())

    # 入力例3 答え2
    N = 10
    p_list = [7,8,9]
    edges = [[0,1],[0,2],[0,3],[0,4],[1,5],
             [2,5],[5,6],[6,7],[6,8],[3,9],
             [4,9]]
    print(main())

    # 入力例4 答え2
    N = 6
    p_list = [4,5]
    edges = [[0,1],[0,2],[1,3],[2,3],[3,4],
             [3,5]]
    print(main())

    # 入力例5 答え0
    N = 4
    p_list = [1,2,3]
    edges = [[1,2],[1,3],[2,3]]
    print(main())