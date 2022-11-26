def changes(A):
    c = 0
    for i in range(2,len(A)):
        if (A[i-2] == A[i-1]):
            if (A[i-1]+1 == A[i]):    
                A[i-1] += 2
                c += 1
            else:
                A[i-1] += 1
                c += 1
        elif (A[i-1] == A[i]):
            A[i] += 1
            c += 1
    print(A)
    return c


if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2  
