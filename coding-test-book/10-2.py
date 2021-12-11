# 298p [팀 결성]

n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
parent = [i for i in range(n+1)]

for _ in range(m):
    opr, a, b = map(int, input().split())
    if opr == 0:
        union_parent(parent, a, b)
    
    elif opr == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES", end = ' ')
        else:
            print("NO", end = ' ')
            
            
            
# 입력예시 1
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1


# 출력예시 1
# NO NO YES