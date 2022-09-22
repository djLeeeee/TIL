# 0922

사실 Today I learned 가 아니라 for Ten day I Learned 라 카더라.



## FFT 알고리즘

미루고 미루던 FFT를 저번 주말에 시간 내서 구현해봤다.

```
from cmath import pi, exp
from sys import stdin

input = stdin.readline


def fft(t, inv=False):
    l = len(t)
    if l == 1:
        return t
    t_even = fft(t[0::2], inv)
    t_odd = fft(t[1::2], inv)
    c = -1 if inv else 1
    wn = [exp(c * 2j * pi * x / l) for x in range(l // 2)]
    res1 = [t_even[x] + wn[x] * t_odd[x] for x in range(l // 2)]
    res2 = [t_even[x] - wn[x] * t_odd[x] for x in range(l // 2)]
    return res1 + res2


n = 1 << 19
a = [0] * n
for _ in range(int(input())):
    a[int(input())] = 1
b = fft(a)
a[0] = 1
c = fft(a)
res = [b[i] * c[i] for i in range(n)]
res = fft(res, inv=True)
res = [round(res[i].real / n) for i in range(n)]
ans = 0
for _ in range(int(input())):
    if res[int(input())]:
        ans += 1
print(ans)
```

하라는 대로 구현한 코드이다. 어떤 분의 블로그 글을 참조해서 작성했는데, 10일 전 일이라 그 분 블로그 주소를 못 찾겠다. 죄송합니다 ㅠㅠ FFT 원리는 정리해놓은 블로그들이 많으니 굳이 정리 안하는 걸로. 애초에 대학교 다닐 때 손계산으로도 풀던 건데 뭐이리 잘 기억이 안 나는지... 너무 놀았나보다.

exp(i) 연산이 일반 `math` 라이브러리에서는 지원이 안 되는 듯 하다. 그래서 `cmath` 라는 라이브러리를 사용했다.

