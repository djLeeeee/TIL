# 0717

내일 대면 수업이다. 후....

면접 본 곳에서 아직 연락을 안 준다. 떨어졌나보다 흑흑

이럴 땐 뭐다? 알고리즘으로 기분 전환을 하자~ 오늘도 틀렸던 문제 위주로 가자!



## 카드 게임과 쿼리 - [백준 24517](https://www.acmicpc.net/problem/24517)

게임 이론

```python
from sys import stdin

input = stdin.readline


def f(i, j):
    if i <= 0:
        dp[i][j] = 0
        return 0
    if dp[i][j] > -1:
        return dp[i][j]
    result = 1
    for bit in range(10):
        if (1 << bit) & j:
            result &= f(i - bit - 1, j - (1 << bit))
    dp[i][j] = result ^ 1
    return dp[i][j]


dp = [[-1] * 1024 for _ in range(65)]
ans = ''
for _ in range(int(input())):
    a, b, k = map(int, input().split())
    s = (k * k + k) // 2
    x, y = (b - a) // s, (b - a) % s
    if k % 2 and x % 2:
        if not f(y, (1 << k) - 1):
            ans += 'swoon\n'
        else:
            ans += 'raararaara\n'
    else:
        if f(y, (1 << k) - 1):
            ans += 'swoon\n'
        else:
            ans += 'raararaara\n'
print(ans.rstrip())
```

예엣날에 알고리즘 처음 했던 시절? 겁도 없이 플레 문제에 덤비던 시절이 있었다. 그 때가 그립긴 한데... 암튼 그 때 신촌 대회였나? 오픈 컨테스트에서 풀고 틀렸던 문제이다.

오늘 다시 보니, 스프라그 그런디 정리로 풀 수 있을 거 같아 쭉 그런디 수를 적어보니, n + 1의 배수일 때만 그런디 수가 0이었다... 하지만 WA.

천천히 생각했더니, 단순하게 그런디 수를 계산할 수 있는 문제가 아니었다. **카드를 (한 사이클에서) 중복 사용할 수 없기 때문**에, 자신의 턴에 뽑고 싶은 카드가 없을 수도 있다. 그렇게 다시 고민하다가, `k`의 범위가 10 이하라는 게 눈에 들어왔다. 그런디 수로 푸는 거라면 이렇게 작을 필요가 없을 것이고, 10~20 정도의 스케일이면 합리적 의심이 가능한 풀이가 있다. 아마도 2<sup>k</sup> 스케일의 풀이가 정답이라는 뜻. 그럼 2<sup>k</sup>를 어디다 쓸 수 있는 지 생각해보면... 비트 연산이지 뭐

남은 수를 `i`, 남은 숫자 카드의 비트 표시를 `j`라 하자. 그 다음 `f(i, j)`를 지금 턴에서 이길 수 있으면 1을, 지면 0을 반환하도록 하자. 그러면,

- `i`가 0 이하면 졌다
- `j`와 비트 체크를 해서 `b`번째 비트가 체크되어 있다 해보자. 그러면, `f(i - b, j - 2<sup>b</sup>)`는 현재 상황에서 `b`를 고른 것을 의미한다. 그러면, 고를 수 있는 숫자를 모두 골라보고 얻은 각각의 `f`가 모두 1이라면, 이 플레이어는 패배한 것이다. 왜냐? 지금 어떤 수를 골라도 다음 플레이어에게 승리 플랜이 존재하는 거니까.
- 이외의 상황이라면 승리 플랜이 존재한다.

이제 구현만 해주면 된다! 당연하지만, 한 사이클에서 얻을 수 있는 합이 정해져 있고 그 사이클에 소모되는 턴이 정해져 있으니 적당히 가공해 주,면 AC.

이제 틀린 문제가 32문제 남았다. 20대까지 해보자!



## 마지막 팩토리얼 수2 - [백준 2554](https://www.acmicpc.net/problem/2554)

정수론

```Python
tail = {2: 6, 6: 8, 8: 4, 4: 2}
n = int(input())
if n == 1:
    print(1)
    exit()
ans = 1
while n > 0:
    r, s = n // 5, n % 5
    if r % 2:
        ans *= 4
    else:
        ans *= 6
    for ss in range(1, n % 5 + 1):
        ans *= ss
    ans %= 10
    for _ in range(r % 4):
        ans = tail[ans]
    n = r
print(ans)
```

이것도 겁없던 시절 문제를 잘못 이해해 틀렸던 문제다. 오늘 다시 보니... 상당히 할만하다. 딱히 막히는 거 없이 풀었던 거 같다.

