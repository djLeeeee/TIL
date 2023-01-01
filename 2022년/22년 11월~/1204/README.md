# 1204

진짜 gRPC 공부하려했는데... 뭐가 일이 계속 생긴 일주일이었다. 그래도 축구는 맘편히 봐서 다행이다 ㅎㅎ

CNS는 면접 보러 오라는데, 솔직히 별로 가고 싶지 않다. 부모님께선 별로 안 좋아하시겠지만, 어지간해선 안 갈 생각이다. 가면 개발 공부 더 못할 거 같아서..



## Heavy-light Decomposition

헤비-라이트-분할- 구현은 입사하고 2주차였나? 그 때 했으니까 3개월 쯤 전에 했었다. LCA 공부를 하고 나서인지, 3개월 전에 봤을 때 머리 아파하면서 코드 짰던 거에 비해 훨씬 수월하게 했다.

가볍게 헤비 라이트 분할에 대해 설명하면, **트리 구조에서 세그먼트 트리로 구간을 관리하기 위해 적용하는 방법**이라고 이해하면 편하다. 트리를 여러 개의 경로로 쪼개서 각각 세그트리를 관리하는 느낌? 트리가 아닌 그래프에서는 적용이 힘들 것 같다. 두 점 사이의 경로가 하나 밖에 없는 트리의 특징 때문에 이 짓을 할 수 있는 것이다. -> 좀 더 생각해보니, 사이클 하나로 이루어진 그래프까지는 괜찮을 듯? 뭐 암튼 트리 제외 대부분의 그래프에서는 적용하기 힘들 것 같다.

그럼 이제 트리를 여러 개의 경로로 쪼개야한다. 당연히 적은 수의 경로로 쪼개야 묶어지는 구간, 즉 계산 최적화되는 부분이 많아질 것이다. 그렇다면 어떻게 해야 경로를 적당히 적게 자를건지 생각해보자. 나는 어떤 루트에서 출발해서, 직속 자식 노드를 루트로 하는 서브 트리의 크기가 가장 큰 쪽으로 이동하며 경로를 만들어 주었다. 더 큰 덩어리 쪽으로 이동한다고 이해하면 될 듯.

이렇게 여러 개의 경로로 쪼개고 난 뒤에는 세그먼트 트리를 적용해주었다. 코드와 같이 설명하는 게 편할 듯 하니, 바로 문제로 넘어가자.



## 트리와 쿼리 - [백준 13510](https://www.acmicpc.net/problem/13510)

> Heavy-light 분할

먼저 트리를 그리자. 루트 노드는 임의로 1이라 했다. 

```Python
def dfs1(idx):
    size[idx] = 1
    for adj in graph[idx]:
        if parent[idx] != adj:
            depth[adj] = depth[idx] + 1
            parent[adj] = idx
            dfs1(adj)
            size[idx] += size[adj]
            tree[idx].append(adj)
            if size[adj] > size[tree[idx][0]]:
                tree[idx][0], tree[idx][-1] = adj, tree[idx][0]


n = int(input())
graph = [[] for _ in range(n + 1)]
tree = [[] for _ in range(n + 1)]
size = [0] * (n + 1)
depth = [0] * (n + 1)
parent = [0] * (n + 1)
edges = [list(map(int, input().split())) for _ in range(n - 1)]
for x, y, _ in edges:
    graph[x].append(y)
    graph[y].append(x)
dfs1(1)
```

리스트 `size`는 서브 트리의 크기를 저장하는 친구로, 경로를 예쁘게 나누기 위해 사용했다. `depth`는 이후 답을 구하기 위해 사용하는 정보로, 루트 노드로부터 얼마나 떨어져 있는지를 저장한다. `parent`는 자신의 직계 부모 노드를 가리킨다. `edges`를 선입력 받은 것은 문제에서 `edges`의 인덱스로 접근해 업데이트를 해야하기 때문에 저렇게 저장해줬다.

그러면 이제 트리가 완성됐다. 그렇다면 이제 구간을 나눌 차례다.

