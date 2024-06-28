class node():
    def __init__(self,val):
        self.val=val
        self.next=None

class linkedList():
    def __init__(self,arr):
        head = node(arr[0])
        self.head = head
        prev = head
        self.len=len(arr)
        for ele in arr[1:]:
            current_node = node(ele)
            prev.next = current_node
            prev = current_node
    
    def goto(self,index):
        if index + 1 > self.len:
            raise IndexError
        element = self.head
        for _ in range(index):
            element = element.next
        return element
    
    def get_at(self,index):
        element = self.goto(index)
        return element.val   
           
    def set_at(self,index,value):
        element = self.goto(index)
        element.val = value 
        
    def insert_first(self,value):
        new = node(value)
        new.next = self.head
        self.head = new
        self.len+=1
     
    def delete_first(self):
        self.head = self.head.next
        self.len-=1
        
    def insert_last(self,value):
        element = self.goto(self.len - 1)
        element.next = node(value)
        self.len += 1   
    
    def delete_last(self):
        element = self.goto(self.len - 2)
        element.next = None
        self.len -= 1 
        
    def insert_at(self, index, value):
        if index == 0:
            self.inssert_first(value)
        else:
            element = self.goto(index - 1)
            new = node(value)
            new.next = element.next
            element.next = new
            self.len += 1   
    
    def delete_at(self,index):
        if index == 0:
            self.delete_first()
        else:
            element = self.goto(index - 1)
            element.next = element.next.next
            self.len -= 1