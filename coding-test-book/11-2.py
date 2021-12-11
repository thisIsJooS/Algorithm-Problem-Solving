# 312p [곱하기 혹은 더하기]

data = input()
res = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    
    if num <= 1 or res <= 1:
        res += num
    
    else:
        res *= num
        
print(res)


# 입력예시 1
# 02984

# 출력예시 1
# 576

# 입력예시 2
# 567

# 출력예시 2
# 210