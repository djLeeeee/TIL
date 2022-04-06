# 0406



## 레드 블루 스패닝 트리 - [백준 4792](https://www.acmicpc.net/problem/4792)

분리 집합

```python
from sys import stdin

input = stdin.readline


def sol():
    def find(target):
        if target == parents[target]:
            return target
        parents[target] = find(parents[target])
        return parents[target]

    def union(a, b):
        a, b = find(a), find(b)
        parents[a] = b

    blue = []
    red = []
    component = n
    parents = list(range(n + 1))
    for _ in range(m):
        c, x, y = input().strip().split()
        x, y = int(x), int(y)
        if find(x) != find(y):
            union(x, y)
            component -= 1
        if c == 'R':
            red.append((x, y))
        else:
            blue.append((x, y))
    if component > 1 or k > len(blue) or k >= n:
        return 0
    parents = list(range(n + 1))
    c_red = n
    d_red = 0
    for x, y in red:
        if find(x) != find(y):
            union(x, y)
            c_red -= 1
        else:
            d_red += 1
    parents = list(range(n + 1))
    c_blue = n
    d_blue = 0
    for x, y in blue:
        if find(x) != find(y):
            union(x, y)
            c_blue -= 1
        else:
            d_blue += 1
    if c_red - 1 <= k and c_blue <= n - k:
        return 1
    return 0


while True:
    n, m, k = map(int, input().split())
    if n == m == k == 0:
        break
    print(sol())
```

모든 간선이 파란색 또는 빨간색으로 색칠되어 있을 때, 파란색 간선을 특정 개수 사용해서 신장 트리를 만들 수 있는지 판별하는 문제였다. `n`개의 점으로 이루어진 그래프에서 파란색 간선을 `k`개 사용해 신장 트리를 싶다고 하자. 내가 생각한 포인트는,

1. `k`는 `n`보다 작아야 한다. 그래야 트리를 만들지.
2. 전체 파란색 간선 수보다 `k`가 작거나 같아야 한다. 자명.
3. 원래 그래프가 연결 그래프여야 한다. 그래야 신장 트리가 존재한다.
4. **파란색 간선만으로 그래프를 그렸을 때, 적어도 (연결 요소의 갯수 - 1) 만큼 빨간색 간선이 반드시 필요하다**. 당연히 빨간색 그래프에 대해서도 성립한다.

4번을 보자. 신장 트리를 만들기 위해 connected component가 1개만 있어야 한다. 파란색 그래프에 `c_blue`개의  c.c가 있다 하자. 각 c.c를 연결해야 하는데, 이는 빨간색 간선을 사용해야 한다. 그러면 몇 개 필요할까? 각 c.c를 vertex로 가지는 새로운 graph를 생각해보면, `c_blue - 1`만큼 간선이 필요할 것이다. 이런 조건을 만족하는 빨간색 간선 집합은 반드시 존재하는게, 원본 그래프는 connected graph니까 항상 찾을 수 있다(disconnected graph는 3번에서 걸러줬다). 

```python
    if c_red - 1 <= k and c_blue <= n - k:
        return 1
    return 0
```

그래서 답을 구하는 `sol`함수 마지막에 위와 같이 값을 반환해주었다. 틀린 로직이 없었는지 1트 AC. 한동안 2 SAT만 풀다가 오랜만에 푼 분리 집합 문제다. 역시 이런 문제가 재밌다 ㅋㅋㅋ



## 길의 개수 - [백준 1533](https://www.acmicpc.net/problem/1533)

분할 정복 행렬 거듭 제곱

```python
from sys import stdin

input = stdin.readline


def multiple_matrix(first, second=None):
    if not second:
        second = first
    sz = len(first)
    res = [[0] * sz for _ in range(sz)]
    for jj in range(sz):
        for ii in range(sz):
            for kk in range(sz):
                res[ii][kk] += first[ii][jj] * second[jj][kk]
    for ii in range(sz):
        for jj in range(sz):
            res[ii][jj] %= div
    return res


div = 10 ** 6 + 3
n, s, e, t = map(int, input().split())
table = [[0] * (5 * n) for _ in range(5 * n)]
for i in range(n):
    for k in range(4):
        table[5 * i + k][5 * i + k + 1] = 1
    line = list(map(int, input().strip()))
    for j in range(n):
        x = line[j]
        if x:
            table[5 * i + x - 1][5 * j] = 1
result = [[0] * (5 * n) for _ in range(5 * n)]
for i in range(5 * n):
    result[i][i] = 1
while t > 0:
    if t & 1:
        result = multiple_matrix(result, table)
    table = multiple_matrix(table)
    t >>= 1
print(result[5 * (s - 1)][5 * (e - 1)])
```

시작점에서 끝까지 정확히 몇 초에 가는 경로가 얼마나 있는지 구하는 문제다. 행렬의 거듭제곱 꼴로 구하고 싶지만, 각 간선의 가중치가 달라 바로 곱하면 문제가 생긴다. 다행히 간선의 가중치가 최대 5여서, 각 간선을 분리시킬 수 있다!

```python
table = [[0] * (5 * n) for _ in range(5 * n)]
for i in range(n):
    for k in range(4):
        table[5 * i + k][5 * i + k + 1] = 1
    line = list(map(int, input().strip()))
    for j in range(n):
        x = line[j]
        if x:
            table[5 * i + x - 1][5 * j] = 1
```

각 인덱스를 5배 해주고, 위의 코드처럼 조건에 맞게 이어주면 되는 것이다. 그 다음은 단순 행렬 거듭 제곱 풀이. `t`의 범위가 매우 크니, 분할 정복으로 계산해주면 AC.

