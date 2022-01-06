N, S = map(int, input().split())
data = list(map(int, input().split()))

end = 0
interval_sum = 0
answer = 1e9

for start in range(N):
    while interval_sum < S and end < N:
        interval_sum += data[end]
        end += 1
    
    if interval_sum >= S:
        answer = min(answer, end-start)


    interval_sum -= data[start]
    
print(answer if answer != 1e9 else 0)
        
    