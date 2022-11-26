import math

class Graph:
    def __init__(self, matrix):
        self.Matrix = matrix
        self.Vertexes = len(matrix)
        self.visited = [False] * len(matrix)
        self.stack = []

    def PreVisit(self, v):
        self.stack.insert(0,v)
        print(v, end=" ")
        return

    def PostVisit(self, v):
        self.stack.remove(v)
        return
    
    def neighbours(self, v):
        nList = []
        for i in range(self.Vertexes):
            if self.Matrix[v][i] != 0:
                nList.append(i)
        return nList

    def df_print(self, v):
        self.PreVisit(v)
        self.visited[v] = True
        nList = self.neighbours(v)
        for i in range(len(nList)):
            if self.visited[nList[i]] != True:
                self.df_print(nList[i])
        self.PostVisit(v)
        if len(self.stack) == 0:
            for i in range(len(self.visited)):
                self.visited[i] = False
            print()
        return
    
    def bf_print(self, v):
        Queue = []
        Queue.append(v)
        self.visited[v] = True
        while len(Queue) > 0:
            v = Queue.pop(0)
            self.PreVisit(v)
            nList = self.neighbours(v)
            for i in range(len(nList)):
                if self.visited[nList[i]] != True:
                    self.visited[nList[i]] = True
                    Queue.append(nList[i])
            self.PostVisit(v)
        for i in range(len(self.visited)):
            self.visited[i] = False
        print()
        return
    
    def weight(self, v1, v2):
        if v1 == v2:
            return 0
        if self.Matrix[v1][v2] != 0:
            return self.Matrix[v1][v2]
        return -1

    def getWeight(self, v1, v2):
        return self.Matrix[v1][v2]
    
    def insert(self, v1, v2, weight):
        self.Matrix[v1][v2] = weight
        return


if __name__ == "__main__":

    matrix = [
    #    0  1  2  3  4  5
        [0, 0, 7, 0, 9, 0], # 0
        [0, 0, 0, 0, 0, 0], # 1
        [0, 5, 0, 1, 0, 2], # 2
        [6, 0, 0, 0, 0, 2], # 3
        [0, 0, 0, 0, 0, 1], # 4
        [0, 6, 0, 0, 0, 0]  # 5   
    ]
    
    graph = Graph(matrix)

    graph.df_print(0)           # 0 2 1 3 5 4 
    graph.bf_print(0)           # 0 2 4 1 3 5 
    print(graph.weight(0, 2))   # 7
    print(graph.weight(3, 4))   # -1