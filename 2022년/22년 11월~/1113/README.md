# 1113

저번 금요일에 입사 후 계속하던 일이 일단락됐다. 이제 좀 개발 공부를 할 수 있지 싶다. 제일 하고 싶은 건 Go랑 리액트 공부?



## LG CNS 코드몬스터 리뷰

어제 코테 감 잃을까봐 LG 코드 몬스터를 한 번 응시했다. 7월달에 네이버 코테 이후 처음인듯? 총 4문제였고 생각보다 어려웠다.

문제 내용 쓰긴 귀찮고 풀었던 후기만 남기면, 1번은 비트마스킹으로 꽤나 최적화 잘된 코드 제출한 느낌. 처음에 구현이 막혔다가 비트마스킹으로 하자는 생각이 드니까 그냥 기계적으로 풀이를 완성했다. 2번은 뭐였는지도 기억 안 나는데 그냥 그래프 문제라 별 어려움 없이 풀었다. 3번은 문자열 탐색 문제인데 문자가 별로 길지도 않고 시간제한도 10초나 돼서 슬라이싱 - `in` 연산자로 구현했다. 솔직히 KMP 같은 건 귀찮으니까... 그래도 약간의 최적화를 위해 메모이제이션을 해줬다.

문제는 4번인데, (문제 써있는 내용은 달랐지만) 핵심은 트리 내에서 여러 경로들이 주어졌을 때, 특정 간선이 몇 번 사용됐는지 출력할 줄 알면 풀 수 있는 문제였다. 2월달인가? SK 코테 봤을 때도 최소 공통 조상 문제가 나온 적 있었다. 이 문제도 최소 공통 조상으로 해결할 수 있다는 생각이 들었다. 트리 내 경로에서 각 경로의 끝점의 최소 공통 조상을 찾고, 그 조상으로부터 각 끝점으로 가는 세그먼트를 생각해서 그 세그먼트들로 세그먼트 트리 느낌의 연산 최적화를 하면 되지 않나? 란 생각이 들었다. 핑계 좀 대자면 금밤에 술 안 마시고 일찍 잤으면 맑은 정신과 함께 풀었지 싶다 ㅋ..

암튼 그래서 최소 공통 조상 문제들을 좀 풀어보자고 마음 먹었다. 백준 티어만 다이아지 LCA, MCMF 이런 것도 못하면 쪽팔리잖아



## 최소 공통 조상 (Least Common Ancestor)

TIL에는 실패해서 안 썼던 거 같지만, Heavy-Light 분할을 8월 초에 구현해 봤었다. 시간 초과가 났었는데 LCA 코드가 제대로 구현되지 못해서 그랬었다. 어찌보면 당연하다. LCA 공부도 안하고 바로 Heavy-light 분할이 될 리가 없지

그래서 정말 오랜만에 백준 단계별 풀어보기에 들어가 LCA 카테고리 문제를 풀기로 했다.

LCA의 아이디어는 이미 알고 있었다. 그래서 그냥 바로 짜봤다.

```Python
from sys import stdin

input = stdin.readline


def find(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    da, db = depth[a], depth[b]
    for bit in range(md):
        if (da - db) & (1 << bit):
            a = parents[a][bit]
    if a == b:
        return a
    for bit in range(md - 1, -1, -1):
        if parents[a][bit] != parents[b][bit]:
            a = parents[a][bit]
            b = parents[b][bit]
    return parents[a][0]


n = int(input())
md = 20
parents = [[0] * md for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
depth = [0] * (n + 1)
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
points = [1]
depth[1] = 1
while points:
    now = points.pop()
    d = depth[now]
    for nei in graph[now]:
        if not depth[nei]:
            depth[nei] = d + 1
            points.append(nei)
            parents[nei][0] = now
del graph
for d in range(1, md):
    for idx in range(1, n + 1):
        parents[idx][d] = parents[parents[idx][d - 1]][d - 1]
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(find(x, y))
```

