# 0102

일단 새해맞이 TIL 폴더 구조를 개편했다. 혹시나 이걸 몇 년 더 쓸 수도 있으니까?

추석 이후 이렇게 길게 쉰 건 오랜만인 거 같다. 덕분에 알고리즘 공부를 많이 했다. hello boj 2023 오프라인 응시자 뽑는 good bye 2022도 응시했는데, 4솔까지 패스인데 3솔 했다. 그놈의 이분 탐색은 잊을만 하면 대회 때 나와 항상 틀리는 것 같다...

그래도 내 알고리즘 커버리지를 늘린, 의미있는 일주일이었다. 마침내 유량 알고리즘을 이해했으니 말 다 했지 뭐



## 유량 알고리즘 - 에드몬드 카프 Edmonds-Karp Algorithm

이해하는 데 많은 도움을 준 블로그 글이 있는데, 지금 다시 찾으려니까 못 찾겠다. 파이프가 마구 얽혀있는 썸네일의 글이었던 기억하는데... 나중에 이건 추가하자.

암튼 이 알고리즘의 정당성이라든지, 시간복잡도라든지 인터넷에 상당히 잘 나와있다. 그럼에도 난 처음 에드몬드 카프를 공부한 게 4월달이었으니까, (물론 그 사이에 계속 공부하진 않았지만) 이해하고 문제를 푸는데 근 8개월이나 걸렸다 ㅋㅋ

일단 바로 어떻게 구현했는지 보자.

```Python
def edmondsKarp(s, e):
    result = 0
    while True:
        # 1번 과정
        visited = [0] * (n + 1)
        que = [s]
        for idx in que:
            for adj in graph[idx]:
                if capacity[idx][adj] > flow[idx][adj] and not visited[adj]:
                    que.append(adj)
                    visited[adj] = idx
                    if adj == e:
                        break
        # 2번 과정
        if not visited[e]:
            break
        # 3번 과정
        f = float('inf')
        idx = e
        while idx != s:
            adj = visited[idx]
            f = min(f, capacity[adj][idx] - flow[adj][idx])
            idx = adj
        # 4번 과정
        if not f:
            break
        result += f
        idx = e
        while idx != s:
            adj = visited[idx]
            flow[adj][idx] += f
            flow[idx][adj] -= f
            idx = adj
    return result
```

에드몬드 카프는 크게 4가지 스텝으로 나눌 수 있다.

1. 시작점 `s`에서 출발해서, bfs 탐색을 한다. 이 때 이웃한 노드로 이동할 수 있는 조건은, 아직 방문하지 않은 노드이고, 연결되어 있으면서, 그 간선에 흐르고 있는 플로우가 용량을 넘어서지 않아야 한다. 방문 리스트 `visited` 같은 경우, `visited[adj] = idx` 와 같이 이용한 간선의 끝 점이 시작점을 가리키도록 하자. (이후 경로 역추적에 사용할 예정) 
2. bfs가 끝났을 때 도착점 `e`에 방문하지 못했다면, 현재까지 흘려보낸 플로우 `result`를 반환한다. 방문했다면, 이제 새로운 플로우를 흘려보내줘야 한다.
3. 끝점에서 경로 역추적으로 시작점까지 이동한다. 동시에 경로 상 간선의 잔여 용량 중 최솟값 `f`를 찾아준다.
4. 만일 `f=0`이면 그대로 종료 (<= 요 부분은 내가 그냥 코드 짜면서 쓴 건데, 없어도 될 거 같다. 확실치는 않음.). 아니라면, `f`의 플로우를 경로 상에 흘려 보내준다. 이 때 해야할 일은, 간선에 흐르고 있는 플로우 양 갱신과, 전체 플로우 갱신을 해주면 된다. 이 과정이 끝나면 1번으로 다시 돌아가서 새로운 플로우를 흘려보낼 수 있는지 찾아주자.

이렇게 짜보았다. 이제 필요한 건 맞는 풀이인지 체크하기다. 체크 방법은 당연 백준 제출이다.



## 도시 왕복하기 1 - [백준 17412](https://www.acmicpc.net/problem/17412)

> 최대 유량

