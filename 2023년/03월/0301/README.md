# 0301

2월달에 TIL을 너무 안 썼다...

어제 엄청 삽질을 했다. 밥 안 먹고 하니까 괜히 쓸데없는 짓을 하고 있었다. 덤으로 다른 회사 분들께 민폐까지... 계속 붙잡고 있기보다 잠시 쉬었다 하는 게 좋을 지도. 그래도 계속 삽질하면서 네트워크의 작동 원리에 대해 많이 이해할 수 있었다. 이제 스프링 삽질을 마저 하자...



## 학교 가지마 - [백준 1420](https://acmicpc.net/problem/1420)

> MFMC

```Python
from collections import defaultdict


def drawGraph(s, e):
    graph[s].add(e)
    graph[e].add(s)
    capacity[(s, e)] = 1


n, m = map(int, input().split())
board = [input() for _ in range(n)]
N = n * m
source = sink = 0
graph = [set() for _ in range(N * 2)]
capacity = defaultdict(int)
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
for i in range(n):
    for j in range(m):
        if board[i][j] == '#':
            continue
        k = i * m + j
        if board[i][j] == 'K':
            source = N + k
        elif board[i][j] == 'H':
            sink = k
        drawGraph(k, N + k)
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < n and 0 <= nj < m and board[ni][nj] != '#':
                nk = ni * m + nj
                drawGraph(N + k, nk)
if sink in graph[source]:
    print(-1)
else:
    flow = 0
    while flow < 4:
        level = [-1] * (N * 2)
        level[source] = 0
        que = [source]
        for idx in que:
            l = level[idx]
            for adj in graph[idx]:
                if level[adj] == -1 and capacity[(idx, adj)] > 0:
                    level[adj] = l + 1
                    que.append(adj)
        if level[sink] == -1:
            break
        flow += 1
        idx = sink
        while idx != source:
            for adj in graph[idx]:
                if level[adj] == level[idx] - 1:
                    capacity[(adj, idx)] -= 1
                    capacity[(idx, adj)] += 1
                    idx = adj
                    break
    print(flow)
```

간만에 랜덤 플레 돌렸는데, 딱 보아하니 플로우 문제라 집었다.

격자판에서 각 노드들을 in & out으로 쪼개고, 평소 하던대로 해주자. 사실 처음엔 아무 생각없이 안 쪼개고 해서 몇 번 틀렸었다 ㅋㅋ

별 특별한 게 없는 문제지만 왜 썼냐면, 최대 플로우가 4이기 때문에 굳이 `sendFlow`의 함수를 만들지 않고 sink에서 source로 역으로 올라가면서 플로우를 1씩 흘려줬다. 하는 김에 `dinic`도 함수 대신 `while` 문으로 옮겨줬다. 
