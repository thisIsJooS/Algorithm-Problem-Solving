n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
def f(arr):
    start = 0
    end_row = n-1
    end_col = m-1
    
    tmp = [[0]*m for _ in range(n)]
    
    while start < end_row and start < end_col:
        #ㅜ
        for i in range(start, end_row):
            tmp[i+1][start] = arr[i][start]
        
        #ㅏ
        for i in range(start, end_col):
            tmp[end_row][i+1] = arr[end_row][i]
        
        #ㅗ
        for i in range(end_row, start, -1):
            tmp[i-1][end_col] = arr[i][end_col] 
        
        #ㅓ
        for i in range(end_col, start, -1):
            tmp[start][i-1] = arr[start][i]
            
        start += 1
        end_row -= 1
        end_col -= 1
        
    return tmp


for _ in range(k):
    arr = f(arr)
    
for a in arr:
    print(*a)