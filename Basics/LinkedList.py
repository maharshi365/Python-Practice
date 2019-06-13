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

    def insert(self, value):
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
        while(curr.next != None):
            curr = curr.next
            print(curr.value)

    def valueAt(self, index):
        curr = self.head.next
        i = 0
        while (i < index):
            curr = curr.next
            i += 1
        return curr.value


l = LinkedList()
print(f'The string is: {l.empty()} --> True')

for i in range(5):
    l.insert(i)
print(f'The String is of Size: {l.size()} --> 5')

print("The List Contains 0 1 2 3 4")
l.printList()

l.pushFront(5)
print("The List Contains 5 0 1 2 3 4")
l.printList()

print(f'The Value at index 0: {l.valueAt(0)} --> 5')
print(f'The Value at index 0: {l.valueAt(3)} --> 2')

print(f'After Popping: {l.popFront()} --> 5')
print("The List Contains 0 1 2 3 4")
l.printList()