```Python
n, p = map(int, input().split())
flow = [[0] * (n + 1) for _ in range(n + 1)]
capacity = [[0] * (n + 1) for _ in range(n + 1) ]
graph = [[] for _ in range(n + 1)]
for _ in range(p):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    capacity[x][y] = 1
print(edmondsKarp(1, 2))
```

단계별로 풀어보기 유량 파트에서 가장 먼저 나오는 문제여서 이 문제로 골랐다.

`edmondsKarp()`는 위 함수 그대로 제출했다. 유량 모델 설계 이런 단계 없이, 문제에서 용량 1짜리 간선들을 어떻게 이으라고 명시가 되어 있어 그대로 만들어 AC를 받았다. 비록 플4 문제지만, 풀고 굉장히 기분이 좋았다.



## 열혈강호 4 - [백준 11348](https://www.acmicpc.net/problem/11348)

> 최대 유량

```Python
def makeGraph(s, e, f=1):
    graph[s].append(e)
    graph[e].append(s)
    capacity[s][e] = f

n, m, k = map(int, input().split())
ini = n + m + 1
mid = n + m + 2
fin = N = n + m + 3
graph = [[] for _ in range(N + 1)]
capacity = [[0] * (N + 1) for _ in range(N + 1)]
flow = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, n + 1):
    _, *js = map(int, input().split())
    for j in js:
        makeGraph(i, n + j)
    makeGraph(ini, i)
    makeGraph(mid, i, k)
makeGraph(ini, mid, k)
for j in range(1, m + 1):
    makeGraph(n + j, fin)
print(edmondKarp(ini, fin))
```

단계별로 풀어보기 유량 파트에서 두번째로 나오는 문제이다. 마찬가지로 `edmondsKarp()`는 위 함수 그대로 제출했다. 

한 명당 최대 1씩의 일을 하는 열혈강호 시리즈 문제에서, k만큼 추가로 일을 할 수 있도록 수정됐다. 그렇다면 이것을 어떻게 모델링을 할 것이냐. 나는 임의의 중간 지점 `mid`를 만들어 해결했다. 이 친구는 `ini`로부터 k만큼의 flow를 받아 모든 사람들에게 나눠준다. 그러면 문제가 원하는 상황과 딱 일치하게 설계가 된다!

이 친구도 별 문제 없이 AC를 받았는데, 다른 분들 풀이에 비해 현저히 느렸다. 다른 분의 풀이를 봤더니 (기억상 jh05013 님 코드였던 거 같다.) 디닉 알고리즘으로 푸셨더라. 그래서 내친 김에 디닉까지 공부하기로 했다.



## 유량 알고리즘 - 디닉 Dinic's Algorithm

요건 바로 코드를 보자.

```Python
def dinic(s, e):

    def sendFlow(idx, limit):
        if limit <= 0:
            return 0
        if idx == e:
            return limit
        result = 0
        l = level[idx]
        for adj in graph[idx]:
            if level[adj] == l + 1:
                c = capacity[idx][adj] - flow[idx][adj]
                if c > 0:
                    v = sendFlow(adj, min(limit - result, c))
                    flow[idx][adj] += v
                    flow[adj][idx] -= v
                    result += v
        if not result:
            level[idx] = -1
        return result

    result = 0
    while True:
        point = [s]
        level = [-1] * (N + 1)
        level[s] = 0
        for idx in point:
            l = level[idx]
            for adj in graph[idx]:
                if level[adj] == -1 and flow[idx][adj] < capacity[idx][adj]:
                    level[adj] = l + 1
                    point.append(adj)
        if level[e] == -1:
            break
        # 요 부분은 문제에 맞게 limit 값을 바꿔서 사용해주자.
        result += makeFlow(s, float('inf'))
    return result
```

에드몬드 카프 알고리즘을 돌리면서 계속 의아했던 점이 있다.

> 경로 역추적으로 플로우를 찾게되면, 최대 한 개의 경로에 대해서만 플로우를 갱신하는 거 아닌가?

실제로 에드몬드 카프 알고리즘의 시간복잡도는 O(VE^2)으로, 간선의 갯수가 많은 일반적인 그래프들에서 꽤 오랜 시간이 걸린다고 한다. 그에 비해 디닉은? O(V^2E)다. 즉 일반적으로 디닉이 더 빠를 것이다.

