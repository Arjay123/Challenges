from collections import namedtuple
from datetime import datetime

Element = namedtuple('Element', ['value', 'priority', 'inserted'])

class PriorityQueue:


    def insert(self, value, priority=0):
        e = Element(value, priority, inserted=datetime.now())
        self.heap.append(e)
        self.heap_size += 1
        self.sift_up(self.heap_size-1)

    def sift_up(self, index):
        if index:
            parent = PriorityQueue._parent(index)
            if self.heap[index].priority > self.heap[parent].priority or (self.heap[index].priority == self.heap[parent].priority and self.heap[index].inserted < self.heap[parent].inserted):
                self.swap(index, parent)
                self.sift_up(parent)

    def max_heapify(self, index):
        left = PriorityQueue._left(index)
        right = PriorityQueue._right(index)

        if left >= self.heap_size:
            return

        large_child = left
        if right < self.heap_size and (self.heap[right].priority > self.heap[left].priority or (self.heap[right].priority == self.heap[left].priority and self.heap[right].inserted < self.heap[left].inserted)):
            # print("%s:%s - %s before %s:%s - %s" % (self.heap[right].value,self.heap[right].priority, self.heap[right].inserted, self.heap[left].value,self.heap[left].priority, self.heap[left].inserted))
            large_child = right

        if self.heap[large_child].priority > self.heap[index].priority or (self.heap[large_child].priority == self.heap[index].priority and self.heap[large_child].inserted < self.heap[index].inserted):
            self.swap(index, large_child)
            self.max_heapify(large_child)

    def build_max_heap(self):
        for i in range(self.heap_size/2, -1, -1):
            self.max_heapify(i)

    def next(self):
        self.build_max_heap()
        self.swap(0, self.heap_size-1)
        self.heap_size -= 1
        val = self.heap.pop(self.heap_size)
        self.max_heapify(0)
        return val


    def swap(self, i, j):
        tmp = self.heap[j]
        self.heap[j] = self.heap[i]
        self.heap[i] = tmp




    @staticmethod
    def _left(index):
        return 2*index + 1

    @staticmethod
    def _right(index):
        return 2*index + 2

    @staticmethod
    def _parent(index):
        return index/2

    def __init__(self, arr=None):
        if not arr:
            arr = []
        self.heap = arr
        self.heap_size = len(self.heap)
        self.build_max_heap()


a = PriorityQueue([Element(value='Arjay Nguyen', priority=1, inserted=datetime.now()), Element(value='Arjay', priority=2, inserted=datetime.now()), Element(value='Chau Nguyen', priority=2, inserted=datetime.now()), Element(value='Chau Nguyen', priority=0, inserted=datetime.now()), Element(value='Chau Nguyen', priority=5, inserted=datetime.now())])

a.insert("Bob", 2)
a.insert("Butt", 2)
a.insert("Bob2", 5)
a.insert("Bobutt", 5)
print(a.heap)
print('')

while(len(a.heap)):
    val = a.next()
    print(str(val.value) + " - " + str(val.priority))