```Python
def dfs2(idx):
    global cnt
    num[idx] = cnt
    cnt += 1
    for adj in tree[idx]:
        if tree[idx][0] == adj:
            top[adj] = top[idx]
        else:
            top[adj] = adj
        dfs2(adj)


top = [0] * (n + 1)
num = [0] * (n + 1)
cnt = 0
dfs2(1)
```

`top`은 자신이 속한 구간의 시작점, 즉 가장 꼭대기를 가리킨다. top[idx]는 idx가 속한 구간의 top node의 idx가 된다. `dfs1`을 수행할 때 가장 빠른 쪽에 가장 큰 서브 트리의 루트를 저장한 걸 이용해주면 된다. 글로벌 변수 `cnt`는 노드의 번호를 다시 매기기 위해 사용한다. 한 구간에 속한 노드들은 꼭대기부터 아래로 내려가면서 1씩 증가한다.

이제 구간을 다 나눴으니 세그 트리를 적용할 차례이다.

```Python
seg = [0] * (2 * n + 1)
for x, y, d in edges:
    if parent[x] == y:
        x, y = y, x
    seg[n + num[y]] = d
for i in range(n - 1, 0, -1):
    seg[i] = max(seg[2 * i], seg[2 * i + 1])
```

굉장히 평소에 하던 세그 트리 초기 작업과 유사하다. 주의할 점은 `idx`가 아닌 새로 매긴 노드 번호 `num[idx]`를 사용해야 한다는 점? 또한 간선 가중치를 하위 노드에 저장한다. 상위 노드에 저장하면 정보가 겹칠 수 있으니까 ㅇㅇ.

이제 거의 다 왔다. 쿼리에서 처리해야 할 건 1. 업데이트 2. 경로 내 최대 구하기 이렇게 2가지이다. 먼저 업데이트를 보면,  

```Python
for _ in range(int(input())):
    s, i, j = map(int, input().split())
    if s == 1:
        x, y, _ = edges[i - 1]
        if parent[x] == y:
            x, y = y, x
        now = n + num[y]
        seg[now] = j
        now //= 2
        while now:
            seg[now] = max(seg[2 * now], seg[2 * now + 1])
            now //= 2
```

정말 별 거 없다. 하위 노드가 속한 세그먼트를 갱신해주면 된다. 이제 답을 출력하는 코드를 보자.

```Python
for _ in range(int(input())):
    s, i, j = map(int, input().split())
    if s == 1:
        # Update
    else:
        result = 0
        while top[i] != top[j]:
            if depth[top[i]] > depth[top[j]]:
                i, j = j, i
            left = n + num[top[j]]
            right = n + num[j]
            while left <= right:
                if left % 2:
                    if result < seg[left]:
                        result = seg[left]
                    left += 1
                if not right % 2:
                    if result < seg[right]:
                        result = seg[right]
                    right -= 1
                left //= 2
                right //= 2
            j = parent[top[j]]
        if i != j:
            if depth[i] > depth[j]:
                i, j = j, i
            left = n + num[i] + 1
            right = n + num[j]
            while left <= right:
                if left % 2:
                    if result < seg[left]:
                        result = seg[left]
                    left += 1
                if not right % 2:
                    if result < seg[right]:
                        result = seg[right]
                    right -= 1
                left //= 2
                right //= 2
        print(result)
```

길지만 별 거 없다. 답 구하는 걸 함수화하는 게 좋았을 거 같긴 하다 ㅋㅋ `i`랑 `j`가 같은 구간에 속할 때까지 더 깊은 쪽 노드를 꼭대기까지 끌어올린다. 왜냐? (`j`가 더 깊다고 하면) `i`에서 `j`로 가려면 `j`의 꼭대기부터 `j`까지를 반드시 거쳐야 한다. 즉 이 구간 내에 답이 있을 수 있다. 그러면 살펴봐야 하는 구간은,

```Python
left = n + num[top[j]]
right = n + num[j]
```

