N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]

data.sort(key = lambda e:e[0])
data.sort(key = lambda e:e[1])


cnt = 0
start = 0

for d in data:
    if d[0] >= start:
        cnt += 1
        start = d[1]


print(cnt)