이 친구는 경로 역추적을 하지 않고, 한 번에 플로우를 여러 경로로 싹 내보낸다! 변수 몇 개를 살펴보면,

- `level` : 이 친구가 source로부터 얼마나 거리가 떨어져있는지를 의미한다. 일반적인 bfs로 점과 점 사이 거리를 구할 때 쓰는 놈이라고 이해하면 편하다.
- `sendFlow()` : 변수를 함수 내에 같이 써야할 것이 있어 별로 좋아하는 구조는 아니지만 함수 내에 함수를 짜줬다. 이 친구는 재귀함수인데, 이름 그대로 플로우를 흘려보낸다. 반환값은 현재 지점에서 다음 지점들로 새로 흘려보낸 플로우의 합이다.
- `limit` : `sendFlow()`의 현재 지점에서 최대로 흘려보낼 수 있는 새로운 플로우 총량이다. 만일 현재 지점이 도착점이라면? `sendFlow()`는 그대로 `limit`을 반환해주면 될 것이다. 만일 `limit`이 0보다 작다면? 추가로 탐색할 것 없이 0을 반환해주자.

`dinic()`의 메인 로직은 에드몬드 카프와 비슷하니 넘어가고, `sendFlow()`를 주로 설명하고자 한다. 

`sendFlow()`의 뼈대는 dfs와 매우 흡사하다. 현재 지점에서 갈 수 있는 모든 지점으로 일단 최대 플로우를 흘려보내고, 실제로 흘려보낼 수 있는 플로우 양을 확인해 각 간선들의 플로우를 갱신해준다. 이웃 지점으로 플로우를 흘려보낼 수 있는 조건은 에드몬드 카프에서의 조건과 동일하다. 각 플로우를 흘려보낼 때 `limit` 값은 **처음 limit에서 현재까지 흘려보낸 플로우를 뺀 양과, 간선이 수용할 수 있는 추가 플로우 양 중 더 작은 걸로 설정해주면 된다.** 말이 어렵지만 생각해보면 자명하다.

에드몬드 카프를 이해하고 이 친구를 보니 비교적 금방 구현했다. 그래서 바로 문제로 넘어갔다.



## 분단의 슬픔 - [백준 13161](https://www.acmicpc.net/problem/13161)

> 최대 유량, 최소 컷 최대 유량 정리

```Python
n = int(input())
source = n + 1
sink = N = n + 2
graph = [[] for _ in range(N + 1)]
capacity = [[0] * (N + 1) for _ in range(N + 1)]
for i, j in enumerate(map(int, input().split())):
    if j == 1:
        makeGraph(source, i + 1, float('inf'))
    elif j == 2:
        makeGraph(i + 1, sink, float('inf'))
for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    for j in range(i, n):
        makeGraph(i, j + 1, arr[j])
        capacity[j + 1][i] = arr[j]
flow = [[0] * (N + 1) for _ in range(N + 1)]
print(dinic(source, sink))
visited = set()
que = [source]
for now in que:
    for nei in graph[now]:
        if nei not in visited and capacity[now][nei] > flow[now][nei]:
            visited.add(nei)
            que.append(nei)
if source in visited:
    visited.remove(source)
print(*visited)
print(*(set(range(1, n + 1)) - visited))
```

이 친구도 단계별로 풀어보기 유량 파트에서 나온 문제다. 솔직히 유량 문제에요~ 라고 말해줬으니까 풀었지, 아니었다면 풀었을진 잘 모르겠다.

암튼 사람들을 두 진영으로 나누는데, 일부 사람들은 사전에 정해놓은 진영이 있는 상황애서 나머지 사람들의 진영을 어떻게 정해야 최소의 슬픔? 값을 얻는지 묻는 문제였다. 최대 유량 최소 컷 정리 이런 거 전혀 생각하지 않고, 그냥 유량 모델로 설계해서 풀었다. 간단하게 설명하면, (최대 유량이 흐른다) = (더 이상 흐를 플로우가 없다) = (source와 sink를 끊었다) = (최소 컷이다)라는 로직이다. 최대 매칭 최소 커버랑 같은 개념이라 이해하는데 별 문제 없었다.

