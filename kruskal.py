from graph import Graph

class ParentTree:
    def __init__(self, vertexes):
        self.array = [-1] * vertexes

    def union(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if (rooti != rootj):
            self.array[rooti] = rootj
            return True
        else:
            return False

    def find(self, v):
        while self.array[v] != -1:
            v = self.array[v]
        return v

def kruskal(graph):
    parTree = ParentTree(graph.Vertexes)
    numMst = graph.Vertexes
    weights = {}
    MSTmatrix =  [[0] * graph.Vertexes for i in range(graph.Vertexes)]
    MST = Graph(MSTmatrix)
    for i in range(graph.Vertexes):
        for j in range(graph.Vertexes):
            if i > j and graph.Matrix[i][j] != 0:
                key = j,i
                weights[key] = graph.Matrix[i][j]
    sortedWeights = dict(sorted(weights.items(), key=lambda item: item[1]))

    while numMst > 1:
        temp = list(sortedWeights.keys())[0]
        sortedWeights.pop(temp)
        if temp == None:
            return
        v = temp[0]
        u = temp[1]
        if parTree.union(v,u):
            MST.insert(v, u, graph.getWeight(v,u))
            MST.insert(u, v, graph.getWeight(v,u))
            numMst -= 1
    return MST
    
 
if __name__ == "__main__":

    matrix = [
    #    0  1  2  3  4  5
        [0, 0, 7, 6, 9, 0], # 0
        [0, 0, 5, 0, 0, 6], # 1
        [7, 5, 0, 1, 0, 2], # 2
        [6, 0, 1, 0, 0, 2], # 3
        [9, 0, 0, 0, 0, 1], # 4
        [0, 6, 2, 2, 1, 0]  # 5    
    ]
    graph = Graph(matrix)
    graph.bf_print(0)   # 0 2 3 4 1 5
    mst = kruskal(graph)
    for i in range(graph.Vertexes):
        for j in range(graph.Vertexes):
            print(f"{mst.getWeight(i,j):3d}", end="")
        print("\n")
    mst.bf_print(0)     # 0 3 2 1 5 4