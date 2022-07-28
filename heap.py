class Heap:
    heap = [None]
    heap_idx = 0
    def __init__(self):
        pass

    def push(self, x):
        if type(x) is not int:
            raise TypeError
        self.heap.append(x)
        self.heap_idx += 1
        curr = self.heap_idx
        parent = curr // 2
        while parent > 0 and self.heap[parent] > self.heap[curr]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[curr]
            self.heap[curr] = tmp
            curr = parent
            parent = curr // 2

    def pop(self):
        if heap_idx == 0:
            return None
        out = self.heap[1]
        if heap_idx == 1:
            self.heap_idx -= 1
            a.pop(1)
            return out
        self.heap[1] = self.heap[self.heap_idx]
        curr = self.heap_idx
        parent = curr // 2
        while parent > 0 and 

n = int(input("Graph size: "))
matrix = []

for i in range(n):
    matrix.append([None] * n)

for i in range(n):
    for j in range(i, n):
        if j == i:
            matrix[i][j] = 0
            continue
        v = int(input(f"Vertex {i} to {j}: "))
        matrix[i][j] = v
        matrix[j][i] = v        
