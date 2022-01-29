import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
def f(arr, k):
    start = 0
    end_row = n-1
    end_col = m-1

    while start < end_row and start < end_col:
        for _ in range(k%(2*(end_row+end_col-2*start))):
            q = deque()
            for i in range(start, end_row):
                q.append(arr[i][start])
            for i in range(start, end_col):
                q.append(arr[end_row][i])
            for i in range(end_row, start, -1):
                q.append(arr[i][end_col])
            for i in range(end_col, start, -1):
                q.append(arr[start][i])
                 
            #ㅜ
            for i in range(start, end_row):
                arr[i+1][start] = q.popleft()

            #ㅏ
            for i in range(start, end_col):    
                arr[end_row][i+1] = q.popleft()
                
            #ㅗ
            for i in range(end_row, start, -1):
                arr[i-1][end_col] = q.popleft()

            #ㅓ
            for i in range(end_col, start, -1):
                arr[start][i-1] = q.popleft()
                        
        start += 1
        end_row -= 1
        end_col -= 1

    return arr

arr = f(arr, k)
    
for a in arr:
    print(*a)


