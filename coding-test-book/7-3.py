# 201p [떡볶이 떡 만들기]
# 0 < n < 1,000,000 이기 때문에 이진탐색을 이용해야 함

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for a in arr:
        if a > mid:
            total += a - mid
    
    
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid -1
    
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        start = mid + 1
        result = mid    # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록

print(result)


# 입력예시 1
# 4 6
# 19 15 10 17


# 출력예시 1
# 15