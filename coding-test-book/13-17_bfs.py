# 344p [경쟁적 전염] 
# https://www.acmicpc.net/problem/18405

from collections import deque

n, k = map(int, input().split())
data, graph = [], []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j)) # 종류, 시간, 행, 열
target_s, target_x, target_y = map(int, input().split())
data.sort()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque(data)

while q:
    virus, s, x, y = q.popleft()
    
    if s == target_s:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])