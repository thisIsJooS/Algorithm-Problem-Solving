* https://docs.python.org/ko/3/

* n <= 1,000 이면 시간복잡도 O(N^2) 가능 , 시간제한이 5초라면 O(N^3)도 가능
* n <= 200,000 이면 시간복잡도 O(NlogN)
* n <= 500,000 인데 1초이면 O(N) 불가능. 무조건 O(logN). ex)이진탐색

* 원형으로 나열된 데이터를 처리하는 경우에는, 문제풀이를 간단히 하기 위하여 길이를 2배로 늘려서 원형을 일자로 만드는 방법이 있다. 혹은 첫 원소와 끝 원소가 붙어있는 경우와 떨어져 있는 경우 두가지로 나누어서 풀이하는 방법도 있다.

* 2차원 배열에서 상하좌우를 확인해야 할 경우에는 dx, dy 배열을 이용하자. 

* 순서가 상관없는 한 쌍들을 처리할 땐, 집합을 이용한다.

* 이진탐색  - 가능한 답 범위에 대하여 이진탐색을 하는 방법도 존재한다.

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

* 반복문 진행 도중 다른 함수에서 e를 건드는 경우 수정된 e로 계속 진행되기 때문에 list()를 입혀줌으로써 레퍼런스를 분리시킨다.
<code>
    
    for e in coord:
        for i, j in e:
            infect(i, j)
    
    # ⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇

    for e in coord:
        for i, j in list(e):
            infect(i, j)
</code>

* 배열에서 가장 작은 원소의 인덱스 값
<code>

    d.index(min(d))
</code>

* 문자열은 인덱스로 조회할 수 있지만, 인덱스로 변경은 할 수 없다.
<code>

    # u 는 문자열
    
    u = u[1:-1]
        for i in range(len(u)):
            if u[i] == '(':
                u = u[:i] + ')' + u[i+1:]   # u[i] = '(' 는 불가능 하다.
            else:
                u = u[:i] + '(' + u[i+1:] 

</code>


* 주어진 맵을 변형하여 외곽에 벽을 둔다. 이렇게 하면 맵을 벗어나지 않는지, 그 범위 판정을 더 간단히 할 수 있다.
<code>
    
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            new_board[i][j] = board[i-1][j-1]

</code>

* 각 원소가 튜플인 리스트에서 몇가지 값만을 따로 뽑은 리스트를 만들 때
<code>

    rates = [(1.0, 4), (0.0, 1), (0.0, 2), (0.0, 3)]
    rates = [i[1] for i in rates]
    
    # [4, 1, 2, 3]
</code>
