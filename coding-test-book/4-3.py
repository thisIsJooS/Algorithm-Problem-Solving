# 118p [게임 개발]

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

mark = [[0]*m for _ in range(n)]

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
mark[x][y] = 1
cnt = 1
turn_time = 0

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


while True:
    turn_left()
    
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if mark[nx][ny] == 0 and arr[nx][ny] == 0:
        x = nx
        y = ny
        mark[x][y] = 1
        cnt += 1
        turn_time = 0
        continue
        
    else:
        turn_time += 1
        
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        
        else:
            break
            
        
        turn_time = 0
        
        
print(cnt)


# 입력예시 1
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# 출력예시 1
# 2

# 입력예시 2
# 5 5
# 1 1 0
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 1 1
# 1 0 1 0 1
# 1 1 1 1 1

# 출력예시 2
# 5