[백준 11438](https://www.acmicpc.net/problem/11438)의 정답 코드이다. 별 어려움 없이 통과해버려서 너무 어이가 없었다... 각 변수의 의미를 써보면,

- `graph` : 트리 구조를 그리기 위한 양방향 간선 그래프. 트리가 완성되면 필요없다.
- `depth` : 루트 노드로부터 떨어진 거리. DFS로 트리를 만들면서 구할 수 있다.
- `parents` : 공통 조상을 찾기 위한 2차원 배열. `parents[idx][k] = p`는 idx 노드의 2<sup>k</sup> 번 째 부모 노드는 p임을 의미한다.

그럼 `parents`를 어떻게 만들 것이냐. 일단 초기 상태를 만들어주자.

```Python
while points:
    now = points.pop()
    d = depth[now]
    for nei in graph[now]:
        if not depth[nei]:
            depth[nei] = d + 1
            points.append(nei)
            parents[nei][0] = now
```

DFS를 실행할 때, 직속 부모-자식 노드 관계의 now-nei는, parents[nei][0] = now라고 저장된다. 그 다음 정보 갱신이 핵심인데, i에서 k 번째 위의 부모 노드를 j라고 할 때, i에서 2 * k 번째 위의 부모 노드는 j에서 k번째 위의 부모 노드와 일치한다. 따라서 아래와 같이 쓸 수 있다.

```Python
for d in range(1, md):
    for idx in range(1, n + 1):
        parents[idx][d] = parents[parents[idx][d - 1]][d - 1]
```

그 다음은 쿼리가 들어왔을 때 답을 출력해줘야 한다. x, y의 LCA를 어떻게 찾아주냐면,

1. x와 y의 깊이를 비교한다. 더 깊은 노드를 더 얕은 노드의 깊이만큼 끌어올린다.
2. 같은 거리만큼 두 노드가 올라가면서 처음으로 같은 노드가 최소 공통 조상이다!

트리 구조를 그려보면 왜 이게 정답인지 알 수 있다. 별 어려운 내용은 아니니 생략.

```Python
def find(a, b):
    
    # 편의상 a를 더 깊은 노드로 설정하기
    if depth[a] < depth[b]:
        a, b = b, a
    da, db = depth[a], depth[b]

    # a를 b와 같은 깊이로 끌어올리기(1번 과정). 비트 연산으로 구현 가능하다.
    for bit in range(md):
        if (da - db) & (1 << bit):
            a = parents[a][bit]

    # 이미 같은 노드를 가리키고 있다면, 그 노드가 공통 조상.
    if a == b:
        return a

    # 같은 거리만큼 두 노드를 끌어올린다(2번 과정).
    for bit in range(md - 1, -1, -1):
        if parents[a][bit] != parents[b][bit]:
            a = parents[a][bit]
            b = parents[b][bit]
    
    # 가장 마지막으로 부모가 다른 위치까지 끌어올렸으니까, 한 칸 더 가야 정답.
    return parents[a][0]
```

이렇게 해서 최소 공통 조상 알고리즘도 구현해봤다. 이젠 웰노운 중에선 정말 유량 알고리즘들만 남은 느낌?



## Meet In The Middle - [백준 24520](https://www.acmicpc.net/problem/11438)

> LCA

새로운 알고리즘을 공부를 했으니, 틀린 문제 중 풀만한 게 있는지 봤는데 이 놈이 딱 걸렸다.

나름 뉴비 시절에 봤던 문제다. 신촌 겨울 알고리즘 캠프 콘테스트 문제였으니까.. 왜인지 모르겠지만 그때 문제들은 아직도 다 기억난다. 스네이크 게임이라던지, 히히 못가 라던지... 다들 웰메이드 문제였던 거 같다. 처음으로 한 PS 대회 문제라 더 그럴지도?

새로운 변수 `dist`를 추가해줬다. 이 친구는,

- `dist` : 정답을 찾기 위한 2차원 배열. `dist[idx][k] = p`는 idx 노드의 2<sup>k</sup> 번 째 부모 노드까지의 거리가 p임을 의미한다.

`dist`의  갱신은 `parents`와 같은 맥락으로 진행해주면 된다.

이제 답을 출력하는 게 문제다. 앞의 LCA에서 좀 더 계산해주면 된다.

1. x와 y의 깊이를 비교한다. 더 깊은 노드를 더 얕은 노드의 깊이만큼 끌어올린다. 이때 올라가는 거리를 저장한다.
2. 최소 공통 조상까지 x, y를 끌어올린다. 이때 올라가는 거리를 저장한다. x부터 lca까지의 거리 left와, y부터 lca까지의 거리 right라 하자.
3. left와 right의 합이 홀수면 -1 (중간 지점 없음)
4. left와 right 중 더 큰 쪽, 즉 가중치를 반영한 깊이가 더 깊은 쪽에서 출발해 (left + right) 를 2로 나눈 거리만큼 위로 올라가면 된다!

구현한 걸 보자.

```Python
def find(a, b):

    # 더 깊은 노드를 편의상 a라 하자
    if depth[a] < depth[b]:
        a, b = b, a
    da, db = depth[a], depth[b]

    # 초기값 설정 
    ma, mb = a, b
    left, right = 0, 0

    # 같은 높이로 맞추기. left도 같이 갱신해주기
    for bit in range(md):
        if (da - db) & (1 << bit):
            left += dist[a][bit]
            a = parents[a][bit]
    
    # lca까지 올라가기. left와 right 갱신 당연히 해주고
    for bit in range(md - 1, -1, -1):
        if parents[a][bit] != parents[b][bit]:
            left += dist[a][bit]
            right += dist[b][bit]
            a = parents[a][bit]
            b = parents[b][bit]
    if a != b:
        left += dist[a][0]
        right += dist[b][0]
    
    # 전체 이동거리 total은 left와 right의 합
    total = left + right
    if total % 2:
        return -1
    
    # 가중치 반영한 깊이가 더 깊은 노드에서 mid만큼 올라가야 한다.
    mid = total // 2
    if left < right:
        ma, mb = mb, ma
    
    # 위에서 lca 직전까지 올라간 것처럼, 이것도 깊이를 mid 직전까지만 올리기
    temp = 0
    for bit in range(md - 1, -1, -1):
        if temp + dist[ma][bit] < mid:
            temp += dist[ma][bit]
            ma = parents[ma][bit]
    
    # 아직 mid 도착 못했으면 한 칸 더 올리기
    # a = b 같이 주어진 경우 이미 temp=mid일 수 있으니 주의
    if temp < mid:
        temp += dist[ma][0]
        ma = parents[ma][0]
    
    # 이제 총 이동거리 temp가 mid와 같다면 발견한 것이고, 없다면 -1
    return ma if temp == mid else -1
```

의도치 않게 틀린 문제를 하나 줄였다. 주말 마지막에 그래도 뭔가 생산적인 일을 해서 다행이다 ㅋ
