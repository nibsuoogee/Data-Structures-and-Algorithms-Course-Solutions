
class HashBucket:
    def __init__(self, M, B):
        self.M = M
        self.B = B
        self.T = [None] * M
        self.O = [None] * M

    def insert(self, x):
        homeBucket = hash(x, self.B)
        pos = homeBucket * (self.M/self.B)
        pos = int(pos)
        bucketCheck = int(homeBucket * (self.M/self.B) + (self.M/self.B))
        while(pos != bucketCheck):
            if (x == self.T[pos]):
                return
            if (None == self.T[pos]):
                self.T[pos] = x
                return
            pos += 1
        for j in range(self.M-1):
            if (x == self.O[j]):
                return
            if self.O[j] == None:
                self.O[j] = x
                return

    def delete(self, x):
        homeBucket = hash(x, self.B)
        pos = homeBucket * (self.M/self.B)
        pos = int(pos)
        bucketCheck = int(homeBucket * (self.M/self.B) + (self.M/self.B))
        while(pos != bucketCheck):
            if (x == self.T[pos]):
                self.T[pos] = "DEL"
                return
            pos += 1
        for j in range(self.M-1):
            if self.O[j] == x:
                self.O[j] = "DEL"
                return

        

    def print(self):
        for i in range(self.M):
            if self.T[i] != None and self.T[i] != "DEL":
                print(self.T[i], end=" ")
        for i in range(self.M):
            if self.O[i] != None and self.O[i] != "DEL":
                print(self.O[i], end=" ")

        print()
        

def hash(x, X):
    sum = 0
    for i in range(len(x)):
        sum += ord(x[i])
    return sum % X

if __name__ == "__main__":
    table = HashBucket(8, 4)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # fOo BM40A1500 123 Bar1 10aaaa1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # BM40A1500 Bar1 10aaaa1
