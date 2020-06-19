"""
Place to pratice creating linked lists.


addAtIndex(int index, int value)
Adds a node with value value after the node at index index
If the index index is invalid do not perform any operation

deleteAtIndex(int index)
Deletes the node at index index
If the index index is invalid do not perform any operation

size()
Returns the total nodes in the linked list

isEmpty()
Returns true if the linked list is empty, false otherwise
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printList(self):
        if self.size == -1:
            print("The list is empty")
            return
        else:
            temp = self.head
            str1 = ""
            arr = []

            while temp != None:
                arr.append(str(temp.data) + "--->")
                temp = temp.next

        return ''.join(arr)

    def addToHead(self, value):

        if self.head == None and self.tail == None:
            self.head = self.tail = Node(value)
            self.size += 1
        else:
            current_node = Node(value)
            current_node.next = self.head
            self.tail = self.head
            self.head = current_node
            self.size += 1

    def addToTail(self, value):
        if self.head == None and self.tail == None:
            self.head = self.tail = Node(value)
            self.size += 1
        else:
            current_node = Node(value)
            self.tail.next = current_node
            self.tail = current_node
            self.size += 1

        return self.head

    def addAtIndex(self, index, value):

        if self.size == 0:
            self.addToHead(value)
            return

        if index > self.size:
            print("illegal")
            return

        counter = 0
        current_node = self.head

        while counter != index:
            current_node = current_node.next
            counter += 1

        if current_node.next == None:
            current_node.next = Node(value)
            self.size += 1
        else:
            temp = Node(value)
            temp.next = current_node.next
            current_node.next = temp
            self.size += 1

    def getSize(self):
        return "Empty" if self.size == 0 else self.size

    def isEmpty(self):
        return True if self.size == 0 else False

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            print("illegal")
            return

        current = self.head

        if index == 0:
            self.head = self.head.next

        else:
            counter = 0
            while counter != index - 1:
                current = current.next
                counter += 1
            current.next = current.next.next
        self.size -= 1


linkedList = LinkedList()
print(linkedList.printList())
print(linkedList.isEmpty())
linkedList.addToHead(3)
print(linkedList.printList())
print(linkedList.getSize())
linkedList.addToHead(2)
print(linkedList.isEmpty())
print(linkedList.printList())
print(linkedList.getSize())
linkedList.addToHead(1)
print(linkedList.printList())
print(linkedList.getSize())
linkedList.addAtIndex(0, 20)
print(linkedList.printList())
print(linkedList.getSize())
linkedList.addAtIndex(1, 30)
print(linkedList.printList())
print(linkedList.getSize())
linkedList.deleteAtIndex(2)
print(linkedList.printList())
print(linkedList.getSize())
