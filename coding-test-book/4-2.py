# 115p [왕실의 나이트]

import sys

input = sys.stdin.readline

data = list(input().rstrip())

steps = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

row, col =  int(data[1]), int(ord(data[0])) - int(ord('a'))

cnt = 0

for s in steps:
    new_row = row + s[0]
    new_col = col + s[1]
    
    if 0<new_row<9 and 0<new_col<9:
        cnt += 1
        
print(cnt)



# 입력예시 1
# a1

# 출력예시 1
# 2