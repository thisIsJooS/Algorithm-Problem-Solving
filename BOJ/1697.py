from collections import deque

a, b = map(int, input().split())

q = deque()
q.append((a, 0))
SIZE = 100001
arr = [0] * (SIZE+1)
arr[a] = 1

def f(q):
    if a==b:
        return 0
    
    if a>b:
        return a-b
    
    while q:
        now, cnt = q.popleft()

        # x-1
        next_pos = now-1
        if 0<= next_pos <= SIZE:
            if next_pos == b:
                return cnt+1
            if arr[next_pos] == 0:
                q.append((next_pos, cnt+1))
                arr[next_pos] = cnt+1


        # x+1
        next_pos = now+1
        if 0<= next_pos <= SIZE:
            if next_pos == b:
                return cnt+1
            if arr[next_pos] == 0:
                q.append((next_pos, cnt+1))
                arr[next_pos] = cnt+1       

        # x*2
        next_pos = now*2
        if 0 <= next_pos <= SIZE:
            if next_pos == b:
                return cnt+1
            if arr[next_pos] == 0:
                q.append((next_pos, cnt+1))
                arr[next_pos] = cnt+1


print(f(q))