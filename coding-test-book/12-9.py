# 323p [문자열 압축] - 2020 카카오 신입 공채
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    
    for step in range(1, len(s)//2+1):
        prev = s[:step]
        compressed = ""
        cnt = 1
        
        for j in range(step, len(s), step):
            now = s[j:j+step]
            if prev == now:
                cnt += 1
            
            else:
                compressed += str(cnt)+prev if cnt >=2 else prev
                prev = now
                cnt = 1
    
        compressed += str(cnt)+prev if cnt >=2 else prev
        answer = min(answer, len(compressed))
    
    return answer


s = input()
print(solution(s))


# 입력예시 1
# ababcdcdababcdcd

# 출력예시 1
# 7

# 입력예시 2
# abcabcabcabcdededededede


# 출력예시 2
# 14


# 입력예시 3
# xababcdcdababcdcd

# 출력예시 3
# 17