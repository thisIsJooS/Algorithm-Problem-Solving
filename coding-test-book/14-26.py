# 363p [카드 정렬하기] 
# https://www.acmicpc.net/problem/1715

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


# 입력예시 1
# 3
# 10
# 20
# 40

# 출력예시 1
# 100