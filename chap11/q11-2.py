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


def main(N: int, edges: list) -> list:
    M = len(edges)

    ans = [0] * M
    # 初期値の設定 ans[M-1]はN個の島から2個を選択する組み合わせ
    ans[-1] = N * (N-1) // 2
    uf = UnionFind(N)

    for i in range(M-1, 0, -1):
        ans[i-1] = ans[i]
        a = edges[i][0]
        b = edges[i][1]

        # 頂点a,bが連結していない場合は、それぞれの連結個数の掛け合わせ分減らす
        if not uf.is_same(a, b):
            ans[i-1] -= uf.size(a) * uf.size(b)
            uf.unite(a, b)
    
    return ans
    

if __name__ == '__main__':
    # 問題サイト入力例1
    N = 4
    edges = [(0, 1),(2, 3),(0, 2),(1, 2),(0, 3)]
    print(main(N, edges))

    # 問題サイト入力例2
    N = 6
    edges = [(1, 2),(0, 1),(4, 5),(2, 3),(3, 4)]
    print(main(N, edges))

    # 問題サイト入力例3
    N = 2
    edges = [(0, 1)]
    print(main(N, edges))