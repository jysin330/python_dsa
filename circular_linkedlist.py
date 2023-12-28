class Node:
    def __init__(self, data):
        self.data = data
        self.next = None




class CircularLinkedList:
    def __init__(self):
        self.head = None



    def push(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        new_node.next = self.head

        if (self.head is not None):
            while (temp.next != self.head):
                temp = temp.next

            temp.next = new_node
        else:
            new_node.next = new_node

        self.head = new_node

    def delete(self, deleteval):
        current_node = self.head
        prev = None

        while current_node:

            if current_node.data == deleteval and current_node == self.head:
                # case1
                # head is the only element in the c list
                if current_node.next == self.head:
                    current_node = None
                    self.head = None
                    return
                # case2
                # there are more element in the c list
                else:
                    # traverse and update head: delete head
                    while (current_node.next != self.head):
                        current_node = current_node.next
                    current_node.next = self.head.next
                    self.head = self.head.next
                    current_node = None
                    return

            elif current_node.data == deleteval:
                prev.next = current_node.next
                current_node = None
                return
            else:

                if current_node.next == self.head:
                    return

            prev = current_node
            current_node = current_node.next

    def countnode(self):
        current = self.head
        self.count = self.count+1
        while (current.next != self.head):
            self.count = self.count+1
            current = current.next

        print(self.count)

    def toCircular(self, head):
        start = head
        while (head.next is not None):
            head = head.next

        head.next = start
        return start

    def printlist(self):
        temp = self.head
        if (self.head is not None):
            while (True):
                print(temp.data)
                temp = temp.next
                if (temp == self.head):
                    break


mycllist = CircularLinkedList()
mycllist.push(5)
mycllist.push(3)
mycllist.push(8)
mycllist.push(2)
mycllist.printlist()
mycllist.delete(2)
mycllist.printlist()
