class node:
    def __init__(self,k, val,freq = 1, prev=None, nx = None):
        self.k = k
        self.val = val
        self.freq = freq
        self.prev = prev
        self.next = nx
    
class list:
    def __init__(self):
        self.head = None
        self.tail = None

    def mt(self):
        return self.head is None and self.tail is None

    def __str__(self):
        p = self.head
        while p:
            print(p.val , end=",")
            p = p.next
        print("<==>" , end = "")
        p = self.tail
        while p:
            print(p.val , end=",")
            p = p.prev
        return ''

    def pop(self):
        k = self.tail.k
        if self.head == self.tail: 
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return k
    
    def remove(self, nod):
        if nod == self.head:
            if nod == self.tail: self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            l , r = nod.prev , nod.next
            l.next = r
            if r is not None:
                r.prev = l
            else:
                self.tail = l
        nod.next = nod.prev = None
          
    def add(self ,nod, k , v):
        if not nod:nod = node(k,v,1,None , self.head)
        if self.head:
            self.head.prev = nod
            nod.next = self.head
        else:
            self.tail = nod
        self.head = nod
        return nod