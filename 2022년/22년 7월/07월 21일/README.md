# 0721



## :diamond_shape_with_a_dot_inside: All Kill - [백준 18527](https://www.acmicpc.net/problem/18527)

수학, 경우의 수

```Python
from sys import stdin

input = stdin.readline


def power(a, b):
    result = 1
    while b > 0:
        if b % 2:
            result *= a
            result %= div
        a *= a
        a %= div
        b //= 2
    return result


div = 998244353
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
ans = 1
m += 1
for x in arr[::-1]:
    m -= x - 1
    ans *= m
    ans %= div
ans *= power(m, div - 2) * (m - n)
ans %= div
print(ans)
```

> [참고] 백준 18527 All Kill, seastar105, 2021.03.22, Tistory
>
> https://seastar105.tistory.com/90

옛날에 위 분 블로그에서 다른 문제를 보다가 문제 제목을 보고 재밌어보여서 읽은 적이 있었다. 북마크만 해놨다가 오늘 문제 다시 읽어봤는데, 풀이가 거의 기억나서 그대로 풀었더니 AC. 다시 저 분 글을 읽어보니 코딩까지 비슷한 느낌?

모든 문제 풀이가 가능하도록 배치를 하는 경우의 수를 구하면 된다. 뒤의 번호를 먼저 배치하는 게 편할 것이다. 그게 제약사항이 더 적으니까. 전체 남은 시간에서, 뒤의 번호들이 걸리는 시간의 합 전에는 아이디어를 떠올려야 하므로, 배치할 수 있는 경우의 수는 아래와 같이 구할 수 있다.

```Python
for x in arr[::-1]:
    m -= x - 1
    ans *= m
    ans %= div
```

하지만, 이것까지만 해선 답이 아니다. 실제로 이대로 제출했다가 WA를 받았다. 몇 가지 이유가 있는데,

- 각 구간이 겹칠 수 있다.
- 겹쳤을 때 우선순위가 낮은 애들이 밀려나가야 하는데, 밀려나가면서 시간 구간을 초과할 수 있다.

배치를 원형 구간에 배치하는 것으로 생각하면, 이 이슈들을 해결할 수 있다. 이제 풀이를 바꿔보자.

1. 위 방법대로 경우의 수를 구한다. (원형에 배치하는 경우에도 경우의 수는 일단 같다.)
2. 시작점을 정한다. 시작점이 배치될 수 있는 곳은 각 구간의 시작점과 끝점, 또는 빈 구간이다.
3. 중복이 생길 수 있다. 중복이 생기는 가짓수는, 전체  남은 구간의 길이만큼이다.

그래서 `ans *= power(m, div - 2) * (m - n)` 이 부분이 생겨났다. 이 때, 나누는 연산은 페르마 소정리로 해준다.

처음으로 푼 루비 문제다! 온전히 노베이스에서 시작한 풀이는 아니었지만, 그래도 기억해내서 코드를 짰다는 데에 의의를 두자. 사실 개인적으로, 루비 정도의 난이도 문제는 아닌 거 같긴 하다. 실제로도 난이도 기여에 다이아로 배정했다. 솔직히 이런 것보다 폴라드 로에 이분 탐색 쓰는 Lugguage였나? 아니면 Algorithm teaching 같은 문제가 훨씬 어려웠지... 루비 문제는 범접할 수 없는 그 특유의 오오라가 있어야 하는데 이 문제에서는 느낄 수가 없었다.

추가로, 루비 문제는 어떤 이모티콘으로 표시할 지 생각해봐야할 거 같다. 뭐 루비 문제를 얼마나 더 풀 수 있을까 싶다만은...



## :diamond_shape_with_a_dot_inside: 최고인 대장장이 토르비욘 - [백준 13361](https://www.acmicpc.net/problem/13361)

분리 집합

```Python
from sys import stdin
from collections import defaultdict

input = stdin.readline


def find(target):
    if not parent[target]:
        parent[target] = target
    if parent[target] != target:
        parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    pa, pb = find(a), find(b)
    if pa == pb:
        is_cycle[pa] = True
    elif pa < pb:
        parent[pb] = pa
        if is_cycle[pb]:
            is_cycle[pa] = True
    else:
        parent[pa] = pb
        if is_cycle[pa]:
            is_cycle[pb] = True


n = int(input())
ans = 0
parent = defaultdict(int)
is_cycle = defaultdict(bool)
for _ in range(n):
    x, y = map(int, input().split())
    ans += x + y
    union(x, y)
memo = defaultdict(list)
for key in parent:
    memo[find(key)].append(key)
for key in memo:
    if is_cycle[key]:
        ans -= sum(memo[key])
    else:
        ans -= sum(memo[key]) - max(memo[key])
print(ans)
```

다이아 문제 중에서 꽤 많은 사람이 푼 문제에 속하지 않을까 싶다. 그렇지만 아이디어는 쉽지 않았다.

'분리 집합'에 한참 꽂혀있을 때 처음 봤던 문제다. 그 때는 키워드를 미리 보고 문제를 푸는 나쁜 버릇이 있었어서... 암튼 일본어 문제 [분리 계획](https://www.acmicpc.net/problem/24452)과 함께 눈여겨봤던 문제다. 분리 계획은 바로 풀었지만, 이 친구는 상당히 오래 걸렸다. 사실 오늘 푼 것도 분리 집합이라는 키워드를 몰랐다면 끝까지 못 풀었을 거 같다.

풀이로 넘어가자. **'철판을 모두 사용하여 검을 만드는 방법이 존재하는 입력만 주어진다.'** 라는 조건이 이 문제의 탐색 시간을 줄여준다. 만약 없다면? 단순 O(n<sup>2</sup>)의 DP 문제가 되지 싶다. 그래서 이걸 어떻게 분리 집합으로 푸냐.두 길이 `x`와 `y`가 주어지면, 두 길이의 값을 나타내는 노드를 연결한다. 이 때, 사이클이 있는지 체크한다. 모든 철판의 길이들에 대해 이 작업을 하면, 여러 연결된 컴포넌트들이 있을 것이다. 이 때, 연결된 컴포넌트들은 두 가지 중 하나이다.

1. v = e + 1, 즉 트리인 경우이다.
2. v = e, 즉 사이클이 존재하는 경우이다.

왜 2가지 밖에 없냐면, 우리가 그린 간선의 의미를 생각해봐야 한다. 간선에서 양 끝 점 중 하나를 너비로 사용해야 한다. 이 때, 너비를 모두 다르게 사용해야 하므로, 각 간선이 고른 점이 서로 겹치면 안 된다. 그렇다는 것은 `v`가 `e` 이상이여야 하는데, 연결된 컴포넌트에서 이걸 만족하는 건 위에 2가지 경우 밖에 없다.

그렇다면 각 경우에 대해서 답을 어떻게 구해야 하는지 보자. 먼저 사이클이 있는 경우엔, 각 노드들이 나타내는 길이의 합만큼이 너비로 사용되야한다. 왜냐? 노드랑 간선의 개수가 같으니까 일대일 대응으로 모두 사용될 것이다. 그리고 트리 구조라면 한 개의 노드를 사용하지 않아도 되는데, 이 때는 가장 길이가 큰 노드를 사용하지 않는 게 이득이다. (사용하지 않는다는 말은, 해당 간선이 의미하는 철판에서 그 길이를 높이로 사용하겠다는 의미이다.) 그리고 우리가 임의로 어떤 노드를 사용하지 않아도, 간선과 노드를 일대일 대응이 항상 가능하다. 그래서 길이 전체 합을 구하고, 너비로 사용할 길이들을 빼주는 방식으로 답을 구했다.
