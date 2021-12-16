* n <= 1,000 이면 시간복잡도 O(N^2) 가능 , 시간제한이 5초라면 O(N^3)도 가능

* 원형으로 나열된 데이터를 처리하는 경우에는, 문제풀이를 간단히 하기 위하여 길이를 2배로 늘려서 원형을 일자로 만드는 방법이 있다. 혹은 첫 원소와 끝 원소가 붙어있는 경우와 떨어져 있는 경우 두가지로 나누어서 풀이하는 방법도 있다.

* 2차원 배열에서 상하좌우를 확인해야 할 경우에는 dx, dy 배열을 이용하자. 

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