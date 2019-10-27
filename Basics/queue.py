class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class queue:
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail
        self.size = 0
    
    def empty(self):
        return self.head == None
    
    def peak (self):
        return self.head.val
    
    def enqueue(self,val):
        temp = Node(val)
        if self.tail != None:
            self.tail.next = temp
        self.tail = temp
        if (self.head == None):
            self.head == temp
    
    def dequeue(self):
        tmp = self.head.val
        self.head = self.head.next
        if(self.head == None):
            self.tail == None
        return tmp