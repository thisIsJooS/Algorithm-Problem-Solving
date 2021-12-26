# 398p [행성 터널] - COCI
# https://www.acmicpc.net/problem/2887

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
        
        
n = int(input())
planets = []
edges = []
parent = [i for i in range(n)]
res = 0

for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))

for k in [0, 1, 2]:
    planets.sort(key = lambda e : e[k])
    for i in range(n-1):
        x1, y1, z1, p_num1 = planets[i]
        x2, y2, z2, p_num2 = planets[i+1]
        dist = min(abs(x2-x1), abs(y2-y1), abs(z2-z1))
        edges.append((dist, p_num1, p_num2))
edges.sort()


for e in edges:
    dist, a, b = e
    
    if find_parent(parent, a)!=find_parent(parent, b):
        union_parent(parent, a, b)
        res += dist

print(res)