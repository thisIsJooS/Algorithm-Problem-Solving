from itertools import *
import sys

input = sys.stdin.readline

n = int(input())
table = []
ans = int(1e9)
arr = [i for i in range(1, n+1)]

for _ in range(n):
    table.append(list(map(int, input().split())))

for i in range(1, n//2+1):
    for teamA in combinations(arr, i):    
        sA, sB = 0, 0
        teamB = [i for i in arr if i not in teamA]
        
        for pair in permutations(teamA, 2):
            sA += table[pair[0]-1][pair[1]-1]
            
        for pair in permutations(teamB, 2):
            sB += table[pair[0]-1][pair[1]-1]
            
        gap = abs(sA-sB)
        ans = min(ans, gap)
        
print(ans)
        