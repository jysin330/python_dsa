class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)

        new_node.next = self.head
        self.head = new_node

    def append(self, new_value):

        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while (temp.next != None):
            temp = temp.next

        temp.next = new_node

    def insert_at(self, prev_node, new_value):
        if prev_node is None:
            print("previous node is seems to be empty")
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def treverse(self, key, new_value):
        temp = self.head

        while (temp.data != key):
            prev = temp
            temp = temp.next

        return self.insert_at(prev, new_value)

    def print(self):
        temp = self.head
        while (temp != None):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.append(3)
    llist.append(4)
    llist.append(6)
    llist.append(7)
    llist.treverse(6, 5)
    llist.print()
