class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAt(self, pre_node, new_data):
        if pre_node is None:
            print("pre_node seems to be empty")
            return

        new_node = Node(new_data)
        new_node.next = pre_node.next
        pre_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def printList(self):
        tmp = self.head
        while (tmp):
            print(tmp.data)
            tmp = tmp.next

    def delete(self, key):
        temp = self.head

        # case1
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # case2
        while (temp is not None):
            if (temp.data == key):
                break
            pre = temp
            temp = temp.next

        # case 3
        if (temp == None):
            return

        pre.next = temp.next
        temp = None

    def deletetotal(self):
        curr = self.head
        while curr:
            del curr.data
            curr = curr.next

    def getnodecount(self, node):
        if (not node):
            return 0
        else:
            return 1+self.getnodecount(node.next)

    def getcount(self):
        return self.getnodecount(self.head)

    def reverseLinked(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev


if __name__ == "__main__":
    llist = LinkedList()
    llist.append(2)
    llist.push(5)
    llist.push(8)
    llist.push(9)
    llist.delete(5)
    # llist.deletetotal()
    llist.printList()
    print(llist.getcount())
    llist.reverseLinked()
    llist.printList()
