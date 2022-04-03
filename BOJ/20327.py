def oper1(arr, l):
    n = len(arr)
    s = 2**l
    for x in range(0, n, s):
        for y in range(0, n, s):
            tmp = []
            for i in range(s):
                row = []
                for j in range(s):
                    row.append(arr[x+i][y+j])
                tmp.append(row)
            
            tmp = reverseTopDown(tmp)
            for i in range(s):
                for j in range(s):
                    arr[x+i][y+j] = tmp[i][j]
    return arr

def oper2(arr, l):
    n = len(arr)
    s = 2**l
    for x in range(0, n, s):
        for y in range(0, n, s):
            tmp = []
            for i in range(s):
                row = []
                for j in range(s):
                    row.append(arr[x+i][y+j])
                tmp.append(row)
            
            tmp = reverseLeftRight(tmp)
            for i in range(s):
                for j in range(s):
                    arr[x+i][y+j] = tmp[i][j]
    return arr

def oper3(arr, l):
    n = len(arr)
    s = 2**l
    for x in range(0, n, s):
        for y in range(0, n, s):
            tmp = []
            for i in range(s):
                row = []
                for j in range(s):
                    row.append(arr[x+i][y+j])
                tmp.append(row)
            
            tmp = rotateRight(tmp)
            for i in range(s):
                for j in range(s):
                    arr[x+i][y+j] = tmp[i][j]
    return arr

def oper4(arr, l):
    n = len(arr)
    s = 2**l
    for x in range(0, n, s):
        for y in range(0, n, s):
            tmp = []
            for i in range(s):
                row = []
                for j in range(s):
                    row.append(arr[x+i][y+j])
                tmp.append(row)
            
            tmp = rotateLeft(tmp)
            for i in range(s):
                for j in range(s):
                    arr[x+i][y+j] = tmp[i][j]
    return arr

def oper5(arr, l):
    n = len(arr)
    new_arr = [[0]*n for _ in range(n)]
    s = 2**l

    for x in range(0, n, s):
        for y in range(0, n, s):
            tmp = []
            for i in range(s):
                row = []
                for j in range(s):
                    row.append(arr[x+i][y+j])
                tmp.append(row)
            
            for i in range(s):
                for j in range(s):
                    new_arr[n-s-x+i][y+j] = tmp[i][j]

    return new_arr

def oper6(arr, l):
    n = len(arr)
    new_arr = [[0]*n for _ in range(n)]
    s = 2**l

    for x in range(0, n, s):
        for y in range(0, n, s):
            tmp = []
            for i in range(s):
                row = []
                for j in range(s):
                    row.append(arr[x+i][y+j])
                tmp.append(row)
            
            for i in range(s):
                for j in range(s):
                    new_arr[x+i][n-s-y+j] = tmp[i][j]

    return new_arr

def oper7(arr, l):
    n = len(arr)
    new_arr = [[0]*n for _ in range(n)]
    s = 2**l

    for x in range(0, n, s):
        for y in range(0, n, s):
            tmp = []
            for i in range(s):
                row = []
                for j in range(s):
                    row.append(arr[x+i][y+j])
                tmp.append(row)
            
            for i in range(s):
                for j in range(s):
                    new_arr[i+y][n-s-x+j] = tmp[i][j]

    return new_arr


def oper8(arr, l):
    n = len(arr)
    new_arr = [[0]*n for _ in range(n)]
    s = 2**l

    for x in range(0, n, s):
        for y in range(0, n, s):
            tmp = []
            for i in range(s):
                row = []
                for j in range(s):
                    row.append(arr[x+i][y+j])
                tmp.append(row)
            
            for i in range(s):
                for j in range(s):
                    new_arr[i+n-s-y][j+x] = tmp[i][j]

    return new_arr

        
def reverseTopDown(arr):
    n = len(arr)
    m = len(arr[0])
    tmp = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            tmp[i][j] = arr[n-i-1][j]
    
    return tmp

def reverseLeftRight(arr):
    n = len(arr)
    m = len(arr[0])
    tmp = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            tmp[i][j] = arr[i][m-1-j]
    
    return tmp

def rotateRight(arr):
    n, m = len(arr), len(arr[0])    # 행, 열
    
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = arr[i][j]
            
    return result


def rotateLeft(arr):
    n, m = len(arr), len(arr[0])    # 행, 열
    
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m-1-j][i] = arr[i][j]
            
    return result



def main():
    N, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(2**N)]
    
    for _ in range(R):
        k, l = map(int, input().split())
        if k==1:
            arr = oper1(arr, l)
        elif k==2:
            arr = oper2(arr, l)
        elif k==3:
            arr = oper3(arr, l)
        elif k==4:
            arr = oper4(arr, l)
        elif k==5:
            arr = oper5(arr, l)
        elif k==6:
            arr = oper6(arr, l)
        elif k==7:
            arr = oper7(arr, l)
        elif k==8:
            arr = oper8(arr, l)
        
    for a in arr:
        print(*a)

main()