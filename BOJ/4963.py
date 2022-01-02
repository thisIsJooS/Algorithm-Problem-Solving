# 149p [음료수 얼려 먹기]

from collections import deque
import sys

input = sys.stdin.readline

while True:

    m, n = map(int, input().split())

    if m==0 and n==0:
        break
    
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))


    cnt = 0

    def count(i, j):
        global cnt

        q = deque()
        q.append((i, j))
        graph[i][j] = 0

        while q:
            i, j = q.popleft()
            adj = get_adj(i, j)

            for n_i, n_j in adj:
                if graph[n_i][n_j] == 1:
                    graph[n_i][n_j] = 0
                    q.append((n_i, n_j))

        cnt += 1


    def get_adj(x, y):
        arr = []
        dx = [0, 0, 1, -1, 1, 1, -1, -1]
        dy = [1, -1, 0, 0, 1, -1, 1, -1]

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 1:
                    arr.append((nx, ny))

        return arr


    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count(i, j)

    print(cnt)