핵심은, 5로 나눈 나머지를 계속 보면 된다는 것이다. 2의 개수가 5의 개수보다 많을 게 확실하니까, 5의 개수로 답을 판별하는 것. 5로 나눈 나머지가 1, 2, 3, 4인 연속한 네수를 곱하면 맨 뒷자리가 4이므로, 이 것들만 또 곱하면 4-6-4-6... 순으로 반복될 것이다. 그 다음은 5를 곱해줘야 하는데, 답이 2, 4, 6, 8 중 하나일 거니까, 5를 곱한 횟수에 따라 어떻게 바뀔 지 쉽게 알 수 있다. (이 역할을 `tail`이 수행한다.)

다 풀고 다른 분 풀이를 보는데, 파이썬 숏코딩에서 재밌는 연산을 발견했다. 바로 `:=`.

```python
a = 12
b = (a := a // 5) + 1
print(a, b) # 2 3
```

파이썬도 저런 게 존재했었다. 뭐 실전에서 쓸 일은 많이 없을 거 같고, 숏코딩할 때 애용할 듯?

틀린 플2 문제도 풀고~ 점수도 1점 올리고~ 2문제만 더 고치면 20대 진입이다.



## 도박사 곰곰 - [백준 25199](https://www.acmicpc.net/problem/25199)

누적합, DP

```Python
from collections import defaultdict

div = 10 ** 9 + 7
n, m = map(int, input().split())
cnt = [0] * (m + 1)
for num in map(int, input().split()):
    cnt[num] += 1
y = max(cnt)
for i in range(m, 0, -1):
    if cnt[i] == y:
        x = i
        break
dp = [defaultdict(int) for _ in range(m + 1)]
for i in range(n + 1):
    dp[0][i] = 1
for i in range(1, x):
    for j in range(n + 1):
        dp[i][j] = dp[i - 1][j] - dp[i - 1][j - y - 1]
    for j in range(n + 1):
        dp[i][j] += dp[i][j - 1]
        dp[i][j] %= div
for i in range(x, m + 1):
    for j in range(n + 1):
        dp[i][j] = dp[i - 1][j] - dp[i - 1][j - y]
    for j in range(n + 1):
        dp[i][j] += dp[i][j - 1]
        dp[i][j] %= div
print((dp[m][n] - dp[m][n - 1]) % div)
```

으... 풀면서 머리 아파 죽는 줄 알았다.

곰곰이가 `x`를 `y` 개 뽑은 게 최선이라 하자. 이제, 아래 식을 생각해보자.

$$
(1+t+\dots+t^y)^{x-1}\ \times (1+t+\dots+t^{y-1})^{m-x+1} 
$$

이 식의 t<sup>n</sup>의 계수가 답이 된다. `x-1`을 최대 `y`개 뽑고, `x` 이상의 수를 최대 `y-1`개 뽑는 상황의 가지수를 구해야 하는데, 위 식을 보면 감이 올 것이다. 누적합으로 한 이유는, 계수 계산을 빨리 하기 위해서다.



## 곰곰이와 자판기 - [백준 25200](https://www.acmicpc.net/problem/25200)

이분 탐색

```Python
from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def sol(idx):

    def search(edge_idx):
        if memo[edge_idx]:
            return memo[edge_idx]
        s, e = edge[edge_idx]
        if not graph[e] or graph[e][-1] < edge_idx:
            memo[edge_idx] = e
            return e
        start = 0
        end = len(graph[e]) - 1
        while start <= end:
            mid = (start + end) // 2
            if graph[e][mid] >= edge_idx:
                result = graph[e][mid]
                end = mid - 1
            else:
                start = mid + 1
        memo[edge_idx] = search(result)
        return memo[edge_idx]

    if not graph[idx]:
        return idx
    return search(graph[idx][0])


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
edge = []
memo = [0] * m
for i in range(m):
    x, y = map(int, input().split())
    edge.append((x, y))
    graph[x].append(i)
print(*[sol(i) for i in range(1, n + 1)])
```

모든 간선을 그리고, 첫번째 간선에서 출발해서 도착 지점으로 이동한다. 그 이후 도착 지점에서 출발하면서 나중에 나온 간선을 찾아줘야 한다. 그래서 이분 탐색으로 해줬다. 근데...

```Python
# ojhoney92 님의 풀이
# https://www.acmicpc.net/source/43497292
import sys; read = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, read().split())
    query = []
    for _ in range(M):
        u, v = map(int, read().split())
        query.append([u-1, v-1])
    
    ans = [i for i in range(N)]
    
    for u, v in query[::-1]:
        ans[u] = ans[v]
    
    print(*[a+1 for a in ans])
```

뒤에서부터 쿼리를 처리를 하면 이런 복잡한 과정이 필요 없었다... 

뭐 그래도, 틀린 문제가 이제 29문제 남았다. 초기 목표는 달성했으니 다행이지만... 내일 대면 수업인데 벌써 새벽 4시다 ㅋㅋ 어떻게든 되겠지