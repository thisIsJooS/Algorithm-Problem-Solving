# 399p [최종 순위] - NWERC 2010
# https://www.acmicpc.net/problem/3665

from collections import deque

def who_is_higher(graph, a, b):
    if b in graph[a]:
        return b, a
    elif a in graph[b]:
        return a, b

    
def check(graph):
    inDeg = [0] * (N+1)
    inDeg[0] = -1
    for i in range(1, N+1):
        for j in graph[i]:
            inDeg[j] += 1
            
    q = deque()
    for i in range(1, N+1):
        if inDeg[i] == 0:
            q.append(i)

    certain = True
    cycle = False
    
    for _ in range(N):
        if len(q) == 0:
            cycle = True
            break
        
        if len(q) >= 2:
            certain = False
            break
        
        now = q.popleft()
        
        for j in graph[now]:
            inDeg[j] -= 1
            if inDeg[j] == 0:
                q.append(j)

    
    if cycle:
        return 2
    elif not certain:
        return 1
    else:
        return 0
    
    
for _ in range(int(input())):
    N = int(input())
    rank = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for i in range(N):
        for j in range(i):
            graph[rank[i]].append(rank[j])
    
    
    M = int(input())
    changed = []
    for _ in range(M):
        a, b = map(int, input().split())
        a, b = who_is_higher(graph, a, b)
        changed.append((a, b))

    for e in changed:
        a, b = e
        graph[b].remove(a)
        graph[a].append(b)
    
    
    T = check(graph)

    if T == 1:
        print('?')
    elif T == 2:
        print("IMPOSSIBLE")
    else:
        for i in range(1, N+1):
            rank[len(graph[i])] = i

        for r in rank:
            print(r, end = ' ')
        print()