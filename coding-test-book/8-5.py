# 226p [효율적인 화폐 구성]

n, m = map(int, input().split())

# n개의 화폐 단위 정보를 입력 받기
arr = []
for _ in range(n):
    arr.append(int(input()))

    
# 한 번 계사노딘 결과를 저장하기 위한 dp테이블 초기화
INF = int(1e9)
d = [0] + [INF] * m
for a in arr:
    if a <= m:
        d[a] = 1
        

# dynamic programming 진행(보텀업)
for i in range(1, m+1):
    # 해당 인덱스에서 각 화폐단위만큼 차이나는 인덱스에 해당하는 값들을 tmp 배열에 저장
    tmp = []
    for a in arr:
        if i > a:
            tmp.append(d[i-a])
    
    
    if len(tmp) != 0:
        d[i] = min(d[i], min(tmp)+1)


if d[m] >= INF:
    print(-1)
else:
    print(d[m])
    

    
# 입력예시 1
# 3 4
# 3
# 5
# 7

# 출력예시 1
# -1

# 입력예시 2
# 2 15
# 2
# 3

# 출력예시 2
# 5
