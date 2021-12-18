# 351p [감시 피하기]
# https://www.acmicpc.net/problem/18428

from itertools import combinations

n = int(input())
g = []
coord_x, coord_t = [], []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    g.append(list(input().split()))
    for j in range(n):
        if g[i][j] == 'X':
            coord_x.append((i, j))
        elif g[i][j] == 'T':
            coord_t.append((i, j))
            

def solution():
    for cand in combinations(coord_x, 3):
        for i, j in cand:       # 이따 되돌려야됨
            g[i][j] = 'O'
        
        if not isPossible():    # 걸렸으면
            for i, j in cand:
                g[i][j] = 'X'
            continue
        
        else:    # 안 걸렸으면
            return True
    
    return False
        
        
def isPossible():
    for x, y in coord_t:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while 0<=nx<n and 0<=ny<n:
                if g[nx][ny] == 'O':
                    break
                elif g[nx][ny] == 'S':               
                    return False
                
                nx += dx[i]
                ny += dy[i]
                
    return True

print('YES' if solution() else 'NO')



# 입력예시 1
# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X

# 출력예시 1
# YES

# 입력예시 2
# 4
# S S S T
# X X X X
# X X X X
# T T T X

# 출력예시 2
# NO