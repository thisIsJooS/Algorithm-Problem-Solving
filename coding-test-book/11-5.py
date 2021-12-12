# 315p [볼링공 고르기]

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

count = [0] * (max(data)+1)
for x in data:
    count[x] += 1
    

res = 0
for i in range(len(count)):
    n -= count[i]
    res += count[i] * n

print(res)

# 입력예시 1
# 5 3 
# 1 3 2 3 2

# 출력예시 1
# 8

# 입력예시 2
# 8 5
# 1 5 4 3 2 4 5 2

# 출력예시 2
# 25