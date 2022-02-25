from collections import deque

def main():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    q = deque()
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append((i, j, 0))
                
    while q:
        x, y, day = q.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            nday = day+1
            
            if not (0<=nx<n and 0<=ny<m):
                continue
                
            if arr[nx][ny] == 0:
                arr[nx][ny] = 1
                q.append((nx, ny, nday))
                
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return -1
            
    return day

print(main())

