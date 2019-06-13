class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


# Implemented so that the head node is does not contain data
class LinkedList:
    def __init__(self):
        self.head = Node()

    def empty(self):
        return self.head.next == None

    def push(self, value):
        newNode = Node(value)
        curr = self.head
        while(curr.next != None):
            curr = curr.next
        curr.next = newNode

    def size(self):
        length = 0
        curr = self.head
        while(curr.next != None):
            length += 1
            curr = curr.next
        return length

    def pushFront(self, value):
        newNode = Node(value)
        newNode.next = self.head.next
        self.head.next = newNode

    def popFront(self):
        value, self.head.next = self.head.next.value, self.head.next.next
        return value

    def printList(self):
        curr = self.head
        toPrint = []
        while(curr.next != None):
            curr = curr.next
            toPrint.append(curr.value)
        print(toPrint)

    def valueAt(self, index):
        curr = self.head.next
        i = 0
        while (i < index):
            curr = curr.next
            i += 1
        return curr.value
    def popBack(self):
        curr = self.head.next
        while(curr.next.next!= None):
            curr = curr.next
        val = curr.next.value
        curr.next=None
        return val

    def front(self):
        val = self.head.next.value
        return val
    
    def back(self):
        curr = self.head.next
        while(curr.next != None):
            curr = curr.next
        return curr.value
    
    def reverse(self):
        curr = self.head
        tempList = LinkedList()
        while(curr.next != None):
            curr = curr.next
            tempList.pushFront(curr.value)

        self.head = tempList.head
    
    def insert(self,value,index):
        curr = self.head
        i = 0
        node = Node(value)
        while(i < index):
            curr = curr.next
            i += 1
        node.next = curr.next
        curr.next = node

    def erase(self,index):
        curr = self.head
        i = 0
        while(i < index):
            curr = curr.next
            i += 1
        curr.next = curr.next.next
    
    def removeValue(self,value):
        curr = self.head
        while(curr.next.value != value):
            curr = curr.next
        curr.next = curr.next.next

    def value_n_from_end(self,n):
        index = self.size() - n
        i = 0
        curr = self.head
        while(i<index):
            curr = curr.next
            i += 1
        return curr.next.value



l = LinkedList()
print(f'The list is empty: {l.empty()} --> True')

for i in range(5):
    l.push(i)
print(f'The list is of Size: {l.size()} --> 5')

print("The List Contains 0 1 2 3 4")
l.printList()

l.pushFront(5)
print("The List Contains 5 0 1 2 3 4")
l.printList()

print(f'The Value at index 0: {l.valueAt(0)} --> 5')
print(f'The Value at index 0: {l.valueAt(3)} --> 2')

print(f'After Popping Front: {l.popFront()} --> 5')
print("The List Contains 0 1 2 3 4")
l.printList()

print(f'After Popping Back: {l.popBack()} --> 4')
print("The List Contains 0 1 2 3")
l.printList()

print(f'Value at Front: {l.front()} --> 0')
print(f'Value at Back: {l.back()} --> 3')

l.reverse()
print("The List Contains 3 2 1 0")
l.printList()

l.reverse()
print("The List Contains 0 1 2 3")
l.printList()

l.insert(6,2)
l.insert(5,3)
print("The List Contains 0 1 6 5 2 3")
l.printList()

l.erase(2)
print("The List Contains 0 1 5 2 3")
l.printList()

l.removeValue(5)
print("The List Contains 0 1 2 3")
l.printList()

print(f'Third Value from End: {l.value_n_from_end(3)} --> 1')