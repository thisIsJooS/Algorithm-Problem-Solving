import heapq

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

INF = int(1e9)
def min_dist(start, end):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
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
    
    return distance[end]

a, b = map(int, input().split())
        
def f():
    r1 = min_dist(1, a) + min_dist(a, b) + min_dist(b, N)
    r2 = min_dist(1, b) + min_dist(b, a) + min_dist(a, N)
    
    ret = min(r1, r2)
        
    return ret if ret<INF else -1

print(f())
    
    

