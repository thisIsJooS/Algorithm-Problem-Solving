# 344p [경쟁적 전염] 
# https://www.acmicpc.net/problem/18405

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
coord = [[] for _ in range(k+1)]
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] != 0:
            coord[arr[i][j]].append((i, j))            
s, x, y = map(int, input().split())
x -= 1; y -= 1;

            
dist = [int(1e9)] * (k+1)
for e in range(1, k+1):
    for i, j in coord[e]:
        dist[e] = min(dist[e], abs(x-i) + abs(y-j))
            

            
print(0 if s<min(dist) else d.index(min(dist)))   



