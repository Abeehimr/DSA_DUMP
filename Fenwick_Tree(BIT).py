class Fenwick_Tree:
    def __init__(self, n , idx_comp = None, string_cnv =False) -> None:
        self.tree = [0]*n
        self.n = n
        if idx_comp is not None:
            self._idx_hash(idx_comp,string_cnv)


    def _idx_hash(self,arr, string_cnv):
        self.idx = {}
        for i in range(self.n):
            v = arr[i]
            if string_cnv:
                v = str(v)
            self.idx[v] = i


    def sum(self,idx: int) -> int:
        if idx >= self.n or idx < -1:
            raise IndexError
        out = 0
        while idx >= 0:
            out += self.tree[idx]
            idx = (idx&(idx+1))-1
        return out

    def add(self,idx: int , v: int) -> None:
        if idx >= self.n or idx < -1:
            raise IndexError
        while idx < self.n:
            self.tree[idx] += v
            idx |= idx + 1
        

