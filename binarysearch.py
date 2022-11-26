def search(A: list, item: int):
    lowest = 0
    highest = len(A)-1
    while lowest <= highest:
        middle = int((lowest + highest) / 2)
        if (A[middle] < item):
            lowest = middle + 1
        elif A[middle] > item:
            highest = middle - 1
        else:
            return middle
    return -1

if __name__ == "__main__":
    A = [1, 2, 3, 6, 10, 15, 22, 27, 30, 31]
    print(search(A, 6))     # 3
    print(search(A, 7))     # -1
    print(search(A, 30))    # 8