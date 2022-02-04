import sys

n = int(input())
data = list(input())
arr = [[None]*n for _ in range(n)]
k = 0
for i in range(n):
    for j in range(i, n):
        arr[i][j] = data[k]
        k+=1
        
sol = []
def solve(i):
    if i == n:
        print(*sol)
        sys.exit()
        return
    
    if arr[i][i] == '-':
        cand = [j for j in range(-10, 0)]
    elif arr[i][i] == '+':
        cand = [j for j in range(1, 11)]
    elif arr[i][i] == '0':
        cand = [0]
        
    for k in cand:
        sol.append(k)
        isOK = True
        
        for j in range(i+1):
            _sum = sum(sol[j:i+1])
            if _sum <= 0 and arr[j][i] == '+':
                isOK = False
                break  
            elif _sum >= 0 and arr[j][i] == '-':
                isOK = False
                break
            elif _sum != 0 and arr[j][i] == '0':
                isOK = False
                break
                
        if isOK:
            solve(i+1)        
        
        sol.pop()

            
solve(0)