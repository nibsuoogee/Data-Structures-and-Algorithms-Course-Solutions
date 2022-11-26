def split(T):
    count = 0
    length = len(T)
    L = [0] * length # cumulative max
    R = [0] * length # cumulative min
    prevMax = 0
    prevMin = T[-1]
    R[-1] = T[-1]
    
    for i in range(1, len(T)):
        if T[-i] < prevMin:
            prevMin = T[-i]
            R[-i] = prevMin
        else:
            R[-i] = prevMin

        if T[i-1] > prevMax:
            prevMax = T[i-1]
            L[i-1] = prevMax
        else:
            L[i-1] = prevMax

    for i in range(1, length):
        if L[i-1] < R[i]:
            count += 1

    return count


if __name__ == "__main__":
    pass
    print(split([1,2,3,4,5])) # 4
    print(split([5,4,3,2,1])) # 0
    print(split([2,1,2,5,7,6,9])) # 3
    print(split([1,2,3,1])) # 0
    print(split([3,2,3,5,7,6,9,1])) # 0