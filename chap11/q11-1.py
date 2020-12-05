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


def main(N: int, edges: list) -> int:
    M = len(edges)

    cnt = 0
    for i in range(M):
        uf = UnionFind(N)
        for j, e in enumerate(edges):
            if j == i:
                continue
            uf.unite(e[0], e[1])
        x, y = edges[i]
        if not uf.is_same(x, y):
            cnt += 1
    
    return cnt


if __name__ == '__main__':
    # p164のグラフ 答え0
    N = 8
    edges = [(4, 1),(4, 2),(4, 6),(1, 3),(1, 6),
             (2, 5),(2, 7),(6, 7),(3, 0),(7, 0),
             (0, 5)]
    print(main(N, edges))

    # 答えが2となるグラフ
    N = 8
    edges = [(1, 0),(1, 2),(0, 3),(2, 3),(2, 7),
             (3, 4),(4, 5),(4, 6),(5, 6)]
    print(main(N, edges))