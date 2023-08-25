class circularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rare+1) % self.size == self.front:
            print("queue is full")
            return
        elif self.front == -1:
            self.rear = 0
            self.front = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear+1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if (self.front == -1):
            print("is empty")
            return
        elif (self.front == self.rear):
            posval = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return posval
        else:
            posval = self.queue[self.front]
            self.front = (self.front+1) % self.size
            return posval
