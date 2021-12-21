s = input()
s = s.upper()
s = list(s)
s.sort()
arr= [0] * 26

for c in s:
    arr[ord(c)-ord('A')] += 1


if arr.count(max(arr)) > 1:
    print('?')
else:
    print(chr(arr.index(max(arr)) + ord('A')))