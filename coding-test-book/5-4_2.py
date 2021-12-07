# 152p [미로 탈출]

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
    

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        if x == n-1 and y == m-1:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if isSafe(nx, ny):
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
                
        
def isSafe(x, y):
    if not (0<=x<n and 0<=y<m):
        return False
    
    if graph[x][y] != 1:
        return False
    
    
    return True


bfs(0, 0)
print(graph[n-1][m-1])
                 
    
# 입력예시 1
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# 출력예시 1
# 10

# 입력예시 2
# 2 25
# 1011101110111011101110111
# 1110111011101110111011101

# 출력예시 2
# 38
