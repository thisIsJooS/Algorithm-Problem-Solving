import sys
input = sys.stdin.readline

def rotate(arr, direction):
    if direction == 1: 
        return [arr[-1]] + arr[:-1]
    else:
        return arr[1:] + [arr[0]]

def solve():    
    n = int(input())
    gear = [0] + [list(map(int, list(input().rstrip()))) for _ in range(n)]
    
    
    for _ in range(int(input())):
        now, dir = map(int, input().split())
        tmp_now = now
        tmp_dir = dir
        
        prev = now - 1
        next = now + 1
        
        waiting = []
        waiting.append((now, dir))
        while 0 < prev:
            if gear[prev][2] == gear[now][6]:
                break
            
            waiting.append((prev, -dir))
            prev -= 1
            now -= 1
            dir = -dir

        now = tmp_now
        dir = tmp_dir
        while next <= n:
            if gear[now][2] == gear[next][6]:
                break
            
            waiting.append((next, -dir))
            next += 1
            now += 1
            dir = -dir

        while waiting:
            now, dir = waiting.pop()
            gear[now] = rotate(gear[now], dir)
        
    ans = 0
    for i in range(1, n+1):
        if gear[i][0] == 1:
            ans += 1 
            
    print(ans)

solve()

