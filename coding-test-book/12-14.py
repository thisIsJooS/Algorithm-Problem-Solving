# 335p [외벽 점검] - 2020 카카오 신입 공채 1차
# https://programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 원형을 선형으로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    
    # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    answer = len(dist) + 1
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count-1]
            for index in range(start, start+length):
                # 취약 지점이 더 있으면 '그 지점으로부터' 새로운 친구 투입
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
                    
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1
    
    return answer