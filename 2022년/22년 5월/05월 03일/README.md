# 0503



## 일방통행 - [백준 1412](https://www.acmicpc.net/problem/1412)

강한 연결 요소

```python
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
    if scc[idx]:
        return
    scc[idx] = component
    for adj in graph_inv[idx]:
        if not scc[adj]:
            dfs_inv(adj)


n = int(input())
board = [input().strip() for _ in range(n)]
graph = [[] for _ in range(n)]
graph_inv = [[] for _ in range(n)]
for s in range(n - 1):
    for e in range(s + 1, n):
        if board[s][e] == 'Y' and board[e][s] == 'N':
            graph[s].append(e)
            graph_inv[e].append(s)
        elif board[s][e] == 'N' and board[e][s] == 'Y':
            graph[e].append(s)
            graph_inv[s].append(e)
visited = [False] * n
stack = []
for i in range(n):
    if not visited[i]:
        dfs(i)
component = 0
scc = [0] * n
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
if component == n:
    print('YES')
else:
    print('NO')
```

양방향 도로를 단방향으로 바꿨을 때 모든 사이클을 없앨 수 있는지 보는 문제였다. 단방향 도로로만 이루어진 사이클이 있다면 당연히 모든 사이클을 없앨 방법이 없다. 그렇다면 양방향이 섞인 사이클에 대해서 생각을 해봐야 하는데, 독립된 사이클에 대해서 당연히 사이클이 없도록 각 양방향 도로의 방향성을 정해줄 수 있다. 그렇다면 독립되지 않은 사이클들의 집합이 문제가 될 것이다. 그림을 그려보면, 독립되지 않은 사이클 들의 집합들에서 양방향의 방향성을 정의할 수 없다면 단방향 사이클이 존재함을 알 수 있다. 그래서 우리는 단방향 사이클이 존재하는지 판별을 해주면 된다. `DFS`로 해결 가능하겠지만, 생각없이 짤 수 있는 `SCC`로 코드를 짰다.



## JavaScript30 - Practice 03 CSS Variables

```css
:root {
    --base: #ffc600;
    --spacing: 10px;
    --blur: 10px; 
}

img {
    background: var(--base);
    padding: var(--spacing);
    filter: blur(var(--blur));
}

.hl {
    color: var(--base);
}
```

```javascript
const inputs = document.querySelectorAll('.controls input');

function effectUpdate () {
  const suffix = this.dataset.sizing || '';
  document.documentElement.style.setProperty(`--${this.name}`, this.value + suffix);
}

inputs.forEach(input => input.addEventListener('change', effectUpdate));
inputs.forEach(input => input.addEventListener('mousemove', effectUpdate));
```

알아갈만한 포인트가 좀 있다.

#### Or 연산자

앞에 값이 `true`라면 앞의 값을, `false`라면 뒤의 값을 반환한다. 즉, 위의 `suffix`를 받아오는 코드는 아래와 같다.

```javascript
const suffix = this.dataset.sizing ? this.dataset.sizing : ''
```

#### Event

- `change`: input의 value가 바뀌었을 때 동작
- `mousemove`: 해당 객체 내에서 마우스가 움직일 때. 이 친구가 없으면 실시간 반영이 안 됨.

#### CSS Variables

오늘 내용 중 제일 중요한 거.

```css
:root {
    --variable: value;
}
```

위와 같은 형태로 저장을 해주면, 같은 css 내에서 저 값에 `var(--variable)`을 통해 접근이 가능하다. 일괄적으로 바꿔야 할 변수값이 있다면 편할 듯.

이제 저 값들을 자바스크립트에서 지정해주는 작업도 필요한데, 일단 css 코드를 불러와야한다.

```javascript
document.documentElement.style // css 호출
```

그 다음 뒤에 `setProperty`와 백틱을 이용하여  `:root` 내 변수의 값을 변경해주면 된다.