from collections import deque
from operator import ne
import sys

input = sys.stdin.readline
SIZE = 100002
n, k = map(int, input().split())

def solve():
    if n >= k:
        return n-k

    dp = [-1] * SIZE
    dp[n] = 0
    
    q = deque()
    q.append((n, 0))

    while q:
        now, cnt = q.popleft()

        #x*2
        next_pos = now*2
        if 0<=next_pos<SIZE and dp[next_pos]<0:
            if next_pos == k:
                return cnt
            dp[next_pos] = cnt
            q.append((next_pos, cnt))
        
        #x-1
        next_pos = now-1
        if 0<=next_pos<SIZE and dp[next_pos]<0:
            if next_pos == k:
                return cnt+1
            dp[next_pos] = cnt+1
            q.append((next_pos, cnt+1))
        
        #x+1
        next_pos = now+1
        if 0<=next_pos<SIZE and dp[next_pos]<0:
            if next_pos == k:
                return cnt+1
            dp[next_pos] = cnt+1
            q.append((next_pos, cnt+1))
        

    
print(solve())
        