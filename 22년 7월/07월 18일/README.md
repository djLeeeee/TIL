# 0718

대학생 때도 거의 안 해본 술자리 두 탕을 뛰었다. 미안해 간아...

다행히 대면 수업 가기 전 새벽에 한 문제 풀어놓아 스트릭은 끊기지 않았다.



## 중앙 트리 - [백준 7812](https://www.acmicpc.net/problem/7812)

트리 DP

```Python
from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 5)


def update(idx):
    result = 1
    for adj, _ in tree[idx]:
        result += update(adj)
    child_size[idx] = result
    return result


while True:
    n = int(input())
    if not n:
        break
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        x, y, d = map(int, input().split())
        graph[x].append((y, d))
        graph[y].append((x, d))
    tree = [[] for _ in range(n)]
    visited = [-1] * n
    point = [0]
    visited[0] = 0
    dp = [0] * n
    while point:
        now = point.pop()
        for nei, d in graph[now]:
            if visited[nei] == -1:
                visited[nei] = visited[now] + d
                dp[0] += visited[nei]
                point.append(nei)
                tree[now].append((nei, d))
    child_size = [0] * n
    update(0)
    point = [0]
    while point:
        now = point.pop()
        for nei, d in tree[now]:
            dp[nei] = dp[now] + (n - 2 * child_size[nei]) * d
            point.append(nei)
    print(min(dp))
```

어제 문제 한 번 쓰윽 읽고 잠자리에 누웠다. 잠들기 전까지 문제를 좀 생각했는데, 할만하다는 생각이 들어서 풀려다가... 대면 수업도 있고 하니 참았다. 대신 새벽 6시에 눈이 떠져 정신 차리고 문제를 풀었다.

3월 13일에 풀었던 문제인 듯 하다. 예전 풀이를 보는데, 말도 안 되는 풀이를 해놨길래 다 갈아엎었다.

그래프 구조에서 임의의 루트 노드를 잡고 트리 구조로 만들어준다. 그 다음, 트리 하위 노드들 갯수를 계산하고 간선을 따라 이동하면서 답을 갱신해주면 끝.

```Python
dp[nei] = dp[now] + (n - 2 * child_size[nei]) * d
```

이 부분은 하위 노드로 이동할 때, `d`만큼 거리가 줄어드는 노드들이 하위 노드의 자식 노드 갯수만큼 있고, 나머지는 다 늘어나므로 `(n - size) + (-size)`로 계산된 결과이다.



## :diamond_shape_with_a_dot_inside: 프리즌 브레이크 - [백준 1886](https://www.acmicpc.net/problem/1886)

이분 매칭

```Python
from sys import stdin
from collections import defaultdict

input = stdin.readline


def update(x, y):
    idx = board[x][y]
    checked = [False] * (pn + 1)
    point = [(x, y)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    day = 0
    while point:
        new = []
        day += 1
        for x, y in point:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] > 0 and not checked[board[nx][ny]]:
                    checked[board[nx][ny]] = True
                    new.append((nx, ny))
                    for ex in range(day, 201):
                        graph[board[nx][ny]].append((ex, -idx))
        point = new


def sol(limit):

    def dfs(idx):
        for t in graph[idx]:
            if t[0] <= limit and not visited[t]:
                visited[t] = True
                if not match[t] or dfs(match[t]):
                    match[t] = idx
                    return 1
        return 0

    match = defaultdict(int)
    for ii in range(1, pn + 1):
        visited = defaultdict(bool)
        if not dfs(ii):
            return 0
    return 1


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
gn = 0
pn = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'D':
            gn += 1
            board[i][j] = -gn
        elif board[i][j] == '.':
            pn += 1
            board[i][j] = pn
        else:
            board[i][j] = 0
graph = [[] for _ in range(pn + 1)]
for i in range(1, m - 1):
    if board[0][i]:
        update(0, i)
    if board[-1][i]:
        update(n - 1, i)
for i in range(1, n - 1):
    if board[i][0]:
        update(i, 0)
    if board[i][-1]:
        update(i, m - 1)
ans = 'impossible'
left = 1
right = 200
while left <= right:
    mid = (left + right) // 2
    if sol(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
```

사실, 이전 풀이가 왜 틀렸는지 반례를 잘 모르겠다.

```Python
def dfs(idx):
    if match_inv[idx]:
        return 0
    for c, adj in graph[idx]:
        if c > ans:
            return 0
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            match_inv[idx] = True
            return 1
    return 0


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
gn = 0
pn = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'D':
            gn += 1
            board[i][j] = -gn
        elif board[i][j] == '.':
            pn += 1
            board[i][j] = pn
        else:
            board[i][j] = 0
graph = [[] for _ in range(pn + 1)]
for i in range(m):
    if board[0][i]:
        update(0, i)
    if board[-1][i]:
        update(n - 1, i)
for i in range(1, n - 1):
    if board[i][0]:
        update(i, 0)
    if board[i][-1]:
        update(i, m - 1)
for ls in graph[1:]:
    if ls:
        ls.sort()
    else:
        print('impossible')
        exit()
ans = 0
res = 0
match_inv = [False] * (pn + 1)
while res < pn:
    match = [0] * (gn + 1)
    ans += 1
    for i in range(1, pn + 1):
        if not match_inv[i]:
            visited = [False] * (gn + 1)
            res += dfs(i)
print(ans)
```

옛날 풀이 먼저 설명해보면,

1. 죄인과 출구를 넘버링해준다.
2. 출구 근처의 죄인들을 찾아 죄인에게 표시해놓는다.
3. 하루 씩 늘리면서 이분 매칭을 한다. 그 날짜에 매칭된 방에는 매칭될 수 없을 것이다.
4. 전체 매칭이 죄인의 수만큼 완료되면 매칭 종료.

아마 날짜에 따라 내가 임의로 죄인들을 탈옥시키면 안 되는 풀이가 존재하는 듯 하다. 반례는 도저히 못 찾겠지만...

그래서 풀이를 바꿨다. 이런 방법으로 이분 매칭을 풀어본 적은 없는 거 같아 상당히 풀면서 재밌었다.

1. 앞의 풀이랑 1, 2번은 같다. 대신, **죄인에게 출구를 표시할 때 오늘 이후의 모든 날짜의 간선을 추가한다.**
2. 이분 탐색으로 `limit` 날짜를 정하고, 그 날짜보다 빠르거나 같게 탈옥할 수 있는 출구가 있으면 매칭을 한다.
3. 매칭이 죄인의 수만큼 완료되면 정답을 갱신한다.

이 풀이는 당연히 반례가 존재할 수 없을 것이다. 전체 사용 가능한 출구를 고려한 것이니까... 근데 WA. 왜 그렇지 하고 코드를 천천히 보는데

```Python
while left < right:
  ...
```

등호를 빼먹었었다. 내 아까운 시간들...

그래도 틀린 문제 + 다이아 문제를 풀어서 기분이 좋았다 ㅎㅎ 틀린 문제는 이제 27문제 밖에 안 남았다.
