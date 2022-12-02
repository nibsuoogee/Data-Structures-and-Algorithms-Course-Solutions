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

class OpenHash:
    def __init__(self, M):
        self.M = M # The size of the hash table...
        self.T = [LinkedList() for i in range(M)] # is used to initialize M linked lists

    def insert(self, s):
        hash = fold(s, self.M) # sending the string/integer to the string folding hash method
        current = self.T[hash].head # setting a pointer to the obtained value's linked list head...
        while(current.data != None): 
            if current.data == s: # if pointing at node containing the original value..
                return # do not go further, the same value is already in the list.
            if current.next == None: # if reached the end of the list..
                new = Node(s, None) # create node
                current.next = new
                self.T[hash].tail = new # set list's tail to it
                self.T[hash].len += 1 # increment list's length
                return
            current = current.next
        current.data = s # set new node's data field to the new value
        self.T[hash].len += 1 # increment list's length

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
                if current.data != None:
                    data.append(current.data)
                current = current.next
            if current.data != None:
                data.append(current.data)
            print(data)
        print()

def fold(s, X):
    sum = 0
    mul = 1
    if type(s) == int:
        s = str(s)
    for i in range(len(s)):
        if i % 4 == 0: # four byte string fold
            mul = 1
        else:
            mul = mul * 256
        sum += ord(s[i]) * mul 
    return sum % X # modulo operator by table size


if __name__ == "__main__":
    table = OpenHash(3)

    start = time.time()   

    print("Step 1: adding values")
    table.insert(12)
    table.print()
    table.insert('hashtable')
    table.print()
    table.insert(1234)
    table.print()
    table.insert(4328989)
    table.print()
    table.insert('BM40A1500')
    table.print()
    table.insert(-12456)
    table.print()
    table.insert('aaaabbbbcccc')
    table.print()

    table.search(-12456)
    table.search('hashtable')
    table.search(1235)

    print()
    table.print()

    print("Removing: 'BM40A1500'")
    table.delete('BM40A1500')
    table.print()
    print("Removing: 1234")
    table.delete(1234)
    table.print()
    print("Removing: 'aaaabbbbcccc'")
    table.delete('aaaabbbbcccc')

    table.print()

    print(time.time() - start)   

    print("matches: ", end="")