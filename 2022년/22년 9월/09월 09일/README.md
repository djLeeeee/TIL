# 0909

콴다 들어간지 어느새 한달이다. 시간이 참 빠르게 지나갔다.

추석 연휴 첫날이기도 하고 오늘은 느긋하게 보내야지



## 스포츠 전문 채널 GSK - [백준 8898](https://www.acmicpc.net/problem/8898)

이분 매칭

```Python
from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            check[idx] = True
            return 1
    return 0


def coloring(idx):
    used_a[idx] = False
    for adj in graph[idx]:
        if match[adj] != idx:
            used_b[adj] = True
            if used_a[match[adj]]:
                coloring(match[adj])


for _ in range(int(input())):
    n = int(input())
    start = [0] + list(map(int, input().split()))
    play = [0] + list(map(int, input().split()))
    dist = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d = list(map(int, input().split()))
        for j in range(i, n + 1):
            dist[i][j] = d[j - i]
            dist[j][i] = d[j - i]
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if start[i] + play[i] + dist[i][j] <= start[j]:
                graph[i].append(j)
    match = [0] * (n + 1)
    check = [False] * (n + 1)
    ans = []
    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        dfs(i)
    used_a = [True] * (n + 1)
    used_b = [False] * (n + 1)
    for i in range(1, n + 1):
        if not check[i]:
            coloring(i)
    ans = []
    for i in range(1, n + 1):
        if not used_a[i] and not used_b[i]:
            ans.append(i)
    print(len(ans))
    print(*ans)
```

한참 이분 매칭에 꽂혔을 때 봤던 문제다.

왼쪽에서 오른쪽(이분 그래프의 왼쪽, 오른쪽)으로 간선을 그릴 때, i번째 경기 후 j번째 경기를 중계할 수 있다면 간선을 이어주었다. 이렇게 하면 몇 개의 경기를 중계하지 않는 것을 정해, 모든 간선이 사라지게 하면 된다. 즉 최소 버텍스 커버를 찾아주면 된다! 그리고 이분 그래프에서 최소 버텍스 커버는 최대 매칭인 것은 잘 알려져 있다.

이분 매칭이야 별 이슈 없이 해냈다. 다만 최소 버텍스 커버를 찾아줄 때 좀 헤맸다. Alternative path였나? 대체 경로라고 불렀던 거 같긴 한데, 암튼 그걸 사용해서 구해줬다. 그래도 이전 문제에서 푼 적이 있어서 금방 했다.



## 배수와 약수의 개수 - [백준 1770](https://www.acmicpc.net/problem/1770)

폴라드 로, 밀러 라빈, 정수론

```Python
from random import randrange
from math import gcd


def power(a, b, mod):
    result = 1
    while b > 0:
        if b % 2:
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result


def Miller_Rabin(num, check):
    if num == check:
        return 1
    k = num - 1
    while True:
        x = power(check, k, num)
        if x == num - 1:
            return 1
        if k % 2:
            if x == 1:
                return 1
            break
        k //= 2
    return 0


def is_prime(t):
    checker = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for c in checker:
        if not Miller_Rabin(t, c):
            return 0
    return 1


def pollard_rho(t):
    global flag
    if not flag:
        return
    if t == 1:
        return
    if is_prime(t):
        if t in div:
            flag = False
            return
        div.add(t)
        return
    x = randrange(2, t)
    y = x
    c = randrange(1, 10)
    g = 1
    while g == 1:
        x = (x * x % t + c)
        y = (y * y % t + c)
        y = (y * y % t + c)
        g = gcd(x - y, t)
        if g == t:
            return pollard_rho(t)
    pollard_rho(g)
    pollard_rho(t // g)


for _ in range(int(input())):
    n = int(input())
    div = set()
    flag = True
    if not n % 4:
        if n == 4:
            print(1)
        else:
            print(-1)
        continue
    if not n % 2:
        div.add(2)
        n //= 2
    pollard_rho(n)
    if not flag:
        print(-1)
    else:
        ans = 1
        for i in range(1, len(div) + 1):
            ans *= i
        print(ans)
```

