
class MinHeap:
    def __init__(self):
        self.list = []
        self.root = None

    
    def permutations(self, k, numbers, included):
        n = 5
        if k == n:
            print(numbers)
        else:
            for i in range (0, n):
                if not included[i]:
                    included[i] = True
                    numbers[k] = i+1
                    self.permutations(k+1, numbers, included)
                    included[i] = False


if __name__ == "__main__":
    heap = MinHeap()
    included = [None] * 5
    numbers = [None] * 5
    heap.permutations(0, numbers, included)
