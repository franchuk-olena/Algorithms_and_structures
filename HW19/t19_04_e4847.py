class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.position = {}

    def _swap(self, i, j):
        self.position[self.heap[i][1]] = j
        self.position[self.heap[j][1]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx][0] > self.heap[parent][0]:
                self._swap(idx, parent)
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        size = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            if left < size and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right < size and self.heap[right][0] > self.heap[largest][0]:
                largest = right
            if largest != idx:
                self._swap(idx, largest)
                idx = largest
            else:
                break

    def add(self, id, priority):
        self.heap.append([priority, id])
        idx = len(self.heap) - 1
        self.position[id] = idx
        self._sift_up(idx)

    def pop(self):
        top = self.heap[0]
        last = self.heap.pop()
        del self.position[top[1]]
        if self.heap:
            self.heap[0] = last
            self.position[last[1]] = 0
            self._sift_down(0)
        print(f"{top[1]} {top[0]}")

    def change(self, id, new_priority):
        idx = self.position[id]
        old_priority = self.heap[idx][0]
        self.heap[idx][0] = new_priority
        if new_priority > old_priority:
            self._sift_up(idx)
        else:
            self._sift_down(idx)


def main():
    pq = PriorityQueue()
    try:
        while True:
            line = input()
            if not line:
                continue
            parts = line.strip().split()
            cmd = parts[0]
            if cmd == "ADD":
                id = parts[1]
                priority = int(parts[2])
                pq.add(id, priority)
            elif cmd == "POP":
                pq.pop()
            elif cmd == "CHANGE":
                id = parts[1]
                new_priority = int(parts[2])
                pq.change(id, new_priority)
    except EOFError:
        pass

if __name__ == "__main__":
    main()
