# 149p [음료수 얼려 먹기]

from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

cnt = 0

def count(i, j):
    global cnt
    
    q = deque()
    q.append((i, j))
    graph[i][j] = 1
    
    while q:
        i, j = q.popleft()
        adj = get_adj(i, j)
        
        for n_i, n_j in adj:
            if graph[n_i][n_j] == 0:
                graph[n_i][n_j] = 1
                q.append((n_i, n_j))
                
    cnt += 1
    

def get_adj(x, y):
    arr = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            if graph[nx][ny] == 0:
                arr.append((nx, ny))
            
    return arr


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            count(i, j)
            
print(cnt)



# 입력예시 1
# 4 5
# 00110
# 00011
# 11111
# 00000

# 출력예시 1
# 3

# 입력예시 2
# 6 6
# 000111
# 111011
# 100001
# 111111
# 001111
# 111101

# 출력예시 2
# 4

