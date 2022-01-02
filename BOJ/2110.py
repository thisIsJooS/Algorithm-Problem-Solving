n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

min_gap = 1
max_gap = arr[-1]-arr[0]
answer = 0
while min_gap <= max_gap:
    gap = (min_gap+max_gap)//2
    cnt = 1
    val = arr[0]
    
    for i in range(n):
        if arr[i] >= val+gap: 
            cnt += 1
            val = arr[i]
    
    if cnt >= c:    # c개 이상의 공유기를 설치할 수 있다
        min_gap = gap+1
        answer = gap
    else:            # c개 이상의 공유기는 설치할 수 없다
        max_gap = gap-1

print(answer)