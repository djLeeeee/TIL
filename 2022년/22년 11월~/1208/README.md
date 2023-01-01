# 1208

드디어 gRPC를 어느 정도 끝냈다. 1주일 내내 들여다봤더니 오늘 아침에 갑자기 많은게 이해가 되기 시작했다. 물론 정상 작동하는지는 좀 더 들여다 봐야 할 듯. 그래도 계속 부딪히면서 확실히 뭔가 성장하는 것 같아 기분이 좋다 ㅎㅎ

TIL 정리하면서 보는데 누락된 다이아 문제가 하나 있었다. 풀이 정리 안 한 플레 문제는 한 두 개 있어도, 다이아를 정리 안 하는 건 좀 선 넘은 거 같아서 오늘이라도 정리하려 한다.



## 보석 가게 - [백준 13575](https://www.acmicpc.net/problem/13575)

> FFT, 분할 정복 거듭제곱

이 친구가 보름 동안 방치되어 있던 문제다. 사실 그럴만도 한게, FFT 풀이가 뭐 특별한 게 없다. k개의 수의 합으로 만들 수 있는 수의 종류를 구하는 문제이므로, 각 가치에 대해 존재하는 곳에 마킹을 하고, k번 거듭 제곱하면 된다. k가 크므로 당연히 분할 정복 거듭제곱 사용해주면 된다. FFT에 분할 정복 거듭제곱은 처음 써본 문제이긴 한데... 별 거 없다. FFT 다이아 문제는 진짜 너무 날먹인 듯.



## 남극 탐험 - [백준 2927](https://www.acmicpc.net/problem/2927)

> Heavy-light 분할, 분리 집합, 오프라인 쿼리

```Python
n = int(input())
penguins = list(map(int, input().split()))
parents = list(range(n + 1))
query = []
graph = [[] for _ in range(n + 1)]
trans = {
    'bridge': 0,
    'penguins': 1,
    'excursion': 2
}
for _ in range(int(input())):
    s, *xy = input().split()
    x, y = map(int, xy) 
    query.append((trans[s], x, y))
    if trans[s] == 0:
        px, py = find(x), find(y)
        if px != py:
            if py > px:
                px, py = py, px
            parents[px] = py
            graph[x].append(y)
            graph[y].append(x)
for i in range(2, n + 1):
    pi = find(i)
    if pi != 1:
        parents[pi] = 1
        graph[1].append(pi)
tree = [[] for _ in range(n + 1)]
depth = [0] * (n + 1)
size = [1] * (n + 1)
parent = [0] * (n + 1)
dfs(1)
del size, graph
num = [0] * (n + 1)
top = list(range(n + 1))
cnt = 0
dfs2(1)
seg = [0] * (2 * n + 2)
for i in range(n):
    seg[n + num[i + 1]] = penguins[i]
for i in range(n, 0, -1):
    seg[i] = seg[2 * i] + seg[2 * i + 1]
ans = []
parents = list(range(n + 1))
for s, x, y in query:
    if s == 0:
        px, py = find(x), find(y)
        if px != py:
            ans.append('yes')
            parents[px] = py
        else:
            ans.append('no')
    elif s == 1:
        now = n + num[x]
        seg[now] = y
        while now > 1:
            now //= 2
            seg[now] = seg[2 * now] + seg[2 * now + 1] 
    else:
        px, py = find(x), find(y)
        if px != py:
            ans.append('impossible')
        else:
            temp = 0
            while top[x] != top[y]:
                if depth[top[x]] > depth[top[y]]:
                    x, y = y, x
                temp += sol(top[y], y)
                y = parent[top[y]]
            if depth[x] > depth[y]:
                x, y = y, x
            temp += sol(x, y)
            ans.append(temp)
print(*ans, sep='\n')
```

