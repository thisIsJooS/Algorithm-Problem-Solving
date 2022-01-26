import copy

n = int(input())
arr = list(map(int, input().split()))
dp = [0] + copy.deepcopy(arr)

def f(arr):
    if n==1:
        return 
    
    for i in range(2, n+1):
        for j in range(1, i//2+1):
            dp[i] = max(dp[i], dp[j]+dp[i-j])
        
        
f(arr)
print(dp[n])