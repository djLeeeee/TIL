# 0724

목-금은 워크샵에, 금-토는 싸피 모임에... 2일 연속 밤샘 술 마셨더니 오늘 3시까지 골골대며 누워있었다. 늙었나보다 ㅠ

오랜만에 solved.ac의 싸피 사람들 쭉 훑어봤는데, 루비 한 분꼐서 10기에 들어오시는 것 같다. 도망쳐요... 시간 버려요...

좀 변태같은 짓을 시작했다. 문제 레이팅 100개 매기기 프로젝트 에서 제일 어려웠던 부분은 아무래도 문제 선정이었는데, 적당히 문제 많이 푼 사람 기록으로 들어가 맞췄지만 레이팅을 매기지 않은 문제들을 쭉 풀고 있다. 그러다보니 아무래도 브실골 문제가 많긴 한데, 뭐 확실히 노베이스에서 문제 고르는 것보단 훨 나은 느낌? 어느새 64문제 최초 레이팅을 매겼는데, 올해 안에 무난하게 100문제 가능할 것 같다. 추가로 지금 1878솔이니까... 2000솔까지 122문제 남았다. 음 여것도 무난하게 성공할 것 같다. 루비 찍기만 어찌저찌하면 되는데... 

뭐 이런 시덥잖은 소리만 쓰려고 TIL을 쓴 건 아니고, 내 기존 NTT 코드보다 훨씬 빠른 풀이를 찾아내 기록하려고 한다.



## NTT 최적화

> 문제 소스 : https://www.acmicpc.net/problem/15050

```Python
# My original / time 16512 ms
def fft(a, inv=False):
    div = 469762049
    R = 3
    la = len(a)
    y = 0
    for x in range(1, la):
        rev = la // 2
        while y >= rev:
            y -= rev
            rev //= 2
        y += rev
        if x < y:
            a[x], a[y] = a[y], a[x]
    step = 2
    while step <= la:
        half = step // 2
        u = power(R, div // step, div)
        if inv:
            u = power(u, div - 2, div)
        for x in range(0, la, step):
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
        cc = div - (div - 1) // la
        for idx in range(la):
            a[idx] = (a[idx] * cc) % div
```

이건 내 기존 코드이다. 바로 더 빠른 코드를 보자.

```Python
# ntt source : boj handle wo01416 / https://www.acmicpc.net/user/wo01416
# time 4402 ms
def reArrangeForFFT(arr):
    N = len(arr)
    halfN, quarN, eightN = N//2, N//4, N//8

    revX = quarN
    for X in range(1, halfN, 2):
        pBit = quarN
        while revX >= pBit + halfN:
            revX -= pBit
            pBit //= 2
        revX += pBit
        arr[X], arr[revX] = arr[revX], arr[X]
    
    revX = eightN
    for X in range(2, quarN, 4):
        pBit = eightN
        while revX >= pBit + quarN:
            revX -= pBit
            pBit //= 2
        revX += pBit
        arr[X], arr[revX] = arr[revX], arr[X]
        arr[X+halfN+1], arr[revX+halfN+1] = arr[revX+halfN+1], arr[X+halfN+1]
    
    revX = 0
    for X in range(4, quarN, 4):
        pBit = eightN
        while revX >= pBit:
            revX -= pBit
            pBit //= 2
        revX += pBit
        if X < revX:
            for a in [0, halfN+1, quarN+2, halfN+quarN+3]:
                arr[X+a], arr[revX+a] = arr[revX+a], arr[X+a]


# various modular prime and its primitive root
# https://invrtd-h.tistory.com/100?category=1302858
mod, g = 998244353, 3
def NTT(arr, isInv = False):
    from math import log2
    N = len(arr)
    logN = int(log2(N))
    reArrangeForFFT(arr)

    step = 2
    for i in range(logN):
        halfStep = step//2
        u = pow(g, (-1 if isInv else 1)*(mod//step), mod)
        for x in range(0, N, step):
            w = 1
            for y in range(x, x + halfStep):
                v = arr[y + halfStep] * w
                arr[y + halfStep] = (arr[y] - v)%mod
                arr[y]            = (arr[y] + v)%mod
                w = (u*w)%mod
        step *= 2
    
    if isInv:
        c = pow(N, -1, mod)
        for i in range(N):
            arr[i] = (arr[i] * c) % mod
```

솔직히 작동 원리를 아직 완벽하게 파악하지 못했다. FFT 자체가 어려워서 원...

애초에 내가 주로 쓰던 NTT도 midori 님 코드 베이스였던 거 같다. 

찾으니까 금방 나오네 ㅋㅋㅋㅋ [22년도 9월 22일](https://github.com/djLeeeee/TIL/tree/master/2022%EB%85%84/22%EB%85%84%209%EC%9B%94/09%EC%9B%94%2022%EC%9D%BC) 자에 midori 님 코드를 확인한 듯 하다. 암튼 이 코드도 좀더 이해해보고 NTT source로 활용하면 좋을 거 같아 기록해본다.

좀 다른 얘기지만, 기록하는 습관이 참 중요한 거 같다. 이렇게 다시 확인할 수 있으니...