플로우를 다 흘려보내고 난 뒤, 각 진영을 어떻게 나눌 건지도 출력해주어야 한다. 이 부분은, source에서 시작해서 bfs를 돌렸다. 1차적으로 1진영을 먼저 고른 사람들을 방문할 것이고, 그 이후엔 플로우가 더 흐를 수 있음에도 더 흐르지 않은 간선들을 타고 가 다른 점들을 방문한다. 만일 용량만큼의 플로우를 다 흘려보냈다면, 최대 유량 경로에 속해있다는 것이고, 이는 최소 컷에 포함되어 있다는 것이므로 같은 진영이 아니다.

문제 기여란을 보니 에드몬드 카프로 구현하면 시간 초과가 나는 듯하다. 앞으로도 어지간한 유량 문제는 디닉으로 구현하지 싶다.



## 스타 대결 - [백준 1031](https://www.acmicpc.net/problem/1031)

> 최대 유량, 그리디?

```Python
def changeFlow(s, e):
    if not flow[s][e]:
        return
    parent = [0] * (N + 1)
    point = [s]
    parent[s] = -1
    main_edge = (s, e)
    for idx in point:
        source_side = (1 <= idx <= n)
        for adj in graph[idx]:
            edge = (idx, adj) if source_side else (adj, idx)
            if main_edge < edge:
                if not parent[adj] and capacity[idx][adj] > flow[idx][adj]:
                    parent[adj] = idx
                    point.append(adj)
    if not parent[e]:
        return
    flow[s][e] = 0
    flow[e][s] = 0
    idx = e
    while idx != s:
        adj = parent[idx]
        flow[adj][idx] += 1
        flow[idx][adj] -= 1
        idx = adj


n, m = map(int, input().split())
source = n + m + 1
sink = N = n + m + 2
graph = [[] for _ in range(N + 1)]
capacity = [[0] * (N + 1) for _ in range(N + 1)]
ka, kb = 0, 0
for i, k in enumerate(map(int, input().split())):
    if k:
        makeGraph(source, i + 1, k)
        ka += k
for j, k in enumerate(map(int, input().split())):
    if k:
        makeGraph(n + j + 1, sink, k)
        kb += k
if ka != kb:
    print(-1)
    exit()
for i in range(1, n + 1):
    for j in range(1, m + 1):
        makeGraph(i, n + j)
flow = [[0] * (N + 1) for _ in range(N + 1)]
total_flow = dinic(source, sink)
if total_flow != ka:
    print(-1)
    exit()
for i in range(1, n + 1):
    for j in range(1, m + 1):
        changeFlow(i, n + j)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(1 if flow[i][n + j] else 0, end='')
    print()
```

이 문제로 말할 것 같으면... 22년 2월 18일 21시 50분에 틀렸던 문제다. 멋모르고 아무 문제나 다 덤비던 시절이다. 지금은 괜히 어설프게 알아서 저때처럼은 못하지 싶다.

일단 유량 모델 설계는 쉽다. 각 팀을 source와 sink에 잇고, 그 사이에 용량 1의 간선을 모두 그려주면 끝. 여기서 플로우를 흘려보내고 최대 플로우가 전체 경기수와 일치하지 않으면 그대로 탐색을 종료하자.

그 다음이 문제다. 만일 일치한다면, 사전 순으로 가장 빠른 대진표를 출력해야 하는데, **플로우를 적절히 바꿔가면서 최대 플로우는 유지하도록 해야한다.** 그렇다면 어떻게 바꿀 것이냐. 가장 앞에 0이 나오는 게 이득이므로, 앞의 경기부터 플로우가 1이 나온다면 0으로 바꾼 뒤, 그 뒤에 경기들을 적절히 재배치하여 플로우 총량을 유지해주면 된다. 이것이 `changeFlow()`의 주요 부분이다.

```Python
for idx in point:
    source_side = (1 <= idx <= n)
    for adj in graph[idx]:
        edge = (idx, adj) if source_side else (adj, idx)
        if main_edge < edge:
            if not parent[adj] and capacity[idx][adj] > flow[idx][adj]:
                parent[adj] = idx
                point.append(adj)
```

