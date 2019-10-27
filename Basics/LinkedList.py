class Node:
    def __init__(self,value,next=None):
        self.val = value
        self.next = next

class linked_list:
    def __init__(self,head=None):
        self.head = head
    
    def __str__(self):
        if not self.empty():
            l = list()
            curr = self.head
            while curr:
                l.append(str(curr.val))
                curr = curr.next
            return ",".join(l)
        else:
            return "The list is empty"

    def empty(self):
        if self.head == None:
            return True
        return False

    def size(self):
        size = 0
        curr = self.head
        while curr:
            curr = curr.next
            size += 1
        return size
    
    def front(self):
        return self.head.val

    def push_front(self,value):
        if self.head == None:
            self.head = Node(value)
        else:
            tmp = Node(value)
            tmp.next = self.head
            self.head = tmp
    
    def pop_front(self):
        val = self.head.val
        self.head = self.head.next
        return val

ll = linked_list()
print(ll)
ll.push_front(3)
ll.push_front(2)
ll.push_front(1)

