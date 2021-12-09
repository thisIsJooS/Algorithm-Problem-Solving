# 198p [부품 찾기]
# 0 < n < 1,000,000 이기 때문에 이진탐색을 이용해야 함


import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
targets = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return True
        
        elif arr[mid] > target:
            end = mid - 1
            
        else:
            start = mid + 1
        
    return False


for target in targets:
    if binary_search(arr, target, 0, len(arr)-1):
        print("yes")
    
    else:
        print("no")