# 376p [정수 삼각형] - IOI 1994년도
# https://www.acmicpc.net/problem/1932

n = int(input())
arr = [[0]*(n+1) for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        arr[i][j+1] = data[j]
        
for i in range(1, n):
    for j in range(1, n+1):
        arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
        
print(max(arr[n-1]))