class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node

        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def findNode(self, data):
        temp = self.head

        while (temp):
            if temp.data == data:
                break
            temp = temp.next

        return temp

    def insertAt(self, prev_val, new_val):

        prev = self.findNode(prev_val)

        new_node = Node(new_val)
        if prev is not None:
            prev.next.prev = new_node
            new_node.next = prev.next
            prev.next = new_node
            new_node.prev = prev

        else:
            print("no doubly linked list found")
            return

    def delete(self, val):

        findnode = self.findNode(val)

        if findnode.prev == None:
            self.head = findnode.next
            findnode.next.prev = None
        elif findnode.next == None:
            findnode.prev.next = None
        else:
            findnode.prev.next = findnode.next
            findnode.next.prev = findnode.prev

        findnode = None

    def printdl(self):
        temp = self.head

        while temp:
            print(temp.data)
            if temp.next == None:
                break
            temp = temp.next


dllist = DoublyLinkedList()

dllist.push(3)
dllist.push(4)
dllist.push(5)
dllist.push(6)
# dllist.printdl()
dllist.insertAt(4, 8)
dllist.delete(3)
dllist.printdl()
