import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
board = [[0]*101 for _ in range(101)]
def main():
    t = int(input())
    for _ in range(t):
        src_x, src_y, d, g = map(int, input().split())
        dst_x, dst_y = src_x+dx[d], src_y+dy[d]
        arr = [(src_x, src_y), (dst_x, dst_y)]
        for _ in range(g):
            arr = rotate(arr)
        draw(arr)
        

def rotate(arr):
    x, y = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        a, b = arr[i]
        arr.append((x+y-b, -x+y+a))
        
    return arr


def draw(arr):
    for (x, y) in arr:
        board[x][y] = 1
        

def solve(arr):
    ans = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
                ans += 1
    
    print(ans)
    
main()
solve(board)            
        