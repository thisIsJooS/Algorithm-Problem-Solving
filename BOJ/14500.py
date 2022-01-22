import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [None for _ in range(20)]
dy = [None for _ in range(20)]

dx[1] = [0, 0, 0, 0]
dy[1] = [0, 1, 2, 3]

dx[2] = [0, 1, 2, 3]
dy[2] = [0, 0, 0, 0]

dx[3] = [0, 0, 1, 1]
dy[3] = [0, 1, 0, 1]

dx[4] = [0, 1, 2, 2]
dy[4] = [0, 0, 0, 1]

dx[5] = [0, 1, 0, 0]
dy[5] = [0, 0, 1, 2]

dx[6] = [0, 0, 1, 2]
dy[6] = [0, 1, 1, 1]

dx[7] = [0, 1, 1, 1]
dy[7] = [0, 0, -1, -2]

dx[8] = [0, 1, 2, 2]
dy[8] = [0, 0, 0, -1]

dx[9] = [0, 1, 1, 1]
dy[9] = [0, 0, 1, 2]

dx[10] = [0, 0, 1, 2]
dy[10] = [0, 1, 0, 0]

dx[11] = [0, 0, 0, 1]
dy[11] = [0, 1, 2, 2]

dx[12] = [0, 1, 1, 2]
dy[12] = [0, 0, 1, 1]

dx[13] = [0, 0, 1, 1]
dy[13] = [0, 1, 0, -1]

dx[14] = [0, 1, 1, 2]
dy[14] = [0, 0, -1, -1]

dx[15] = [0, 0, 1, 1]
dy[15] = [0, 1, 1, 2]

dx[16] = [0, 0, 0, 1]
dy[16] = [0, 1, 2, 1]

dx[17] = [0, 1, 2, 1]
dy[17] = [0, 0, 0, -1]

dx[18] = [0, 1, 1, 1]
dy[18] = [0, -1, 0, 1]

dx[19] = [0, 1, 2, 1]
dy[19] = [0, 0, 0, 1]


answer = 0
for k in range(1, 20):
    for x in range(n):
        for y in range(m):
            total = 0
            valid = True
            
            for i in range(4):
                nx = x + dx[k][i]
                ny = y + dy[k][i]
                
                if not (0<=nx<n and 0<=ny<m):
                    valid = False
                    break
                
                total += arr[nx][ny]
                
            if valid:
                answer = max(answer, total)
                
print(answer)




# 입력예시 1
# 5 5
# 1 2 3 4 5
# 5 4 3 2 1
# 2 3 4 5 6
# 6 5 4 3 2
# 1 2 1 2 1

# 출력예시 1
# 19