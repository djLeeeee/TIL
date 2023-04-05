# 0406

모처럼 새로운 알고리즘을 배웠다. 바로 본론으로 들어가자.



## 이산 로그 Discrete Logarithm

아래 식을 만족하는 정수 쌍이 있다고 하자.

$a^x \equiv y \mod p$

여기서 로그를 양변 씌운다 생각해보자. 물론 기존의 로그 정의와는 달라질 것이다.

$x \equiv \log_{a}y \mod p$

요게 대략적인 이산 로그의 개념이다. 해싱 등 실생활에 쓰인다는데, 뭐 그건 일단 넘어가자. 내가 관심있는 건, $\log_{a}y \mod p$를 어떻게 구할 것인가 이다.

여기서 chatGPT의 힘을 빌렸다. 구할 수 있는 방법을 물어보니 baby-giant step이라는 방법이 있다고 한다. 설명을 읽고 바로 코드를 짜봤다.

```Python
def dlp(p, b, n):
    # return \log_{b} n \mod p
    sp = int(p ** 0.5) + 1
    baby_steps = {}
    for i in range(sp + 1):
        q = power(b, i, p)
        if baby_steps.get(q) is None:
            baby_steps[q] = i
    giant_step = power(b, (p - 2) * sp, p)
    for j in range(sp + 1):
        if n in baby_steps:
            return j * sp + baby_steps[n]
        n *= giant_step
        n %= p
    return -1
```

이 친구는 보다시피 $\sqrt{p}$의 시간 복잡도를 가진다. 원리는 간단하다.
소수 p에 대해서, 페르마 소정리에 의해 $a^p\equiv a \mod p$를 만족한다.
이걸 이용해서, 이산 로그의 값이 $p$를 주기로 반복될 것을 알 수 있다.

제곱근 분할법의 개념을 여기서 갖고오자.
딕셔너리를 이용해 k = 1부터 $\sqrt{p}$까지 $a^k$의 값을 저장한다.
만일 이 딕셔너리에 찾는 값이 있다면? 바로 탐색 종료다.
없다면? 찾는 값에 $a^{-\sqrt{p}}$를 곱해주자. 페르마 소정리를 잘 써주자.
그리고 찾을 때까지 반복한다.

제곱근 분할법이 (대부분) 세그트리로 바꿀 수 있듯이, 이걸 구하는 알고리즘도 자연의 섭리에 따라 $\log p$에 구하는 방법이 있을 것 같았으나,
도무지 생각이 안 나 일단 포기하고 문제를 풀기로 했다.

이런 개꿀 알고리즘이 있을 줄이야. 바로 문제를 풀어보자



## 이산 로그 - [백준 4357](https://www.acmicpc.net/problem/4357)

> 이산 로그

```Python
def power(a, b, c):
    d = 1
    while b:
        if b % 2:
            d *= a
            d %= c
        a *= a
        a %= c
        b //= 2
    return d


def sol(p, b, n):
    sp = int(p ** 0.5) + 1
    baby_steps = {}
    for i in range(sp + 1):
        q = power(b, i, p)
        if baby_steps.get(q) is None:
            baby_steps[q] = i
    giant_step = power(b, (p - 2) * sp, p)
    for j in range(sp + 1):
        if n in baby_steps:
            return j * sp + baby_steps[n]
        n *= giant_step
        n %= p
    return -1


while True:
    try:
        x, y, z = map(int, input().split())
    except ValueError or EOFError:
        break
    res = sol(x, y, z)
    print(res if res != -1 else "no solution")
```

위 코드 그대로이다. 문제 자체가 이산 로그를 구하는 것이므로 그대로 적용해주자.

덕분에 점수가 1 올랐다. 이게 얼마만인가.



## N의 존재 - [백준 7936](https://www.acmicpc.net/problem/7936)

> 이산 로그

```Python
def sol(p, a, m):
    """
    :param p: prime number
    :param a:
    :param m:
    :return: q s.t (q^q + q^m) \equiv a \mod p
    """
    if p < 1000:
        for q in range(1, p * p - p + 1):
            if (power(q, q, p) + power(q, m, p)) % p == a:
                return q
        return -1
    x = 1
    while x < p:
        # y = log_{x}_{a - x^m} mod p
        y = dlp(p, x, (a - power(x, m, p)) % p)
        if y != -1:
            k = (y - x) % (p - 1)
            return k * p + x
        x += 1


for _ in range(int(input())):
    r = sol(*map(int, input().split()))
    if r >= 0:
        print(f'TAK {r}')
    else:
        print("NIE")
```

> 주어진 $m$, $p$, $a$에 대해 $n^n + n^m \equiv a \mod p$ 가 되는 $n$을 구하자!

페르마의 소정리 대환장 파티인 문제였다. 좌변을 좀 정리해보자. $n \equiv x \mod p$일 때

