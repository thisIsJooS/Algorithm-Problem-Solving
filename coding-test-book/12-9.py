# 323p [문자열 압축] - 2020 카카오 신입 공채
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += (str(count)+prev) if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        
        compressed += str(count) + prev if count >= 2 else prev
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