# 262p [전보]

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    


def dijkstra(start):
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
                
dijkstra(c)


# 도달할 수 있는 노드의 개수
cnt = 0
for i in range(len(distance)):
    if 0 < distance[i] < INF:
        cnt += 1
    
    else:
        distance[i] = -1


print(a, max(distance))


# 입력예시 1
# 3 2 1
# 1 2 4
# 1 3 2


# 출력예시 1
# 2 4
