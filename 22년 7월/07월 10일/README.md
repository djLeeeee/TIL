# 0710

어느새 점수가 반올림하면 2400점이 되는 점수가 됐다.

다이아4에서 점수 안 올라서 조금 힘들었는데... 시작하고 3달 만에 2200점 다이아를 갔는데, 그 다음 3달동안 160점 밖에 못 올리긴 했지만... 루비는 갈 수 있는건가??



## 화려한 마을 - [백준 12999](https://www.acmicpc.net/problem/12999)

mo's 알고리즘

```python
from sys import stdin
from collections import defaultdict

input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
querys = []
for i in range(m):
    s, e = map(int, input().split())
    querys.append((s - 1, e - 1, i))
sn = n ** 0.5
querys.sort(key=lambda x: (x[0] // sn, x[1]))
ans = [0] * m
cnt = defaultdict(int)
cnt_inv = defaultdict(int)
cnt_inv[0] = n
ps, pe, _ = querys[0]
for idx in range(ps, pe + 1):
    cnt_inv[cnt[arr[idx]]] -= 1
    cnt[arr[idx]] += 1
    cnt_inv[cnt[arr[idx]]] += 1
mx = max(cnt.values())
for s, e, i in querys:
    if ps < s:
        for idx in range(ps, s):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] -= 1
            cnt_inv[cnt[arr[idx]]] += 1
            if not cnt_inv[mx]:
                mx -= 1
    elif s < ps:
        for idx in range(s, ps):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] += 1
            cnt_inv[cnt[arr[idx]]] += 1
            if cnt[arr[idx]] > mx:
                mx = cnt[arr[idx]]
    if pe < e:
        for idx in range(pe + 1, e + 1):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] += 1
            cnt_inv[cnt[arr[idx]]] += 1
            if cnt[arr[idx]] > mx:
                mx = cnt[arr[idx]]
    elif e < pe:
        for idx in range(e + 1, pe + 1):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] -= 1
            cnt_inv[cnt[arr[idx]]] += 1
            if not cnt_inv[mx]:
                mx -= 1
    ps, pe = s, e
    ans[i] = str(mx)
print('\n'.join(ans))
```

업데이트가 없으면 mo's로 뚝딱~ 특별히 설명할 포인트는 없다. 



## :diamond_shape_with_a_dot_inside: 제곱수의 합 (More Huge) - [백준 17633](https://www.acmicpc.net/problem/17633)

폴라드 로, 밀러 라빈, 라그랑지 네 제곱수 정리, 르 장드르 세 제곱수 정리, 페르마의 두 제곱수 정리

```python
from collections import defaultdict
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
    if t == 1:
        return
    if is_prime(t):
        div[t] += 1
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


def sol(t):
    while not t % 4:
        t //= 4
    if t % 8 == 7:
        return 4
    if int(t ** 0.5) * int(t ** 0.5) == t:
        return 1
    if not t % 2:
        t //= 2
    pollard_rho(t)
    for key, value in div.items():
        if key % 4 == 3 and value % 2:
            return 3
    return 2


target = int(input())
div = defaultdict(int)
print(sol(target))
```

> [참고] 제곱수의 합, ho94949, 2019.10.18, 삼성소프트웨어멤버십
>
> http://www.secmem.org/blog/2019/10/18/sum-of-squares/

위 글이 없었으면 저얼대 못 풀었을 거 같다. 옛날에 DP였나? 로 훨씬 작은 스케일의 문제를 풀었을 때, 위 글을 읽어봤었다.

폴라드 로 관련 문제를 보는데 위 글에서 봤던 기억이 있는 문제가 있었다. 글에서는 네 개의  수를 구하는 것까지 구현되어 있지만, 가우스 인수라는 개념이 아직은 잘 이해되지 않아 이해되는 부분까지의 문제만 풀었다. 네 개의 수를 구하는 건 루비2 난이도로, 괜히 루비가 아닌 거 같다.. 사용된 정리들을 쭉 보자.

