from collections import deque

import sys
input = sys.stdin.readline

K, N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t, h = map(int, input().split())
    graph[b].append((a, t, h))    # 노드 거리 두께
    graph[a].append((b, t, h))
start, end = map(int, input().split())


INF = int(1e9)
min_time = INF
dp = [[INF]*K for _ in range(N+1)]
dp[start][0] = 0

q = deque()
q.append((start, 0, 0, [start]))

 
while q:
    print(q)
    now, time, h, visited = q.popleft()
    
    for e in graph[now]:
        if e[0] not in visited:
            new_time = time+e[1]
            new_h = h+e[2]

            if new_h >= K:
                continue
                
            if e[0] == end:
                min_time = min(min_time, new_time)
                continue
                
            if new_time < dp[e[0]][new_h]:
                dp[e[0]][new_h] = new_time
                q.append((e[0], new_time, new_h, visited+[e[0]]))
            
    
print(min_time if min_time < INF else -1)