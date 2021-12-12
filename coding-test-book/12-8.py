# 322p [문자열 재정렬]

data = input()

arr = []
val = 0

for d in data:
    if d.isalpha():
        arr.append(d)
    else:
        val += int(d)
        
arr.sort()
if val != 0:
    arr.append(str(val))
    
print(''.join(arr))


# 입력예시 1
# K1KA5CB7

# 출력예시 1
# ABCKK13

# 입력예시 2
# AJKDLSI412K4JSJ9D


# 출력예시 2
# ADDIJJJKKLSS20