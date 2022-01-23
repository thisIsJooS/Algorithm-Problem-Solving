import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
    
min_gap = 1e9
nums = [i for i in range(N)]
cnt = 0
combination = list(combinations(nums, N//2))
for team1 in combination:
    if cnt >= len(combination)//2:
        break
    cnt += 1
        
    team2 = [n for n in nums if n not in team1]
    
    score1, score2 = 0, 0
    
    for comb in combinations(team1, 2):
        i, j = comb
        score1 += arr[i][j] + arr[j][i]
    
    for comb in combinations(team2, 2):
        i, j = comb
        score2 += arr[i][j] + arr[j][i]
    
    gap = abs(score1 - score2)
    min_gap = min(gap, min_gap)
    
print(min_gap)
  
    
    
# 입력예시 1
# 4
# 0 1 2 3
# 4 0 5 6
# 7 1 0 2
# 3 4 5 0

# 출력예시 1
# 0