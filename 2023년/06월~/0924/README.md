# 0924

생존 신고 느낌

드디어 2000솔을 했다. 2000번째 문제를 뭔가 의미있는 걸로 하고 싶었지만...
아레나 하다보니 어느새 2000솔을 넘어가 있었다 ㅠ

신규 알고리즘도 터득했다. 서큘레이션 알고리즘인데, 뭐 거창한 건 없다.
네트워크 플로우에서 사이클을 만든다라고 해야하나..
[이 문제](https://www.acmicpc.net/problem/20135)를 보면 무슨 얘기인지 알 수 있을 듯.
문제 풀이 원리는 간단하다. 현재 있는 플로우에서 source와 sink에서 유량을 흘려보내 강제로 잉여 유량을 없애면 된다. 

```Python
n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
source = n + 1
sink = N = n + 2
graph = [[] for _ in range(N + 1)]
flow = [[0] * (N + 1) for _ in range(N + 1)]
capacity = [[0] * (N + 1) for _ in range(N + 1)]
edges = [list(map(int, input().split())) for _ in range(m)]
for ini, fin, mi, ma in edges:
    arr[ini] -= mi
    arr[fin] += mi
    drawGraph(ini, fin, ma - mi)
fromSource = 0
toSink = 0
for i in range(1, n + 1):
    if arr[i] > 0:
        drawGraph(source, i, arr[i])
        fromSource += arr[i]
    elif arr[i] < 0:
        drawGraph(i, sink, -arr[i])
        toSink += -arr[i]
if fromSource != toSink:
    print(-1)
    exit()
realFlow = dinic(source, sink)
if realFlow == fromSource:
    print(1)
    for ini, fin, mi, ma in edges:
        print(flow[ini][fin] + mi)
else:
    print(-1)
```

디닉은 항상 쓰던 그 함수이니 첨부하지 않으련다.

[노다지 올림피아드 문제들을 찾았다.](https://www.acmicpc.net/category/774)
빈집털이 느낌으로다가 첫 솔브 & 기여 스택 쌓고 있다 :+1:

회사일이 바쁘긴 한데, 성장하는 느낌이 나서 썩 나쁘지 않다.
엘지 트윈스 팬 20년으로 다져진 멘탈은 쉽게 무너지지 않는다 ㅎ
