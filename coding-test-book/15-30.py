# 370p [가사 검색] - 2020 카카오 신입 공채 1차
# https://programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    
    new_words = [[] for _ in range(10001)]
    reversed_words = [[] for _ in range(10001)]
    for w in words:
        new_words[len(w)].append(w)
        reversed_words[len(w)].append(w[::-1])
    
    for i in range(10001):
        new_words[i].sort()
        reversed_words[i].sort()
    
    
    for q in queries:
        length = len(q)
        if q[0] != '?':
            left = bisect_left(new_words[length], q.replace('?', 'a'))
            right = bisect_right(new_words[length], q.replace('?', 'z'))
            
            answer.append(right-left)
        
        else:
            q = q[::-1]
            left = bisect_left(reversed_words[length], q.replace('?', 'a'))
            right = bisect_right(reversed_words[length], q.replace('?', 'z'))
            
            answer.append(right-left)
    
    
    return answer


a = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
print(a)