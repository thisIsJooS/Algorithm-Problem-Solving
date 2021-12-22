# 382p [편집거리] - Goldman Sachs 인터뷰

a = input()
b = input()

arr = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(len(a)+1):
    for j in range(len(b)+1):
        if i==0:
            arr[i][j] = j
            continue
        if j==0:
            arr[i][j] = i
            continue
            
        if a[i-1] == b[j-1]:
            arr[i][j] = arr[i-1][j-1]
        else:
            arr[i][j] = min(arr[i-1][j-1], arr[i][j-1], arr[i-1][j]) + 1

print(arr[len(a)][len(b)])

