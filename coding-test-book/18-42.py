# 395p [탑승구] - CCC
# https://www.acmicpc.net/problem/10775

import sys

G = int(input())
P = int(input())
planes = []
for _ in range(P):
    planes.append(int(input()))
    
parent = [i for i in range(G+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a>b:
        parent[a] = b
    else:
        parent[b] = a
        
for i in range(len(planes)):
    pa = find_parent(parent, planes[i])
    
    if pa == 0:
        print(i)
        sys.exit()

    union_parent(parent, pa, pa-1)

print(P)    