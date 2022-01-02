from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
arr = []
room_locations = []
virus_locations = deque()
res = 0      
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] == 0:
            room_locations.append((i, j))
        if arr[i][j] == 2:
            virus_locations.append((i, j))    
        

def infect_all():
    q = deque()
    q = copy.deepcopy(virus_locations)
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 0:
                arr[nx][ny] = 2
                q.append((nx, ny))
        
for candidate in list(combinations(room_locations, 3)):
    cnt = 0 
    for x, y in candidate:
        arr[x][y] = 1
        
    infect_all()
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    
    res = max(res, cnt)
    
    for x, y in room_locations:
        arr[x][y] = 0


print(res)