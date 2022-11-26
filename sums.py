def sums(items):
    n = len(items)
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
                subset.append(items[j])
        subsets.append(subset)
    subsets.pop(0)
    UniqueSums = []
    for subset in subsets:
        sum = 0
        for value in subset:
            sum += value
        if sum in UniqueSums:
            continue
        UniqueSums.append(sum)   
    return len(UniqueSums)


if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    #print(sums([2, 2, 3]))                  # 5
    #print(sums([1, 3, 5, 1, 3, 5]))         # 18
    #print(sums([1, 15, 5, 23, 100, 55, 2])) # 121