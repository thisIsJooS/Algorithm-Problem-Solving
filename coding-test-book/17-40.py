# 390p [숨바꼭질] - USACO

import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance = [INF] * (n+1)
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
            
        for e in graph[now]:
            cost = dist + e[1]
            if cost < distance[e[0]]:
                distance[e[0]] = cost
                heapq.heappush(q, (cost, e[0]))
    
    
dijkstra(1)
distance[0] = 0
print(distance.index(max(distance)), max(distance), distance.count(max(distance)))
    

# 입력예시 1
# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2


# 출력예시 1
# 4 2 3