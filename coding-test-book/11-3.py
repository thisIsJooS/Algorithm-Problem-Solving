# 312p [곱하기 혹은 더하기]

import math

data = list(map(int,input()))

cnt = 0

for i in range(1, len(data)):
    if data[i-1] != data[i]:
        cnt += 1
        

print(math.ceil(cnt/2))


# 입력예시 1
# 0001100

# 출력예시 1
# 1

# 입력예시 2
# 00000001


# 출력예시 2
# 1


# 입력예시 3
# 11001100110011000001

# 출력예시 3
# 4