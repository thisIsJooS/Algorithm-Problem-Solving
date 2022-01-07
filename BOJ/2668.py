N = int(input())
graph = [-1]
for i in range(1, N+1):
    graph.append(int(input()))
    

res = []

def dfs(v, start):
    visited[v] = True
    
    if not visited[graph[v]]:
        dfs(graph[v], start)
    
    if graph[v] == start:
        res.append(start)
        
        
for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i, i)
    
print(len(res))
print(*res, sep='\n')