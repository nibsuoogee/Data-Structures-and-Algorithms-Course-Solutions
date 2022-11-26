# DSA course materials referenced for assistance

def qsort(A, i, j):
    pivotindex = findpivot(A, i, j)
    A[pivotindex], A[j] = A[j], A[pivotindex]
    k = partition(A, i, j-1, A[j])
    A[k], A[j] = A[j], A[k] 
    if (k-i) > 1:
        qsort(A, i, k-1)
    if (j-k) > 1:
        qsort(A, k+1, j)

def partition(A, left, right, pivot):
    while left <= right:
        while A[left] < pivot:
            left += 1
        while A[right] >= A[left] and A[left] >= pivot:
            right -= 1
        if right > left:
            A[left], A[right] = A[right], A[left] 
    return left

def findpivot(A, i, j):
    return int((i+j)/2) 
  
if __name__ == "__main__":
    A = [9, 7, 1, 8, 5, 3, 6, 2, 4]
    print(A)    # [9, 7, 1, 8, 5, 3, 6, 2, 4]
    qsort(A, 0, len(A)-1)
    print(A)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]