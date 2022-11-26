def jumps(n, a, b):
    dp = [0] * (n+1)
    dp[n] = 1
    for i in range(n-1, -1, -1):
        if i + a <= n and dp[i + a] != 0:
            dp[i] += dp[i+a]
        if i + b <= n and dp[i + b] != 0:
            dp[i] += dp[i+b]
    
    return dp[0]

if __name__ == "__main__":
    print(jumps(4, 1, 2)) # 5
    print(jumps(8, 2, 3)) # 4
    print(jumps(11, 6, 7)) # 0
    print(jumps(30, 3, 5)) # 58
    print(jumps(100, 4, 5)) # 1167937