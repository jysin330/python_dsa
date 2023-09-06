class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class circularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        temp = self.head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        else:
            new_node.next = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node
            return

    def print(self):
        temp = self.head

        while (True):
            print(temp.data)
            temp = temp.next
            if (temp == self.head):
                break


llist = circularLinkedList()
llist.push(4)
llist.push(5)
llist.push(6)
llist.push(7)

llist.print()
