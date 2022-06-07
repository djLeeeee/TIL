# 0606



## 구간 합 구하기 - [백준 2042](https://www.acmicpc.net/problem/2042)

세그먼트 트리

```python
from sys import stdin
from collections import defaultdict

input = stdin.readline


def update(node, s, e):
    tree[node] += t
    if s == e:
        return
    mid = (s + e) // 2
    if mid < target:
        update(node * 2 + 1, mid + 1, e)
    else:
        update(node * 2, s, mid)


def get_sum(node, s, e, start, end):
    if s > e:
        return
    if start == s and end == e:
        return tree[node]
    mid = (s + e) // 2
    if mid < start:
        return get_sum(2 * node + 1, mid + 1, e, start, end)
    elif mid >= end:
        return get_sum(2 * node, s, mid, start, end)
    else:
        return get_sum(2 * node + 1, mid + 1, e, mid + 1, end) + get_sum(2 * node, s, mid, start, mid)


n, m, k = map(int, input().split())
tree = defaultdict(int)
arr = []
for target in range(n):
    t = int(input())
    arr.append(t)
    update(1, 0, n - 1)
for _ in range(m + k):
    state, init, fin = map(int, input().split())
    if state == 1:
        t = fin - arr[init - 1]
        target = init - 1
        arr[init - 1] = fin
        update(1, 0, n - 1)
    elif state == 2:
        print(get_sum(1, 0, n - 1, init - 1, fin - 1))
```

ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 드디어 풀었다 ㅋㅋㅋㅋㅋㅋ 나한텐 이게 플레고 다이아 문제라고 ㅋㅋ

4달 전에 겁없이 아무 문제나 건들던 시절, 세그트리에 크게 데이고 나서 계속 미루던 문제다. 그러다 오늘에서야 더 이상 미룰 수 없어 풀었다.

원리는 잘 알고 있어 구현만 하면 됐다. 오늘 풀어보니 굳이 미룰 필요는 없었을 듯. 세그 트리 작동 원리는 워낙 유명하니 따로 안 써야지 ㅎ

통과는 됐지만, 문제는 시간이 너무 오래 걸렸다. 이럴 땐 뭐다? 고수 님들 코드 카피가 답이다. 파이썬 중에 시간이 제일 빠른 코드를 갖고 왔다.

```python
import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())

def ini_tree():
    for i in range(N):
        tree[N + i] = int(sys.stdin.readline().rstrip())
    for i in range(N - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]


def query(left, right):
    result = 0
    left += N - 1
    right += N - 1

    while left <= right:
        if left % 2 == 1:
            result += tree[left]
            left += 1
        if right % 2 == 0:
            result += tree[right]
            right -= 1
        left //= 2
        right //= 2

    return result


def update(idx, value):
    idx += N - 1
    tree[idx] = value
    idx //= 2
    while idx >= 1:
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
        idx //= 2


tree = [0] * (2 * N)

ini_tree()

query_update = []

for _ in range(M + K):
    query_update.append(list(map(int, sys.stdin.readline().rstrip().split())))

for q_u in query_update:
    if q_u[0] == 1:
        update(q_u[1], q_u[2])
    else:
        sys.stdout.write(str(query(q_u[1], q_u[2])) + "\n")
```

처음 보는 분이긴 한데, [joungju257](https://www.acmicpc.net/user/joungju257) 님의 코드다. 내 코드가 이 분 코드보다 5배 정도 오래 걸렸는데, 원인을 분석해보자. 

1. **함수 호출 회수가 적다.**

   재귀가 아닌 while 문으로 처리하는 게 더 좋긴 할 듯.

2. `ini_tree` **함수가 환상적이다**

   나는 왜 굳이 저따구로 짰는가... 이 분 방법이 훨씬 이해가 쉽다.

3. `defaultdict`**을 사용하지 않았다.**

어떻게 해야할지 방향성은 잡혔다. 드가자~



## 세그먼트 트리

```python
from sys import stdin

input = stdin.readline

n, m, k = map(int, input().split())
tree = [0] * (2 * n)
for i in range(n):
    tree[n + i] = int(input())
for i in range(n - 1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]
for _ in range(m + k):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        idx = query[1] + n - 1
        tree[idx] = query[2]
        idx //= 2
        while idx >= 1:
            tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
            idx //= 2
    elif query[0] == 2:
        result = 0
        left = query[1] + n - 1
        right = query[2] + n - 1
        while left <= right:
            if left % 2:
                result += tree[left]
                left += 1
            if not right % 2:
                result += tree[right]
                right -= 1
            left //= 2
            right //= 2
        print(result)
```

뭐 굳이 새로 쓰는 이유는.. joungju님 코드를 계속 쓸 순 없으니까. 내 스타일로 어레인지했다.

