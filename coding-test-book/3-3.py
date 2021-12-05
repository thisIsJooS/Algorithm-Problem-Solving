# 96p [숫자 카드 게임]

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))
    
res = []

for i in range(n):
    res.append(min(arr[i]))
    
print(max(res))



# 입력예시 1
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 출력예시 1
# 2

# 입력예시 2
# 2 4
# 7 3 1 8
# 3 3 3 4

# 출력예시 2
# 3