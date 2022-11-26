#original source: https://www.geeksforgeeks.org/power-set/
def subsets(n: int) -> list:
    powerSetSize = 2**n
    setSize = n
    i = 0
    j = 0
    set = []
    subsets = []
    for i in range(n):
        set.append(i+1)
    for i in range(powerSetSize):
        subset = []
        for j in range(setSize):
            if i & 1<<j:
                subset.append(set[j])
        subsets.append(subset)
    subsets.pop(0)
    return subsets


if __name__ == "__main__":
    print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    #print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
                        #  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
                        #  [2, 3, 4], [1, 2, 3, 4]]

    #S = subsets(10)
    #print(S[95])    # [6, 7]
    #print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
    #print(S[826])   # [1, 2, 4, 5, 6, 9, 10]