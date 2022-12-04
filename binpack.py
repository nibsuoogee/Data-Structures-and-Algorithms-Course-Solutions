import copy
def binpack(items, S):
    items.sort(reverse=True)
    unused = copy.deepcopy(items)
    current_bin = []
    bins = []
    ptr = 0
    while len(unused) > 0:
        while ptr < len(unused):
            if (sum(current_bin) + unused[ptr]) <= S:
                current_bin.append(unused[ptr])
                unused.remove(unused[ptr])
                continue
            ptr += 1
        bins.append(current_bin)
        current_bin = []
        ptr = 0
    return bins
    
 
if __name__ == "__main__":

    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10

    bins = binpack(items, B)

    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]}")

# A possible output:
#   bin 1: [9]
#   bin 2: [3, 3, 4]
#   bin 3: [6, 3]
#   bin 4: [10]
#   bin 5: [6]
#   bin 6: [8]
#   bin 7: [6]