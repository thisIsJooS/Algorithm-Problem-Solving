# 346p [괄호 변환] - 2020 카카오 신입 공채 1차 
# https://programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    answer= ''
    
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if p == '':
        return ''
    
    # 만약 p가 이미 "올바른 괄호 문자열" 이라면 그대로 return 하면 됩니다.
    if isRight(p):
        return p
    
    # 2. 문자열 p를 두 "균형잡힌 문자열" u, v로 분리합니다.
    u, v = divide(p)
    
    # 3-1. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 시작합니다.
    if isRight(u):
        return u + solution(v)
    
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        answer = '(' + solution(v) + ')'
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == '(':
                u = u[:i] + ')' + u[i+1:]
            else:
                u = u[:i] + '(' + u[i+1:] 
        answer += u
        
    return answer
                

def isRight(s):
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
            
    return True


def divide(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt == 0:
            return p[:i+1], p[i+1:]
            