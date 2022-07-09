# 0709

며칠만의 TIL인가....

일주일 동안 원없이 논 거 같다. 번아웃? 까진 아니었던 거 같은데, 이렇게 놀고 나니 알고리즘 문제들이 다시 잘 풀리는 기분이다.

아예 문제 안 푼 건 아니고, solved.ac 한별이 여름 엽서 이벤트 점수 채우기 용으로 플레 그래프 문제 10문제 정도 푼 듯하다. 사실 2일 전부터 쓰려고 했는데, 최근 잡고 있는 [다이아 문제](https://www.acmicpc.net/problem/1626)가 더어어ㅓ어어럽게 안 풀려서 TIL에 쓸 내용이 없었다. 풀고 만다...

이외에도 socket.io를 좀 자습했다. 1주일 정도 공부하면서 내린 결론은,

> 공식 문서는 답을 알고 있다.

진짜 모르겠으면 공식 문서 읽자. 없는 게 없다.

사이드 프로젝트로 방송? 느낌의 플랫폼을 제작해보고 있는데(트위치 같은 느낌), 모듈화를 통해 소켓을 여러 개 양산해내는 것은 해냈지만 완전히 분리시키는 걸 실패했다. 내 생각에는, 서버도 모듈화해서, 서버를 분리해야 데이터가 따로따로 관리될텐데 이렇게 할 바엔 제대로 된 db와 서버를 만드는 게 낫다고 생각이 든다. 그래서 일단은 한 서버 안에서, 소켓에 마킹?이라고 해야 하나 이름을 지어준다? 느낌으로, 어느 소켓에 데이터를 전송해야 하는지 표시해주는 쪽으로 진행할 생각이다.  



## 폴라드 로 알고리즘

소인수분해 알고리즘인데, 상당히 골 때린다.

> [참고] 소인수 분해 알고리즘 #3 폴라드 로 알고리즘, ruz, 2020.09.03, tistory
>
> https://aruz.tistory.com/140

```python
from random import randrange
from math import gcd


def pollard_rho(t):
    if t == 1:
        return
    if not t % 2:
        div.append(2)
        pollard_rho(t // 2)
        return
    if is_prime(t):
        div.append(t)
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
```

`is_prime`은 밀러 라빈으로 구현한 함수다. 뭐 이건 일단 넘어가고.

어떤 2차 함수 `f`와 어떤 소수 `p`를 잡자. 

함수의 변수에 함수의 대입값을 다시 집어넣는... 말로 표현 못 하겠는데...
$$
x = x_0,f(x_0),f(f(x_0)),f(f(f(x_0)))...
$$
위에 처럼 쭉 대입을 하면서 `mod p`를 해주면, 분명 사이클이 생길 것이다. 증명 과정은 넘어가자. 아름다운 수학이라면 분명 생길 거란 느낌이 들긴 한다. 암튼 사이클이 생길 때까지 돌리다 보면, 분명 두 연속된 `x`에 대해 차이값이 소인수분해할 수와 최대공약수를 가지는 시점이 생길 수 있다. 그렇다는 건 뭐다? 그 최대공약수가 타겟의 인수가 된다. 대입하는 식을 잘 보면 이해할 수 있다.

```python
        if g == t:
            return pollard_rho(t)
```

사이클을 보도록 인수를 못 찾았으면, random 인수 설정이 잘 못 됐다는 뜻으로, 처음부터 다시 시작한다. 다시 시작하면 random 인수도 변경될 것이다.

이제 실전으로 가자.



## :diamond_shape_with_a_dot_inside: 큰 수 소인수분해 - [백준 4149](https://www.acmicpc.net/problem/4149)

폴라드 로, 밀러 라빈

```python
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
    if not t % 2:
        ans.append(2)
        pollard_rho(t // 2)
        return
    if is_prime(t):
        ans.append(t)
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


target = int(input())
if is_prime(target):
    print(target)
    exit()
ans = []
pollard_rho(target)
ans.sort()
print(*ans, sep='\n')
```

폴라드 로 알고리즘을 활용하면 바로 풀 수 있는 문제였다.

주의할 점은, 폴라드 로 알고리즘은 인수를 찾아줄 뿐 그 인수가 소수임을 보장하지 않기 때문에, 밀러-라빈으로 소수 판정을 하면서 인수 중 소수인 것을 소인수 목록에 추가해줬다. 

이거 말고도 두 문제 더 풀었다. 폴라드 로 알고리즘 코드를 그대로 사용했다. 특별한 건 없다.

- [백준 13926 gcd(n, k) = 1](https://www.acmicpc.net/problem/13926)
- [백준 10854 Divisions](https://www.acmicpc.net/problem/10854)