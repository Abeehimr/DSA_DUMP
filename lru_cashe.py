class node:
    def __init__(self,k, val,prev=None, nx = None):
        self.k = k
        self.val = val
        self.prev = prev
        self.next = nx
class ll:
    def __init__(self):
        self.head = None
        self.tail = None

    def rmv(self):
        k = self.tail.k
        self.tail = self.tail.prev
        self.tail.next = None
        return k

    def btf(self, nod):
        l , r = nod.prev , nod.left
        l.next = r
        r.prev = l
        nod.prev = None
        nod.next = self.next
        self.head = nod

    def chval(self, nod, v):
        nod.val = v
        self.btf(nod)

    def add(self , k , v):
        nod = node(k,v,None , self.head)
        self.head = nod
        return nod

class LRUCache:
    def __init__(self, capacity: int):
        self.h = {}
        self.l = ll()
        
    def get(self, key: int) -> int:
        if key not in self.h: return -1
        else:
            self.l.btf(self.h[key])
            return self.h[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            self.l.chval(self.h[key] , value)
        else:
            h[key] = self.l.add(key,value)
            if len(h) > capacity:
                h.pop(self.l.rmv())


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
