# 99p [1이 될 때까지]

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 0

while n >= k:
    if n % k == 0:
        n //= k
        cnt += 1
    
    else:
        n -= 1
        cnt += 1
        
        
# 일일이 1씩 뺄 경우 n이 큰 수 일경우 상당히 오래 걸릴 것이다.
cnt += (n-1)
        
print(cnt)


# 입력예시 1
# 25 5

# 출력예시 1
# 2