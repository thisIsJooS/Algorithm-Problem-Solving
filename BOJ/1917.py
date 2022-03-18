cubic = []
cubic.append([
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])

cubic.append([
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])

cubic.append([
    [0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])

cubic.append([
    [0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])

cubic.append([
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])

cubic.append([
    [0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])

cubic.append([
    [0, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])

cubic.append([
    [0, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])

cubic.append([
    [0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])

cubic.append([
    [1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])

cubic.append([
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])


def rotate(a):    # 시계방향 회전 
    n, m = len(a), len(a[0])    # 행, 열
    
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = a[i][j]
            
    return result

def reverse_lr(a):  # 좌우 반전
    n, m = len(a), len(a[0])
    
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = a[i][m-j-1]
    
    return result

def reverse_td(a):  # 상하 반전
    n, m = len(a), len(a[0])
    
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = a[n-i-1][j]
    
    return result

def solve():
    tmp = [list(map(int, input().split())) for _ in range(6)]
    arr = [[0] * 18 for _ in range(18)] # tmp를 가운데로 두고 감싸는 형태의 18*18 배열
    for i in range(6, 12):
        for j in range(6, 12):
            arr[i][j] = tmp[i-6][j-6]
    
    for cub in cubic:   # 가능한 모든 형태의 전개도에 대하여
        for _ in range(4):
            cub = rotate(cub)   # 90도 회전해보고
            if check(arr, cub):
                return True
            
            if check(arr, reverse_lr(cub)): # 좌우 반전도 해보고
                return True
            
            if check(arr, reverse_td(cub)): # 상하 반전도 해본다
                return True


def check(arr, cub):    # arr 안에 패턴이 일치하는게 있는지 검사함
    isOk = None
    for i in range(13):
        for j in range(13):
            isOk = True
            for x in range(6):
                if not isOk: 
                    break
                for y in range(6):
                    if arr[i+x][j+y] != cub[x][y]:
                        isOk = False
                        break
            if isOk: 
                return True
    return False
    
    
def main():
    for _ in range(3):
        if solve():
            print('yes')
        else:
            print('no')
            
main()