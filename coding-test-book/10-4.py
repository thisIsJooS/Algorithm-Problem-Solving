# 303p [커리큘럼]

from collections import deque
import copy

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0] * (n+1)


for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for d in data[1:-1]:
        graph[d].append(i)
        indegree[i] += 1



def topology_sort():
    res = copy.deepcopy(time)
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()

        for j in graph[now]:
            indegree[j] -= 1
            res[j] = max(res[j], res[now] + time[j])
            if indegree[j] == 0:
                q.append(j)
    
    print(res[1:])
    
    
topology_sort()             


# 입력예시 1
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1


# 출력예시 1
# 10 20 14 18 17

