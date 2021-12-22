# 381p [못생긴 수] - Google 인터뷰

k = int(input())
arr =  []

def dfs(n):
    if n<=5:
        return True
    
    if n%2==0:
        if dfs(n//2): return True
    elif n%3==0:
        if dfs(n//3): return True
    elif n%5==0:
        if dfs(n//5): return True
    
    else:
        return False
    
i = 1
while len(arr) < k: 
    if dfs(i): 
        arr.append(i)
    i+=1

print(arr[k-1])