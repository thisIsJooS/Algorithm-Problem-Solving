N = int(input())

ret = 0
for i in range(1, N+1):
    ret += i*(N//i)
    
print(ret)