def pairs(s):
    distances = []
    bits = 1
    sum = 0
    for bit in s:
        if (bit == "1"):

            if (len(distances) == 0):
                distances.append(0)
            else:
                distances[len(distances)-1] += 1
                if len(s) == bits:
                    print("1: ", end="")
                    print(distances)
                    break
            distances.append(distances[len(distances)-1])
            print("1: ", end="")
            print(distances)
        elif bit == "0":
            distances[len(distances)-1] += 1
            print("0: ", end="")
            print(distances)
        bits += 1
    
    for n in distances:
        sum += n
    return sum

if __name__ == "__main__":
    print(pairs("100101")) # 10
    #print(pairs("101")) # 2
    #print(pairs("100100111001")) # 71