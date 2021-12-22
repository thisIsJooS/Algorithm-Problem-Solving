# 377p [퇴사] - 삼성전자 SW 역량테스트
# https://www.acmicpc.net/problem/14501

n = int(input())
T, P = [], []
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
M = 0
def dfs(day=0, p=0):
    global M
    
    if day > n:
        return 
    
    if day == n:
        M = max(M, p)
        return 
    
    M = max(M, p)
    
    dfs(day+T[day], p+P[day])
    dfs(day+1, p)
    
dfs()
print(M)