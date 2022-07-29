# 0728

이제서야 코로나를 걸릴 줄이야... 여태 잘 버텼거늘... 그래도 나쁘지 않다. 수업 안 들어도 돼서 알고리즘 풀 시간이 늘어났다.

새로운 점수 발굴 코너를 찾았다. 바로 수학, 특히 조합, 확률, 통계 쪽. 수리과 복수 전공할 때 전공자들한테 밀리지 않던 쪽이었는데, 여기서 빛을 볼 줄은 몰랐다. 덕분에 점수 쉽게 올리는 중~



## :diamond_shape_with_a_dot_inside: Hey, Better Bettor - [백준 8878](https://www.acmicpc.net/problem/8878)

Gambler's ruin

```Python
def power(a, b):
    res = 1
    while b > 0:
        if b % 2:
            res *= a
        a *= a
        b //= 2
    return res


def solve(w, l):
    p = (1 - power(f, l)) / (1 - power(f, w + l))
    return p * w - (1 - p) * l * (1 - n)


n, m = map(lambda x: float(x) / 100, input().split())
if m == 0:
    print(0)
    exit()
f = (1 - m) / m
ans = 0
win, lose = 1, 1
while True:
    pre = 0
    flag = False
    while True:
        now = solve(win, lose)
        if now >= ans:
            ans = now
            flag = True
        else:
            if flag:
                win -= 1
            break
        win += 1
        pre = now
    if not flag:
        break
    lose += 1
print(ans)
```

또 루비 문제를 풀어버렸다! 솔직히 루비 정도의 난이도는 아니지만... 도박꾼의 파산 문제를 이미 알고 있어서 쉽게 푼 거 같다.

일단 승리, 패배 수를 정해보자. 이제 이걸 다르게 생각해 볼건데, 승리 수는 딜러의 자산, 패배 수는 내 자산이라고 생각해보자. 그러면 도박꾼의 파산 문제에서 계산되는 것처럼, 딜러와 나 자신의 파산 확률을 구할 수 있다. 딜러가 파산됐다는 것은 내가 전체 승리 수만큼 벌었다는 뜻이다. 내가 파산했다는 것은 내가 전체 패배 수만큼 잃었으며, 재환급을 받아야 한다는 뜻이다. 즉, 딜러가 파산할 확률을 `p`라고 하면, 이익의 기댓값 `E`는

$$
E = p \cdot w - (1 - p) \cdot l \cdot (1 - n)
$$

라고 표현될 것이다. 이게 `solve`함수의 역할.

그럼 이제 최적의 승리/패배 조합을 찾아야 한다. 여기서 한 가지 생각을 해보자.

> f(x, y) = solve(x, y)은 위로 볼록한 형태일 것이다. 최적의 w, l이 유일한 극값(좋은 전문 용어가 있었던 거 같은데 기억이 안 난다..)이 될 것이고, w나 l을 고정시키고 단면을 잘랐을 때도 위로 볼록한 포물선 비스무리한 형태일 거다.

흠... 증명은 솔직히 못하겠다. 머릿속으론 극값이 하나 튀어나오는 게 자명한데... 미적분으로 보여야 하나?

암튼, 저 생각이 맞다는 가정 하에 문제를 풀었다. 승수를 1씩 늘려가면서 현재 패배의 수에서의 최적의 승리 수를 찾는다. 답을 갱신했다면 패배 수를 더 늘려보고, 반복한다. 갱신 못 했다? 그대로 종료한다.

수학 문제 최고! 다이아3에 도달했다. 골드-플레 시절 때처럼 점수가 팍팍 오르니 의욕이 난다 ㅎㅎ



## :diamond_shape_with_a_dot_inside: 동전 던지기 - [백준 14853](https://www.acmicpc.net/problem/14853)

조합, 확률

```Python
from sys import stdin

input = stdin.readline

t = int(input())
query = [tuple(map(int, input().split())) for _ in range(t)]
ans = [0] * t
for tc in range(t):
    n1, m1, n2, m2 = query[tc]
    now = 1
    for k in range(m1 + 1):
        now *= n1 + 1 - k
        now /= n1 + n2 + 2 - k
    ans[tc] += now
    for k in range(1, m2 + 1):
        now *= ((m1 + k) * (n2 - k + 2)) / (k * (n1 + n2 - m1 - k + 2))
        ans[tc] += now
print(*ans, sep='\n')
```

