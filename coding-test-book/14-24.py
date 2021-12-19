# 360p [안테나] - 2019 SW 마에스트로 입학 테스트
# https://www.acmicpc.net/problem/18310

n = int(input())
data = list(map(int, input().split()))
data.sort()
print(data[(n-1)//2])
 

# 입력예시 1
# 4
# 5 1 7 9

# 출력예시 1
# 5