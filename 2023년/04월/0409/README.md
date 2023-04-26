# 0409

요즘 알고리즘 문제 풀이에 탄력을 받았다. 개발 공부는.. 음... 이 TIL만 쓰고 시작하련다.

kriiicon 문제들을 풀어보고 있다. 수학 스킬 + 알고리즘 문제들이라 정수론 문제가 많다보니 푸는 재미가 있다.



## 흑백 이미지 찾기 - [백준 11398](https://www.acmicpc.net/problem/11398)

> FFT(NTT), CRT, prefix sum

다이아1 문제에 기여로 다이아1을 남겼는데, 아래 평가들이 절사되면서 루비가 되버렸다. 오우... 개인적으로 다1이 적당한 것 같다. 더 많은 사람이 풀면 다1로 수렴할 듯.

여러 칸에 대해서, $px + q = y$가 되는 지 체크하는 문제였다. 당연히 모든 칸을 체크하면 시간 초과가 날 것이다.
$y$를 이항하면 $px + q - y = 0$이 되는 지 체크하는 문제가 되고, 모든 칸이 0이 된다 체크는? 제곱해서 더하는 걸로 바꿀 수 있다.

$\sum(px + q - y)^2 = p^2\sum{x^2} + rcq^2 + \sum{y^2} + 2pq\sum{x} - 2q\sum{y} -2p\sum{xy} = 0$

$p$, $q$ 는 서로 다른 두 좌표를 잇는 직선을 구하면 된다! 여기서 문제가 하나 생기긴 하는데, 뒤에 답 구할 때 다시 보자. 또, $y$에 대한 항은 상수이다. 미리 구해주자.

그럼 남은 항은 $x^2$, $x$, $xy$ 의 $\sum$ 값이다. 여기서 $x^2$과 $x$는 2차원 누적 합을 이용해 계산해놓자. 기본적인 누적 합 구조로 구현이 가능하다. `sumA`와 `sumAsq`로 표현해줬다.

```Python
N = 1 << 21
n, m = map(int, input().split())
imgA = [list(map(int, input().split())) for _ in range(n)]
sumA = [[0] * (m + 1) for _ in range(n + 1)]
sumAsq = [[0] * (m + 1) for _ in range(n + 1)]
arrA = [0] * N
for i in range(n):
    for j in range(m):
        sumA[i][j] = sumA[i - 1][j] + sumA[i][j - 1] - sumA[i - 1][j - 1] + imgA[i][j]
        sumAsq[i][j] = sumAsq[i - 1][j] + sumAsq[i][j - 1] - sumAsq[i - 1][j - 1] + imgA[i][j] * imgA[i][j]
        arrA[m * i + j] = imgA[i][j]
r, c = map(int, input().split())
imgB = [list(map(int, input().split())) for _ in range(r)]
sumB = sumBsq = 0
arrB = [0] * N
dr, dc = 0, 0
lt = imgB[0][0]
for i in range(r):
    for j in range(c):
        if imgB[i][j] != lt:
            dr, dc = i, j
        sumB += imgB[i][j]
        sumBsq += imgB[i][j] * imgB[i][j]
        arrB[m * (r - i - 1) + (c - j - 1)] = imgB[i][j]
```

문제는 $xy$인데, 이거 구하려고 거의 하룻동안 고민했다. 그러다가 FFT가 떠올랐다. 각 좌표값을 계수로, 위에서 오른쪽으로 0, 1, ... 을 지수로 하도록 식을 만들면 얼추 감이 잡힌다. 이미지 A는 정방향으로 지수를 부여하고, B는 역방향으로 부여하면? 그 두 식을 곱했을 때 특정 지수의 계수는 $\sum{xy}$를 의미하는 값이 된다!

여기서 또 한 가지 주의할 점은, $\sum{xy}$는 최대 $10^6 \times 2^{36}$이므로, 기존의 NTT에서 값에 오류가 생길 수 있다! 이미 이런 경우 처리를 해봤다. CRT를 이용해 정확한 값을 구해주자. 그러려면 두번 NTT를 해주면 된다.

```Python
memoA = arrA[:]
memoB = arrB[:]
fft(arrA)
fft(arrB)
for i in range(N):
    arrA[i] *= arrB[i]
fft(arrA, inv=True)
fft(memoA, option=1)
fft(memoB, option=1)
for i in range(N):
    memoA[i] *= memoB[i]
fft(memoA, inv=True, option=1)
ans = 0
```

다시 $p$, $q$ 얘기로 돌아오자. 당연히 정수 좌표에 대해서만 볼 거니까, 유리수 계수일거니 분수로 표현할 수 있다. 그리고 일반식은,

$(x_2 - x_1) y = (y_2 - y_1)x + x_2y_1 - x_1y_2$

