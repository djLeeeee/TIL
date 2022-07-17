# 0716

틀린 문제 없애기 프로젝트 2일차. 현재 37문제 남았다.

하면서 느낀 건데, 굉장히 어렵다. 괜히 틀린 채로 남아있는 문제들이 아니다...



## 트리 색칠하기 - [백준 1693](https://www.acmicpc.net/problem/1693)

트리 DP

```Python
from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 5)


def sol(idx, pc):
    if dp[idx][pc]:
        return dp[idx][pc]
    if not tree[idx]:
        return (pc == 1) + 1
    result = float('inf')
    for color in range(1, 20):
        if color != pc:
            now = color
            for adj in tree[idx]:
                now += sol(adj, color)
            if now < result:
                result = now
    dp[idx][pc] = result
    return result


n = int(input())
if n == 1:
    print(1)
    exit()
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = [False] * (n + 1)
tree = [[] for _ in range(n + 1)]
point = [1]
visited[1] = True
while point:
    x = point.pop()
    for y in graph[x]:
        if not visited[y]:
            visited[y] = True
            point.append(y)
            tree[x].append(y)
dp = [[0] * 20 for _ in range(n + 1)]
print(sol(1, 0))
```

사용할 최대 색깔 수를 먼저 정해야 한다. 생각해보면, 트리의 높이가 최대 사용 색깔 수가 된다. 그래서 넉넉하게 20개의 색깔을 사용한다고 정의하고 시작했다.

그 다음부터는 단순 재귀 함수 구현이다. 근데 계속 시간 초과가 떴다... 꼼꼼히 읽어보니 메모이제이션을 안 해놨드라. 그래서 메모이제이션을 추가해줘 AC.

어제에 이어 틀린 문제 한 문제 더 없앴다. 이제 남은 건 36문제.



## 사냥꾼 - [백준 10985](https://www.acmicpc.net/problem/10985)

기하

```Python
from sys import stdin
from math import acos

input = stdin.readline

for _ in range(int(input())):
    x1, y1, x2, y2, r = map(float, input().split())
    xy1 = x1 * x1 + y1 * y1
    xy2 = x2 * x2 + y2 * y2
    xy = (x2 - x1) ** 2 + (y2 - y1) ** 2
    yx = x1 * y2 - x2 * y1
    if x1 == x2 and y1 == y2:
        ans = 0
    else:
        d = abs(yx) / (xy ** 0.5)
        if d >= r:
            ans = xy ** 0.5
        else:
            t = yx * (y2 - y1) / xy
            if (x1 <= t and x2 <= t) or (x1 >= t and x2 >= t):
                ans = xy ** 0.5
            else:
                r1 = acos(r / xy1 ** 0.5) + acos(r / xy2 ** 0.5)
                r2 = acos((xy1 + xy2 - xy) / (2 * xy1 ** 0.5 * xy2 ** 0.5))
                ans = (xy1 - r * r) ** 0.5 + (xy2 - r * r) ** 0.5 + (r2 - r1) * r
    print('{:.3f}'.format(round(ans, 3)))
```

어려운 로직은 1도 없다. 문제점 / 보완점은,

- `acos`의 범위를 생각 안했다. 그래서 답이 pi * r 만큼 차이날 때가 있던 거 같다.
- 식이 너무 복잡해지길래, 반복되는 연산은 `xy1` 같이 미리 계산해놨다.

기하 문제는 항상 풀 때마다 귀찮다. 이 문제도 귀찮아서 틀리고 안 고친 감이 적잖게 있다. 암튼 남은 틀린 문제는 이제 35문제.



## 빵집 - [백준 3109](https://www.acmicpc.net/problem/3109)

DFS, 그리디

```Python
from sys import stdin

input = stdin.readline


def dfs(x, y):
    if y == m - 1:
        return 1
    for d in range(3):
        nx = x + dx[d]
        if 0 <= nx < n and arr[nx][y + 1] == '.' and not visited[nx][y + 1]:
            visited[nx][y + 1] = True
            if dfs(nx, y + 1):
                return 1
    return 0


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = 0
dx = [-1, 0, 1]
for i in range(n):
    if arr[i][0] == '.':
        ans += dfs(i, 0)
print(ans)
```

