# 0623

세그먼트 트리 문제들이 풀리기 시작하면서 어느새 CLASS 7 까지 3문제 밖에 안 남았다.

이번 주에 찍어보자!



## 구간 합 구하기 2 - [백준 10999](https://www.acmicpc.net/problem/10999)

sqrt decomposition (제곱근 분할이라고 쓰면 되려나?)

```python
from sys import stdin

input = stdin.readline

n, q1, q2 = map(int, input().split())
arr = [int(input()) for _ in range(n)]
sn = int(n ** 0.5)
square_sum = [0] * (n // sn + 1)
ex = [0] * (n // sn + 1)
for i in range(n):
    square_sum[i // sn] += arr[i]
for _ in range(q1 + q2):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        _, s, e, k = query
        s -= 1
        e -= 1
        i, j = s // sn, e // sn
        if i == j:
            if s % sn == 0 and e % sn == sn - 1:
                ex[i] += k
            else:
                for t in range(s, e + 1):
                    arr[t] += k
        else:
            for t in range(i + 1, j):
                ex[t] += k
            ri, rj = s % sn, e % sn
            if ri == 0:
                ex[i] += k
            else:
                for t in range(ri, sn):
                    arr[i * sn + t] += k
                square_sum[i] += k * (sn - ri)
            if rj == sn - 1:
                ex[j] += k
            else:
                for t in range(rj + 1):
                    arr[j * sn + t] += k
                square_sum[j] += k * (rj + 1)
    elif query[0] == 2:
        _, s, e = query
        s -= 1
        e -= 1
        i, j = s // sn, e // sn
        if i == j:
            ans = sum(arr[s:e + 1]) + ex[i] * (e - s + 1)
        else:
            ri, rj = s % sn, e % sn
            ans = ex[i] * (sn - ri) + ex[j] * (rj + 1)
            for t in range(i + 1, j):
                ans += square_sum[t] + ex[t] * sn
            for t in range(ri, sn):
                ans += arr[i * sn + t]
            for t in range(rj + 1):
                ans += arr[j * sn + t]
        print(ans)
```

전형적인 세그먼트 트리 문제다. 풀려다가, 인덱스 조작이 너무 귀찮아서 새로운 풀이를 찾아냈다!

>  **모든 구간을 n<sup>1/2</sup>로 자르고 관리하자!** 

변수 설명을 하자면,

- `ex` : 루트 n으로 자른 구간 전체의 모든 원소에 더해진 값이다.
- `square_sum` : 루트 n으로 자른 구간의 합이다. 이 때, 실제 구간의 합과 다를 수 있다. (`ex` 변수 값이 포함되지 않은 합이다.)

그 다음은 단순 계산이다. 그 헷갈리는 세그먼트 트리보다 조금 느릴지 몰라도, 훨씬 간단하다. 코드 보면 전혀 어려운 부분 없이 단순 구현이다.

안타깝게도, sqrt decomposition, 즉 제곱근 분할법이라고 이미 존재하는 풀이 방법이었다. 뭐 당연히 그러겠지...

그래도 2 SAT를 코사라주로 메모리 최적화하는 방법을 찾았을 때처럼 설렜다 ㅋㅋ 

이 문제랑은 전혀 상관없지만, 2SAT 코사라주 최적화는 나 밖에 안 쓰는 것 같긴 하다. 내가 발견한 내용을 공유하고 싶은데, 주위에 이런 내용을 아는 사람이 없어서 입이 근질근질하다...