가 된다. 고등학교 교육과정인데 이렇게 장황하게 쓴 이유는, 저 두 직선을 나타내기 위해선 두 점을 뽑아야 하는데 이를 어떻게 뽑을 것인가? 하는 문제 때문이다. 이미지 A의 구간은 계속 바뀌기 때문에 고정하기 쉽지 않으니, 이미지 B로 눈을 돌리자. (0, 0)과 비교를 하면서 다른 값이 존재하는 지 체크를 하고, 값이 다르다면 그 좌표 $(dr, dc)$를 기록해주자. 만일 다 값이 같다면? 친절하게 예제에서 설명해줬다. 모든 박스가 표절이 되므로 바로 답을 출력해주자.
위에 코드랑 약간 중복되는 부분이 있긴 하다 ㅋㅋ

```Python
dr, dc = 0, 0
lt = imgB[0][0]
for i in range(r):
    for j in range(c):
        if imgB[i][j] != lt:
            dr, dc = i, j
        sumB += imgB[i][j]
        sumBsq += imgB[i][j] * imgB[i][j]
        arrB[m * (r - i - 1) + (c - j - 1)] = imgB[i][j]
if dr == dc == 0:
    print((n - r + 1) * (m - c + 1))
    exit()
```

그러면 이제 답을 구해보자.

```Python
p1, p2 = 2281701377, 1092616193
sumYsq = sumBsq
sumY = sumB
y1 = imgB[0][0]
y2 = imgB[dr][dc]
for i in range(r - 1, n):
    for j in range(c - 1, m):
        # Prefix sum
        sumXsq = sumAsq[i][j] - sumAsq[i - r][j] - sumAsq[i][j - c] + sumAsq[i - r][j - c]
        sumX = sumA[i][j] - sumA[i - r][j] - sumA[i][j - c] + sumA[i - r][j - c]
        
        # CRT
        v1 = arrA[i * m + j]
        v2 = memoA[i * m + j]
        sumXY = ((v2 - v1) * power(p1, p2 - 2, p2)) % p2 * p1 + v1
        
        # p, q, d
        x1 = imgA[i - r + 1][j - c + 1]
        x2 = imgA[i - r + 1 + dr][j - c + 1 + dc]
        if x1 == x2:
            continue
        p = y2 - y1
        q = x2 * y1 - x1 * y2
        d = x2 - x1

        # check answer
        temp = p * p * sumXsq + q * q * r * c + d * d * sumYsq
        temp += 2 * p * q * sumX - 2 * q * d * sumY - 2 * p * d * sumXY
        
        # is the square sum zero? 
        if temp == 0:
            ans += 1
print(ans)
```

다른 내용은 다 설명했고, 남은 내용은 왜 `if x1 == x2:continue`인지 이다. `y1`이랑 `y2`는 다른 값으로 잡아놨는데 `x1`과 `x2`가 같다? 그러면 답이 될 수 없는 경우이므로 탐색할 이유가 없다. 

`d`라는 변수는, 분수의 분모를 관리하기 귀찮으므로 미리 곱해주기 위해 만들어줬다.

캬 재밌는 문제였다. 진짜 하루가 살살 녹는 문제였다



## 제비 - [백준 13182](https://www.acmicpc.net/problem/13182)

> 확률론, 점화식 풀기...

간만에 공책 꺼내서 식 정리를 했다. 5페이지나 써서 풀었다... 다 올리긴 그렇고, 핵심 식이 나온 페이지 하나 찍어놨다.

![KakaoTalk_20230409_145553089](https://user-images.githubusercontent.com/97663863/230757027-358d0e21-8e42-4add-a030-e8039ff1eb78.jpg)

첫 점화식을 구해보자.

$P_{r, k} = \dfrac{r + g + b}{r + b} + \dfrac{r}{r + b}\cdot P_{r - 1, k} + \dfrac{b}{r + b} \cdot P_{r, k -1}$

사실 이 식도 바로 나오진 않는다. 빨/파/초 뽑았을 때의 행동 별로 기댓값을 표현한 식을 정리한 결과다.

이제 이 점화식을 풀면 된다. 화이팅! 진짜 생 노가다 작업이다.

```Python
mod = 10 ** 9 + 7
for _ in range(int(input())):
    r, g, b, k = map(int, input().split())
    print(add(
        mul(k, frac(b + g, b)),
        mul(r, add(1, minus(power(frac(b, b + 1), k))))
    ))
```

뭐 점화식 풀어서 일반항 계산만 하면 되니 코드는 짧다. 그냥 식을 우르르 쓰기엔 알아보기 힘들어서 내가 익숙한(...) 꼴로 바꿔봤다. `frac`은 당연히 진짜 분수가 아니고 모듈러 곱셈 역원을 이용한 결과다.
