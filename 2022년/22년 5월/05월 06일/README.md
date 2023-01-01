# 0506



## :diamond_shape_with_a_dot_inside: 개구리3 - [백준 15568](https://www.acmicpc.net/problem/15568)

2 SAT

```python
from sys import stdin, setrecursionlimit
from collections import defaultdict

input = stdin.readline
setrecursionlimit(5 * 10 ** 6)


def draw_or_edge(x, y):
    graph[-x].append(y)
    graph[-y].append(x)


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
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


n, m = map(int, input().split())
info = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    info[i] = [0] + list(map(int, input().split()))
leaf = [[] for _ in range(n + 1)]
frog = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    l1, l2 = map(int, input().split())
    frog[i] = [l1, l2]
    leaf[l1].append(i)
    leaf[l2].append(-i)
graph = defaultdict(list)
node = n + 1
for group in leaf[1:]:
    if len(group) > 1:
        for k in range(len(group) - 1):
            draw_or_edge(-(node + k), node + k + 1)
            draw_or_edge(-group[k], node + k)
            draw_or_edge(-(node + k), -group[k + 1])
        draw_or_edge(-group[-1], node + len(group) - 1)
    node += len(group)
for _ in range(m):
    l1, l2, topic = map(int, input().split())
    for f1 in leaf[l1]:
        for f2 in leaf[l2]:
            if info[abs(f1)][topic] != info[abs(f2)][topic]:
                draw_or_edge(-f1, -f2)
stack = []
visited = [False] * (2 * node + 1)
for i in range(1, node + 1):
    if not visited[i]:
        dfs(i)
    if not visited[-i]:
        dfs(-i)
scc = [0] * (2 * node + 1)
component = 0
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
flag = True
result = [0] * (n + 1)
for i in range(1, n + 1):
    if scc[i] > scc[-i]:
        result[frog[i][0]] = i
    elif scc[i] < scc[-i]:
        result[frog[i][1]] = i
    else:
        flag = False
        break
if flag:
    print('YES')
    print(*result[1:])
else:
    print('NO')
```

돌아온 2 SAT 문제~ 간만에 다이아 너무 좋고~~

새로 배울만한 포인트는 딱히 없다. 그룹 내 최대 1개가 참일 때 간선을 그룹 크기만 그리는 테크닉을 기억하면 별 어려움 없이 해결할 수 있었다. 1트 AC도 충분히 가능한 문제였는데, 개구리가 몇 번 연꽃에 앉아야 하는지로 출력해서(출력 양식과 반대로 출력했다) 문제를 찾느라 좀 시간이 걸렸다...

[개구리 2](https://www.acmicpc.net/problem/15567) 문제를 읽어보니 이 문제와 다른 게 없어서 같은 코드로 제출해서 정답을 받았다. 플1 + 다5 개꿀~