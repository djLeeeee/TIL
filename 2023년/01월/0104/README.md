# 0104

MCMF 쪽을 보고 있다. [두부장수 장홍준3](https://www.acmicpc.net/problem/14424)이란 문제로 보고 있는데, 무지막지한 최적화가 필요한 듯 하다. 해결이 되면 한 번에 정리해서 올려야지. 두부장수 장홍준1과 2가 정답 처리된 것 봐서는 놓치고 있는 포인트 하나가 있지 싶다.



## 책 구매하기 2 - [백준 11406](https://www.acmicpc.net/problem/11406)

> 최대 유량

```Python
from sys import stdin

input = stdin.readline

def makeGraph(s, e, f=1):
    graph[s].append(e)
    graph[e].append(s)
    capacity[s][e] = f


def dinic(s, e):
    def sendFlow(now, limit):
        if limit <= 0:
            return 0
        if now == e:
            return limit
        res = 0
        for nei in graph[now]:
            if level[now] + 1 == level[nei] and capacity[now][nei] > 0:
                f = sendFlow(nei, min(capacity[now][nei], limit - res))
                res += f
                capacity[now][nei] -= f
                capacity[nei][now] += f
        return res

    result = 0
    while True:
        point = [s]
        level = [-1] * (N + 1)
        level[s] = 0
        for idx in point:
            l = level[idx]
            for adj in graph[idx]:
                if capacity[idx][adj] and level[adj] == -1:
                    level[adj] = l + 1
                    point.append(adj)
        if level[e] == -1:
            return result
        result += sendFlow(s, float('inf'))


n, m = map(int, input().split())
source = n + m + 1
sink = N = n + m + 2
graph = [[] for _ in range(N + 1)]
capacity = [[0] * (N + 1) for _ in range(N + 1)]
for i, a in enumerate(map(int, input().split())):
    makeGraph(source, i + 1, a)
for j, b in enumerate(map(int, input().split())):
    makeGraph(j + n + 1, sink, b)
for j in range(m):
    for i, c in enumerate(map(int, input().split())):
        if c:
            makeGraph(i + 1, j + n + 1, c)
print(dinic(source, sink))
```

위에서 MCMF 최적화를 하다가 기존의 짜던 최대 유량 알고리즘을 좀 더 깔끔하게 쓸 수 있겠다는 생각이 들었다. 기존의 함수에선 flow와 capacity 이중 리스트 2개를 이용해 플로우 체크를 했는데, 그럴 이유가 없다는 걸 깨달았다.

새로 푼 이 유량 문제에서 보면, 단순하게 capacity 하나로 관리하고, 플로우가 흐르면 그 값을 바로 바꿔준다. 로직이 다른게 없어서 깊게 설명할 건 없을 거 같다. 이중 리스트를 하나로 통합해 코드가 훨씬 깔끔해진 느낌이다.
