# 0502



## 생물 농축 - [백준 1293](https://www.acmicpc.net/problem/1293)

배낭 문제, 위상 정렬

```python
from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
info = [0] + [tuple(map(int, input().split())) for _ in range(n)]
metal = [0] * (n + 1)
food = deque()
for i in range(1, n + 1):
    if info[i][0] == 0:
        food.append(i)
        metal[i] = info[i][1]
deg = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    deg[y] += 1
can_eat = [[] for _ in range(n + 1)]
while food:
    idx = food.popleft()
    for adj in graph[idx]:
        if metal[idx]:
            can_eat[adj].append(idx)
        deg[adj] -= 1
        if deg[adj] == 0:
            need, limit, _ = info[adj]
            dp = [-1] * (limit + 1)
            dp[0] = 0
            for eat_food_idx in can_eat[adj]:
                c = info[eat_food_idx][2]
                m = metal[eat_food_idx]
                while m <= limit:
                    for now in range(limit, m - 1, -1):
                        if dp[now - m] >= 0 and dp[now] < dp[now - m] + c:
                            dp[now] = dp[now - m] + c
                    c *= 2
                    m *= 2
            for m in range(1, limit + 1):
                if dp[m] >= need:
                    metal[adj] = m
                    break
            food.append(adj)
            if adj == n:
                if metal[n]:
                    print('yes')
                    print(metal[n])
                else:
                    print('no')
                exit()
```

간만에 DP 문제다. 포식자와 먹이 간의 그래프를 그리고, 위상 정렬을 통해 아직 확인하지 않은 먹이 사슬 최하위가 중금속이 누적되어도 생존할 수 있는지를 배낭 문제로 확인해준다. 이 때 예전에 썼던 방법인, 중금속 양을 2배 씩 해서 확인해주어 실행 시간을 줄여주었다.

```python
for eat_food_idx in can_eat[adj]:
    c = info[eat_food_idx][2]
    m = metal[eat_food_idx]
    while m <= limit:
        for now in range(limit, m - 1, -1):
            if dp[now - m] >= 0 and dp[now] < dp[now - m] + c:
                dp[now] = dp[now - m] + c
                c *= 2
                m *= 2
```

배낭 문제 2번이었나? 그 문제를 전에 푼 덕에 수월하게 풀었다.