n, k = map(int, input().split())

table = [[0]*(k+1) for _ in range(n+1)]
table[0] = [1 for _ in range(k+1)]

for i in range(n+1):
    table[i][1] = 1
    
for i in range(1, n+1):
    for j in range(2, k+1):
        val = 0
        for h in range(i+1):
            val += table[h][j-1]
        table[i][j] = val
        
print(table[n][k]%1000000000)
