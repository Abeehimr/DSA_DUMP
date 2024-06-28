from random import randint

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i - 1 )//2

class Binary_Heap():
    def __init__(self):
        self.Q = []

    def __len__(self):
        return len(self.Q)

    def __iter__(self):
        yield from self.Q
            
    def find_max(self):
        return self.Q[0]
    
    def slow_build(self , A):
        for x in A:
            self.Q.append(x)

    def build(self, A):
        if len(self) > 0:
            return False
        self.Q = A.copy()
        for i in range(len(self) - 1 , -1 , -1):
            self.max_heapify_down(i)


    def max_heapify_up(self, i):
        if parent(i) >= 0 and self.Q[parent(i)].key < self.Q[i].key:
            self.Q[parent(i)] ,  self.Q[i] = self.Q[i], self.Q[parent(i)]
            self.max_heapify_up(parent(i))

    def insert(self, x):
        self.Q.append(x)
        self.max_heapify_up(len(self) - 1)

    def max_heapify_down(self , i):
        if (left(i) < len(self) and self.Q[i].key < self.Q[left(i)].key) or (right(i) < len(self) and self.Q[i].key < self.Q[right(i)].key):

            if left(i) < len(self)  and (right(i) >= len(self) or (right(i) < len(self) and self.Q[right(i)].key < self.Q[left(i)].key)):
                self.Q[i] ,  self.Q[left(i)] = self.Q[left(i)], self.Q[i]
                self.max_heapify_down(left(i)) 
            else:
                self.Q[i] ,  self.Q[right(i)] = self.Q[right(i)], self.Q[i]
                self.max_heapify_down(right(i))

    def delete_max(self):
        self.Q[0] ,  self.Q[len(self) -1] = self.Q[len(self) - 1], self.Q[0]
        self.Q.pop()
        self.max_heapify_down(0)

def Heap_Sort(A):
    pass

class obj:
    def __init__(self , key , item = None):
        self.key = key
        self.item = item



if __name__ == "__main__":
    ky = [ obj(x) for x in set([randint(0,100) for _ in range(15)])]
    print([x.key for x in ky])

    Q = Binary_Heap()
    QQ = Binary_Heap()

    Q.build(ky)
    QQ.slow_build(ky)
    
    print([x.key for x in Q])
    print([x.key for x in QQ])