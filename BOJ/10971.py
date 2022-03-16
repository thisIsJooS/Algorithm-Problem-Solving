from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
arr = [i for i in range(n)]

ans = 1e9
for p in permutations(arr, n):
    val = 0
    for i in range(n):
        if graph[p[i]][p[(i+1)%n]] == 0:
            val += 1e9
        else:
            val += graph[p[i]][p[(i+1)%n]]

    ans = min(ans, val)

print(ans)