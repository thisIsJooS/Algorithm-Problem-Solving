# Kruskal
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
        
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

plan = list(map(int, input().split()))
res = True
for i in range(1, m):
    if find_parent(parent, i) != find_parent(parent, i+1):
        res = False
        break

    
print("YES" if res else "NO")

# ==================================================================================
# Floyd

n, m = map(int, input().split())
graph = [[False]*(n+1)]
for _ in range(n):
    tmp = [False]
    for node in list(map(int, input().split())):
        if node == 0:
            tmp.append(False)
        else:
            tmp.append(True)
            
    graph.append(tmp)
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])
            
data = list(map(int, input().split()))
res = True
for i in range(1, m+1):
    if not graph[i][i+1]:
        res = False
        break
        
print("YES" if res else "NO")