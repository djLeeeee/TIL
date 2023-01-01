# 0515



## :diamond_shape_with_a_dot_inside: 보드 색칠하기 - [백준 13444](https://www.acmicpc.net/problem/13444)

이분 매칭

```python
from sys import stdin, setrecursionlimit
from collections import defaultdict

input = stdin.readline
setrecursionlimit(10 ** 4)


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n, m = map(int, input().split())
board = [input() for _ in range(n)]
node = 0
edge_r = 0
edge_c = 0
row = defaultdict(list)
col = defaultdict(list)
graph = defaultdict(list)
for i in range(n):
    for j in range(m):
        if board[i][j] == '#':
            node += 1
            if j + 1 < m and board[i][j + 1] == '#':
                edge_r += 1
                row[(i, j)].append(edge_r)
                row[(i, j + 1)].append(edge_r)
            if i + 1 < n and board[i + 1][j] == '#':
                edge_c += 1
                col[(i, j)].append(edge_c)
                col[(i + 1, j)].append(edge_c)
            if row[(i, j)] and col[(i, j)]:
                for r in row[(i, j)]:
                    graph[r] += col[(i, j)]
ans = node - edge_r - edge_c
match = [0] * (edge_c + 1)
for i in range(1, edge_r + 1):
    visited = [False] * (edge_c + 1)
    ans += dfs(i)
print(ans)
```

[백준 9495 바둑](https://www.acmicpc.net/problem/9495) 과 풀이의 결이 비슷하다.

일단 최대 색칠 회수를 생각해보자. 자명하게, 전체 흰색 칸의 개수가 된다. 안타깝게도 이대로 답이 아니라, 한 번에 여러 칸 색칠이 가능하다. 여러 칸을 색칠한다는 것은 그 칸들이 한 줄로 붙어있어야 한다. 이제 생각을 바꿔서, 서로 붙어있는 두 칸이 흰 색이라고 생각해보자. 그 사이를 새로운 노드로 하면... 말이 어렵다 음...

옛날에 vertex를 edge로 바꾸고, edge를 vertex로 바꾸는 graph를 그린 적이 있다. 그거랑 비슷한 느낌이다. 평소대로라면 칸을 vertex로, 붙어있는 두 칸을 edge로 이어주는 방식으로 graph를 그렸다면, 이젠 약간 다르다. 붙어있는 두 칸을 vertex로 하고, 같은 칸을 공유하는 vertex 간에 간선을 이어준다. 이 때, **상하로 붙어있는 칸이 의미하는 vertex와 좌우로 붙어있는 칸이 의미하는 vertex 간에 이어주면, 이분 그래프가 나온다**. 코드로 돌아가서, 변수들이 어떤 의미인지 보자.

- `node` : 전체 흰색 칸의 수.

- `edge_r` : 좌우로 붙은 두 칸을 의미하는 vertex. 1부터 시작해서 차례대로 부여한다.

- `edge_c` :  상하로 붙은 두 칸을 의미하는 vertex. 1부터 시작해서 차례대로 부여한다.

- `row` : key를 한 칸으로 하고, 그 칸을 공유하는 `edge_r`들의 리스트를 value로 하는 dictionary.

- `col` : key를 한 칸으로 하고, 그 칸을 공유하는 `edge_c`들의 리스트를 value로 하는 dictionary.

- `graph` : 위에서 설명한 방법대로 그리는 이분 그래프. 아래 같이 그려줄 수 있다.

  >     if row[(i, j)] and col[(i, j)]:
  >     	for r in row[(i, j)]:
  >     		graph[r] += col[(i, j)]

이제부터가 핵심이다. 이렇게 해서 그린 하나의 점이 어떤 의미인지 생각해보면, **색칠 회수를 1 줄일 수 있는 포텐셜을 가지고 있는 점이다.** 그렇다면 이상적으로 배치됐을 때 답은 (전체 흰색 칸 수) - (그래프 점의 수), 즉 `(node - edge_r - edge_c)`가 된다. 하지만 모든 점들이 동시에 답을 1 줄일 수는 없다. 서로 공존할 수 없는 경우가 있는데, 이들의 관계를 좀만 생각해보면 우리가 직전에 간선을 그린 경우에 해당한다! **한 칸이 연속 색칠하는 줄에 포함된다고 할 때, 행과 열 두 방향 동시에 포함될 수 없으니까.** 그렇다면 최소 버텍스 커버의 수만큼 답을 더해주어야 한다. 그래서 이분 매칭 돌리고 최대 매칭의 수를 더해주면 AC!

처음으로 다이아3 문제를 풀었다. 후우... 루비 딱 기다려라...
