from bisect import bisect_left, bisect_right

n = int(input())

data = list(map(int, input().split()))
data.sort()
input()
cand = list(map(int, input().split()))
    
for c in cand:
    left = bisect_left(data, c)
    right = bisect_right(data, c)
    
    if left == right:
        print(0)
    else:
        print(1)
    
    
    # left 와 right의 걊이 같으면 없는거임
