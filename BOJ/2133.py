import sys
input = sys.stdin.readline

def main():
    N = int(input())
    if N%2 != 0:
        return 0
    
    dp = [0]*(N+1)
    dp[0] = 1
    
    for n in range(2, N+1):
        i = 2
        while n-i >= 0:
            if i==2:
                dp[n] = dp[n-i] * 3
            else:
                dp[n] += dp[n-i] * 2
            i += 2
    
    return dp[N]

print(main())
    
    
