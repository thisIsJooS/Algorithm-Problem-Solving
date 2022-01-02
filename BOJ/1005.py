import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    dGraph = [[] for __ in range(n+1)]
    inDeg = [0] * (n+1)
    cost = [0] + list(map(int, sys.stdin.readline().split()))
    costSoFar = [0] * (n+1)
    q = deque()
    
    for __ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        inDeg[b] += 1
        dGraph[a].append(b)
        
    
    for i in range(1, n+1):
        if inDeg[i] == 0:
            q.append(i)
            costSoFar[i] = cost[i]
            
    
    while q:
        now = q.popleft()
        for i in dGraph[now]:
            inDeg[i] -= 1
            costSoFar[i] = max(costSoFar[i], costSoFar[now] + cost[i])
            if inDeg[i] == 0:
                q.append(i)
                
    ans = int(sys.stdin.readline())
    print(costSoFar[ans])