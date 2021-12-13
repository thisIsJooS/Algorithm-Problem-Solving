# 325p [자물쇠와 열쇠] - 2020 카카오 신입 공채
# https://programmers.co.kr/learn/courses/30/lessons/60059

import copy

# 2차원 리스트 90도 회전
def rotate(arr):
    n = len(arr)
    ret = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = arr[i][j]
    
    return ret


# 자물쇠의 중간 부분이 모두 1인지 확인
def isAllOne(arr):
    n = len(arr) // 3
    
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if arr[i][j] != 1:
                return False
            
    return True
                

def solution(key, lock):
    n, m = len(lock), len(key)
    
    #자물쇠의 크기를 기존의 3배로 변환
    arr = [[0]*(3*n) for _ in range(3*n)]
    
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            arr[i+n][j+n] = lock[i][j]
    
    
    for i in range(2*n):
        for j in range(2*n):
            # 4가지 방향에 대하여 확인
            for _ in range(4):
                key = rotate(key)    # 열쇠 회전
                # 자물쇠에 열쇠를 끼워 넣기
                for x in range(m):
                    for y in range(m):
                        arr[x+i][y+j] += key[x][y]
                
                # 새로운 자물쇠에 열쇠가 정확히 들어 맞는지 검사
                if isAllOne(arr):
                    return True
                
                # 자물쇠에 열쇠를 다시 빼기
                for x in range(m):
                    for y in range(m):
                        arr[x+i][y+j] -= key[x][y]
                
                
    return False


