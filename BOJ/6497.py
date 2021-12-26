# 397p [어두운 길] - University of Uim Local Contest
# https://www.acmicpc.net/problem/6497

import heapq

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    N, M = map(int, input().split())
    
    if N == 0 and M == 0:
        break
        
    parent = [i for i in range(N+1)]
    edges = []
    total_cost = 0
    for _ in range(M):
        a, b, cost = map(int, input().split())
        total_cost += cost
        edges.append((cost, a, b))

    edges.sort()
    
    cost_mst = 0
    for e in edges:
        cost, a, b = e
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            cost_mst += cost


    print(total_cost - cost_mst)