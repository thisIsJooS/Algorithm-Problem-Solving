import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dice = [0]*7
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def solve():
    global dice, x, y
    for c in command:
        nx, ny = x+dx[c], y+dy[c]
        if not (0<=nx<n and 0<=ny<m):
            continue
            
        if c==1:
            dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
        elif c==2:
            dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
        elif c==3:
            dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]
        elif c==4:
            dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]
            
            
        if board[nx][ny] == 0:
            board[nx][ny] = dice[6]
        else:
            dice[6] = board[nx][ny]
            board[nx][ny] = 0
        x, y = nx, ny
        
        print(dice[1])

solve()