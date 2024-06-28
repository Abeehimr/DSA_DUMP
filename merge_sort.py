from random import shuffle
def main():
    shuffle(l:=[1,2,3,4,5,6,7,8,9,10,11])
    print(l)
    ans = merge_sort(l)
    print (ans)


def merge_sort(l):
    if len(l) == 1:
        return l  
    x = len(l)//2
    a = merge_sort(l[:x])
    b = merge_sort(l[x:])
    return merge(a,b)
    
def merge(a,b):
    i = 0
    j = 0
    o = []
    while len(o) != len(a) + len(b):
        if a[i] <= b[j]:
            o.append(a[i])
            i+=1
            if i == len(a):
                o += b[j:]    
        else:
            o.append(b[j])
            j+=1
            if j == len(b):
                o+= a[i:]
    return o

def merge_sort(self,a=0,b=None):
    if b is None: b = len(self.l)
    if 1 < b-a:
        c = (a+b+1)//2
        self.merge_sort(a,c)
        self.merge_sort(c,b)
        x , y = self.l[a:c] , self.l[c:b]
        self.merge(x,y,len(x),len(y),a,b)
def merge(self,L,R,i,j,a,b):
    if a < b:
        if (j <= 0) or (i > 0 and L[i-1]+R[j-1] > R[j-1]+L[i-1]):
            self.l[b-1] = L[i-1]
            i -= 1
        else:
            self.l[b-1] = R[j-1]
            j -= 1
        self.merge(L,R,i,j,a,b-1)

main()