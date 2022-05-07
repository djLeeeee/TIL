# 0505



## 중복 없는 님 게임 - [백준 16889](https://www.acmicpc.net/problem/16889)

스프라그-그런디 정리, 런타임 전 처리

```python
from sys import stdin

input = stdin.readline

_ = input()
nums = list(map(int, input().split()))
gn = 0
dp = [
    0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7,
    7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10
]
for num in nums:
    gn ^= dp[num]
print('koosaga' if gn else 'cubelover')
```

돌무더기 크기가 60 밖에 안 되길래, 런타임 전처리 돌려서 그런디 수를 다 구해줬다. 약간 치트키를 쓴 느낌이긴 하지만... 뭐 암튼 정답은 맞췄다.



## 최소 체인 커버 - [백준 13503](https://www.acmicpc.net/problem/13503)

이분 매칭

```python
from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(2 * 10 ** 5)


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
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
ans = n
match = [0] * (n + 1)
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    ans -= dfs(i)
print(ans)
```

솔직히 이분 매칭이라는 키워드를 보지 못했으면 이 풀이를 생각 못 했을 거 같다...

**사이클이 없는 방향 그래프이기 때문에 가능한 풀이이다.** 요점은, 간선을 하나의 매칭으로 생각하는 것이다. 1번에서 2번으로 가는 간선을, 이분 그래프의 왼쪽 1번에서 오른쪽 2번으로 가는 매칭으로 생각해주면 된다는 뜻. 그 다음 n - (최대 매칭의 수)를 해주면 답이 나온다. 최대 매칭에 포함된 매칭에 해당하는 간선이 체인에 속한다고 생각해주면 된다. 최대 매칭이 n개 나오면 예외 처리를 해줘야 하나 잠시 고민했는데, 사이클이 없기 떄문에 n개의 매칭이 나올 수는 없다.(n개의 매칭이 있으면 원본 그래프에 필연적으로 사이클이 생긴다)