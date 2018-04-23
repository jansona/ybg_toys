class Node(object):
    def __init__(self, n):
        self.val = n
        self.next = None

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def enter(self, n):
        if self.head==None:
            self.head = Node(n)
            self.tail = self.head
        else:
            point = self.head
            while point.next!=None and point.next.val<=n:
                if point.next.val==n:
                    return
                # print(point.val, end=' ')
                point = point.next
            tpoint = point.next
            point.next = Node(n)
            point.next.next = tpoint
    
    def out(self):
        if self.head==None:
            print("The queue is empty.")
            return None
        else:
            temp = self.head.val
            self.head = self.head.next
        return temp


def dbl_linear(n):
    counter = 0
    l = []
    q = Queue()
    q.enter(1)
    while counter<=n:
        temp = q.out()
        l.append(temp)
        q.enter(2 * temp + 1)
        q.enter(3 * temp + 1)
        counter+=1
    return temp

print(dbl_linear(20))