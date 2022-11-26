
def swap(A, B, C):
    A[B], A[C] = A[C], A[B]
    return A

def isort(A):
    if (len(A) > 1000):
        return A
    for i in range(len(A)):
        if (A[i] > 1000):
            return A
        j = i-1
        while (j>=0) and (A[j] > A[j+1]):
            A = swap(A, j, j+1)
            j = j-1
    return A

if __name__ == "__main__":
    A = [4, 3, 6, 2, 9, 7, 1, 8, 5]
    A = isort(A)
    print(A)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]