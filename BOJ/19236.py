# https://www.acmicpc.net/problem/19236

import copy

EMPTY = -1

# 번호가 num인 물고기의 좌표를 찾는다. 없으면 (= 이미 먹혔으면) None을 return
def find_pos(arr, num):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == num:
                return (i, j)

    return None


# 물고기의 방향을 바꾼다.
def turn_left(direction):
    return (direction+1)%8


# 물고기의 이동 구현. now_x, now_
def fish_move(arr, shark_x, shark_y):
    for i in range(1, 17):
        pos = find_pos(arr, i)
        if pos == None:
            continue
            
        x, y = pos
        direction = arr[x][y][1]
        
        for _ in range(8):
            nx = x+dx[direction]
            ny = y+dy[direction]
            
            if not (0<=nx<4 and 0<=ny<4):
                direction = turn_left(direction)
                continue
            
            if nx==shark_x and ny==shark_y:
                direction = turn_left(direction)
                continue
            
            arr[x][y][1] = direction
            arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
            break
        
        
# 현재 상어가 이동할 수 있는 좌표들을 리스트로 반환한다.
def find_movable_pos(arr, shark_x, shark_y, direction):
    res = []
    
    for i in range(1, 4):
        nx, ny = shark_x+dx[direction]*i, shark_y+dy[direction]*i
        if not (0<=nx<4 and 0<=ny<4):
            continue
        
        if arr[nx][ny][0] == EMPTY:
            continue
        
        res.append((nx, ny))
        
    return res
    

def dfs(arr, total, shark_info):    # shark_info : (x, y, direction)
    global answer
    arr = copy.deepcopy(arr)
    
    shark_x, shark_y, direction = shark_info
    total += arr[shark_x][shark_y][0]
    arr[shark_x][shark_y][0] = EMPTY
    
    fish_move(arr, shark_x, shark_y)
    
    movable_pos = find_movable_pos(arr, shark_x, shark_y, direction)
    
    # 더 이상 이동할 수 있는 위치가 없다면 return
    if len(movable_pos) == 0:
        answer = max(answer, total)
        return
    
    for pos in movable_pos:
        nx, ny = pos
        info = (nx, ny, arr[nx][ny][1])
        dfs(arr, total, info)
        
    
arr = [[None]*4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = [data[2*j], data[2*j+1]-1]    # [물고기번호, 방향]

        
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0
dfs(arr, 0, (0, 0, arr[0][0][1]))
print(answer)
    
    