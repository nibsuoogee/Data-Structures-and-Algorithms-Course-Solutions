def triangle(a, b, c):
    if ((a+b) > c) and ((b+c) > a) and ((c+a) > b):
        return True
    return False

if __name__ == "__main__":
    print(triangle(3, 5, 4))    # True
    print(triangle(-1, 2, 3))   # False
    print(triangle(5, 9, 14))   # False
    print(triangle(30, 12, 29)) # True