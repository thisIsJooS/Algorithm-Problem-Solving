import sys
from collections import deque

def solve():
    for _ in range(int(input())):
        main()
        
        
def main():
    n = int(input())
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    
    arr = [[1e9]*n for _ in range(n)]
    arr[x][y] = 0
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if x==a and y==b:
            break
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if not isSafe(nx, ny, n):
                continue
            
            if arr[nx][ny] > arr[x][y]+1:
                arr[nx][ny] = arr[x][y]+1
                q.append((nx, ny))

            
    print(arr[a][b])
        
        
def isSafe(x, y, n):
    if not (0<=x<n and 0<=y<n):
        return False
    return True

solve()