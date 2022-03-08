import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
dp_left = [1] * n
dp_right = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp_left[i] = max(dp_left[i], dp_left[j]+1)
            
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            dp_right[i] = max(dp_right[i], dp_right[j]+1)
    
dp = []
for i in range(n):
    dp.append(dp_left[i] + dp_right[i] - 1)

print(max(dp))