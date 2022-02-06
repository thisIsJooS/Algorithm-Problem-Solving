from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
lis = []
insert_pos = []

for i in range(n):
    if i==0:
        lis.append(arr[i])
        insert_pos.append(i)        
        continue
        
        
    if lis[-1] < arr[i]:
        insert_pos.append(len(lis))
        lis.append(arr[i])
        
    else:
        idx = bisect_left(lis, arr[i])
        insert_pos.append(idx)
        lis[idx] = arr[i]
        

ans = max(insert_pos)
print(ans+1)

lis = []
for i in range(n-1, -1, -1):
    if insert_pos[i] == ans:
        lis.append(arr[i])
        ans -= 1
        
while lis:
    print(lis.pop(), end=' ')