$n^n \equiv x^n \equiv x^{p - 1}\cdots x^{p - 1} \cdot x^{n \% (p - 1)} \equiv x^{n \% (p - 1)} \mod p$

편의를 위해 $n \equiv y \mod (p - 1)$ 라 하면,

$n^n \equiv x^y \mod p$ 이고 $n^m \equiv x^m \mod p$ 가 된다.

따라서 우리가 구하는 문제는 아래와 같이 다시 쓸 수 있다.

$x^y + x^m \equiv a \mod p$

여기서 뜬금없지만 NTT에서 하던 걸 갖고 오자.
$p$가 충분히 크다면 원시근 $k$를 가질 것이다.
그렇다면 $x=k$일 때, $k^y\equiv a - k^m$에서 우변의 값은 고정되고,
$y$는 반드시 존재한다. 물론 우변이 0이 아니라면.
그렇다면 $n \equiv (y - x)\times p + x$를 만족하므로,
$x$를 원시근으로 만들고 $y$를 찾아주면 된다!

...라는 흐름으로 가고 싶었는데 도무지 원시근을 찾는 방법을 모르겠다.
그래서 정말 무식하게 풀었다.

```Python
    x = 1
    while x < p:
        # y = log_{x}_{a - x^m} mod p
        y = dlp(p, x, (a - power(x, m, p)) % p)
        if y != -1:
            k = (y - x) % (p - 1)
            return k * p + x
        x += 1
```

바로 $x$ 를 1씩 증가해주면서 답 찾기... 근데 시간 초과가 안 떴다. 이게 왜 됨?

화욜 밤에 문제를 처음 읽고, 수요일 출퇴근 시간에 고민했더니 어찌저찌 풀렸다.
폴라드 로 이후 이렇게 해결한 게 정말 오랜만이라 재밌었다 ㅋㅋ



## 피보나미얼 - [백준 11397](https://www.acmicpc.net/problem/11397)

정수론 개념 문제 (정확히는 이산 로그 뿐이지만) 좀 풀었더니 수학 문제 더 풀고 싶어졌다.
그래서 적당한 문제 찾던 중 재밌어 보여서 잡은 문제다.

결국엔 피보나치 다 곱한 수를 소인수분해 해야하는데, 우리가 관심 있는 건 1000 이하의 소인수를 몇 개나 가지고 있느냐다.
그럼 피사노 주기를 각 1~1000에 대해서 구해주자!라고 접근했다가, 틀린 걸 알았다.
p가 1000까지 인 거고, n은 더 커질 수 있으니까...

그러다가 이미 구해놓은 주기들에서 재밌는 성질을 발견했다.
$t_p$를 소수 $p$의 피사노 주기라고 하면, $t_{p^2} = p \times t_p$를 만족했다.
$p=2$일 때만 2, 4, 8 부분에서 예외가 생겼다.
아쉽게도 이게 모든 수에 대해서 성립한다는 건 증명 못했다.
뭐 어찌됐건 1000까지 반례가 없는 걸 보면 수학의 아름다움에 의해 만족할 것이다.

그러면 이제 $F_n$은 $p$로 몇 번 나눠질 지 생각해보자. 이걸 $d_p$라 하면,

$d_p = \displaystyle{\sum_{k=1}^{\infty}} \left [ \frac{n}{t_{p^k}} \right ] = \displaystyle{\sum_{k=1}^{\infty}} \left [ \frac{n}{t_{p}\times p^{k - 1}} \right ]$

물론 마찬가지로 2는 예외 처리해주자.

```Python
n, m = map(int, input().split())
prime = [True] * 1001
for i in range(2, 32):
    if prime[i]:
        for j in range(2 * i, 1001, i):
            prime[j] = False
div = [0] * 1001
div[2] += n // 3
div[2] += n // 6
t = 6
while t <= n:
    div[2] += n // t
    t *= 2
for i in range(3, 1001):
    if prime[i]:
        p = i
        a, b = 0, 1
        t = 1
        while b:
            a, b = b, a + b
            a %= p
            b %= p
            t += 1
        while t <= n:
            div[p] += n // t
            t *= i
```

그러면 `div[p]`애는 `p` 로 몇 번 나눌 수 있는지 저장됐다! 이제 답을 출력해주자.

```Python
for i in range(2, m + 1):
    ans = float('inf')
    k = i
    for j in range(2, 32):
        if prime[j] and not k % j:
            c = 0
            while not k % j:
                c += 1
                k //= j
            ans = min(ans, div[j] // c)
    if k != 1:
        ans = min(ans, div[k])
    print(ans)
```

뭐 별 건 없다. 소인수 분해하고 각 소인수에 대해 답을 갱신해주자.


역시 수학이 점수 올리는 데에는 최고다.