위의 코드는 [백준 10531 Golf Bot](https://www.acmicpc.net/problem/10531) 의 정답 코드이다. FFT 구현 성공했구나! 하는 기쁜 마음에, 다른 FFT 문제에서도 같은 함수를 사용했는데, 바로 시간 초과가 나왔다...



## Golf Bot - [백준 10531](https://www.acmicpc.net/problem/10531)

FFT

```Python
"""
출처: https://www.acmicpc.net/source/44798125 (작성자: midori)
"""
from sys import stdin

input = stdin.readline
div = 469762049


def power(a, b, mod):
    result = 1
    while b:
        if b % 2:
            result *= a
            result %= mod
        b //= 2
        a *= a
        a %= mod
    return result


def fft(a, inv=False):
    n = len(a)
    y = 0
    for x in range(1, n):
        rev = n // 2
        while y >= rev:
            y -= rev
            rev //= 2
        y += rev
        if x < y:
            a[x], a[y] = a[y], a[x]
    step = 2
    while step <= n:
        half = step // 2
        u = power(3, div // step, div)
        if inv:
            u = power(u, div - 2, div)
        for x in range(0, n, step):
            w = 1
            for y in range(x, x + half):
                v = a[y + half] * w
                a[y + half] = (a[y] - v) % div
                a[y] += v
                a[y] %= div
                w *= u
                w %= div
        step *= 2
    if inv:
        c = div - (div - 1) // n
        for idx in range(n):
            a[idx] = (a[idx] * c) % div


temp = [int(input()) for _ in range(int(input()))]
arr = [0] * (max(temp) * 2 + 1)
for i in temp:
    arr[i] = 1
arr[0] = 1
s = len(arr) * 2 - 1
l = 1 << s.bit_length()
arr += [0] * (l - len(arr))
fft(arr)
for i in range(l):
    arr[i] *= arr[i]
fft(arr, inv=True)
cnt = 0
for _ in range(int(input())):
    if int(arr[int(input())]):
        cnt += 1
print(cnt)
```

FFT를 다른 분들은 어떻게 구현해놓은지 참고하기로 했다. 골프 봇 문제에서 빠른 시간에 해결한 코드 중 이해가 가는 [midori](https://www.acmicpc.net/user/midori) 님의 코드를 참고했다.

코드를 보다보면 처음부터 이상한 숫자가 나온다. `div=46972049` 이 부분인데, 정말 뜬금 없었다. 소수인거 같긴 한데, 내가 아는 일반적인? 소수 10^9 + 7 을 사용하니 오답이 나왔다. 그래서 46972049로 구글에 그대로 검색하니, [바로 윗줄에 FFT 내용이 나왔다.](https://cubelover.tistory.com/12) 이 숫자의 정체는 FFT에서 자주 나오는 소수였다.

일반적인 FFT에서, 내가 처음에 구현한 부분을 보면 아래와 같은 부분이 있다.

```
res = [round(res[i].real / n) for i in range(n)]
```

이 부분을 나도 쓰면서도 이상하다고 생각했다. 복소수 연산을 하는데 정밀도 부분에서 문제가 생길 수 있지 않을까? 그런 관점에서 나온게 NTT, Number Theoretic FFT라고 한다. cubelover 님 블로그에 잘 정리되어 있다. cubelover 님을 게임 이론 문제 지문에서 많이 봤었는데, 이렇게 블로그에서 보니 기분이 묘했다. 암튼 midori 님의 코드를 이해한 뒤 대강 내 스타일로 어레인지 해봤다. 말이 어레인지일 뿐, 사실상 midori 님이 작성한 코드에 변수명이랑 함수 형태만 바꿔줬다.

개념 설명은 여기까지 하고, 이게 왜 FFT 문제인지 보자. 한 번에 이동할 수 있는 거리가 정해져있고, 정해진 최대 횟수만큼 이동을 해 갈 수 있는 거리의 가지수를 구하는 문제이다. 이런 문제를 수식의 곱으로 바꾸어 풀 수 있다. 그 다음 존재하는 차수 항을 모두 찾아주면 끝. 긴 수식의 곱이니 n<sup>2</sup>가 아닌 nlogn 방식의 FFT가 필요한 문제였다.



## 골드바흐 파티션 2 - [백준 17104](https://www.acmicpc.net/problem/17104)

FFT

```Python
from sys import stdin

input = stdin.readline
div = 469762049


def power(a, b, mod):
    result = 1
    while b:
        if b % 2:
            result *= a
            result %= mod
        b //= 2
        a *= a
        a %= mod
    return result


def fft(a, inv=False):
    n = len(a)
    y = 0
    for x in range(1, n):
        rev = n // 2
        while y >= rev:
            y -= rev
            rev //= 2
        y += rev
        if x < y:
            a[x], a[y] = a[y], a[x]
    step = 2
    while step <= n:
        half = step // 2
        u = power(3, div // step, div)
        if inv:
            u = power(u, div - 2, div)
        for x in range(0, n, step):
            w = 1
            for y in range(x, x + half):
                v = a[y + half] * w
                a[y + half] = (a[y] - v) % div
                a[y] += v
                a[y] %= div
                w *= u
                w %= div
        step *= 2
    if inv:
        c = div - (div - 1) // n
        for idx in range(n):
            a[idx] = (a[idx] * c) % div


n = 1 << 20
sn = 1 << 10
arr = [1] * (n // 2) + [0] * (n // 2)
arr[0] = 0
for i in range(1, sn + 1):
    if arr[i]:
        for j in range(3 * i + 1, n, 2 * i + 1):
            arr[j] = 0
fft(arr)
for i in range(n):
    arr[i] *= arr[i]
fft(arr, inv=True)
for _ in range(int(input())):
    m = int(input())
    if m == 4:
        print(1)
    else:
        print((arr[m // 2 - 1] + 1) // 2)
```

이전에 짜놓은 개떡같은 FFT 알고리즘이 시간 초과가 나서, FFT 외적인 부분에서 이미 극도의 시간 최적화를 해놨었다. NTT를 적용하자마자 바로 AC. 덕분에 제출된 파이썬 중 에서는 제일 빠른 코드가 탄생했다.

FFT로 할 수 있는 건 쉽게 파악할 수 있는 문제였다. 소수 차수를 표시하고, 제곱해주면 되니까. 그러면 이걸 어떻게 효율적으로 할 수 있을지 보면,

1. 에라토스테네스의 체에서 제곱근까지만 찾고, 홀수만 체크한다. 웰노운.
2. 홀수를 2로 나눈 몫으로 표시한다. 대신 FFT 후에 정답을 구할 때 약간의 체크를 해줘야 한다.
3. 어떤 소수 p, q에 대해 p + p는 한 번, p + q는 두 번 카운팅 된다. p + q와 q + p를 구분하지 않으므로 유의해야 한다. 이는 전체 가짓수가 홀수이면 p + p 케이스가 있고, 짝수면 없다는 관찰을 통해 어떻게 답을 구해야 할지 알 수 있었다.

덕분에 FFT를 할 수열의 길이도 절반으로 줄어들었다. 이렇게 열심히 시간 최적화를 한 게 CHT 문제 풀었을 때가 마지막인 거 같기도 하고.. 간만에 제대로 된 문제를 푼 느낌이 든다.
