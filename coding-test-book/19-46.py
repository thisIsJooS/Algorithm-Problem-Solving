# https://www.acmicpc.net/problem/16236

from collections import deque

n = int(input())
graph = []
x, y = None, None    # 상어의 위치 저장
q = []        # 먹을 수 있는 물고기의 좌표 저장
shark_size = 2
ate_cnt = 0
time = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = int(1e9)
    
    
# x, y에서 i, j 까지의 거리를 구해보자    - BFS
def get_distance(src_x, src_y, dst_x, dst_y):   
    distance = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append((src_x, src_y))
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<n):
                continue

            if graph[nx][ny] > shark_size:
                continue
            
            if distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
                
            if nx == dst_x and ny == dst_y:
                return distance[nx][ny]
        
    return INF


# 현재 상어의 좌표에서 가장 가까운 물고기의 좌표와 거리를 return
def pop(q, x, y):
    arr = []
    for e in q:
        i, j = e
        dist = get_distance(x, y, i, j)
        
        arr.append((dist, i, j)) 
    arr.sort()
    min_dist, min_x, min_y = arr[0]
    q.remove((min_x, min_y))
    
    return min_dist, min_x, min_y


# 그래프 초기화
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
            graph[i][j] = 0
        elif 0 < graph[i][j] < shark_size:
            q.append((i, j))
            
            
while q:
    dist, i, j = pop(q, x, y)   # 현재 상어의 위치로부터 가장 가까운 물고기의 좌표와 거리 pop
    if dist == INF:
        break
    
    x, y = i, j
    graph[x][y] = 0
    time += dist        # 시간 추가
    ate_cnt += 1
    
    if ate_cnt == shark_size:
        shark_size += 1
        ate_cnt = 0    
        # 새롭게 먹을 수 있는 물고기 추가
        for i in range(n):
            for j in range(n):
                if graph[i][j] == shark_size-1:
                    q.append((i, j))
    
print(time)
