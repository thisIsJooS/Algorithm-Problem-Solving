# 367p [정렬된 배열에서 특정 수의 개수 구하기] - Zoho 인터뷰 

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

left = bisect_left(arr, x)
right = bisect_right(arr, x)

answer = right-left
print(answer if right<n else -1)


# 입력예시 1
# 7 2
# 1 1 2 2 2 2 3

# 출력예시 1
# 4


# 입력예시 2
# 7 4
# 1 1 2 2 2 2 3

# 출력예시 2
# -1