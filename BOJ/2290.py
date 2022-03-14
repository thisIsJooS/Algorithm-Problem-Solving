import sys
input = sys.stdin.readline

s, data = input().strip().split()
s = int(s)
data = list(map(int, list(data)))

w = s+2
h = 2*s+3

arr = [[[' ']*(w) for _ in range(h)] for _ in range(10)]

for i in range(h):
    if i==0 or i==2*s+2:
        for j in range(w):
            if j!=0 and j!=w-1:
                arr[0][i][j] = '-'
    
    elif i!=s+1:
        arr[0][i][0] = '|'
        arr[0][i][s+1] = '|'

for i in range(h):
    if i==0 or i==s+1 or i==2*s+2:
        continue
    arr[1][i][s+1] = '|'


for i in range(h):
    if i==0 or i==s+1 or i==2*s+2:
        for j in range(w):
            if j!=0 and j!=w-1:
                arr[2][i][j] = '-'
    
    elif i < s+1:
        arr[2][i][s+1] = '|'
    else:
        arr[2][i][0] = '|'
        
for i in range(h):
    if i==0 or i==s+1 or i==2*s+2:
        for j in range(w):
            if j!=0 and j!=w-1:
                arr[2][i][j] = '-'
                arr[3][i][j] = '-'
                arr[5][i][j] = '-'
                arr[6][i][j] = '-'
                arr[8][i][j] = '-'
                arr[9][i][j] = '-'
    
    elif i < s+1:
        arr[2][i][s+1] = '|'
        arr[3][i][s+1] = '|'
        arr[5][i][0] = '|'
        arr[6][i][0] = '|'
        arr[8][i][0] = '|'
        arr[8][i][s+1] = '|'
        arr[9][i][0] = '|'
        arr[9][i][s+1] = '|'
    else:
        arr[2][i][0] = '|'
        arr[3][i][s+1] = '|'
        arr[5][i][s+1] = '|'
        arr[6][i][0] = '|'
        arr[6][i][s+1] = '|'
        arr[8][i][0] = '|'
        arr[8][i][s+1] = '|'
        arr[9][i][s+1] = '|'
    

for i in range(h):
    if i==0 or i==h-1:
        continue
    
    if i == s+1:
        for j in range(w):
            if j!=0 and j!=w-1:
                arr[4][i][j] = '-'
    
    elif i<s+1:
        arr[4][i][0] = '|'
        arr[4][i][s+1] = '|'
    
    else:
        arr[4][i][s+1] = '|'

for i in range(h):
    if i==0:
        for j in range(w):
            if j!=0 and j!=w-1:
                arr[7][i][j] = '-'
    
    elif i!=s+1 and i!=h-1:
        arr[7][i][s+1] = '|'


ans = [[' ']*(len(data)*w) for _ in range(h)]
for i in range(h):
    for j in range(len(ans[0])):
        ans[i][j] = arr[data[j//w]][i][j%w]
        

for i in range(len(ans)):
    for j in range(len(ans[0])-1, 0, -1):
        if j%w==0:
            ans[i] = ans[i][:j] + [' '] + ans[i][j:]

for i in range(len(ans)):
    for j in range(len(ans[0])):
        print(ans[i][j], end='')
    print()
    
    
# 5 12414134143
#           -----                                   -----                           ----- 
#        |       | |     |       | |     |       |       | |     |       | |     |       |
#        |       | |     |       | |     |       |       | |     |       | |     |       |
#        |       | |     |       | |     |       |       | |     |       | |     |       |
#        |       | |     |       | |     |       |       | |     |       | |     |       |
#        |       | |     |       | |     |       |       | |     |       | |     |       |
#           -----   -----           -----           -----   -----           -----   ----- 
#        | |             |       |       |       |       |       |       |       |       |
#        | |             |       |       |       |       |       |       |       |       |
#        | |             |       |       |       |       |       |       |       |       |
#        | |             |       |       |       |       |       |       |       |       |
#        | |             |       |       |       |       |       |       |       |       |
#           -----                                   -----                           ----- 