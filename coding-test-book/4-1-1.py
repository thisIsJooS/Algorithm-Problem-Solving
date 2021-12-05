# 110p [상하좌우]

import sys

input = sys.stdin.readline

n = int(input())
data = list(input().split())

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 1, 1

for d in data:
    i = move_types.index(d)
    x += dx[i]
    y += dy[i]
    
    if x < 1:
        x = 1
    
    if x > n:
        x = n
    
    if y < 1:
        y = 1
    
    if y > n:
        y = n
        
print(x, y)


# 입력예시 1
# 5
# R R R U D D

# 출력예시 1
# 3 4