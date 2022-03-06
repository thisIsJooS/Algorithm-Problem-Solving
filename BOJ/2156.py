import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [0] + [int(input()) for _ in range(n)]
    if n==1:
        return arr[n]
    if n==2:
        return sum(arr)
    
    dp = [0] * (n+1)
    dp[1] = arr[1]
    dp[2] = arr[1]+arr[2]
    
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])
        
    return dp[n]

print(solve())