그렇게 1트 AC를 받았다. 유량 문제가 풀리고 나니 정말 재밌다. 처음 분리집합이랑 2SAT 풀 때 같은 느낌?



## 도시 왕복하기 2 - [백준 2316](https://www.acmicpc.net/problem/2316)

> 최대 유량

```Python
n, p = map(int, input().split())
N = 2 * n
graph = [[] for _ in range(N + 1)]
capacity = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(3, n + 1):
    makeGraph(n + i, i)
makeGraph(1, n + 1, p)
makeGraph(n + 2, 2, p)
for _ in range(p):
    x, y = map(int, input().split())
    makeGraph(x, n + y)
    makeGraph(y, n + x)
print(dinic(1, 2))
```

도시 왕복하기 1과 다르게, 이젠 각 도시에 한 번만 방문할 수 있게 바뀌었다. 보자마자 한 점을 두 점으로 쪼개서, 두 점 사이에 용량 1 짜리 간선을 그리잔 생각이 들었다. 그대로 그려주고 나머지 간선들을 추가해주면 AC. 이 때 쪼갠 점 중 한 점은 간선 받는 용도, 다른 한 점은 간선 나가는 용도로 나눠주었다.



## 뉴 매직 스퀘어 - [백준 1518](https://www.acmicpc.net/problem/1518)

> 이분 매칭, 그리디?

```Python
board = [list(map(int, input().split())) for _ in range(5)]
graph = [[] for _ in range(26)]
used = [False] * 26
for i in range(5):
    for j in range(5):
        if board[i][j]:
            k = board[i][j]
            used[k] = True
            graph[k].append(5 * i + j + 1)
            for v in range(1, k):
                graph[v] += list(range(5 * i + 1, 5 * i + j + 1))
            for v in range(k + 1, 26):
                graph[v] += list(range(5 * i + j + 2, 5 * i + 6))
            break
    else:
        temp = list(range(5 * i + 1, 5 * i + 6))
        for v in range(1, 26):
            graph[v] += temp
ans = []
for i in range(5):
    for j in range(5):
        now = 5 * i + j + 1
        if board[i][j]:
            graph[board[i][j]] = [now]
            continue
        for v in range(1, 26):
            if not used[v] and now in graph[v]:
                memo = graph[v][:]
                graph[v] = [now]
                match = [0] * 26
                for t in range(1, 26):
                    visited = [False] * 26
                    if not dfs(t):
                        graph[v] = memo[:]
                        break
                else:
                    board[i][j] = v
                    used[v] = True
                    break
        else:
            print(-1)
            exit()
for line in board:
    print(*line)
```

