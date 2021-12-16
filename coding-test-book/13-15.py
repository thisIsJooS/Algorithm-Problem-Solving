# 339p [특정 거리의 도시 찾기]
# https://www.acmicpc.net/problem/18352

import sys
import heapq

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    
dist = [1e9] * (n+1)
    
def dijkstra(start):
    q = []    
    dist[start] = 0
        
    heapq.heappush(q, (0, start))
    
    while q:
        d, now = heapq.heappop(q)
        
        if  d > dist[now]:
            continue
            
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(x)

if k not in dist:
    print(-1)
else:
    for i in range(len(dist)):
        if dist[i] == k:
            print(i)
            
            
# 입력예시 1
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

# 출력예시 1
# 4

# 입력예시 2
# 4 3 2 1
# 1 2
# 1 3
# 1 4
 
# 출력예시 2
# -1


# 입력예시 3
# 4 4 1 1
# 1 2
# 1 3
# 2 3
# 2 4

# 출력예시 3
# 2
# 3
