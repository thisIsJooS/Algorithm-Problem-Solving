# 223p [바닥 공사]

n = int(input())

d = [0] * (n+1)

d[1], d[2] = 1, 3

for i in range(3, n+1):
    d[i] = 2*d[i-2] + d[i-1]
    
print(d[n])

# 입력예시 1
# 3

# 출력예시 1
# 5