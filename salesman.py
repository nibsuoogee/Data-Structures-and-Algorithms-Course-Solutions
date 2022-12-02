import math
import copy

def salesman(city_map):
    for i in range(len(city_map)):
        for j in range(len(city_map)):
            pass
            #print(f'{city_map[i][j]:4}', end=" ")
        #print()
    #print()
    city_map_copy = copy.deepcopy(city_map)
    path = []
    path.append(0)
    for i in range(len(city_map_copy)):
        for j in range(len(city_map_copy)):
            if city_map_copy[i][j] == 0:
                city_map_copy[i][j] = math.inf
    (reduced_map, red) = reduction(city_map_copy)
    upper_bound = math.inf
    unvisited = []
    for i in range(1,len(city_map_copy)):
        unvisited.append(i)

    previous = 0
    infinitized_matrixes = [None] * len(reduced_map)
    infinitized_matrixes[0] = copy.deepcopy(reduced_map)
    prev_reduced = infinitized_matrixes[0]
    for i in range(len(city_map_copy)):
        costs = [math.inf] * len(reduced_map)
        for j in unvisited:
            next = j
            temp_map = copy.deepcopy(prev_reduced)
            temp_map = infinitize(temp_map, previous, next)
            temp_map[next][previous] = math.inf
            for node in path:
                temp_map[next][node] = math.inf
            (temp_map, infinitized_red) = reduction(temp_map)
            infinitized_matrixes[next] = copy.deepcopy(temp_map)
            if infinitized_red == math.inf:
                infinitized_red = 0

            costs[j] = red + infinitized_red + reduced_map[previous][next]
            a = red
            b = infinitized_red
            c = reduced_map[previous][next]
            d = 0
            #print("rm: ",reduced_map[previous][next])
        #print(costs)
        previous = costs.index(min(costs))
        #if previous != 0:
        unvisited.remove(previous)
        path.append(previous)
        
        prev_reduced = infinitized_matrixes[previous]
        if len(unvisited) <= 0:
            path.append(0)
            return path
    return

def infinitize(temp_map, row, column):
    for i in range(len(temp_map)):
        for j in range(len(temp_map)):
            if i == row or j == column:
                temp_map[i][j] = math.inf
    return temp_map

def reduction(red_map):
    row_reduction = 0
    column_reduction = 0

    for i in range(len(red_map)):
        min_row = math.inf
        for j in range(len(red_map)):
            if red_map[i][j] < min_row:
                min_row = red_map[i][j]
            
        for j in range(len(red_map)):
            if red_map[i][j] != math.inf:
                red_map[i][j] -= min_row
        row_reduction += min_row

    #print("row:")
    for i in range(len(red_map)):
        for j in range(len(red_map)):
            pass
            #print(f'{red_map[i][j]:4}', end=" ")
        #print()

    for i in range(len(red_map)):
        min_column = math.inf
        for j in range(len(red_map)):
            if red_map[j][i] < min_column:
                min_column = red_map[j][i]
            
        for j in range(len(red_map)):
            if red_map[j][i] != math.inf:
                red_map[j][i] -= min_column
        column_reduction += min_column

    #print("column:")
    for i in range(len(red_map)):
        for j in range(len(red_map)):
            pass
            #print(f'{red_map[i][j]:4}', end=" ")
        #print()  

    red = row_reduction + column_reduction
    return (red_map, red)
   
if __name__ == "__main__":
    
    cost = 0

    city_map = [
    #     0   1   2   3   4
        [ 0, 12, 19, 16, 29],   # 0
        [12,  0, 27, 25,  5],   # 1
        [19, 27,  0,  8,  4],   # 2
        [16, 25,  8,  0, 14],   # 3
        [29,  5,  4, 14,  0]    # 4
        ]

    path = salesman(city_map)
    for i in range(len(city_map)):
        cost += city_map[path[i]][path[i+1]]
    print(path)     # [0, 1, 4, 2, 3, 0]
    print(cost)     # 45