트리 구조에서 업데이트가 일어나면서, 구간에서의 답을 구해야 한다? 의심의 여지가 없이 heavy-light 분할을 활용해줘야 한다. 하지만 여기서 한 가지 문제가 있다. 일반적인 분할 문제와 달리, 쿼리를 처리하면서 중간중간 간선이 새로 생긴다.(시작할 때 트리 형태가 아니다) 여기서 이 문제를 쉽게 해주는 조건이 하나 있다.

> 이미 연결된 섬들 간에는 간선을 잇지 않는다.

그렇다면 오프라인 쿼리로 모든 쿼리를 다 본 다음, 최소 스패닝 트리 하듯이 분리 집합으로 트리를 구성해준다. 모든 쿼리를 다 봤는데도 트리가 완성되지 않았다면, 각 컴포넌트들의 루트를 1(전체 트리의 루트)와 연결해주면 된다. 그래야 헤비라이트 분할하기 편하니까 ㅇㅇ

트리가 구성된 다음부터는 분할해주고, 쿼리 처리해주면 된다. 이때 건설 쿼리가 나온다면 다리를 지을 지 안 지을 지 알아야 하므로 분리 집합을 새로 해줘야 한다. 여행 쿼리 또한 분리 집합으로 시작점과 도착점이 연결되어 있는지 확인 가능하다. 

푸는 내내 재밌었다. 역시 그래프 문제가 고민하는 맛이 있다. 물론 못 풀면 기분이 좋지 않다. 요 문제 또한 클래스8 조건 문제 중 하나였다.



## Starting a Scenic Railroad Service - [백준 15337](https://www.acmicpc.net/problem/15337)

> 누적 합, 세그먼트 트리

```Python
from sys import stdin

input = stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
l = 10 ** 5
start = [0] * (l + 1)
end = [0] * (l + 1)
for x, y in arr:
    start[x] += 1
    end[y] += 1
for i in range(1, l + 1):
    start[i] += start[i - 1]
    end[i] += end[i - 1]
ans = [0, 0]
stack = []
seg = [0] * (2 * l)
for x, y in arr:
    p1 = start[y - 1] - end[x]
    if p1 > ans[0]:
        ans[0] = p1
    left = l + x - 1
    right = l + y - 2
    while left <= right:
        if left % 2:
            seg[left] += 1
            left += 1
        if not right % 2:
            seg[right] += 1
            right -= 1
        left //= 2
        right //= 2
for i in range(1, l):
    seg[2 * i] += seg[i]
    seg[2 * i + 1] += seg[i]
ans[1] = max(seg[l:-1])
print(*ans)
```

의자가 최대로 필요한 상황이 언제일지 생각해보면, **어떤 구간에 대해, 제일 많이 겹치는 구간의 갯수**가 된다. 음.. 그니까 임의의 구간 k에 대해 자신과 겹치는 구간의 갯수를 a<sub>k</sub>라고 정의했을 때, max(a<sub>k</sub>)를 구해주면 된다. 전체 시간 구간이 그렇게 길지 않으므로, 누적 합으로 처리 가능하다. 어떻게 구하는지는 코드에 굉장히 직관적으로 나타나있다.

그 다음은 의자가 최소로 필요한 상황이다. 요건 **가장 사람이 많은 순간 몇 명이 있었는지**를 구하면 된다. 마찬가지로 시간 구간이 그리 길지 않으므로 시간을 세그먼트로 관리해줄 거다. s~e 까지의 구간의 모든 칸에 1 씩 더해야 하는 작업을 우리는 세그로 쉽게 할 수 있다. 약간의 레이지 세그 느낌으로 얼마 더해야 하는지만 마킹하고 마지막에 합산해줬다. 여기서 한가지 주의할 점은, s~e 구간의 모든 칸에 1씩 더할 때 s부터 e-1번째 세그에만 표시해야 한다.(나는 시작점을 기준으로 구간을 나타냈기 때문에 그렇다.)

요 친구도 클래스8 문제 중 하나였다. 어쩌다보니 클래스8이 2문제 밖에 안 남았다. 10점 딱 대라~
