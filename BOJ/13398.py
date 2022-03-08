import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
dp = [a for a in arr]   # 하나도 빼지 않았을 경우
dp2 = [a for a in arr]  # 하나를 뺸 경우

for i in range(1, n):
    dp[i] = max(dp[i], dp[i-1]+arr[i])
    dp2[i] = dp[i]
        
    if i-2 >= 0 and dp[i] < dp[i-2] + arr[i]: # arr[i-1]을 제외한 경우가 합이 더 크게 나오는 경우
        dp2[i] = dp[i-2] + arr[i]   
    
    dp2[i] = max(dp2[i], dp2[i-1] + arr[i])
    
print(max(max(dp), max(dp2)))

