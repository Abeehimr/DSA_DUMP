from random import randint
from timeit import default_timer as t
class item:
    def __init__(self,key):
        self.key = key
        self.value = None

def main():
    #ky = [randint(0,9) for _ in range(10)]
    ky = [125,100,99,100,110,111,123,118,114,115]
    A = [item(key) for key in ky]
    B = A.copy()

    start1= t()
    radix_sort_mit(B)
    end1 = t()
    print("MIT",end1 - start1 , "sec")
    start2 = t()
    radix_sort(A)
    end2 = t()

    print("VS")
    print("IBHRAHEEM",end2 - start2 ,"sec")
    print("\n##################\n")
    print("ibraheem\t\tMIT")
    for i in range(len(ky)):
        print(A[i].key,"\t\t",B[i].key)


def radix_sort_mit(A):
    "Sort A assuming items have non-negative keys"
    n = len(A)
    u = 1 + max([x.key for x in A])             # O(n) find maximum key
    c = 1 + (u.bit_length() // n.bit_length())
    
    class Obj: pass
    D = [Obj() for a in A]
    for i in range(n):                          # O(nc) make digit tuples
        D[i].digits = []
        D[i].item = A[i]
        high = A[i].key
        for j in range(c):                      # O(c) make digit tuple
            high, low = divmod(high, n)
            D[i].digits.append(low)
    
    for i in range(c):                          # O(nc) sort each digit
        for j in range(n):                      # O(n) assign key i to tuples
            D[j].key = D[j].digits[i]
        counting_sort_mit(D)                        # O(n) sort on digit i
    for i in range(n):                          # O(n) output to A
        A[i] = D[i].item

def counting_sort_mit(A):
    u = max([itm.key for itm in A])
    D = [[] for _ in range(u+1)]
    for x in A:
        D[x.key].append(x)
    i = 0
    for chain in D:
        for x in chain:
            A[i] = x
            i+=1

def radix_sort(A):
    n = len(A)
    u = max([itm.key for itm in A])
    c = len(base_converter1(u,n))

    for itm in A:
        itm.key = base_converter1(itm.key,n,c)

    for i in range(c):
        counting_sort(A,i)
    
    for itm in A:
        itm.key = base_returner(itm.key,c,n)

def counting_sort(A,index):
    u = max([itm.key[index] for itm in A])
    D = [[] for _ in range(u+1)]
    for x in A:
        D[x.key[index]].append(x)
    i = 0
    for chain in D:
        for x in chain:
            A[i] = x
            i+=1
    
def base_converter1(number, base , length = 0):
    temp = []
    while number > 0:
        number,digit = divmod(number,base)
        temp.append(digit)
    if len(temp) < length:
        for _ in range(length - len(temp)):
            temp.append(0)
    return tuple(temp)

def base_converter2(number, base , length):
    temp = []
    for _ in range(length):
        number,digit = divmod(number,base)
        temp.append(digit)
    return temp

def base_returner(toopel,length,base):
    num = 0
    for i in range(length - 1,0,-1):
        num += toopel[i]
        num *= base
    num += toopel[0]
    return num

def test():
    ky = [randint(1000000,9999999) for _ in range(1000000)]
    n = 1000000
    start = t()
    for u in ky:
        c = base_converter1(u,2,10)
    end = t()
    print("ibraheem",end-start,"sec")
    print("VS")
    start = t()
    for u in ky:
        c = base_converter2(u,2,10)
    end = t()
    print("MIT",end-start,"sec")

if __name__ == "__main__":
    main()