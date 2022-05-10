from collections import deque

def main():
    n, m = map(int, input().split())
    board = [[i, i] for i in range(101)]
    for _ in range(n+m):
        x, y = map(int, input().split())
        board[x] = [x, y]
    visited = [False] * 101
    
    q = deque([(1, 0)])
    while q:
        now, cnt = q.popleft()
        if now == 100:
            print(cnt)
            return
        
        for dice in range(1, 7):
            next = now + dice
            if next > 100: continue
            
            next = board[next][1]
            if visited[next]: continue
            
            visited[next] = True
            q.append((next, cnt+1))


main()