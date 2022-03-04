import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def solve():
    global N, L
    ans = 0
    
    for k in range(N):
        arr = board[k]
        visited = [False]*N
        isOK = True
        for i in range(1, N):
            if arr[i] == arr[i-1]:
                continue
            
            if abs(arr[i-1] - arr[i]) != 1:
                isOK = False
                break
            
            if arr[i-1] < arr[i]:
                if L > i:
                    isOK = False
                    break
                
                for j in range(1, L+1):
                    if arr[i-j] != arr[i-1] or visited[i-j]:
                        isOK = False
                        break
                    visited[i-j] = True
            
            elif arr[i-1] > arr[i]:
                if L > N-i:
                    isOK = False
                    break
                
                for j in range(1, L+1):
                    if arr[i-1+j] != arr[i] or visited[i-1+j]:
                        isOK = False
                        break
                    visited[i-1+j] = True
            
        if isOK:
            ans += 1
            
    for y in range(N):
        arr = []
        for x in range(N):
            arr.append(board[x][y])
        visited = [False]*N
        isOK = True
        for i in range(1, N):
            if arr[i] == arr[i-1]:
                continue
            
            if abs(arr[i-1] - arr[i]) != 1:
                isOK = False
                break
            
            if arr[i-1] < arr[i]:
                if L > i:
                    isOK = False
                    break
                
                for j in range(1, L+1):
                    if arr[i-j] != arr[i-1] or visited[i-j]:
                        isOK = False
                        break
                    visited[i-j] = True
            
            elif arr[i-1] > arr[i]:
                if L > N-i:
                    isOK = False
                    break
                
                for j in range(1, L+1):
                    if arr[i-1+j] != arr[i] or visited[i-1+j]:
                        isOK = False
                        break
                    visited[i-1+j] = True
            
        if isOK:
            ans += 1
                
    print(ans)
    
solve()