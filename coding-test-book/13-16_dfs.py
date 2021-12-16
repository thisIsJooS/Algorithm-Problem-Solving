# 341p [연구소] - 삼성전자 SW 역량테스트
# https://www.acmicpc.net/problem/14502

from itertools import combinations

n, m = map(int, input().split())
arr = []
room_locations = []
virus_locations = []
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
        

# 주어진 맵에 대하여 전부 감염시킨다 - dfs
def infect(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 0:
            arr[nx][ny] = 2
            infect(nx, ny)

        
for candidate in list(combinations(room_locations, 3)):
    cnt = 0 
    # 3개를 골라 벽을 세운다
    for x, y in candidate:
        arr[x][y] = 1
    
    # 기존 바이러스 위치에서 dfs로 감염시킨다
    for x, y in virus_locations:
        infect(x, y)
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    
    res = max(res, cnt)
    
    # 처음 배열로 복귀시킨다
    for x, y in room_locations:
        arr[x][y] = 0


print(res)

