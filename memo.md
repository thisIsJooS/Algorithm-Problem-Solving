* n <= 1,000 이면 시간복잡도 O(N^2) 가능 , 시간제한이 5초라면 O(N^3)도 가능

<hr>

* 2차원 배열 속 원소에 이렇게 접근도 가능하다.
<code>

    arr= [[1, 0, 0], [2, 3, 4]]

    for a in arr:
        x, y, z = a
        print(x, y, z)
    
</code>

* 배열을 입력받는 동시에 특정 원소 존재 여부를 체크하면 더 간결해진다.
<code>

    for i in range(n):
        data = list(map(int, input().split()))
        arr.append(data)
    
        for j in range(n):
            if arr[i][j] == 2:
                arr1.append((i, j))
            elif arr[i][j] == 1:
                arr2.append((i, j))
</code>