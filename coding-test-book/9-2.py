# 259p [미래도시]
# n이 한정적이라면 플로이드 워셜 알고리즘을 사용해도 된다.  graph[1][k] + graph[k][x]

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]



for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))
    
x, k = map(int, input().split())


def dijkstra(start, target):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
            
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
                
    
    return distance[target]


res = dijkstra(1, k) + dijkstra(k, x)
if res >= INF:
    print(-1)
else:
    print(res)
    
    
    
    
# 입력예시 1
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# 출력예시 1
# 3

# 입력예시 2
# 4 2
# 1 3
# 2 4
# 3 4

# 출력예시 2
# -1