골드 문제 최고...

설명할 건 딱히 없다. dfs로 경로 찾는데, 약간 그리디 적으로 최대한 위 쪽으로 이동하는 경로를 찾는다.

오늘 틀린 문제 3문제나 해치웠다. 남은 문제 34개...



## Fail Them All! - [백준 24599](https://www.acmicpc.net/problem/24599)

2 SAT, 그리디?

```Python
from sys import stdin

input = stdin.readline


def dfs(idx):
    if visited[idx]:
        return
    visited[idx] = True
    for adj in graph[idx]:
        if not visited[adj]:
            dfs(adj)
    stack.append(idx)


def dfs_inv(idx):
    global flag
    if scc[idx] or not flag:
        return
    scc[idx] = component
    if scc[-idx]:
        if scc[-idx] == component:
            flag = False
            return
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


m, n = map(int, input().split())
graph = [[] for _ in range(2 * n + 1)]
for _ in range(m):
    order = input().rstrip()
    node = []
    for i in range(n):
        if order[i] == 'T':
            node.append(i + 1)
        elif order[i] == 'F':
            node.append(-i - 1)
    l = len(node)
    for i in range(l - 1):
        for j in range(i + 1, l):
            graph[node[i]].append(-node[j])
            graph[node[j]].append(-node[i])
stack = []
visited = [False] * (2 * n + 1)
for i in range(1, n + 1):
    if not visited[-i]:
        dfs(-i)
    if not visited[i]:
        dfs(i)
scc = [0] * (2 * n + 1)
component = 0
flag = True
while stack and flag:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
if flag:
    ans = ''
    for j in range(1, n + 1):
        graph[j].append(-j)
        stack = []
        visited = [False] * (2 * n + 1)
        for i in range(1, n + 1):
            if not visited[i]:
                dfs(i)
            if not visited[-i]:
                dfs(-i)
        scc = [0] * (2 * n + 1)
        component = 0
        flag = True
        while stack and flag:
            now = stack.pop()
            if not scc[now]:
                component += 1
                dfs_inv(now)
        if flag:
            ans += 'F'
        else:
            ans += 'T'
            graph[-j].append(j)
            graph[j].pop()
    print(ans)
else:
    print(-1)
```

크으 어제 푹 잤더니 오늘 뭔가 잘 풀린다.

꽤 오랜 기간 내 속을 썩힌 문제다. 2 SAT에 한참 꽂혔을 때 풀다가 막혔던 기억이 난다. 2 SAT를 할 때 간선 배치와 정점 탐색 순서를 최대한 그리디 적으로 접근해 한 번의 2 SAT로 해결하는 쪽으로 접근했는데, 실패했다.

오늘 문제를 다시 보니, n이 100 밖에 되지 않았다. 그래서 2 SAT를 100번 돌렸다. 어떻게 100번이냐 하면...

1. 원래 상태의 그래프에서 2 SAT를 그린다. 여기서부터 논리 오류가 생기면 답이 없는 것이니 `-1`을 출력한다.
2. 그리디 적으로, 1번 답이 `F`여야 사전 순으로 빠르다. 따라서, 1번 답이 `F`가 되는 간선을 그리고 2 SAT를 또 돌린다.
3. 만약 논리 오류가 없다면, 1번 답을 `F`로 고정한다. 논리 오류가 생겼다면, 1번 답을 `T`로 고정하고, 2번에서 그린 간선을 `T` 간선으로 수정한다.
4. 2~3번 과정을 2번, 3번, ... 100번 문제에 대해 계속한다.

이렇게 해주면 모든 문제의 정답을 최대한 빠른 사전 순으로 만들 수 있다! 

틀린 문제 33문제 남았다. 오늘 20대 진입하나?
