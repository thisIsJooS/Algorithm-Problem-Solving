# 332p [치킨 배달] - 삼성전자 SW 역량테스트
# https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
arr = []
chicken = []    # 치킨집 좌표를 담을 배열
house = []      # 집 좌표를 담을 배열

for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
    
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i, j))
        elif arr[i][j] == 1:
            house.append((i, j))
            
            
candidates = list(combinations(chicken, m))


# 좌표 x,y의 치킨거리
def get_chicken_distance(x, y, chicken):
    min_distance = INF
    for c in chicken:
        i, j = c
        val = abs(x-i) + abs(y-j)
        min_distance = min(min_distance, val)
        
    return min_distance


res = INF
for comb in candidates:
    # comb : ( (0, 1), (3, 0) )
    val = 0
    for i, j in house:
        val += get_chicken_distance(i, j, comb)
    
    res = min(res, val)
    
print(res)



# 입력예시 1
# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

# 출력예시 1
# 5

# 입력예시 2
# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2
 
# 출력예시 2
# 10


# 입력예시 3
# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0

# 출력예시 3
# 11