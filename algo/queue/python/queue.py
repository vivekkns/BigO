
# Queue
# insertions are done at one end (rear) and
# deletions are done at other end (front)
#
# FIFO
#
# Queue
#
#
# +--------+-------+-------+--------------------+------+
# |        |       |       |                    |      |
# |        |       |       |                    |      |
# |        |       |       |                    |      |
# +---^----+-------+-------+--------------------+--+---+
#     |                                            ^
#     +                                            | rear (insertions)
# front (deletions)                                +
#

# Operations
#
# - enqueue (trying to enqueue an element in a full queue is called - Overflow)
# - dequeue (trying to dequeue an element in a empty queue is called - Underflow)
#
# Aux operations
# - front
# - queuesize
# - isempty
# - isfull


#
# queue using fixed size array
#

class Queue:
    def __init__(self, size):
        self.size = size
        self.A = [0]*size
        self.front = -1
        self.rear = -1

    def isempty(self):
        if self.front == -1:
            return True
        return False

    def isfull(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        return False

    def enqueue(self, data):
        if self.isfull():
            raise Exception('Overflow')
        if self.rear == -1:
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.A[self.rear] = data

    def dequeue(self):
        if self.isempty():
            raise Exception('Underflow')
        data = self.A[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return data

    def __call__(self, *args, **kwargs):
        print self.A, 'front=', self.front, 'rear=', self.rear


#
# queue using linked list
#

class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None


class Queue_list:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        if self.front is None:
            return True
        return False

    def enqueue(self, data):
        n = Node(data)
        if self.rear is None:
            self.rear = n
            self.front = self.rear
        else:
            self.rear.Next = n
            self.rear = n

    def dequeue(self):
        if self.isempty():
            raise Exception('Underflow')
        n = self.front
        self.front = self.front.Next
        if self.front is None:
            self.front = self.rear = None
        return n.data

    def __call__(self, *args, **kwargs):
        temp = self.front

        while temp is not None:
            print temp.data
            temp = temp.Next

if __name__ == '__main__':

    q = Queue(5)

    q.enqueue(2)
    q.enqueue(20)
    q.enqueue(-2)
    q()
    print q.dequeue(), q.dequeue(), q.dequeue()

    q = Queue_list()
    q.enqueue(2)
    q.enqueue(20)
    q.enqueue(-2)
    q()
    print q.dequeue(), q.dequeue(), q.dequeue()
