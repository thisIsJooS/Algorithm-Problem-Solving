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
    x, c = input().split()
    info.append((int(x), c))
    
    
def turn(direction, c):
    if c == 'D':
        direction = (direction+1)%4
    else:
        direction = (direction-1)%4
        
    return direction
    
    
x, y = 1, 1
q = deque()
q.append((x, y))
time = 0
direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    for i in info:
        if time == i[0]:
            direction = turn(direction, i[1])
            break
    
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if nx<1 or ny<1 or nx>n or ny>n or board[nx][ny]==1:
        time += 1 
        break
    
    if board[nx][ny] != 2:
        a, b = q.popleft()
        board[a][b] = 0
    
    x, y = nx, ny
    q.append((x, y))
    board[x][y] = 1
    time += 1
    
print(time)