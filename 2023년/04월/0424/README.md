# 0424

설계 구조 공부를 왜 하나 했는데, 이제야 이해가 된다. 그래서 조금씩 공부하고 있다.

우리 뭐시기랑 ybm에서 코딩 대회를 연다고 한다. 언어별 부문이 따로 있어서 파이썬으로 지원했다. 상금 받아야지 흐흐

회사랑 야구장이 무척이나 가깝다는 걸 이제서야 깨달았다. 내일도 갈 예정. 현재 직관 5전 5승인데 슬슬 불안하다...

다이아 랜디를 해보는 중이다. 근데 결국 내가 풀 수 있는 문제들만 풀다보니 뭔가 우물 안 개구리 느낌 ㅠ



## AGCU CUP (와쿠컵)

[백준 대회](https://www.acmicpc.net/contest/view/967)에 간만에 참여했다. 15문제 모두 실버 정도의 난이도로, 누가누가 빨리 푸나 대결이었다. 아쉽게도 대회 시작 90분 뒤에 대회가 연 걸 알아 한 박자 늦었다... 당연히 올솔 했다. 만일 90분 일찍 들어왔더라면 4등이었을텐데... 조금 아쉽다.



## Rock Paper Scissors - [백준 14958](https://www.acmicpc.net/problem/14958)

> FFT

다랜디에서 푼 문제 중 그나마 기록을 남길만한 문제였다. 가위바위보의 패 순서가 정해져있고, 어디부터 게임에 참여해야 최대 승수가 나올지 묻는 문제였다.
가위 바위 보 끼리 각각 각각 다항식으로 표현하고 곱해줬다. 그다음 가위로 이김 + 바위로 이김 + 보로 이김 을 더해 답을 구해줬다.

```Python
N = 1 << 18
rockA = [0] * N
rockB = [0] * N
scissorsA = [0] * N
scissorsB = [0] * N
paperA = [0] * N
paperB = [0] * N
n, m = map(int, input().split())
arrA = input().strip()
arrB = input().strip()
for i in range(n):
    if arrA[i] == 'R':
        rockA[i] = 1
    elif arrA[i] == 'S':
        scissorsA[i] = 1
    else:
        paperA[i] = 1
mid = N // 2
for i in range(m):
    if arrB[i] == 'R':
        rockB[mid - i] = 1
    elif arrB[i] == 'S':
        scissorsB[mid - i] = 1
    else:
        paperB[mid - i] = 1
fft(rockA)
fft(rockB)
fft(scissorsA)
fft(scissorsB)
fft(paperA)
fft(paperB)
for i in range(N):
    rockA[i] *= paperB[i]
    scissorsA[i] *= rockB[i]
    paperA[i] *= scissorsB[i]
fft(rockA, True)
fft(scissorsA, True)
fft(paperA, True)
ans = 0
for i in range(mid, mid + n):
    temp = rockA[i] + scissorsA[i] + paperA[i]
    if temp > ans:
        ans = temp
print(ans)
```

다시 보니 굳이 3번 나눌 필요 없이, N * 3 의 길이를 곱하면 되는 문제였다.. 뭐 어쩃든 통과했으니 넘어가자.



## Bus Stop - [백준 18570](https://www.acmicpc.net/problem/18570)

> FFT, 제곱근 분할, 적분, 통계

꿀잼 문제였다! 공책 한 5페이지 정도 사용했다.

![20230424_234035](https://user-images.githubusercontent.com/97663863/234031147-fa599569-60e1-4d2b-aa68-f1551dd98054.jpg)

latex로 쓰기 귀찮아 공책 내용을 한 장에 정리해봤다. 이제 이걸 풀어보려하니...

- 일반화 해보려했는데 실패
- $n \le 10^5$ 여서 일차식 n개를 단순하게 곱하는 건(이후 적분) $O(n^2)$으로 시간 초과 확정.

그러다가 제곱근 분할법을 생각해냈다. $\sqrt{n}$ 개 만큼 식을 자르고, $\sqrt{n}$ 개는 그냥 일차식의 곱셈을 한다. 그 다음 fft를 하고, fft 한 애들끼리 곱한다. 그러면 끝!

```Python
for i in range(n // sn + 1):
    if i * sn >= n:
        break
    temp = [0] * N
    temp[0] = 1
    for j in range(sn):
        k = i * sn + j
        if k == n:
            break
        for t in range(j + 1, -1, -1):
            # \times (a_k - x)
            temp[t] *= arr[k]
            temp[t] -= temp[t - 1]
            temp[t] %= mod
    fft(temp)
    for j in range(N):
        sf[j] *= temp[j]
        sf[j] %= mod
```

이렇게 하면 $\sqrt{n}$번의 각 for 문에 대해,

- $\sqrt{n}$개의 일차식을 직접 곱하기. $O(n)$
- fft를 한다. $O(\sqrt{n}\log n)$
- 식을 곱한다. $O(n)$

그러면 시간 복잡도는? $O(n\sqrt{n})$ 으로 원하는 수준까지 줄였다~ 이제 남은 건, 이걸 fft로 거꾸로 하면 우리가 원하는 정적분 안의 식을 구했다. 그러면 이제 답을 구하자.

```Python
ans = 0
m = min(arr)
for i in range(n + 1):
    ans += frac(mul(sf[i], power(m, i + 1)), mul(i + 1, d))
    ans %= mod
print(ans)
```

단순 정적분 대입이다. 요것도 내가 익숙한 꼴로 바꿔서 답을 구했다.

캬~ 다3을 랜디로 풀어버리네~ 하고 좋아했는데, 다른 분 풀이를 보니, $O(n\log n)$이 가능했다.. 분할 정복으로, fft를 하면 끝이었다... 뭐 암튼 제곱근 분할로도 가능하도록 설계된 문제인 것 같다.


