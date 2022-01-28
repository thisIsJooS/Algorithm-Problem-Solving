N, M, C = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))
    
R = list(map(int, input().split()))

def f1(arr):
    arr.reverse()
    return arr
    

def f2(arr):
    N, M = len(arr), len(arr[0])
    tmp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmp[i][j] = arr[i][M-1-j]
            
    return tmp
    
    
def f3(arr):
    N, M = len(arr), len(arr[0])
    tmp = [[0]*N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            tmp[j][N-1-i] = arr[i][j]
            
    return tmp
    

def f4(arr):
    N, M = len(arr), len(arr[0])
    tmp = [[0]*N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            tmp[M-1-j][i] = arr[i][j]
            
    return tmp
    
    
def f5(arr):
    n = len(arr)//2
    m = len(arr[0])//2
    
    g1 = arr[:n]
    for i in range(len(g1)):
        g1[i] = g1[i][:m]
        
    g2 = arr[:n]
    for i in range(len(g2)):
        g2[i] = g2[i][m:]
        
    g3 = arr[n:]
    for i in range(len(g3)):
        g3[i] = g3[i][m:]
        
    g4 = arr[n:]
    for i in range(len(g4)):
        g4[i] = g4[i][:m]
    
    for i in range(len(g4)):
        g4[i] += g1[i]
        g3[i] += g2[i]
        
    arr = g4 + g3
    
    return arr


def f6(arr):
    n = len(arr)//2
    m = len(arr[0])//2
    
    g1 = arr[:n]
    for i in range(len(g1)):
        g1[i] = g1[i][:m]
        
    g2 = arr[:n]
    for i in range(len(g2)):
        g2[i] = g2[i][m:]
        
    g3 = arr[n:]
    for i in range(len(g3)):
        g3[i] = g3[i][m:]
        
    g4 = arr[n:]
    for i in range(len(g4)):
        g4[i] = g4[i][:m]
        
    for i in range(len(g4)):
        g2[i] += g3[i]
        g1[i] += g4[i]
        
    arr = g2 + g1
        
    return arr

        
for r in R:
    if r==1:
        arr = f1(arr)
    elif r==2:
        arr = f2(arr)
    elif r==3:
        arr = f3(arr)
    elif r==4:
        arr = f4(arr)
    elif r==5:
        arr = f5(arr)
    else:
        arr = f6(arr)
    
for a in arr:
    print(*a)