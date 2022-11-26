
# referenced code for prime number 
# generation: https://www.javatpoint.com/pyhton-print-all-prime-number-in-an-interval

def primes(N):
    Aprimes = []
    if N > 100000:
        return 0
    # start of referenced code
    for i in range(N+1):  
        if i > 1:  
            for n in range (2, i):  
                if (i % n) == 0:  
                    break  
            else:  
                Aprimes.append(i)
    # end of referenced code
    return len(Aprimes)

if __name__ == "__main__":
    print(primes(7))  # 4
    print(primes(15))  # 6
    print(primes(50)) # 15