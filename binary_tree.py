def height(A):
    if A: return A.height
    return -1
def size(A):
    if A: return A.size
    return 0

class bin_node:
    def __init__(self,x):
        self.item = x
        self.parent = None
        self.left = None
        self.right = None
        self.subtree_update()

    def subtree_iter(A):
        """from ??"""
        if A.left : yield from A.left.subtree_iter()
        yield A
        if A.right : yield from A.right.subtree_iter()

    def subtree_first(A):
        if A.left : A.left.subtree_first()
        else : return A

    def subtree_last(A):
        if A.right : A.right.subtree_last()
        else : return A

    def successor(A):
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent
    
    def predecessor(A):
        if A.left: return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent
    
    def subtree_insert_before(A,B):
        if A.left:
            A = A.left.subtree_last()
            A.right , B.parent = B , A
        else:
            A.left , B.parent = B , A

    def subtree_insert_after(A,B):
        if A.right:
            A = A.right.subtree_first()
            A.left , B.parent = B , A
        else:
            A.right , B.parent = B , A

    def subtree_delete(A):
        if A.left or A.right:
            if A.left: B = A.predecessor()
            else:      B = A.successor()
            A.item , B.item = B.item , A.item
            return B.subtree_delete()
        if A.parent:
            if A is A.parent.left : A.parent.left = None
            else:                   A.parent.right = None
        return A
    
class rotations():
    def rotate_right(D):
        assert D.left
        B, E = D.left, D.right
        A, C = B.left, B.right
        D, B = B, D
        D.item, B.item = B.item, D.item
        B.left, B.right = A, D
        D.left, D.right = C, E
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

        # My code 
        # PROBLEM: when A is root then cannot make X root because we need T
        # if not A or not A.left:
        #     return False
        # X = A.left
        
        # if not A.parent:
        #     X.parent = None
        #     T.root = X
        # elif A.parent.right is A:
        #     A.parent.right , X.parent = X , A.parent
        # elif A.parent.left is A:
        #     A.parent.left , X.parent = X , A.parent

        # if X.right:
        #     A.left , X.right.parent = X.right , A 
        # else:
        #     A.left = None

        # X.right , A.parent = A , X
        
    def rotate_left(B):
        assert B.right
        A, D = B.left, B.right
        C, E = D.left, D.right
        B, D = D, B
        B.item, D.item = D.item, B.item
        D.left, D.right = B, E
        B.left, B.right = A, C
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

class rebalance():
    def subtree_update(A):
        A.height = 1 + max(height(A.right) , height(A.left))

    def skew(A):
        return A.right.height() - A.left.height()
    
    def rebalance(A):
        if A.skew == 2:
            if A.right.skew() < 0:
                A.right.rotate_right()
            A.rotate_left()
        elif A.skew == -2:
            if A.left.skew() > 0:
                A.left.rotate_left()
            A.rotate_right()

    def maintain(A): # O(log n)
        A.rebalance()
        A.subtree_update()
        if A.parent:
            A.parent.maintain()

class bin_tree:
    def __init__(self,node_type = bin_node):
        self.root = None
        self.size = 0
        self.node_type = node_type

    def __len__(self):
        return  self.size
    
    def __iter__(self):
        if self.root:
            for A in self.root.subtree_iter():
                yield A.item


class BST(bin_node, rotations , rebalance):
    def subtree_find(A,k):
        if k < A.item.key:
            if A.left: return A.left.subtree_find(k)
        elif k > A.item.key:
            if A.right: return A.right.subtree_find(k)
        else:
            return A
        return None
    
    def subtree_find_next(A,k):
        if A.item.key  <= k:
            if A.right: return A.right.subtree_find_next(k)
            else:       return None
        elif A.left:
            B = A.left.subtree_find_next(k)
            if B:       return B
        return A
    
    def subtree_find_prev(A,k):
        if A.item.key  >= k:
            if A.left: return A.left.subtree_find_prev(k)
            else:       return None
        elif A.right:
            B = A.right.subtree_find_prev(k)
            if B:       return B
        return A
    
    def subtree_insert(A,B):
        if B.item.key < A.item.key:
            if A.left: A.left.subtree_insert(B)
            else:      A.subtree_insert_before(B)
        elif B.item.key > A.item.key:
            if A.right: A.right.subtree_insert(B)
            else:      A.subtree_insert_after(B)

