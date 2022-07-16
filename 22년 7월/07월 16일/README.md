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
