# 353p [인구 이동]
# https://www.acmicpc.net/problem/16234

from collections import deque

n, l, r = map(int, input().split())
g = []
cnt = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    g.append(list(map(int, input().split())))
    
def completed():
    for i in range(n):
        for j in range(n):
            if j != n-1:
                gap = abs(g[i][j] - g[i][j+1])
                if l <= gap <= r:
                    return False
            if i != n-1:
                gap = abs(g[i][j] - g[i+1][j])
                if l <= gap <= r:
                    return False
    return True


while not completed():
    cnt += 1
    union_num = 1
    union_map = [[0]*n for _ in range(n)]
    
    for _i in range(n):
        for _j in range(n):
            if union_map[_i][_j] == 0:
                q = deque([(_i, _j)])
                union = deque([(_i, _j)])
                union_count = 1
                union_people = g[_i][_j]
                union_map[_i][_j] = union_num
                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0<=nx<n and 0<=ny<n and union_map[nx][ny]==0 and l<=abs(g[nx][ny]-g[x][y])<=r:
                            union_map[nx][ny] = union_num
                            union_count += 1
                            union_people += g[nx][ny]
                            q.append((nx, ny))
                            union.append((nx, ny))

                for x, y in union:
                    g[x][y] = union_people // union_count
                    
            union_num += 1

print(cnt)