> #### 라그랑지 네 제곱수 정리
>
> 모든 자연수는 네 제곱의 합으로 표현이 가능하다.
>
> #### 르 장드르 세 제곱수 정리
>
> n = 4<sup>a</sup> (8b + 7) 꼴이 아닌 모든 자연수는 세 제곱의 합으로 표현이 가능하다.
>
> #### 페르마 두 제곱수 정리
>
> 소인수 중 4k+3의 지수가 홀수가 없으면 두 제곱의 합으로 표현이 가능하다.

즉, 위 세 정리를 종합하여 input이 타겟, output이 필요한 제곱의 최소 숫자로 하는 `sol` 함수를 짜보면 아래와 같다.

```python
def sol(t):
    while not t % 4:
        t //= 4
    if t % 8 == 7:
        return 4
    if int(t ** 0.5) * int(t ** 0.5) == t:
        return 1
    if not t % 2:
        t //= 2
    pollard_rho(t)
    for key, value in div.items():
        if key % 4 == 3 and value % 2:
            return 3
    return 2
```

폴라드 로와 밀러 라빈은 미리 짜놓은 게 있어서 조금만 수정해서 사용했다.



## :diamond_shape_with_a_dot_inside: Lugguge - [백준 20226](https://www.acmicpc.net/problem/20226)

폴라드 로, 밀러 라빈, 이분 탐색

```python
from sys import stdin, setrecursionlimit
from collections import defaultdict
from random import randrange
from math import gcd

input = stdin.readline
setrecursionlimit(10 ** 5)


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
    if t == 1:
        return
    if not t % 2:
        div_p[2] += 1
        pollard_rho(t // 2)
        return
    if is_prime(t):
        div_p[t] += 1
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


def dfs(num, idx):
    if idx == n:
        div.append(num)
        return
    t = div_arr[idx]
    for exp in range(div_p[t] + 1):
        dfs(num * t ** exp, idx + 1)


ans = []
while True:
    target = int(input())
    if not target:
        break
    if target == 1:
        now = 3
    elif is_prime(target):
        now = target + 2
    else:
        div_p = defaultdict(int)
        pollard_rho(target)
        div = []
        div_arr = list(div_p)
        n = len(div_p)
        dfs(1, 0)
        div.sort()
        m = len(div)
        now = target + 2
        for i in range(m):
            if div[i] ** 3 > target:
                break
            remain = target // div[i]
            start = i
            end = m // 2 + 1
            while start <= end:
                mid = (start + end) // 2
                if div[mid] * div[mid] > remain:
                    end = mid - 1
                else:
                    res = mid
                    start = mid + 1
            for j in range(res, i - 1, -1):
                if not remain % div[j]:
                    if now > div[i] + div[j] + remain // div[j]:
                        now = div[i] + div[j] + remain // div[j]
                    break
    ans.append(now)
print(*ans, sep='\n')
```

내일 수업 때문에 일찍 자려고 하는데... 머리 속에서 풀이가 일렁거려서 도무지 잠을 잘 수가 없더라. 폴라드 로 쓰는 건 당연하고, 이제 이후 풀이가 문제였다. 전체 약수를 dfs로 뽑아내고 정렬을 한 다음 이분 탐색으로 가능한 조합을 찾았다. 이 때, 최적화에 많이 신경 써줬다. 

1. `div[i]`는 세 수 중 제일 작은 수이다. 이 수는 타겟의 세제곱근보다 작거나 같아야 한다.
2. `div[j]`는 세 수 중 중간이다. 이 수는 `div[i]`로 나눈 값의 제곱근보다 작거나 같아야 한다. 이 때 `j`의 최댓값 `res`를 이분 탐색으로 찾아줬다.
3. 이제 `res`부터 1 씩 감소하면서 `j`를 설정하면서, 나눠지는 시점을 찾는다. 나눠지는 순간, 추가 탐색을 할 필요는 없으니 그대로 종료한다.

2시에 자려했지만 3시에 자게 됐다. 흠.... 점수 올린 거로 만족하자...
