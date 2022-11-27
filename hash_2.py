import time
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)
        self.len = 0

class HashLinear:
    def __init__(self, M):
        self.M = M
        self.T = [LinkedList() for i in range(M)]


    def insert(self, s):
        hash = fold(s, self.M)
        current = self.T[hash].head
        while(current.data != None):
            if current.data == s:
                return
            if current.next == None:
                new = Node(s, None)
                current.next = new
                self.T[hash].tail = new
                self.T[hash].len += 1
                return
            current = current.next
        current.data = s
        self.T[hash].len += 1

    def delete(self, s):
        hash = fold(s, self.M)
        current = self.T[hash].head
        # delete if first
        if current.data == s:
            self.T[hash].head = current.next
            return
        # delete if middle
        while(current.next.next != None):
            if current.next.data == s:
                current.next = current.next.next
                break
            current = current.next   
        # delete if last
        if current.next.data == s:
            current.next = None
            self.T[hash].tail = current

        

    def search(self, s):
        hash = fold(s, self.M)
        current = self.T[hash].head
        while(current.data != None):
            if current.data == s:
                print("Found: {0}".format(s))
                return True
            if current.next != None:
                current = current.next
            else:
                break
        print("Didn't find: {0}".format(s))
        return False

    def print(self):
        for list in self.T:
            current = list.head
            data = []
            while(current.next != None):
                data.append(current.data)
                current = current.next
            data.append(current.data)
            print(data)

        print()

def fold(s, X):
    sum = 0
    mul = 1
    if type(s) == int:
        s = str(s)
    for i in range(len(s)):
        if i % 4 == 0:
            mul = 1
        else:
            mul = mul * 256
        sum += ord(s[i]) * mul
    return sum % X



if __name__ == "__main__":
    table = HashLinear(3)

    start = time.time()   

    table.print()
    print()

    table.insert(12)
    table.insert('hashtable')
    table.insert(1234)
    table.insert(4328989)
    table.insert('BM40A1500')
    table.insert(-12456)
    table.insert('aaaabbbbcccc')

    table.print()
    print()

    table.search(-12456)
    table.search('hashtable')
    table.search(1235)

    table.delete('BM40A1500')
    table.delete(1234)
    table.delete('aaaabbbbcccc')

    table.print()

    print(time.time() - start)   

    print("matches: ", end="")