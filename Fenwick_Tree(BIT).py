class Fenwick_Tree:
    def __init__(self, n: int, idx_comp = None | list[int], str_protocol = False) -> None:
        self.tree = [0]*n
        self.n = n
        self.str_protocol = str_protocol
        if idx_comp is not None:
            self._idx_hash(idx_comp)


    def _idx_hash(self,arr):
        self.idx = {}
        for i in range(self.n):
            v = arr[i]
            if self.str_protocol:
                v = str(v)
            self.idx[v] = i


    def sum(self,i: int) -> int:
        if hasattr(self,'idx'):
            if self.str_protocol:
                i = str(i)
            if i not in self.idx:
                raise IndexError
            i = self.idx[i]

        if i >= self.n or i < -1:
            raise IndexError
        out = 0
        while i >= 0:
            out += self.tree[i]
            i = (i&(i+1))-1
        return out

    def add(self,i: int , v: int) -> None:
        if hasattr(self,'idx'):
            if self.str_protocol:
                i = str(i)
            if i not in self.idx:
                raise IndexError
            i = self.idx[i]

        if i >= self.n or i < -1:
            raise IndexError
        
        while i < self.n:
            self.tree[i] += v
            i |= i + 1
        


if __name__ == '__main__':
    f = Fenwick_Tree(6,[7,4,3,2,1,-2],True)
    print(f.idx)
    print(f.sum(2))
    f.add(7,1)
    f.add(3,1)
    f.add(-2,1)
    print(f.sum(-2))
