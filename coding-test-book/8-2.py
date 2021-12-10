# 217p [1로 만들기]

n = int(input())

d = [0] * (n+1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
        
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)
        
print(d[n])




# 입력예시 1
# 26


# 출력예시 1
# 3

# 입력예시 2
# 12345

# 출력예시 2
# 11
