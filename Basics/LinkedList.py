class Node:
    def __init__(self,value=None):
        self.val = value
        self.next = None

class linked_list:
    def __init__(self):
        self.head = Node()
    
    def size(self):
        size = 0
        curr = self.head
        while curr.next != None:
            size += 1
            curr = curr.next

