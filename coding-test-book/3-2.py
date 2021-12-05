# 92p [큰 수의 법칙]

import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort(reverse = True)

first, second = arr[0], arr[1]
res = 0

for i in range(1, m+1):
    if i % (k+1) == 0:
        res += second
    else:
        res += first
        
print(res)


# # 입력 예시
# 5 8 3
# 2 4 5 4 6

# # 출력 예시
# 46
