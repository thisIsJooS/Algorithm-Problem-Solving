# 149p [음료수 얼려 먹기]

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if not (0<=x<n and 0<=y<m):
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        
        return True
    
    return False

cnt = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1

print(cnt)
    
    
    
# 입력예시 1
# 4 5
# 00110
# 00011
# 11111
# 00000

# 출력예시 1
# 3

# 입력예시 2
# 6 6
# 000111
# 111011
# 100001
# 111111
# 001111
# 111101

# 출력예시 2
# 4

