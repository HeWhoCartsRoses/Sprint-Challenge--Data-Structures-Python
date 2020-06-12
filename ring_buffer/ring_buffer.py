class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []
        self.count = 0

    def append(self, item):
        if len(self.arr) == self.capacity:
            last = self.count % self.capacity
            self.arr.pop(last)
            self.arr.insert(last, item)
            self.count += 1
        else:
            self.arr.append(item)
            self.count += 1

    def get(self):
        return self.arr
