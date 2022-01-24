N = int(input())
arr = list(map(int, input().split()))

def f(arr):
    for i in range(N-1, 0, -1):
        if arr[i-1] < arr[i]:
            x = i-1
            y = i
            
            for j in range(N-1, y-1, -1):
                if arr[x] < arr[j]:
                    arr[x], arr[j] = arr[j], arr[x]
                    break
                    
            arr = arr[:y] + sorted(arr[y:])
            
            return arr
    
    return -1

arr = f(arr)
if arr == -1:
    print(arr)
else:
    print(*arr)
    
    
# 입력예시 1
# 4
# 1 2 3 4

# 출력예시 1
# 1 2 4 3 