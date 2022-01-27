N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

def dfs(graph, v, arr, visited):
    if len(arr)==5:
        return True
    
    for w in graph[v]:
        if w not in visited:
            ret = dfs(graph, w, arr+[w], visited+[w])
            if ret:
                return True
            
    return False


def f():
    for i in range(N):
        ret = dfs(graph, i, [i], [i])
        if ret:
            return True
        
    return False

ans = f()
print(1 if ans else 0)