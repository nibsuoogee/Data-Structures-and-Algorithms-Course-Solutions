
# inspiration for solution from Rajput-Ji
# original available: https://www.geeksforgeeks.org/sum-of-all-distances-between-occurrences-of-same-characters-in-a-given-string/

def pairs(s):
    ones = 0
    length = 0
    sum = 0
    for i in range(0,len(s)):
        if (s[i] == "1"):
            sum += ones * i -length
            length += i
            ones += 1
    return sum

if __name__ == "__main__":
    print(pairs("100101")) # 10
    print(pairs("101")) # 2
    print(pairs("100100111001")) # 71
    print(pairs("1001001110010")) # 71
    print(pairs("0110")) # 1