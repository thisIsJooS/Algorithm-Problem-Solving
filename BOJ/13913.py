from collections import deque

n, k = map(int, input().split())
SIZE = 100001
arr = [0] * SIZE
arr[n] = -1
def f():
    # n==k
    if n==k:
        return 0, []
    
    # k < n
    if k < n:
        return n-k, [i for i in range(n, k-1, -1)]
    
    
    q = deque()
    q.append((n, 0, [n]))
    
    while q:
        now, cnt, route = q.popleft()

        # x+1
        next = now+1
        if next == k:
            return cnt+1, route+[next]
        
        if next < SIZE and arr[next]==0:
            q.append((next, cnt+1, route+[next]))
            arr[next] = cnt+1
        
        # x-1
        next = now-1
        if next == k:
            return cnt+1, route+[next]
        
        if next >= 0 and arr[next] == 0:
            q.append((next, cnt+1, route+[next]))
            arr[next] = cnt+1
            
        # x*2
        next = now*2
        if next == k:
            return cnt+1, route+[next]
        
        if next < SIZE and arr[next]==0:
            q.append((next, cnt+1, route+[next]))
            arr[next] = cnt+1
            
            
cnt, route = f()
print(cnt)
if len(route)==0:
    print(n)
else:
    print(*route)