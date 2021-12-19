# 361p [실패율] - 2019 카카오 신입 공채 1차
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    n = len(stages)
    rates = []
    for i in range(1, N+1):    # 스테이지 1부터 N 까지
        c = stages.count(i)
        if n==0:
            rate = 0
        else:
            rate = c/n
            n -= c
        rates.append((rate, i))
    
    rates.sort(key = lambda e : e[0], reverse=True)
    rates = [i[1] for i in rates]
    
    return rates


# 입출력 예시 :
    
# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4,4,4,4,4]))

# [3, 4, 2, 1, 5]
# [4, 1, 2, 3]