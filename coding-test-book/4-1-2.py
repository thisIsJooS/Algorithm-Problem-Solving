# 113p [시각]

import sys

input = sys.stdin.readline

n = int(input())
cnt = 0 

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            data = str(h)+str(m)+str(s)
            
            if '3' in data:
                cnt += 1
                
print(cnt)



# 입력예시 1
# 5

# 출력예시 1
# 11475
