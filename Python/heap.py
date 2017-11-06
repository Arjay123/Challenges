import math

class MaxHeap:

    def __init__(self):
        self.heap = [7, 5, 3, 4, 1, 2]



    def insert(self, val):
        self.heap.append(val)
        self.sift_up(len(self.heap)-1)


    def sift_up(self, index):
        if index:
            parent = (index-1)/2
            if self.heap[index] > self.heap[parent]:
                tmp = self.heap[index]
                self.heap[index] = self.heap[parent]
                self.heap[parent] = tmp
                self.sift_up(parent)


    def print_heap(self):
        level = 0
        line = ""

        for index in range(0, len(self.heap)):
            index_level = int(math.log(index+1, 2))

            if index_level != level:
                print(line)
                line = ""
                level = index_level

            line += str(self.heap[index]) + " "
        print(line)


h = MaxHeap()
h.insert(8)
h.insert(10)
h.insert(6)
h.insert(11)
h.print_heap()