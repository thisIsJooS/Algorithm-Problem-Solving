# 355p [블록 이동하기] - 2020 카카오 신입 공채 1차
# https://programmers.co.kr/learn/courses/30/lessons/60063
# get_next_pos() 함수에서 회전을 구현하는 코드

from collections import deque

def solution(board):
    n = len(board)
    
    # 주어진 맵을 변형하여 외곽에 벽을 둔다. 이렇게 하면 맵을 벗어나지 않는지, 그 범위 판정을 더 간단히 할 수 있다.
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            new_board[i][j] = board[i-1][j-1]
            
    q = deque()
    visited = []
    now = {(1, 1), (1, 2)}
    q.append((now, 0))
    visited.append(now)
    
    while q:
        pos, cost = q.popleft()
        
        for p in list(pos):
            x, y = p
            if x==n and y==n:
                return cost
        
        # 방문하지 않았다면 q에 append 하자마자 visited에도 append
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)
        
    return 0


def get_next_pos(pos, board):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    next_pos = []    # 반환 결과
    pos = list(pos)    # set 자료형인 현재 위치 정보를 list형으로 변환
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    
    # 상, 하, 좌, 우 // board를 전처리할 것이기 때문에 맵을 벗어나는 경우는 고려하지 않아도 된다.
    for i in range(4):
        pos1_next_x, pos1_next_y = pos1_x + dx[i], pos1_y + dy[i]
        pos2_next_x, pos2_next_y = pos2_x + dx[i], pos2_y + dy[i]
        
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    
    # 회전
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x+i, pos2_y), (pos2_x, pos2_y)})
                
    # 회전
    if pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                next_pos.append({(pos1_x, pos1_y+i), (pos1_x, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
    
    return next_pos