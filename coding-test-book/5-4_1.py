# 152p [미로 탈출]

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
    

cnt = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    q.append((None, None))
    graph[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        if x == None:
            cnt += 1
            q.append((None, None))
            continue
            
        if x == n-1 and y == m-1:
            cnt += 1
            break
            
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isSafe(nx, ny):
                q.append((nx, ny))
                graph[nx][ny] = 0
        

def isSafe(x, y):
    if not (0<=x<n and 0<=y<m):
        return False
    
    if graph[x][y] == 0:
        return False
    
    return True


bfs(0, 0)
print(cnt)


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
