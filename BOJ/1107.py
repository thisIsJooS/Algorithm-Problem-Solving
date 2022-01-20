import sys
input = sys.stdin.readline

def check(n):
    n = str(n)
    for i in n:
        if i in arr:
            return False
    return True

now = 100
target = int(input())
k = int(input())
if k!=0:
    arr = list(input().rstrip().split())

    answer = abs(100-target)
    for i in range(1000001):
        if check(i):
            answer = min(answer, len(str(i)) + abs(i-target))

    print(answer)
    
else:
    print(min(abs(100-target), len(str(target))))