요래 써질 것이다. 다 적용한 뒤에는 `j`를 위로 올려야하는데, `top[j]`까지의 정보는 모두 사용했으므로 그보다 한 칸 위인 `parent[top[j]]`로 올려주자. 그리고 같은 구간에 속했다면, 이제 그 구간만 답에 적용하면 된다. 그렇다면 그 구간은 아래와 같을 것이다.

```Python
left = n + num[i] + 1
right = n + num[j]
```

여기서 왜 `left`에 1을 더해주냐. 이는 우리가 간선 정보를 하위 노드에 저장했기 때문이다. `left`에 1을 더해주지 않으면 간선을 하나 더 보게 되므로 틀릴 것이다. 이대로 답을 출력해주면 끝!

대전의 박사들 퇴근 기다리면서 기계동 카페서 혼자 코드 좀 두드리다보니 완성됐다. 3달 전에는 왜 이걸 못한거지 싶을 정도로 쉽게 되버렸다.

헤비 라이트 분할보단 플로우를 먼저 할 줄 알았는데, 또다시 플로우가 뒷전으로 미뤄졌다. 미안해 플로우야...



## Cow Land - [백준 17033](https://www.acmicpc.net/problem/17033)

> Heavy-light 분할

```Python
from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 5)


def dfs(idx):
    for adj in graph[idx]:
        if parent[idx] != adj:
            parent[adj] = idx
            depth[adj] = depth[idx] + 1
            tree[idx].append(adj)
            dfs(adj)
            size[idx] += size[adj]
            if size[adj] > size[tree[idx][0]]:
                tree[idx][-1] = tree[idx][0]
                tree[idx][0] = adj


def dfs2(idx):
    global cnt
    num[idx] = cnt
    cnt += 1
    if tree[idx]:
        top[tree[idx][0]] = top[idx]
        dfs2(tree[idx][0])
        for adj in tree[idx][1:]:
            top[adj] = adj
            dfs2(adj)


def sol(idx, adj):
    left = n + num[idx]
    right = n + num[adj]
    result = 0
    while left <= right:
        if left % 2:
            result ^= seg[left]
            left += 1
        if not right % 2:
            result ^= seg[right]
            right -= 1
        left //= 2
        right //= 2
    return result


n, q = map(int, input().split())
val = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
size = [1] * (n + 1)
depth = [0] * (n + 1)
parent = [0] * (n + 1)
tree = [[] for _ in range(n + 1)]
dfs(1)
del graph, size
cnt = 0
num = [0] * (n + 1)
top = [0] * (n + 1)
top[1] = 1
dfs2(1)
seg = [0] * (2 * n)
for i in range(n):
    seg[n + num[i + 1]] = val[i]
for i in range(n - 1, 0, -1):
    seg[i] = seg[2 * i] ^ seg[2 * i + 1]
for _ in range(q):
    s, i, j = map(int, input().split())
    if s == 1:
        now = n + num[i]
        seg[now] = j
        while now > 1:
            now //= 2
            seg[now] = seg[2 * now] ^ seg[2 * now + 1]
    else:
        ans = 0
        while top[i] != top[j]:
            if depth[top[i]] > depth[top[j]]:
                i, j = j, i
            ans ^= sol(top[j], j)
            j = parent[top[j]]
        if depth[i] > depth[j]:
            i, j = j, i
        ans ^= sol(i, j)
        print(ans)
```

뭐 구조는 똑같다. 대신 완벽히 익혔는지 체크하기 위해 이전 코드 참고 안 하고 처음부터 쭉 짜봤다. 또한 이제 간선이 아닌 노드에 가중치가 있으므로 고려할 부분이 좀 더 줄어들었다.

한 달 동안 LCA에, 헤비라이트 분할에... 구현 가능한 알고리즘 폭이 더 넓어졌다. 이젠 정말 플로우를 해야할텐데... 암튼 헤비 라이트 분할 2문제를 풀었더니 2점이나 올랐다. class 8도 4문제 밖에 안 남았다 ㅎㅎ 
