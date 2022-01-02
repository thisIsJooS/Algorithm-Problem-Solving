import heapq

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))


res = 0
while q:
    if len(q) == 1:
        break
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    c = a+b
    res += c
    heapq.heappush(q, c)
    
print(res)