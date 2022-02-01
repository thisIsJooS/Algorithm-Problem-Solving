from collections import deque
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())

q = deque()
dp = [[INF]*(n+2) for _ in range(n//2+2)]
# clipboard, screen, time
q.append((0, 1, 0))
dp[0][1] = 0


while q:
    clip, screen, time = q.popleft()
    
    # screen to clipboard
    try:
        if screen > 0 and dp[screen][screen] > time+1:
            dp[screen][screen] = time+1
            q.append((screen, screen, time+1))
    except:
        pass
    
    # clipboard to screen
    try:
        if clip > 0 and dp[clip][clip+screen] > time+1:
            dp[clip][clip+screen] = time+1
            q.append((clip, clip+screen, time+1))
    except:
        pass
    
    # delete one element in screen
    try:
        if screen > 0 and dp[clip][screen-1] > time+1:
            dp[clip][screen-1] = time+1
            q.append((clip, screen-1, time+1))
    except:
        pass


ans = INF
for i in range(len(dp)):
    ans = min(ans, dp[i][n])

print(ans)