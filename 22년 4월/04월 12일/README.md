# 0412

바쁘다 바빠!



## 2018 KAKAO BLIND RECRUITMENT

알고리즘 심화 스터디에서 진행했다. 문제 풀이 스킬은 그렇다 치고 여러 모듈들을 습득할 수 있었다.

```python
import re

my_str.re.split('[1-9]+')
```

`my_str`을 1부터 9까지의 숫자로 `split`을 하고... 자세한 건 [정규식 연산 공식 문서](https://docs.python.org/ko/3/library/re.html) 참고하자.

마지막 문제는 딱 봐도 트라이 구조로 푸는 문제라 '아 이거 귀찮네...'라고 생각하면서 안 풀었던 거 같다. 지나고 나니 굉장히 안 좋은 생각이었다. 다른 분들은 트라이 구조 없이 단순 정렬 - 문자열 탐색으로 푸셨다. 옛날처럼 다시 이런 문제들도 도전하는 버릇을 들이자.



## Django project

`index`페이지에 css 적용하기

:thinking: 다음 과제 : `create plan` 버튼에 알맞은 테마 찾기



## 유치원 - [백준 5009](https://www.acmicpc.net/short/status/5009/1003/1)

2 SAT, 이분 탐색

```python
from sys import stdin

input = stdin.readline


def draw_or_edge(x, y):
    graph[-x].append(y)
    graph[-y].append(x)


def draw_edge(x, y):
    cx, cy = past[x], past[y]
    if (cx + 1) % 3 == cy:
        draw_or_edge(x, -y)
    elif (cx - 1) % 3 == cy:
        draw_or_edge(-x, y)
    else:
        draw_or_edge(x, y)
        draw_or_edge(-x, -y)


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
    if scc[idx]:
        return
    scc[idx] = component
    if scc[-idx] == scc[idx]:
        flag = False
        return
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


n = int(input())
past = [0] * (n + 1)
rank = [[0] for _ in range(n + 1)]
for i in range(1, n + 1):
    c, *r = map(int, input().split())
    past[i] = c
    rank[i] += r
start = 0
end = n - 1
while start <= end:
    middle = (start + end) // 2
    graph = [[] for _ in range(2 * n + 1)]
    for i in range(1, n + 1):
        for j in range(middle + 1, n):
            draw_edge(i, rank[i][j])
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
        ans = middle
        end = middle - 1
    else:
        start = middle + 1
print(ans)
```

다이아5 위에도 사람이 살아요

반이 3개가 있는 상황에서 이게 어떻게 2 SAT지? 싶을 수 있는데, 문제 조건에 이런 게 있다.

> 작년과 같은 선생님의 반에 속하는 학생은 없어야 한다.

이 구문을 좀만 바꿔서 생각해보면,

> 학생들은 이전 반보다 1이 크거나, 작은 반 (mod 3) 으로 가야 한다!

학생들의 선택지(정확히는 학생들이 선택하는 것은 아니지만)가 2개로 좁혀졌다. 이제 +1 인 반으로 가는 것을 `True`, - 1로 가는 걸 `False`로 정의해주자. 이제부터는 완전 2 SAT이다. 문제는 2 SAT를 몇 등까지 돌릴까이다. 2 SAT가 시간 복잡도가 그리 빠른 알고리즘은 아니여서 여러 번 하는 것이 좋지 않지만, 이 문제에서는 `n`이 200보다 작거나 같은 자연수여서 이진 탐색으로 해당 등수를 찾아주면 그렇게 많이 탐색을 하지 않겠다는 판단이 섰다. 그래서 이진 탐색 + 2 SAT라는 새로운 방법으로 문제를 풀어봤다. 다행히 AC. 파이썬 중에서, pypy3까지 포함해서도, 시간이 제일 빨랐다. 2 SAT 최고~~
