class UnionFind():

    def __init__(self, n: int) -> None:
        self.n = n
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x: int) -> int:
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    
    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False
        
        if self.siz[x] < self.siz[y]:
            x, y = y, x
        
        # yをxの子にする
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True
    
    def size(self, x: int) -> int:
        return self.siz[self.root(x)]


from collections import defaultdict

def main(N: int, k_edges: list, l_edges: list) -> list:
    K = len(k_edges)
    L = len(l_edges)

    uf_road = UnionFind(N)
    uf_train = UnionFind(N)

    for e in k_edges:
        a, b = e
        uf_road.unite(a, b)
    
    for e in l_edges:
        a, b = e
        uf_train.unite(a, b)
    
    d = defaultdict(int)
    for i in range(N):
        #print(uf_road.root(i), uf_train.root(i))
        d[(uf_road.root(i), uf_train.root(i))] += 1
    
    ans = []
    for i in range(N):
        # 同じ親とつながっている都市とは、必然的につながっている事になる
        ans.append(d[(uf_road.root(i), uf_train.root(i))])
    return ans
    

if __name__ == '__main__':
    # 問題サイト入力例1
    N = 4
    k_edges = [(0, 1),(1, 2),(2, 3)]
    l_edges = [(1, 2)]
    print(main(N, k_edges, l_edges))

    # 問題サイト入力例2
    N = 4
    k_edges = [(0, 1),(1, 2)]
    l_edges = [(0, 3),(1, 2)]
    print(main(N, k_edges, l_edges))

    # 問題サイト入力例3
    N = 7
    k_edges = [(0, 1),(1, 2),(1, 4),(5, 6)]
    l_edges = [(2, 4),(3, 4),(2, 3),(5, 6)]
    print(main(N, k_edges, l_edges))
