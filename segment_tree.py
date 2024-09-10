class SegmentTree:
    def __init__(self, n: int, idx_comp = None , str_protocol = False) -> None:
        self.tree = [float('inf')]*(2*n)
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

    def _get_index(self,i: int) -> int:
        if hasattr(self,'idx'):
            if self.str_protocol:
                i = str(i)
            if i not in self.idx:
                raise IndexError
            i = self.idx[i]

        if i >= self.n or i < -1:
            raise IndexError
        return i

    def sum(self,l: int , r: int) -> int:
        l = self._get_index(l) + self.n
        r = self._get_index(r) + self.n

        mn = float('inf')
        while l <= r:
            if l&1 == 1:
                mn = min(mn , self.tree[l])
                l += 1
            if r&1 == 0:
                mn = min(mn , self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return mn



    def add(self,i: int , v: int) -> None:
        i = self._get_index(i) + self.n
        self.tree[i] = v
        i >>= 1
        while i >= 1:
            self.tree[i] = min(self.tree[2*i] , self.tree[2*i + 1])
            i >>= 1
        


if __name__ == '__main__':
    s = SegmentTree(5)
    for i in range(5):
        s.add(i,i+1)
    print(s.sum(2,4))