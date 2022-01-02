n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n - 1), [False]*(2*n - 1)

def solve(j):
    global ans
    if j == n:
        ans += 1
        return
    
    for i in range(n):
        if not (a[i] or b[i+j] or c[j-i+n-1]):
            a[i] = b[i+j] = c[j-i+n-1] = True
            solve(j+1)
            a[i] = b[i+j] = c[j-i+n-1] = False
            
            
solve(0)
print(ans)