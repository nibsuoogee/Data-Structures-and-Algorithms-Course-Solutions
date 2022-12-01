import math

def salesman(city_map):
    order = [None] * (len(city_map)+1)
    order[0] = 0
    order[-1] = 0
    bound = 999999
    order = permutations(1, city_map, order, bound)
    return order


def permutations(k, city_map, order, bound):
    cost = 0
    prev_vertex = 0
    for i in order[1:(len(city_map)+1)]:
        if i == None:
            break
        cost += city_map[prev_vertex][i]
        prev_vertex = i
    if cost > bound:
        return
    if k == (len(city_map)):
        return order
    else:
        for i in range(1,len(city_map)):
            if i not in order[1:len(city_map)]:
                order[k] = i
                temp = permutations(k+1, city_map, order, bound)
                if temp is not None:
                    order = temp
                    return order
                else:
                    order[k] = None
                

   
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