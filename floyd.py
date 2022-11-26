from graph import Graph
import math


def floyd(graph):
    D = [[0] * graph.Vertexes for i in range(graph.Vertexes)]
    for i in range(graph.Vertexes):
        for j in range(graph.Vertexes):
            if graph.weight(i,j) != 0:
                D[i][j] = graph.weight(i,j)

    print()
    for k in range(graph.Vertexes):
        for i in range(graph.Vertexes):
            for j in range(graph.Vertexes):
                if (D[i][k] != math.inf) and (D[k][j] != math.inf) and (D[i][j] > (D[i][k] + D[k][j])):
                    D[i][j] = (D[i][k] + D[k][j])
                    
    for k in range(graph.Vertexes):
        for i in range(graph.Vertexes):
            if D[k][i] == math.inf:
                D[k][i] = 0


    return D
    

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
    D = floyd(graph)
    for i in range(6):
        for j in range(6):
            print(f"{D[i][j]:2d}", end=" ")
        print()
    #  0 12  7  8  9  9 
    #  0  0  0  0  0  0 
    #  7  5  0  1 16  2 
    #  6  8 13  0 15  2 
    #  0  7  0  0  0  1 
    #  0  6  0  0  0  0 