import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

ans = [0]*(n+1)
stack = [arr[1]]
def f():
    if n==1:
        return ans
    
    for i in range(2, n+1):
        if arr[i-1] > arr[i]:
            ans[i] = i-1
            stack.append(arr[i])
            
        else:
            while stack:
                p = stack.pop()
                if p < arr[i]:
                    continue
                
                else:
                    ans[i] = arr.index(p)
                    stack.append(p)
                    stack.append(arr[i])
                    break
            
            if not stack:
                stack.append(arr[i])
                ans[i] = 0
    
    return ans


ans = f()
if ans.count(0) == len(ans):
    print(0)
else:
    print(*ans[1:])