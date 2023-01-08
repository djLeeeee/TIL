# 0108

진짜 주말 내내 알고리즘만 들여다봤다. 근데 [이 놈](https://www.acmicpc.net/problem/14424)이랑 [이 놈](https://www.acmicpc.net/problem/20564), 그리고 [이 놈](https://www.acmicpc.net/problem/13427)을 오랜 시간 들여다봤음에도 겁나게 안 풀린다... 3문제 다 풀 수 있을 듯 안 풀려서 굉장히 약이 오른다. 그르르...



### 트리와 쿼리 3 - [백준 13512]

> Heavy-light decomposition

```Python
from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def dfs(idx):
    for adj in graph[idx]:
        if not parent[adj]:
            parent[adj] = idx
            tree[idx].append(adj)
            dfs(adj)
            size[idx] += size[adj]
            if size[adj] > size[tree[idx][0]]:
                tree[idx][-1] = tree[idx][0]
                tree[idx][0] = adj


def dfs2(idx):
    global cnt
    num[idx] = cnt
    inv[cnt] = idx
    cnt += 1
    if tree[idx]:
        top[tree[idx][0]] = top[idx]
        dfs2(tree[idx][0])
        for adj in tree[idx][1:]:
            top[adj] = adj
            dfs2(adj)


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
tree = [[] for _ in range(n + 1)]
size = [1] * (n + 1)
parent = [0] * (n + 1)
parent[1] = -1
top = [0] * (n + 1)
dfs(1)
del graph, size
num = [0] * (n + 1)
inv = [0] * (n + 1)
top[1] = 1
cnt = 0
inv[-1] = -1
dfs2(1)
seg = [n] * (2 * n)
for _ in range(int(input())):
    st, u = map(int, input().split())
    if st == 1:
        u = n + num[u]
        if seg[u] != n:
            seg[u] = n
        else:
            seg[u] = u - n
        u //= 2
        while u:
            seg[u] = min(seg[2 * u], seg[2 * u + 1])
            u //= 2
    else:
        ans = n
        while u > 0:
            left = n + num[top[u]]
            right = n + num[u]
            while left <= right:
                if left % 2:
                    if ans > seg[left]:
                        ans = seg[left]
                    left += 1
                if not right % 2:
                    if ans > seg[right]:
                        ans = seg[right]
                    right -= 1
                left //= 2
                right //= 2
            u = parent[top[u]]
        print(inv[ans])
```

트리 구조에서 세그트리 쓰기? 전형적인 Heavy-light decomposition 문제였다.

평소와 다르게 모든 점으로부터 1까지의 경로를 확인하면 됐기 때문에, `depth` 변수가 필요없을 것 같아 지웠다. 경로 상에 가장 1에 가까운 놈은, 우리가 부여한 새로운 번호 `num[idx]`가 제일 작을테니 단순하게 `min` 함수로 세그 트리를 관리해주고 마지막에 `inv[cnt]`를 해줬다. 

진짜 간신히 1점 올렸다. 솔브닥 점수가 뭔 의미가 있겠냐만은... 그래도 루비는 찍어보고 싶다.
