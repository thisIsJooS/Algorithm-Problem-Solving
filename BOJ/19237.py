from collections import deque

N, M, K = map(int, input().split()) # arr행 개수, 상어의 개수, 냄새가 사라지기까지 시간
arr = [[None]*N for _ in range(N)]
shark_info = [None] * (M+1)
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] != 0:
            shark_info[data[j]] = [i, j]
    
direction_input = [0] + list(map(int, input().split()))
for i in range(1, M+1):
    shark_info[i].append(direction_input[i])

# 1번 상어의 상태가 UP일때 우선순위 리스트 : priority[1][1]
priority = [[] for _ in range(M+1)]
for i in range(1, M+1):    
    priority[i].append([])
    for j in range(4):
        priority[i].append(list(map(int, input().split())))
        
# shark_info
# None
# [0, 0, 4]
# [3, 3, 3]

def shark_move(arr, shark_info):
    next_pos_list = deque()
    for i in range(1, M+1):
        if shark_info[i] is None:
            continue

        shark_x, shark_y, shark_dir = shark_info[i]
        next_x, next_y, next_direction = next_pos(arr, i, shark_x, shark_y, shark_dir)
        
        next_pos_list.append((i, next_x, next_y, next_direction))    # (상어번호, 다음 x좌표, 다음 y좌표, 다음 방향)
        
    while next_pos_list:
        # 같은 칸에 오면 번호가 큰 상어가 먹히기
        i, next_x, next_y, next_direction = next_pos_list.popleft()
        for n, x, y, d in list(next_pos_list):
            if x == next_x and y == next_y:
                if i < n:
                    next_pos_list.remove((n, x, y, d))
                    shark_x, shark_y, shark_dir = shark_info[n]
                    arr[shark_x][shark_y][2] = False
                    shark_info[n] = None
        
        shark_x, shark_y, shark_dir = shark_info[i]
        
        # 그 칸에 냄새가 없으면
        if arr[next_x][next_y] == None:
            arr[next_x][next_y] = [i, K+1, True]
            arr[shark_x][shark_y][2] = False
            shark_info[i] = [next_x, next_y, next_direction]
            continue
        
        
        # 그 자리에 상어는 없고 냄새만 있으면
        arr[next_x][next_y] = [i, K+1, True]
        arr[shark_x][shark_y][2] = False
        shark_info[i] = [next_x, next_y, next_direction]
        
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                arr[i][j][1] -= 1
                if arr[i][j][1] == 0:
                    arr[i][j] = None


# priority
# []
# [[], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]
# [[], [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]

# UP = 1
# DOWN = 2
# LEFT = 3
# RIGHT = 4
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def next_pos(arr, shark_num, now_x, now_y, now_direction):
    # 인접한 칸중 아무 냄새가 없는 칸의 방향을 잡음
    for direction in priority[shark_num][now_direction]:
        nx = now_x + dx[direction]
        ny = now_y + dy[direction]
        
        if not (0<=nx<N and 0<=ny<N):
            continue
            
        if arr[nx][ny] is None:
            return nx, ny, direction
    
    
    # 인접한 칸 전부다 냄새가 있으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
    for direction in priority[shark_num][now_direction]:
        nx = now_x + dx[direction]
        ny = now_y + dy[direction]
        
        if not (0<=nx<N and 0<=ny<N):
            continue
            
        if arr[nx][ny][0] == shark_num:
            return nx, ny, direction

            
def shark_check(shark_info):
    for i in range(2, len(shark_info)):
        if shark_info[i] != None:
            return False
    return True
    

time = 0
for i in range(1, M+1):
    if shark_info[i] is None:
        continue
    shark_x, shark_y, shark_dir = shark_info[i]
    arr[shark_x][shark_y] = [i, K, True]    # [상어번호, 남은 시간, 현재 상어 존재 여부]
    
while True:
    if time >= 1000:
        print(-1)
        break
    
    shark_move(arr, shark_info)
    time += 1
    
    if shark_check(shark_info):
        print(time)
        break