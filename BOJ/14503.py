import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0
def clear(x, y):
    global ans
    arr[x][y] = 2
    ans += 1   
    
def left(d):
    return (d+3)%4


def isSafe(x, y):
    if not(0<=x<n and 0<=y<m):
        return False
    return True

def isWall(x, y):
    if arr[x][y] == 1:
        return True
    return False


def visited(x, y):
    if arr[x][y] == 2:
        return True
    return False

def main():
    global x, y, d
    clear(x, y)
    while True:
        possible = False
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not isSafe(nx, ny):
                continue
            if arr[nx][ny] == 0:
                possible = True
                break
            
        if not possible:
            nd = (d+2)%4
            x, y = x+dx[nd], y+dy[nd]
            if not isSafe(x, y) or isWall(x, y):
                return
            continue
        
        nd = left(d)
        nx, ny = x+dx[nd], y+dy[nd]
        if isSafe(nx, ny) and not isWall(nx, ny) and not visited(nx, ny):
            x, y, d = nx, ny, nd
            clear(x, y)
            continue
        
        d = nd
        
main()
print(ans)
        
            
        