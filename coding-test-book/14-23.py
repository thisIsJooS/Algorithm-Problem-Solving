# 359p [국영수]
# https://www.acmicpc.net/problem/10825

from operator import itemgetter

n = int(input())
data = []
for _ in range(n):
    name, kor, eng, math = input().split()
    data.append([int(kor), int(eng), int(math), name])


for key, reverse in ((3, False), (2, True), (1, False), (0, True)):
    data.sort(key = itemgetter(key), reverse = reverse)


for d in data:
    print(d[3])
    
    
# 입력예시 1
# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90

# 출력예시 1
# Donghyuk
# Sangkeun
# Sunyoung
# nsj
# Wonseob
# Sanghyun
# Sei
# Kangsoo
# Haebin
# Junkyu
# Soong
# Taewhan