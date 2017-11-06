class Heap:
    def insert(self, val):
        self.heap.append(val)
        self.sift_up(len(self.heap) - 1)
        self.heap_size += 1

    def sift_up(self, index):
        if index:
            parent = (index-1)/2
            if self.heap[index] > self.heap[parent]:
                self.swap(index, parent)
                self.sift_up(parent)

    def max_heapify(self, index):
        left = 2*index + 1
        right = 2*index + 2

        if left >= self.heap_size:
            return

        large_child = left
        if right < self.heap_size and self.heap[right] > self.heap[left]:
            large_child = right

        if self.heap[large_child] > self.heap[index]:
            self.swap(index, large_child)
            self.max_heapify(large_child)

    def build_max_heap(self):
        for i in range(self.heap_size/2, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        while self.heap_size > 1:
            self.build_max_heap()
            self.swap(0, self.heap_size-1)
            self.heap_size -= 1
            self.max_heapify(0)

    def swap(self, i, j):
        if i < self.heap_size and j < self.heap_size:
            self.heap[i] = self.heap[i] ^ self.heap[j]
            self.heap[j] = self.heap[i] ^ self.heap[j]
            self.heap[i] = self.heap[i] ^ self.heap[j]


    def __init__(self, arr=None):
        if not arr:
            arr = []
        self.heap = arr
        self.heap_size = len(arr)
        self.build_max_heap()

a = Heap([1, 2, 3, 4, 5])
print("a: %s" % (a.heap))

b = Heap()
c = Heap()
c.insert(1)
c.insert(2)
b.insert(5)
print("c: %s, b: %s" % (c.heap, b.heap))
a.heap_sort()
print(a.heap)

