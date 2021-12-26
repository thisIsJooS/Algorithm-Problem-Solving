N, W = map(int, input().split())
weight = [0]
value = [0]
for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)
    

dp = [[0]*(W+1) for _ in range(N+1)]

for n in range(1, N+1):
    for w in range(1, W+1):
        if weight[n] > w:
            dp[n][w] = dp[n-1][w]
            
        else:
            valWith = value[n] + dp[n-1][w-weight[n]]
            valWithout = dp[n-1][w]
            dp[n][w] = max(valWith, valWithout)

print(dp[N][W])