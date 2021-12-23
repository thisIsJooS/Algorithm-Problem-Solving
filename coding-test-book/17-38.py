# 386p [정확한 순위] 

from collections import deque

n, m = map(int, input().split())
arr_h = [[] for _ in range(n+1)]
arr_l = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr_h[a].append(b)
    arr_l[b].append(a)

cnt = 0
for i in range(1, n+1):
    lower, higher = 0, 0
    
    # get higher
    q = deque()
    visited = [False] * (n+1)
    for h in arr_h[i]:
        q.append(h)
        visited[h] = True
    higher += len(arr_h[i])
    while q:
        now = q.popleft()
        for h in arr_h[now]:
            if not visited[h]:
                q.append(h)
                visited[h] = True
                higher += 1
    
    # get lower
    q = deque()
    visited = [False] * (n+1)
    for h in arr_l[i]:
        q.append(h)
        visited[h] = True
    lower += len(arr_l[i])
    
    while q:
        now = q.popleft()
        for h in arr_l[now]:
            if not visited[h]:
                q.append(h)
                visited[h] = True
                lower += 1

    if higher+lower == n-1:
        cnt += 1

print(cnt)
