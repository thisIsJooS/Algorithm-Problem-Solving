# 349p [연산자 끼워 넣기] - 삼성전자 SW 역량 테스트 
# https://www.acmicpc.net/problem/14888

from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
# +, -, x, //의 개수
opers_count = list(map(int, input().split()))
opers = []
for i in range(4):
    for j in range(opers_count[i]):
        opers.append(i)
        
        
def calc(a, op, b):
    if op == 0:
        return a+b
    
    elif op == 1:
        return a-b
    
    elif op == 2:
        return a*b
        
    elif op == 3:
        return int(a/b)
        
        
min_val, max_val = int(1e9), -int(1e9)
for oper in list(permutations(opers, len(opers))):
    res = arr[0]
    for i in range(n-1):
        res = calc(res, oper[i], arr[i+1])
    
    max_val = max(max_val, res)
    min_val = min(min_val, res)
    
    
print(max_val)
print(min_val)




# 입력예시 1
# 2
# 5 6
# 0 0 1 0

# 출력예시 1
# 30
# 30

# 입력예시 2
# 3
# 3 4 5
# 1 0 1 0

# 출력예시 2
# 35
# 17

# 입력예시 3
# 6
# 1 2 3 4 5 6
# 2 1 1 1

# 출력예시 3
# 54
# -24