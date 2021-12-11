# 311p [모험가 길드]

n = int(input())
data = list(map(int, input().split()))
data.sort()


count = 0
result = 0
for d in data:
    count += 1
    if count >= d:
        result += 1
        count = 0 
        
print(result)


# 입력예시 1
# 5
# 2 3 1 2 2

# 출력예시 1
# 2