# 0414



## 미세먼지 안녕! - [백준 17144](https://www.acmicpc.net/problem/17144)

구현

```python
from sys import stdin

input = stdin.readline


def spread():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    new_board = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if board[x][y] > 0:
                new_board[x][y] += board[x][y]
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] >= 0:
                        new_board[nx][ny] += board[x][y] // 5
                        new_board[x][y] -= board[x][y] // 5
    new_board[ccw][0] = -1
    new_board[cw][0] = -1
    return new_board


def rotate():
    x = ccw
    while x > 1:
        board[x - 1][0] = board[x - 2][0]
        x -= 1
    y = 0
    while y + 1 < m:
        board[0][y] = board[0][y + 1]
        y += 1
    x = 0
    while x < ccw:
        board[x][-1] = board[x + 1][-1]
        x += 1
    y = m - 1
    while y > 1:
        board[ccw][y] = board[ccw][y - 1]
        y -= 1
    x = cw + 1
    while x + 1 < n:
        board[x][0] = board[x + 1][0]
        x += 1
    y = 0
    while y + 1 < m:
        board[-1][y] = board[-1][y + 1]
        y += 1
    x = n - 1
    while x > cw:
        board[x][-1] = board[x - 1][-1]
        x -= 1
    y = m - 1
    while y > 1:
        board[cw][y] = board[cw][y - 1]
        y -= 1
    board[ccw][1] = 0
    board[cw][1] = 0
    return


n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    if board[i][0] == -1:
        ccw, cw = i, i + 1
        break
for _ in range(t):
    board = spread()
    rotate()
print(sum([sum(line) for line in board]) + 2)
```

간만에 구현 문제~



## :diamond_shape_with_a_dot_inside: Railroad - [백준 21865](https://www.acmicpc.net/problem/21865)

2 SAT, 구현

```python
from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def draw_or_edge(x, y):
    graph[-x].append(y)
    graph[-y].append(x)


def draw_nor_edge(x, y):
    graph[x].append(-y)
    graph[y].append(-x)


def draw_xor_edge(x, y):
    graph[-x].append(y)
    graph[-y].append(x)
    graph[y].append(-x)
    graph[x].append(-y)


def draw_false_edge(x):
    graph[x].append(-x)


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
    if scc[idx] == scc[-idx]:
        print('NO')
        exit()
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
graph = [[] for _ in range(8 * n * m + 1)]
for i in range(n):
    for j in range(m):
        now = (m * i + j) * 4
        if board[i][j] == 'L':
            draw_xor_edge(now + 1, now + 3)
            draw_xor_edge(now + 2, now + 4)
        elif board[i][j] == 'X':
            for d in range(1, 5):
                draw_false_edge(now + d)
        elif board[i][j] == 'O':
            for ii in range(2, 5):
                for jj in range(1, ii):
                    draw_or_edge(now + ii, now + jj)
        else:
            draw_nor_edge(now + 1, now + 2)
            draw_nor_edge(now + 1, now + 4)
            draw_nor_edge(now + 3, now + 2)
            draw_nor_edge(now + 3, now + 4)
            draw_nor_edge(now + 1, -(now + 3))
            draw_nor_edge(now + 3, -(now + 1))
            draw_nor_edge(now + 2, -(now + 4))
            draw_nor_edge(now + 4, -(now + 2))
di = [0, -1, 0, 1, 0]
dj = [0, 0, -1, 0, 1]
trans = [0, 3, 4, 1, 2]
for i in range(n):
    for j in range(m):
        if board[i][j] != 'X':
            now = (m * i + j) * 4
            for d in range(1, 5):
                ni = i + di[d]
                nj = j + dj[d]
                nei = (m * ni + nj) * 4
                if 0 <= ni < n and 0 <= nj < m and board[ni][nj] != 'X':
                    draw_xor_edge(now + d, -(nei + trans[d]))
                else:
                    draw_false_edge(now + d)
stack = []
visited = [False] * (8 * m * n + 1)
for i in range(1, 4 * m * n + 1):
    if not visited[i]:
        dfs(i)
    if not visited[-i]:
        dfs(-i)
component = 0
scc = [0] * (8 * m * n + 1)
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
print('YES')
answer = [[0] * m for _ in range(n)]
trans = {
    1111: chr(43), 1101: chr(62), 1110: chr(118), 111: chr(60),
    1011: chr(94), 1100: chr(114), 1001: chr(76), 110: chr(55),
    11: chr(74), 101: chr(124), 1010: chr(45)
}
for i in range(n):
    for j in range(m):
        now = (m * i + j) * 4
        check = 0
        for d in range(1, 5):
            if scc[now + d] > scc[-(now + d)]:
                check += 10 ** (d - 1)
        if board[i][j] == 'X':
            answer[i][j] = board[i][j]
        elif check in trans:
            answer[i][j] = trans[check]
        else:
            answer[i][j] = '.'
for line in answer:
    print(''.join(line))
```

전설의 2 SAT 빌런

4방향에 대해 모두 논리식을 부여해줬다. 그 다음은 천천히 구현하는 2 SAT. 의외로 설명할 건 많이 없다.

잔실수 때문에 10트나 걸렸다. `n`을 `m`으로 쓴다던지... 다음부턴 신경쓰자