n = int(input())
data = [list(input())[::-1] for _ in range(n)]
dic = dict()
answer = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] not in dic:
            dic[data[i][j]] = 0
        dic[data[i][j]] += 10**j


arr = sorted(dic.items(), key = lambda x: x[1], reverse=True)
for i in range(len(arr)):
    answer += arr[i][1] * (9-i)

print(answer)

# data
# ['F', 'C', 'G']
# ['B', 'E', 'D', 'C', 'A']

# dic
# {'F': 1, 'C': 1010, 'G': 100, 'B': 1, 'E': 10, 'D': 100, 'A': 10000}