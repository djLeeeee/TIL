# 0408

다이아 가나연???

## :diamond_shape_with_a_dot_inside: 실험 - [백준 19703](https://www.acmicpc.net/problem/19703)

2 SAT

```python
from sys import stdin, setrecursionlimit
from collections import defaultdict

input = stdin.readline
setrecursionlimit(10 ** 6)


def draw_edge(x, y):
    graph[-y].append(x)
    graph[-x].append(y)


def dfs(idx):
    if visited[idx]:
        return
    visited[idx] = True
    for adj in graph[idx]:
        if not visited[adj]:
            dfs(adj)
    stack.append(idx)


def dfs_inv(idx):
    if scc[idx]:
        return
    scc[idx] = component
    if scc[-idx] == component:
        print('NIE')
        exit()
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


n, m, a, b = map(int, input().split())
group = defaultdict(list)
graph = defaultdict(list)
for _ in range(a):
    i, j = map(int, input().split())
    group[j].append(i)
gn = n + 1
for g in group.values():
    for k in range(len(g) - 1):
        draw_edge(-gn - k, gn + k + 1)
        draw_edge(-g[k], gn + k)
        draw_edge(-gn - k, -g[k + 1])
    draw_edge(-g[-1], gn + len(g) - 1)
    gn += len(g)
for _ in range(b):
    i, j = map(int, input().split())
    draw_edge(i, j)
stack = []
visited = defaultdict(bool)
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
    if not visited[-i]:
        dfs(-i)
scc = defaultdict(int)
component = 0
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
print('TAK')
```

문제 자체는 진작에 풀었다. 근데 계속 TLE를 받았다. 그룹에 대한 간선을 그리는 부분이 문제였다. 원래는 그룹에 대해서 간선을 아래와 같이 그렸다.

```python
for _ in range(a):
    i, j = map(int, input().split())
    for k in group[j]:
        graph[k].append(-i)
        graph[i].append(-k)
    group[j].append(i)
```

크기 n의 그룹이 있다면, O(n<sup>2</sup>) 개 만큼의 간선을 그려준 셈이다. 이걸로도 풀리면 이 문제가 다이아를 받았을리가 없다. 이제 n<sup>2</sup> 이 아닌 [O(n)개의 간선을 그려주는 방법](https://blog.naver.com/jh05013/221454612761)이 있다! 운좋게도 jh05013님의 블로그를 찾았다. 역시 대단하시다...

A<sub>1</sub> ~ A<sub>n</sub>에서 최대 1개가 True인 상황을 생각해보자. 새로운 점 B<sub>1</sub> ~ B<sub>n</sub>을 만들어준 뒤, 아래의 논리식 대로 간선을 그어주면 된다. 이 때 각 B<sub>i</sub> 는, A<sub>1</sub> ~ A<sub>i</sub> 중 한 개 이상이 참일 때 참인 명제이다.
$$
\sim B_i \or B_{i + 1} \\
\sim A_i \or B_i \\
\sim B_i \or \sim A_{i + 1}
$$
간선을 그릴 떄 `draw_edge`라는 함수를 정의해 사용했다. 정점의 개수를 정확히 알 수 없으므로 `defaultdict` 모듈을 사용했다.

2 SAT를 나름 마스터했다고 생각했는데, 더 많이 연습해야겠다...



## :diamond_shape_with_a_dot_inside: Turf Wars - [백준 15880](https://www.acmicpc.net/problem/15880)

2 SAT

```python
from sys import stdin, setrecursionlimit
from collections import defaultdict

input = stdin.readline
setrecursionlimit(10 ** 4)


def or_edge(x, y):
    graph[-x].append(y)
    graph[-y].append(x)


def check(p1, p2):
    x1, y1, x2, y2 = p1
    x3, y3, x4, y4 = p2
    if x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1:
        return False
    return True


def new_area(x):
    x1, y1, x2, y2 = map(int, input().split())
    group.append((x1, y1, x2, y2, x))
    for x3, y3, x4, y4, k in ground:
        if check((x3, y3, x4, y4), (x1, y1, x2, y2)):
            or_edge(k, x)


def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    for adj in graph[x]:
        if not visited[adj]:
            dfs(adj)
    stack.append(x)


def dfs_inv(x):
    if scc[x]:
        return
    scc[x] = component
    if scc[x] == scc[-x]:
        print('NO')
        exit()
    for adj in graph[-x]:
        if not scc[-adj]:
            dfs_inv(-adj)


n = int(input())
graph = defaultdict(list)
ground = []
idx = 0
for _ in range(n):
    m = int(input())
    group = []
    for i in range(1, m):
        or_edge(-(idx + i), idx + m + i)
        or_edge(-(idx + m + i), -(idx + i + 1))
        or_edge(-(idx + m + i), idx + m + i + 1)
        new_area(idx + i)
    or_edge(-(idx + m), idx + 2 * m)
    new_area(idx + m)
    ground += group
    idx += 2 * m
stack = []
visited = defaultdict(bool)
for i in range(1, idx + 1):
    if not visited[i]:
        dfs(i)
    if not visited[-i]:
        dfs(-i)
scc = defaultdict(int)
component = 0
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
print('YES')
```

이전 문제랑 같은 맥락이다.

하루 다이아 2 sol... 이건 귀하군요....



## [Codeforces Round #781 Div.2](https://codeforces.com/contest/1665)

언제나처럼 3 sol.

4번째 문제는 `flush`를 사용하는 문제였다. 관련해서 공부하자.



## Royal guards - [백준 7058](https://www.acmicpc.net/problem/7058)

이분 매칭

```python
from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == 0 or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
rn = 0
cn = 0
row = [[0] * m for _ in range(n)]
row_inv = {}
col = [[0] * m for _ in range(n)]
col_inv = {}
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and not row[i][j]:
            rn += 1
            jj = j
            while jj < m and board[i][jj] != 2:
                if board[i][jj] == 0:
                    row[i][jj] = rn
                    row_inv[rn] = i + 1
                jj += 1
for j in range(m):
    for i in range(n):
        if board[i][j] == 0 and not col[i][j]:
            cn += 1
            ii = i
            while ii < n and board[ii][j] != 2:
                if board[ii][j] == 0:
                    col[ii][j] = cn
                    col_inv[cn] = j + 1
                ii += 1
graph = [[] for _ in range(rn + 1)]
for i in range(n):
    for j in range(m):
        if not board[i][j]:
            graph[row[i][j]].append(col[i][j])
match = [0] * (cn + 1)
ans = 0
for i in range(1, rn + 1):
    visited = [False] * (cn + 1)
    ans += dfs(i)
print(ans)
for i in range(1, cn + 1):
    if match[i]:
        print(row_inv[match[i]], col_inv[i])
```

이분 매칭해주면 되는 문제다. 개념은 이미 지겹도록 쓴 듯 하니 넘어가자.

대신 정답 출력을 위해 `row_inv`와 `col_inv`를 추가해줬다.

다이아까지 단 4점 남았다... 후우... 설레서 미칠 거 같다...