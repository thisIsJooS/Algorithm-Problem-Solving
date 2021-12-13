# 327p [뱀] - 삼성전자 SW 역량테스트
# https://www.acmicpc.net/problem/3190


from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 2
    
l = int(input())
info = []
for _ in range(l):
    a, b = input().split()
    info.append((int(a), b))
    

def turn(direction, c):
    if c == 'D':
        direction = (direction+1)%4

    else:
        direction = (direction-1)%4        

    return direction


time = 0
x, y = 1, 1
direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()
q.append((x, y))

while True:
    # 회전할 시간인 경우 회전 
    for i in info:
        if time == i[0]:
            direction = turn(direction, i[1])
            break
        
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 맵 범위 밖이거나, 뱀의 몸통이 있는 위치라면
    if nx<1 or nx>n or ny<1 or ny>n or board[nx][ny] == 1:
        time += 1
        break
    
    else:
        x, y = nx, ny
    
    # 사과가 없으면 꼬리자르기
    if board[x][y] != 2:
        a, b = q.popleft()
        board[a][b] = 0
    
    q.append((x, y))
    board[x][y] = 1
    time += 1


print(time)
    
    
    
    
# 입력예시 1
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# 출력예시 1
# 9

# 입력예시 2
# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L
 
# 출력예시 2
# 21


# 입력예시 3
# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L

# 출력예시 3
# 13