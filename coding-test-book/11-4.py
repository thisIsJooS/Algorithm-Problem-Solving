# 314p [만들 수 없는 금액]

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1

for x in data:
    if target < x:
        break
    target += x
        
print(target)


# 입력예시 1
# 5 
# 3 2 1 1 9

# 출력예시 1
# 8

# 입력예시 2
# 3
# 3 5 7


# 출력예시 2
# 1
