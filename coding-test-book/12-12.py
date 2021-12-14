# 329p [기둥과 보 설치] - 2020 카카오 신입 공채
# https://programmers.co.kr/learn/courses/30/lessons/60061

def possible(x, y, a, q):
    if a == 0: # 기둥
        if y==0:
            return True
        if [x-1, y, 1] in q:
            return True
        if [x, y, 1] in q:
            return True
        if [x, y-1, 0] in q:
            return True

    else:     # 보
        if [x, y-1, 0] in q:
            return True
        if [x+1, y-1, 0] in q:
            return True
        if [x-1, y, 1] in q and [x+1, y, 1] in q:
            return True
        
    return False
        
    
def solution(n, build_frame):
    answer = []

    for data in build_frame:
        x, y, a, b = data
        
        if b == 1:     # 설치
            if possible(x, y, a, answer):
                answer.append([x, y, a])
            
        elif b == 0:     # 삭제
            if [x, y, a] in answer:
                answer.remove([x, y, a])
            
            for data in answer:
                _x, _y, _a = data
                if not possible(_x, _y, _a, answer):
                    answer.append([x, y, a])
                    break

    return sorted(answer)