import sys
from collections import deque
input = sys.stdin.readline


for _ in range(int(input())):
    error = False
    func = list(input().rstrip())
    n = int(input())
    arr_str = input().rstrip()
    arr_str = arr_str[1:-1]
    
    arr = deque()
    if arr_str != '':
        li = list(arr_str.split(','))
        for l in li:
            arr.append(l) 
    else:
        arr = []
    
    R = False
    D_cnt = 0
    for f in func:
        if R == False:
            if f == 'D':
                if len(arr) == 0:
                    error = True
                    break
                arr.popleft()
            elif f == 'R':
                R = True
        
        elif R == True:
            if f == 'D':
                D_cnt += 1
            elif f == 'R':
                R = False
                if D_cnt != 0:
                    for _ in range(D_cnt):
                        if len(arr) == 0:
                            error = True
                            break
                        arr.pop()
                D_cnt = 0
                
    if R == True:
        if D_cnt != 0:
            for _ in range(D_cnt):
                if len(arr) == 0:
                    error = True
                    break
                arr.pop()

    
    len_arr = len(arr)
    if error:
        print('error')
    else:
        s = '['
        if R == True:
            for i in range(len_arr-1, -1, -1):
                s += arr[i]
                s += ','
        else:
            for a in arr:
                s += a
                s += ','
        if len_arr != 0:
            s = s[:-1]
        s += ']'
        
        print(s)