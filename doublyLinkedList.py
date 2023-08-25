class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class doublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("prev node cannot be none")

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def addAtLast(self, new_value):
        new_node = Node(new_value)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        else:
            last = self.head
            while (last.next is not None):
                last = last.next

            last.next = new_node
            new_node.prev = last
            return

    def print(self, node):
        while (node is not None):
            print(node.data, end=" ")
            node = node.next


llist = doublyLinkedList()
llist.push(7)
llist.push(9)
llist.insertAfter(llist.head, 40)
llist.insertAfter(llist.head.next, 60)
llist.addAtLast(20)
llist.addAtLast(80)
llist.print(llist.head)