확률론 시간에 비슷한 문제를 다룬 경험이 있다. 연습반이었던 거 같은데... 교수님 말고 조교 아님 학생 풀이였다. 뭐 옛날 일이니 넘어가고.

문제를 그대로 풀려면 아마 적분을 해야 할 것이다. 이중 적분이라 쉽지도 않을거고? 그렇다면 이걸 어떻게 생각하면 좋냐. 길이가 1인 막대기 위에 점을 찍는다고 생각해보자. 모든 시행을 독립적으로 하여, `n1+n2`개를 찍는다. 이 점들은 (거의)각각의 동전 던지기를 의미한다. 여기서, 2번 더 찍는다. 그럼 `n1+n2+2`개의 점이 찍혀 있을텐데, 이제 `p`와 `q` 그리고 모든 동전 던지기 시행을 각 점에 매칭시킬 것이다.

일단 전체 경우의 수를 구해보자. 점은 다 찍었으니까 신경 끄고, `p`의 동전에 관련된 점들을 일단 골라야 한다. 그러므로 전체 경우의 수는 <sub>n1+n2+2</sub>C<sub>n1+1</sub>이 된다.

`p`의 동전에서 `p` 점보다 왼쪽에 가까운 점들을 앞면, 먼쪽을 뒷면이 나온거라 생각해보자. 그러면 앞면이 나온 횟수는 정해져 있으므로 `p`의 위치가 정해지고, 마찬가지로 `q`의 위치도 정해진다.

우리가 구하고 싶은 건 `p < q` 의 확률이다. 즉, 우리 막대기에서 `q`가 `p`보다 오른쪽에 있을 확률을 구하면 된다. `p`가 제일 앞에 있을 때는 `m1 + 1` 번 째 점일 때다. 그럼 제일 뒤에 있을 때는? `m1 + m2 + 1`번 째 점일 때다. 이 때, `p`가 `m1+k+1`번 째 점에 있을 때 가능한 경우의 수는 아래와 같다.

$$
{m_1 + k \choose m_1} {n_1 + n_2 - m_1 - k + 1 \choose n_1 - m_1}
$$

간략하게 설명하면, `p` 앞의 점에서 앞면이 나올 점 `m1`개를 뽑아주고, 뒤 쪽의 점에서 뒷면이 나올점 `n1-m1`개를 골라준다(`q` 제외하고 카운트). 그래서 이걸 다 더하면 답이 나온다. 간단한 combination 계산이길래, 처음에는 코드를 

```Python
def combination(n, r):
    return dp[n] // (dp[r] * dp[n - r])


dp = [1] * 2003
for i in range(2, 2003):
    dp[i] = dp[i - 1] * i
for _ in range(int(input())):
    n1, m1, n2, m2 = map(int, input().split())
    total = combination(n1 + n2 + 2, n1 + 1)
    res = 0
    for k in range(m2 + 1):
        res += combination(m1 + k, m1) * combination(n1 + n2 - m1 - k + 1, n1 - m1)
    print(res / total)
```

위와 같이 짰다. 근데 TLE. 연산량이 많지 않은데 왜 시간 초과가 나는 거야... 하면서 원인 분석에 들어갔다.

1. `input`과 `print`를 반복하면서 사용. io buffer 이슈인가 해서 고쳤는데 별 차이 없었다.
2. 함수 호출 시간. 아닐 거 알면서 고쳐봤다. 역시 그대로.
3. **dp의 숫자가 너무 큼**. Overflow 이슈였다. 2000!를 그대로 저장해놨으니, 연산 처리 속도가 그만큼 느려진 것이다! 그래서 다 약분하고 최소한의 계산만을 그 때 그 때 계산하는 쪽으로 진행해서 AC.

간단하게 구한 것처럼 써놓았지만, 인덱스가 헷갈려서 꽤 고생했다. 특히 `p`와 `q` 위치 지정 이슈에서 시간을 좀 잡아먹었다. 다이아2인데 이 정도는 해야지...
