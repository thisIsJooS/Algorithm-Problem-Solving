from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().split())

board = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
q.append((0, 0, 0))
ans = [[1e9]*m for _ in range(n)]
ans[0][0] = 0

def solve():
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if not (0<=nx<n and 0<=ny<m):
                continue
            
            if board[nx][ny] == 0 and ans[nx][ny] > cnt:
                q.append((nx, ny, cnt))
                ans[nx][ny] = cnt
            
            elif board[nx][ny] == 1 and ans[nx][ny] > cnt+1:
                q.append((nx, ny, cnt+1))
                ans[nx][ny] = cnt+1
                
    print(ans[n-1][m-1])
    
solve()
            