# 182p [두 배열의 원소 교체]

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)
cnt = 0

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    

        
print(sum(a))


# 입력예시 1
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

# 출력예시 1
# 26