틀린 문제 중 유량으로 풀만한게 있나 쭉 훑던 중 이 친구가 눈에 들어왔다. 처음에는 유량으로 풀려다가, 이전에 [Fail Them All!](https://www.acmicpc.net/problem/24599) 문제를 풀 때 사용한 방법을 응용하면 되겠지 싶어 이분 매칭 + 그리디로 풀어줬다. 여기서 `dfs()`는 평소에 하던 이분 매칭 함수 그대로 썼다. 

제일 앞에서부터 넣을 수 있는 가장 작은 숫자를 넣고 이분 매칭을 돌린다. 이 때 맨 처음 이분 매칭이 안 된다면? 가능한 케이스가 없으므로 그대로 종료. 된다면 다음 칸으로 넘어가고, 또 제일 작은 숫자부터 차례대로 넣으면서 이분 매칭을 해준다. 5 by 5의 작은 판에 대해서 하는 거라 시간 제한 신경 안 쓰고 맘껏 구현했다. 그래서 리스트에 in 연산도 정말 오랜만에 사용했다 ㅋㅋ

이렇게 다른 문제에서 푼 아이디어로 문제를 풀게 되면 확실히 짬이 중요하단 걸 느낀다. 내년엔 나도 알고리즘 괴물이 되어있으면 좋겠다.



## 볼록 껍질 알고리즘 Convex Hull

나름 메이저한 알고리즘인데 유량 알고리즘처럼 예전에 공부하다가 때려치웠었다. 단계별로 풀어보기에 있길래 이 친구도 다시 봐야곘다~ 하고 봤는데 생각보다 할만했다.

볼록 껍질의 정의는 넘어가자. 말에서 느껴지는 그 느낌이 볼록 껍질의 정의 그대로의 내용이다.

여러 점에서 볼록 껍질에 항상 속하는 점을 생각해보면, 가장 오른쪽(여러 개라면 그 중 제일 위쪽)에 있는 점은 항상 포함될 것이다. 이 점을 원점으로 잡자. 이제 원점에서 다른 점들을 바라보면 다 왼쪽에 있을 것이다. 그럼 이제 이 점들과 원점을 잇고, 양의 y축 방향과 이루는 각도를 계산해본다. 이는 내적으로 계산할 수 있다. 이 각도를 기준으로 점들을 다시 정렬해주자. 그러면 볼록 껍질의 점들 또한 껍질 위의 순서대로 정렬될 것이다! 이는 그림을 그려보면 이해가 된다.

이제 정렬된 점들을 차례대로 보면서 이 점이 볼록 껍질 내의 점인지 판별한다. a에서 b로 가는 선이 마지막으로 확인한 볼록껍질 후보라 하자. 이때 확인할 점 c에 대해, a에서 c로 가는 선이 ab읜 왼쪽인지 오른쪽인지 확인해야 한다. 이미 원점과의 각도 순으로 정렬했기 때문에, 그려지는 방향이 제한적이라 왼쪽 오른쪽이라고만 말해도 명확하게 설명이 된다. 만약 왼쪽에 있다면 ac의 선분 안에 b가 속하는 그림으로 바뀌어야 하므로 b를 빼주고 다시 확인한다. 오른쪽에 있다면 abc 순으로 껍질이 생길 수도 있다는 뜻이다. 그렇다면 왼쪽 오른쪽은 어떻게 판별해 줄 것이냐. 외적을 쓰면 된다!

이때 외적 결과가 0, 즉 한 직선에 나오는 경우가 있을 수도 있다. 만일 같은 방향으로 쭉 진행하는 것이라면 b를 빼주면 될 것이고, 반대 방향으로 움직인다면 c를 그냥 pass하면 된다. 대부분의 케이스에선 신경 쓸 일이 없지만, 마지막 점이 원점과 그 전 점을 지나는 직선 위를 지나는 경우를 확인해줘야 한다. 음... 그니까 (0, 0)에서 껍질이 시작할 것이고, 쭉 보다가 뒤에서 두번쨰 점이 (-2, 4)이고 마지막 점이 (-1, 2)라면 (-1, 2)를 걸러줘야 한다는 뜻이다.

개념은 금방 이해됐으니 문제를 풀어보기로 했다.



## 볼록 껍질 - [백준 1708](https://www.acmicpc.net/problem/1708)

> 볼록 껍질

```Python
from sys import stdin

input = stdin.readline

n = int(input())
ps = [list(map(int, input().split())) for _ in range(n)]
ps.sort()
ox, oy = ps.pop()
for i in range(n - 1):
    ps[i][0] -= ox
    ps[i][1] -= oy
ps.sort(key=lambda xy: xy[1] / (xy[0] * xy[0] + xy[1] * xy[1]) ** 0.5)
cvh = [(0, 0), (ps[0][0], ps[0][1])]
for px, py in ps[1:]:
    while True:
        fx, fy = cvh[-2]
        sx, sy = cvh[-1]
        a, b = sx - fx, sy - fy
        c, d = px - fx, py - fy
        det = a * d - b * c
        if det > 0:
            cvh.pop()
        elif det < 0:
            cvh.append((px, py))
            break
        else:
            if a * c >= 0 and b * d >= 0:
                if abs(c) >= abs(a) and abs(d) >= abs(b):
                    cvh[-1] = (px, py)
                break
            else:
                cvh.pop()
ans = len(cvh)
a, b = cvh[-2]
c, d = cvh[-1]
if not a * d - b * c:
    ans -= 1
print(ans)
```

문제에서부터 볼록 껍질을 구하라고 되어있다. 위 알고리즘 설명대로 구현해주자.

이렇게 컨벡스헐도 풀 수 있게 되었다. 이젠 진짜 문자열 알고리즘들과, 센트로이드라든지 다차원 세그라든지 마이너한 친구들만 남은 것 같다.
