# 1127

바쁜 1주일이었다. 대강 요약하면,

- 사이드 플젝 같이 하실 분들이랑 인사했다. Go 공부 열심히 하자.
- 플레 문제도 3문제? 정도 풀었다.
- 웹에서 컴포넌트?를 개발할 일이 생겼는데, 기존에 작업하신 웹페이지의 디자인 패턴이 나에겐 생소했다. 하나씩 뜯어보면서 이해해가는 중.
- LG CNS 코테 본선 갔다왔다. 재미로 갔는데, 문제가 별로여서 괜히 갔다고 후회 중이다
- 모바일 웹에서도 깃에다가 새 파일 만들고 커밋이 가능했다. 자주 쓰진 않을 거 같고 이동 중에 마크다운 파일 작성할 때 정도나 쓸 듯? 

Go 공부도 본격적으로 해보고, gRPC 내용도 슬슬 알아봐야겠다. 뭐 어찌됐건 여느때와 다름없이 오늘의 TIL은 알고리즘 풀이가 주 내용이다.

아 그리고 velog.io에 글을 처음 써봤다. 생각보다 UI가 깔끔하고 잘 돼 있었다. 여차하면 TIL 내용을 거기에도 올려볼까 고민 중이다. 아니면 재밌는 알고리즘 성질 정도? 시간이 날 때 좀 써보자



## 굉장한 학생 - [백준 2336](https://www.acmicpc.net/problem/2336)

> 세그먼트 트리

```Python
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
grade = [[0, 0, 0] for _ in range(n)]
for i in range(n):
    grade[a[i] - 1][0] = i + 1
    grade[b[i] - 1][1] = i + 1
    grade[c[i] - 1][2] = i + 1
grade.sort()
ans = 0
tree = [float('inf')] * (2 * n + 1)
for _, x, y in grade:
    idx = n + x
    while idx:
        if tree[idx] > y:
            tree[idx] = y
        idx //= 2
    temp = float('inf')
    left = n + 1
    right = n + x
    while left <= right:
        if left % 2:
            if temp > tree[left]:
                temp = tree[left]
            left += 1
        if not right % 2:
            if temp > tree[right]:
                temp = tree[right]
            right -= 1
        left //= 2
        right //= 2
    if temp >= y:
        ans += 1
print(ans)
```

이분 매칭을 처음 배웠을 때 어떻게든 매칭 문제로 바꿔서 풀어보려고 몸부림쳤었던 나름 유서깊은 문제다. 결국은 세그트리가 익숙해진 지금에서야 풀었지만.

첫번째 점수로 정렬을 한 뒤, 두번째 점수를 idx, 세번째 점수를 value로 하도록 트리를 만들어가자. 정렬을 했으므로 어떤 학생의 정보를 트리에 업데이트할 때, 두 세 번째 점수 둘다 낮으면 그 학생은 굉장한 학생이 아니다. 이제 이 점수가 둘다 낮은 걸 어떻게 체크해주냐가 메인 이슈다. 이때 조금 생각해보면 학생 정보를 저장한 뒤, 1 ~ idx 까지 중에 최저 등수가 value보다 작으면 안 된다는 걸 알 수 있다.

세그트리로 구현해주면 끝. 생각보다 싱겁게 풀려버렸다.



## 트리의 외심 - [백준 17399](https://www.acmicpc.net/problem/17399)

> LCA

세 개의 정점과 떨어진 거리가 같은 점을 찾는 문제였다. 트리의 거리 구하기? 이젠 DFS가 아닌 LCA로 해결할 수 있다. x, y, z 세 점에 대한 외심을 구해야 한다면,

1. 두 점 간의 거리가 홀수이면 외심은 없다. 자명.
2. x, y의 중간을 xy... 마찬가지로 정의하자. 만약 외심이 존재한다면, xy, yz, zx 중 적어도 두 개는 같은 값을 가진다. 그리고 그 값이 외심이 된다.

2번 성질로 문제를 풀면 된다. 그림을 그려보면 왜 저리 되는지 알 수 있다. 코드 자체도 문제 내용 그대로 구현하면 끝난다. 코드 첨부하러 가기 귀찮다



## Sky Tax - [백준 13896](https://www.acmicpc.net/problem/13896)

> LCA

```Python
from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 5)


def dfs(idx):
    size[idx] = 1
    for adj in graph[idx]:
        if not size[adj]:
            tree[idx].append(adj)
            parents[adj][0] = idx
            depth[adj] = depth[idx] + 1
            size[idx] += dfs(adj)
    return size[idx]


def lca(x, y):
    if depth[x] < depth[y]:
        x, y = y, x
    d = depth[x] - depth[y]
    for bit in range(20):
        if d >> bit & 1:
            x = parents[x][bit]
    if x == y:
        return x
    for bit in range(19, -1, -1):
        px = parents[x][bit]
        py = parents[y][bit]
        if px != py:
            x, y = px, py
    return parents[px][0]


for tc in range(1, int(input()) + 1):
    n, q, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    tree = [[] for _ in range(n + 1)]
    parents = [[0] * 20 for _ in range(n + 1)]
    size = [0] * (n + 1)
    depth = [0] * (n + 1)
    dfs(r)
    for t in range(1, 20):
        for i in range(1, n + 1):
            parents[i][t] = parents[parents[i][t - 1]][t - 1]
    nr = r
    print(f'Case #{tc}:')
    for _ in range(q):
        s, k = map(int, input().split())
        if s == 0:
            nr = k
        elif nr == k:
            print(n)
        else:
            rr = lca(nr, k)
            if rr == k:
                dd = depth[nr] - depth[k] - 1
                t = 0
                temp = nr
                while dd:
                    if dd % 2:
                        temp = parents[temp][t]
                    t += 1
                    dd //= 2
                print(n - size[temp])
            else:
                print(size[k])
```

문제를 한 줄 요약하면,

> 루트 노드가 계속 바뀔 때, 특정 노드를 루트로 하는 서브트리의 노드 갯수를 log n 에 구하여라!

처음 루트 노드 `r`, 나중에 바뀐 루트 노드 `nr`, 타겟 노드 `k`라 하자. 이제 처음 트리에 대해서 `nr`과 `k`의 위치 관계에 따라 답이 어떻게 되는지 보자. `lca = lca(nr, k)`일 때,

- **(중요)** `lca = k`이면 `k`에서 `nr`로 가는 길에서 첫 번째로 나오는 노드를 `t`라 했을 때, `k`를 루트 노드로 하는 서브트리의 노드 갯수는 `n - size[t]`가 된다! 
- `lca = nr`이면 `nr`을 노드로 하면 `k` 쪽 서브 트리들은 가만히 있으면 된다.
- 나머지 경우에선, `nr`과 `k`가 다른 브랜치에 속해 있다는 뜻이다. `nr`을 루트 노드로 다시 트리를 구성하는 걸 상상해보면, `nr`을 루트로 하는 서브 트리의 구성 요소는 바뀌지 않는다.

트리를 그림 그려놓고, 루트 노드의 위치에 따라 답이 어떻게 되는지 확인해보면 이해하기 쉽다.

평소의 LCA와 다르게, 서브 트리의 노드 갯수를 저장할 리스트 `size`를 답을 구하기 위해 추가했다. 또한, 재귀적으로 트리를 구성하면서 다른 부수적인 값들을 얻기 위해 DFS로 트리 구성을 구현한 부분이 조금 특이한 점?
