import copy

data = [[0] * 12]
for _ in range(10):
    data.append([0] + list(map(int, list(input()))) + [0])
data.append([0]*12)

ndata = [[0]*12 for _ in range(12)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def f():
    vertex = []
    for x in range(1, 11):
        for y in range(1, 11):
            if data[x][y] == 1:
                cnt = 0
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if data[nx][ny]==0:
                        cnt += 1
                if cnt==3:
                    vertex.append((x, y))

    if len(vertex) == 3:
        pass
    
    elif len(vertex) == 2:
        v1, v2 = vertex
        x1, y1 = v1
        x2, y2 = v2
        
        if data[x1][y2]==1:
            vertex.append((x1, y2))
        
        elif data[x2][y1]==1:
            vertex.append((x2, y1))
        
        else:
            return None
        
    else:
        return None
    
    vertex.sort()
    
    if not isOk(vertex):
        return None
    
    tri_type = triangle_type(vertex)
    v1, v2, v3 = vertex
    x1, y1 = v1
    x2, y2 = v2
    x3, y3 = v3
    
    if tri_type == 1:
        for i in range(x1, x3+1):
            for j in range(x3+1-i):
                ndata[i][y1+j] = 1
        
    elif tri_type == 2:
        for i in range(x1, x3+1):
            for j in range(x3+1-i):
                ndata[i][y2-j] = 1

    elif tri_type == 3:
        for i in range(x1, x3+1):
            for j in range(i-x1+1):
                ndata[i][y1+j] = 1

        
    elif tri_type == 4:
        for i in range(x1, x3+1):
            for j in range(i-x1+1):
                ndata[i][y1-j] = 1
        
        
    elif tri_type == 5:
        for i in range(x1, x2+1):
            for j in range(i-x1+1):
                ndata[i][y1-j] = 1
        
        for i in range(x2, x3+1):
            for j in range(x3+1-i):
                ndata[i][y1-j] = 1

                
    elif tri_type == 6:
        for i in range(x1, x2+1):
            for j in range(i-x1+1):
                ndata[i][y1+j] = 1
        
        for i in range(x2, x3+1):
            for j in range(x3+1-i):
                ndata[i][y1+j] = 1
        
        
    elif tri_type == 7:
        for i in range(x1, x3+1):
            for j in range(i-x1+1):
                ndata[i][y1-j] = 1
        
        for i in range(x1, x3+1):
            for j in range(i-x1+1):
                ndata[i][y1+j] = 1
        
    elif tri_type == 8:
        for i in range(x1, x3+1):
            for j in range(x3+1-i):
                ndata[i][y3-j] = 1
        
        for i in range(x1, x3+1):
            for j in range(x3+1-i):
                ndata[i][y3+j] = 1
    
    
    if isEqual(data, ndata):
        return vertex
    else:
        return None

    
def isOk(vertex):
    v1, v2, v3 = vertex
    x1, y1 = v1
    x2, y2 = v2
    x3, y3 = v3
    
    a = (x1-x2)**2 + (y1-y2)**2
    b = (x1-x3)**2 + (y1-y3)**2
    c = (x2-x3)**2 + (y2-y3)**2
    

    a, b, c = sorted([a, b, c])

    if a==b and a+b == c:
        return True
    
    return False
    
    
def triangle_type(vertex):
    v1, v2, v3 = vertex
    x1, y1 = v1
    x2, y2 = v2
    x3, y3 = v3
    
    if x1==x2 and y1==y3:
        return 1
    elif x1==x2 and y2==y3:
        return 2
    elif y1==y2 and x2==x3:
        return 3
    elif y1==y3 and x2==x3:
        return 4
    elif y1==y3 and y2<y1:
        return 5
    elif y1==y3 and y2>y1:
        return 6
    elif x2==x3:
        return 7
    elif x1==x2:
        return 8
    
    
def isEqual(a, b):
    for i in range(1, 11):
        for j in range(1, 11):
            if a[i][j] != b[i][j]:
                return False
            
    return True


vertex = f()
if vertex:
    for v in vertex:
        print(*v)
        
else:
    print(0)