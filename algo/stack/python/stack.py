import sys
#
# Stack
#
# Ordered list, insertion and deletion happens in one end (LIFO)
#
# Operations:-
# Main operations:-
# 1) push (overflow can happen)
# 2) pop (underflow can happen)
#
# Aux operation:-
# 1) Top()
# 2) Size()
# 3) isempty()
# 4) isfull()


class Stack:
    def __init__(self, size):
        self.size = size
        self.A = [0] * size
        self.top = -1

    def isfull(self):
        return self.top == self.size-1

    def isempty(self):
        return self.top == -1

    def push(self, data):
        if self.isfull():
            raise Exception('Stack Overflow')
        self.top +=1
        self.A[self.top] = data

    def pop(self):
        if self.isempty():
            raise Exception('Stack Underflow!')

        self.top -= 1
        return self.A[self.top+1]

    def __call__(self, *args, **kwargs):
        print self.A[:self.top+1]


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None

#
# Stack using linked list
#


class Stack_List:
    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head is None

    def push(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
        else:
            n.right = self.head
            self.head = n

    def pop(self):
        if self.isempty():
            raise Exception('Underflow')

        n = self.head
        self.head = self.head.right

        return n.data

    def __call__(self, *args, **kwargs):
        n = self.head

        while n is not None:
            sys.stdout.write(str(n.data) + ' -> ')
            n = n.right
        print

if __name__ == '__main__':

    print('Stack using array')
    s = Stack(4)
    s.push(2)
    s.push(22)
    s.push(-15)
    s.push(43)
    s()
    print 's.pop()=', s.pop()
    s()

    print('\n\nStack using linked list')

    sl = Stack_List()
    sl.push(2)
    sl.push(22)
    sl.push(-15)
    sl.push(43)
    sl()
    print 'sl.pop()=', sl.pop()
    sl()
