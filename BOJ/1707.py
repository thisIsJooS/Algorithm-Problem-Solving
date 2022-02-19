from collections import deque

def main():
    for _ in range(int(input())):
        V, E = map(int, input().split())
        graph = [[] for __ in range(V+1)]
        for ___ in range(E):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
            
        if isBipartite(graph):
            print('YES')
        else:
            print('NO')
            
            
def isBipartite(graph):
    vertices = len(graph)
    colors = [None] * vertices
    visited = [False] * vertices
    
    
    for i in range(1, vertices):
        q = deque()
        q.append(i)
    
        while q:
            now = q.popleft()
            if visited[now]:
                continue

            if colors[now] == None:
                colors[now] = 0

            now_color = colors[now]
            visited[now] = True

            for v in graph[now]:
                if colors[v] == now_color:
                    return False

                colors[v] = 1- now_color
                q.append(v)
        
    return True


main()