문제 내용 자체는 외우기 워낙 쉽다 보니, 걸을 때나 지하철 탈 때 틈틈이 고민했던 문제다. 그러다 오늘 머리 자르러 가는 지하철 안에서 풀이가 생각났다. 그리고 동생 머리 자르는 동안 지금까지 짜놓은 폴라드 로 구조체를 예전 백준 푼 문제에서 쓰윽 가져와 폰으로 해결했다 ㅋㅋㅋ 다이아 문제를 폰으로 풀어버리다니 해놓고도 어이가 없다 ㄹㅇ

10<sup>18</sup> 스케일의 소인수를 구해야 하니 폴라드 로와 밀러 라빈을 사용하는 건 자명했다. 이제 소인수를 구하고 난 뒤엔, 소인수들의 지수를 잘 조정해 약수의 개수가 `N`이 되도록 해야 한다. 소인수 분해 결과가 아래와 같다 하자.

$$
N = p_1^{s_1} p_2^{s_2} \cdots p_t^{s_t} \\
$$

문제 조건을 만족하는 수가 무한히 많은 상황은 언제인가를 생각해내는 것이 이 문제의 핵심이었다. 현재 사용한 `t`개의 소수 대신 다른 소수를 사용해서 조건에 맞는 수를 만들 수 있다면, 소수는 무한하므로 만족하는 경우도 무한히 많아진다. 즉, 우리는 **t개의 소인수만을 이용해서 수를 만들어야 한다!**

이제 조금만 더 생각해보면 답을 구할 수 있다. t개의 소인수만을 이용해야만 만들 수 있는 상황은 언제일까? 일단,우리는 이미 약수의 갯수를 구하는 공식을 알고 있다.

$$
M = p_1^{r_1} p_2^{r_2} \cdots p_t^{r_t} \; (s_i \le r_i) \\
(M의 \; 약수) = (r_1 + 1) \cdots (r_t + 1) = N
$$

그리고 문제가 원하는 건, 위 t개의 항을 곱한 결과를 `N`이 되도록 하는 것이다. 각 항은 1보다 커야 한다. 그리고 **어떤 항이 합성수(=pq)이면, 그 항의 값을 p로 하고 새로운 항을 만들어 그 값을 q로 하는 것이 가능해진다.** 즉, 모든 항은 1 보다 큰 합성수가 아닌 수여야 한다. 바꿔 말하면? 모든 항은 소수다! `N`이 t개의 소인수를 가지는데, t개의 소수의 곱으로 표현된다는 것은 모든 소인수분해 했을 때의 지수가 1이라는 뜻이 된다. 즉, 소인수분해를 해주고 지수가 2 이상이면 그대로 탐색을 종료해주면 된다.

그렇다면 무한하지 않은 경우가 가능할 때 답은 얼마일지 생각해보자. 이건 간단하다. 서로 다른 소수 t개의 순서를 정해주면 끝이다. 즉, 답은 t! 이 된다.

폰 파이썬 앱을 이용하긴 했지만, 아무래도 폰이다 보니 구현해놓은 폴라드 로 함수를 문제에 맞게 수정하기 힘들었다. 내가 이상하게 짠 거일지 모르지만, 기존의 폴라드 로 함수에서 2의 배수를 따로 체크하던 거를 함수 밖으로 빼줬다. 그와 동시에 4의 배수이면 안 되므로 4의 배수이면 탐색을 하지 않도록 했다. 작은 수에서의 예외 체크를 해주니 4일 때 1가지만 가능했다. 그대로 예외 처리를 해주어 AC.

2달 동안 남는 시간마다 고민한 문제였던만큼, 푸는 과정이 매우 재미있었다. 이제 다음으로 고민할만한 내용이 쉬운 문제를 찾아야 하는데...
