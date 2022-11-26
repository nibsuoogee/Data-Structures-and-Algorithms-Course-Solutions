class HashLinear:
    def __init__(self, M):
        self.M = M
        self.T = [None] * M

    def insert(self, x):
        home = fold(x, self.M)
        pos = home
        i = 1
        while(None != self.T[pos]):
            if (x == self.T[pos]):
                return
            pos = (home + i) % self.M
            i += 1
        self.T[pos] = x


    def delete(self, x):
        home = fold(x, self.M)
        pos = home
        i = 1
        while(x != self.T[pos]):
            if (None == self.T[pos]):
                return
            pos = (home + i) % self.M
            i += 1
        self.T[pos] = "DEL"

    def print(self):
        for i in range(self.M):
            if self.T[i] != None and self.T[i] != "DEL":
                print(self.T[i], end=" ")

        print()


def hash(x, X):
    sum = 0
    for i in range(len(x)):
        sum += ord(x[i])
    return sum % X

def fold(x, X):
    s = str(x)
    sum = 0
    mul = 1
    for i in range(len(s)):
        if i % 4 == 0:
            mul = 1
        else:
            mul = mul * 256
        sum += ord(s[i]) * mul
    #print(x)
    #print(sum)
    return sum % X



if __name__ == "__main__":
    table = HashLinear(8)
    table.insert("aaaa")
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # 10aaaa1 BM40A1500 Bar1