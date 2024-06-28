class UnionFind():
    def __init__(self,lenght) -> None:
        self.parent = [i for i in range(lenght)]
        self.rank = [0]*lenght
        self.size = [1]*lenght

    def find_normal(self,x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
    
    #path comprehension
    def find_path_I(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find_path_I(self.parent[x])
            return self.parent[x]
        else:
            return x
        
    def find_path_II(self,x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]

        while self.parent[x] != x:
            par = self.parent[x]
            self.parent[x] = root
            x = par
        return root
    
    #path splitting
    def find_split(self,x):
        while self.parent[x] != x:
            x,self.parent[x] = self.parent[x] , self.parent[self.parent[x]]
        return x
    
    #path halving
    def find_halv(self,x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    #union
    def union_normal(self,x,y):
        xpar , ypar = self.find_path_I(x) , self.find_path_I(y)
        self.parent[ypar] = xpar

    def union_rank(self,x,y):
        xpar , ypar = self.find_path_I(x) , self.find_path_I(y)
        if self.rank[xpar] > self.rank[ypar]:
            self.parent[ypar] = xpar
        elif self.rank[xpar] < self.rank[ypar]:
            self.parent[xpar] = ypar 
        else:
            self.parent[ypar] = xpar
            self.rank[xpar] += 1

    def union_size(self,x,y):
        xpar , ypar = self.find_path_I(x) , self.find_path_I(y)
        if self.size[xpar] > self.size[ypar]:
            self.parent[ypar] = xpar
            self.size[xpar] += self.size[ypar]
        elif self.size[xpar] < self.size[ypar]:
            self.parent[xpar] = ypar 
            self.size[ypar] += self.size[xpar]
        else:
            self.parent[ypar] = xpar
            self.size[xpar] += self.size[ypar]
