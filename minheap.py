class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = self.right = None

class MinHeap:
    def __init__(self):
        self.list = []
        self.root = None

    def push(self, key):
        self.insert_help(self.root, key)
        return

    def insert_help(self, rt, key):
        self.list.append(key)
        rt = len(self.list)-1
        self.swapper(rt, key)
        

    def swapper(self, rt, key):
        if rt <= 0:
            return
        if self.list[rt] < self.list[int((rt-1)/2)]:
            self.list[rt] = self.list[int((rt-1)/2)]
            self.list[int((rt-1)/2)] = key
            self.swapper(int((rt-1)/2), key)
        

    def pop(self):
        popped = self.list.pop(0)
        rt = 0
        i = int(((len(self.list)-1)-1)/2)
        while i > -1:
            self.siftdown(i)
            i -= 1
        return popped

    def siftdown(self, rt):
        smaller = rt
        leftChildIndex = (2*rt+1)
        rightChildIndex = (2*rt+2)
        listMaxIndex = len(self.list)-1
        if leftChildIndex <= listMaxIndex:
            if self.list[leftChildIndex] < self.list[rt]:
                smaller = leftChildIndex
        if rightChildIndex <= listMaxIndex:
            if self.list[rightChildIndex] < self.list[rt]:
                smaller = rightChildIndex
        if smaller != rt:
            #self.list[rt], self.list[smaller] = self.list[smaller], self.list[rt]
            temp = self.list[rt]
            self.list[rt] = self.list[smaller]
            self.list[smaller] = temp
            self.siftdown(smaller)

        
                

    def print(self):
        for key in self.list:
            print(key, end=" ")
        print()
        pass


if __name__ == "__main__":
    #items = [4, 8, 6, 5, 1, 2, 3]
    items = [3, 10, 13, 2, 5, 12, 8, 9, 4, 6, 7, 14]
    heap = MinHeap()
    [heap.push(key) for key in items]
    heap.print()        # 1 4 2 8 5 6 3 
    print(heap.pop())   # 1
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    #heap.print()        # 2 4 3 8 5 6  
    heap.print() # 8 9 12 10 14 13 