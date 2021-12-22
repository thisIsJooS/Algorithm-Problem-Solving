# 375p [금광] - Flipkart 인터뷰

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [[] for _ in range(n)]
    data = list(map(int, input().split()))
    
    for i in range(len(data)):
        arr[i//m].append(data[i])
    
    new_arr = [[0]*m for _ in range(n+2)]
    for i in range(n):
        for j in range(m):
            new_arr[i+1][j] = arr[i][j]

    
    res = 0
    for j in range(1, m):
        for i in range(1, n+1):
            new_arr[i][j] += max(new_arr[i-1][j-1], new_arr[i][j-1], new_arr[i+1][j-1])
            
            if j==m-1:
                res = max(res, new_arr[i][j])

    print(res)
    

# 입력예시 1
# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

# 출력예시 1
# 19
# 16