# 316p [무지의 먹방 라이브] - 2019 카카오 신입 공채
# https://programmers.co.kr/learn/courses/30/lessons/42891

import heapq

def solution(food_times, k):
    n = len(food_times)
    
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 heapq를 사용
    q = []
    for i in range(n):
        # (음식시간, 음식번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))
        
    time = 0    # 먹기 위해 사용한 시간
    prev = 0    # 직전에 다 먹은 음식 시간
    
    while time + (q[0][0]-prev)*n <= k:
        now = heapq.heappop(q)[0]
        time += (now-prev)*n
        n -= 1    # 다 먹은 음식 제외
        prev = now    # 이전 음식 시간 재설정
    
    # 음식의 번호 기준으로 정렬
    q.sort(key = lambda x : x[1])
        
    return q[(k-time)%n][1]