class Set_Binary_Tree(bin_tree): # Binary Search Tree
    def __init__(self):
        super().__init__(BST)

    def iter_order(self):
        yield from self

    def build(self, X):
        for x in X:
            self.insert(x)

    def find_min(self):
        if self.root: return self.root.subtree_first().item

    def find_max(self):
        if self.root: return self.root.subtree_last().item

    def find(self, k):
        if self.root:
            node = self.root.subtree_find(k)
            if node: return node.item

    def find_next(self, k):
        if self.root:
            node = self.root.subtree_find_next(k)
            if node: return node.item

    def find_prev(self, k):
        if self.root:
            node = self.root.subtree_find_prev(k)
            if node: return node.item

    def insert(self, x):
        new_node = self.node_type(x)
        if self.root:
            self.root.subtree_insert(new_node)
            if new_node.parent is None: return False # when the key is dA.parentlicate
        else:
            self.root = new_node # insert in an empty BST
        self.size += 1
        return True
    
    def delete(self, k):
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_delete()
        if ext.parent is None: self.root = None # when the only key in BST(root) is deleted
        self.size -= 1
        return ext.item

class size_node(bin_node , rotations , rebalance):
    def subtree_update(A):
        super().subtree_update()
        A.size = 1
        if A.right: A.size += A.right.size
        if A.left: A.size += A.left.size

    def subtree_at(A, i): 
        assert A
        if size(A.left) > i:
            A.left.subtree_at(i)
        elif size(A.left) < i:
            A.right.subtree_at(i -A.left.size -1)
        elif size(A.left) == i:
            return A
        

class seq_binary_tree(bin_tree):
    def __init__(self):
        super().__init__(size_node)

    def build(self,X):
        A = X.copy()
        def build_subtree(A,i,j):
            c = (i+j)//2
            root = self.node_type(A[c])
            if i < c:
                root.left = build_subtree(A,i,c-1)
                root.left.parent = root #making root the parent of left subtree 
            if c < j:
                root.right = build_subtree(A,c+1,j)
                root.right.parent = root
            return root
        self.root = build_subtree(A,0,len(A)-1)
        self.size = self.root.size

    def get_at(self, i):
        assert self.root
        return self.root.subtree_at(i).item
    
    def set_at(self, i, x):
        assert self.root
        self.root.subtree_at(i).item = x

    def insert_at(self, i, x):
        new_node = self.Node_Type(x)
        if i == 0:
            if self.root:
                node = self.root.subtree_first()
                node.subtree_insert_before(new_node)
            else:
                self.root = new_node
        else:
            node = self.root.subtree_at(i - 1)
            node.subtree_insert_after(new_node)
        self.size += 1

    def delete_at(self, i):
        assert self.root
        node = self.root.subtree_at(i)
        ext = node.subtree_delete()
        if ext.parent is None: self.root = None
        self.size -= 1
        return ext.item
    
    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self): return self.delete_at(0)
    def insert_last(self, x): self.insert_at(len(self), x)
    def delete_last(self): return self.delete_at(len(self) - 1)

class obj:
    def __init__(self,key):
        self.key = key
        self.value = None

from random import randint
def main():
    # ky = [ obj(x) for x in set([randint(0,100) for _ in range(15)])]
    # print([x.key for x in ky])
    T = seq_binary_tree()
    T.build([10,6,8,5,1,3])
    print([x for x in T])
    T.get_at(4)
    T.set_at(4, -4)
    T.insert_at(4, 18)
    T.insert_at(4, 12)
    T.delete_at(2)
    print([x for x in T])

if __name__ == "__main__":
    main()