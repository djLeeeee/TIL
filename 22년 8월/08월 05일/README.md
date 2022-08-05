# 0805

SSAFY를 퇴소했다. 근 200일 동안 몸을 담았던 곳이다보니 막상 떠나려니 시원섭섭하다. 이제야 플젝에 흥미가 붙었기도 했었고... 사필귀정이라는 말이 생각난다. 계속 열심히 살아보자. 콴다 수학 엔진 개발도 상당히 재밌어 보이니까



## Rasterized Lines - [백준 23362](https://www.acmicpc.net/problem/23362)

폴라드 로, 밀러 라빈, 오일러 피 함수

```Python
from sys import stdin, setrecursionlimit
from collections import defaultdict
from random import randrange
from math import gcd

input = stdin.readline
setrecursionlimit(10 ** 5)


def power(a, b, mod=False):
    result = 1
    while b > 0:
        if b % 2:
            if mod:
                result = (result * a) % mod
            else:
                result *= a
        if mod:
            a = (a * a) % mod
        else:
            a *= a
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
for _ in range(int(input())):
    input()
    target = int(input())
    if target == 1:
        now = 1
    else:
        now = 0
        if is_prime(target):
            div = [1, target]
        else:
            div_p = defaultdict(int)
            pollard_rho(target)
            div = []
            div_arr = list(div_p)
            n = len(div_p)
            dfs(1, 0)
        for d in div:
            div_p = defaultdict(int)
            pollard_rho(d + 1)
            ex = 1
            for key, value in div_p.items():
                ex *= power(key, value) - power(key, value - 1)
            now += ex
    ans.append(now)
print(*ans, sep='\n')
```

오늘 문제 풀 계획은 없었는데... 싸피 퇴소 후 약속 시간까지 시간이 붕 떠버리는 바람에 풀어버렸다. 역시 점수 올리기에는 수학 문제가 최고다. 이미 구현해놓은 폴라드 로 함수가 있어서 편하게 할 수 있었다. 

문제를 쉽게 풀어쓰면, n이라는 숫자가 주어졌을 때, 가로 a, 세로 b의 직사각형의 대각선이 지나는 정사각형의 갯수가 n개가 되는 (a, b) 쌍의 갯수를 구하는 문제였다. 지하철 안에서 계속 문제를 들여다보다가, 카페에서 아이디어가 번뜩였다.

> 서로소 a, b에 대해 가로 a, 세로 b의 직사각형의 대각선은 총 a + b - 1 개의 정사각형을 지난다!

증명은 생각보다 쉽다. (1, 1) 정사각형에서 (a, b) 정사각형으로 이동하는 경로 중 대각선을 완전히 포함하는 경로를 생각해보자. 경로는 x, y 방향 양 쪽 다 + 방향으로만 움직일 것이다. 그리고, x, y가 동시에 늘어날 순 없다. 왜냐고? a, b가 서로소니까. 그러므로, 총 정사각형은 (a + b) - (1 + 1) + 1 개 지난다는 결론이 나온다.

그럼 이제 문제를 어떻게 해결해야 되냐. n이 주어지면 약수들을 모두 구해준다. 약수는 Lugguage 문제에서 DFS를 활용하여 구한 적이 있다. 이제 잘 생각해보면, 문제에서 구해야 할 것은 합이 n의 약수 + 1 이 되는 서로소 a, b 쌍의 갯수가 된다.

a와 b가 서로소임은, a와 a+b가 서로소임과 동치이다. 그러므로, 약수를 모두 구하고, 약수 + 1 보다 작은 수 중 서로소인 수의 갯수를 구해주면 된다. 이건 오일러 피 함수를 이용해 쉽게 구할 수 있고, 오일러 피 함수를 사용하기 위해 폴라드 로를 또 해주면 된다.

![image](https://user-images.githubusercontent.com/97663863/183048104-09755741-90d3-4e6a-8d0f-63178de40457.png)

푼 사람이 나 포함 3명 밖에 없는 문제다. 오예~

