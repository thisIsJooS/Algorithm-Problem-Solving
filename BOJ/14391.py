n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input()))))

ans = 0
for b in range(1<<m*n):
    _sum = 0
    # 가로 0  세로 1
    
    #가로방향
    for i in range(n):
        now = 0
        for j in range(m):
            k = i*m + j
            
            if b&(1<<k) == 0:
                now = now*10 + arr[i][j]
            else:
                _sum += now
                now = 0
                
        _sum += now
    
    # 세로 방향
    for j in range(m):
        now = 0
        for i in range(n):
            k = i*m + j
            
            if b&(1<<k) != 0:
                now = now*10 + arr[i][j]
            else:
                _sum += now
                now = 0
            
        _sum += now
        
    ans = max(ans, _sum)
    
    
print(ans)