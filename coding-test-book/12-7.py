# 321p [럭키 스트레이트]

data = list(map(int, input()))

n = len(data)
mid = n // 2

left = data[:mid]
right = data[mid:]


if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
    
    
    

# 입력예시 1
# 123402

# 출력예시 1
# LUCKY

# 입력예시 2
# 7755


# 출력예시 2
# READY