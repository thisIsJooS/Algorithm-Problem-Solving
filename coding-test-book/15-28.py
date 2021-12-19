# 368p [고정점 찾기] - Amazon 인터뷰 


def binary_search(arr, low=0, high=None):
    if high is None:
        high = len(arr)
    
    while low < high:
        mid = (low+high)//2
        
        if arr[mid] == mid:
            print(mid)
            return
        
        elif arr[mid] > mid:
            high = mid
        
        else:
            low = mid+1
    
    print(-1)
    return 

n = int(input())
arr = list(map(int, input().split()))
binary_search(arr)


# 입력예시 1
# 5
# -15 -6 1 3 7

# 출력예시 1
# 3


# 입력예시 2
# 7
# -15 -4 2 8 9 13 15

# 출력예시 2
# 2


# 입력예시 3
# 7
# -15 -4 3 8 9 13 15


# 출력예시 3
# -1