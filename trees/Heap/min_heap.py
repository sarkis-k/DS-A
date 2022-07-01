class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def sift_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                self.heap_list[index], self.heap_list[index // 2] = self.heap_list[index // 2], self.heap_list[index]
            index = index // 2

    def sift_down(self, index):
        while index * 2 <= self.current_size:
            min_ch = self.min_child(index)

            if self.heap_list[index] > self.heap_list[min_ch]:
                self.heap_list[index], self.heap_list[min_ch] = self.heap_list[min_ch], self.heap_list[index]
            index = min_ch

    def min_child(self, index):
        if (index * 2) + 1 > self.current_size:
            return index * 2
        else:
            if self.heap_list[index * 2] < self.heap_list[(index * 2) + 1]:
                return index * 2
            else:
                return (index * 2) + 1

    def insert(self, value):
        self.heap_list.append(value)
        self.current_size += 1
        self.shift_up(self.current_size)

    def delete_min(self):
        if len(self.heap_list) == 1:
            return "empty heap"

        root = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.current_size -= 1
        self.shift_down(1)
        return root


