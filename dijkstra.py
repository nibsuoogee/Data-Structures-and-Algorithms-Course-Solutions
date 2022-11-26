from graph import Graph
import math


def dijkstragraph(graph, start):
    D = [math.inf] * graph.Vertexes
    D[start] = 0
    new_graph = Graph([[0] * graph.Vertexes for i in range(graph.Vertexes)])
    previous = [-1] * graph.Vertexes

    for i in range(graph.Vertexes):
        v = minVertex(graph, D)
        graph.visited[v] = True
        if D[v] == math.inf:
            continue
        nList = graph.neighbours(v)
        for j in range(len(nList)):
            w = nList[j]
            if (D[w] > (D[v] + graph.weight(v,w))):
                D[w] = D[v] + graph.weight(v,w)
                previous[w] = v   
    print(D)

    #print("previous: ",previous)
    a = 1
    for i in range(len(previous)): # optimal path graph construction
        new_graph.insert(previous[i],i,graph.getWeight(previous[i],i))
    a = 1
    for i in range(graph.Vertexes):
        graph.visited[i] = False
    #for i in range(graph.Vertexes):
    #    for j in range(graph.Vertexes):
    #        print(f"{new_graph.getWeight(i,j):3d}", end="")
    #    print("\n")
    #print()
    return new_graph

def minVertex(graph, D):
    v = 0
    for i in range(graph.Vertexes):
        if graph.visited[i] == False:
            v = i
            break
    for i in range(graph.Vertexes):
        if (graph.visited[i] == False) and (D[i] < D[v]):
            v = i
    return v

if __name__ == "__main__":

    matrix = [
        [0, 25,  6,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0, 10,  3,  0,  0,  0,  0,  0],
        [0,  0,  0,  7,  0, 25,  0,  0,  0,  0],
        [0,  0,  0,  0, 12, 15,  4, 15, 20,  0],
        [0,  0,  0,  0,  0,  0,  0,  2,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  2,  0],
        [0,  0,  0,  0,  0,  0,  0,  8, 13, 15],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  5],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
        ] 
    
    matrix2 = [
        [0,  3,  5,  6,  0,  0,  0,  5],
        [3,  0,  8,  0,  7,  8,  0,  1],
        [5,  8,  0,  5,  7,  0,  6,  0],
        [6,  0,  5,  0,  0,  6,  0,  0],
        [0,  7,  7,  0,  0,  0,  8,  2],
        [0,  8,  0,  6,  0,  0,  5,  0],
        [0,  0,  6,  0,  8,  5,  0,  0],
        [5,  1,  0,  0,  2,  0,  0,  0]
        ]
    
    graph = Graph(matrix)

    new_graph = dijkstragraph(graph, 0)
    new_graph.df_print(0)           # 0 1 2 3 4 5 6 7 9 8 
    new_graph.bf_print(0)           # 0 1 2 3 4 5 6 7 8 9
    print(new_graph.weight(3, 6))   # 4
    print(new_graph.weight(5, 8))   # -1