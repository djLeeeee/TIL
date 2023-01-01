# 10월 31일

사실 Today I learned 가 아니라 for Twenty days I Learned 라 카더라 2

주말만이라도 TIL을 쓰려고 했는데, 한 번 안 써 버릇했더니 손이 잘 안 가기 시작한다. 애초에 그저께 쓰려고 했는데, 우리의 엘쥐 놈들이 아아아주 기분 나쁘게 경기를 져서 도무지 할 기분이 들지 않았다. 덕분에 LG 우승 VS 루비 찍기 대결은 1년 미뤄졌다. 

그래도 알고리즘은 매일 한 문제 씩은 풀었다. 다이아 문제도 풀었고, 심심해서 점수 안 오르는 거 알면서도 플레 문제도 꽤 풀었다.

지금 하고 있는 일이 얼추 마무리되면 제대로 TIL을 다시 써보려 한다. Go 공부도 하고, Docker 좀 제대로 다루고 싶다. Computational geometry 서적도 좀 찾아보면 좋을 거 같고? 다음 TIL 쓸 때쯤에는 이런 내용이 들어가 있을지도 ㅇㅇ

암튼 오늘 정리할 TIL은 저번과 마찬가지로 20일간 풀었던 문제 중 기록할 만한 것들이다. 풀은 순서가 아닌, 난이도가 점점 올라가는 순서로 작성했다.



## 감시 피하기 - [백준 18428](https://www.acmicpc.net/problem/18428)

> 구현

```Python
def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n = int(input())
board = [list(input().split()) for _ in range(n)]
row = [[0] * n for _ in range(n)]
col = [[0] * n for _ in range(n)]
rn, cn = 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for x in range(n):
    for y in range(n):
        if board[x][y] == 'S':
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 'T':
                        print("NO")
                        exit()
                    else:
                        move = 0
                        while 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'X':
                            move += 1
                            nx += dx[d]
                            ny += dy[d]
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'T':
                            if d % 2:
                                cn += 1
                                for i in range(1, move + 1):
                                    col[x + dx[d] * i][y + dy[d] * i] = cn
                            else:
                                rn += 1
                                for i in range(1, move + 1):
                                    row[x + dx[d] * i][y + dy[d] * i] = rn
if rn <= 3 and cn <= 3:
    need = rn + cn
    graph = [[] for _ in range(rn + 1)]
    for x in range(n):
        for y in range(n):
            if row[x][y] and col[x][y]:
                graph[row[x][y]].append(col[x][y])
    match = [0] * (cn + 1)
    for i in range(1, rn + 1):
        visited = [False] * (cn + 1)
        need -= dfs(i)
        if need <= 3:
            print("YES")
            exit()
    else:
        print("NO")
else:
    print("NO")
```

스터디 문제로 골라갔던 건데, 최적화를 최대한 해서 풀어보고 싶었다. 거를 수 있는 건 다 거르고 나서, 마지막에 이분 매칭으로 답을 구했는데, 이 부분이 매우 몹시 많이 맘에 들지 않는다. 어렵진 않았지만 나중에라도 읽고 고쳐보라고 기록을 해놓기로 했다.



## 최솟값과 최댓값 - [백준 2357](https://www.acmicpc.net/problem/2357)

> 세그먼트 트리

```Python
n, m = map(int, input().split())
min_tree = [0] * (2 * n)
for i in range(n):
    x = int(input())
    min_tree[n + i] = x
max_tree = min_tree[:]
for i in range(n - 1, 0, - 1):
    min_tree[i] = min(min_tree[2 * i], min_tree[2 * i + 1])
    max_tree[i] = max(max_tree[2 * i], max_tree[2 * i + 1])
for _ in range(m):
    init, fin = map(int, input().split())
    init += n - 1
    fin += n - 1
    m = 10 ** 9
    M = 1
    while init <= fin:
        if init % 2:
            m = min(m, min_tree[init])
            M = max(M, max_tree[init])
            init += 1
        if not fin % 2:
            m = min(m, min_tree[fin])
            M = max(M, max_tree[fin])
            fin -= 1
        init //= 2
        fin //= 2
    print(m, M)
```

세그먼트 트리의 기초 중의 기초 문제라 할 수 있겠다. 옛날 같았으면 제곱근 분할법으로 구현했겠지만... 세그 트리를 쉽게 구현할 수 있는 지금 더 이상 그럴 필요가 없어졌다. 반 년 전만 해도 세그 트리 구현 못 해서 쩔쩔맸는데, 막힘없이 세그 트리를 구현할 수 있게 된 것을 기념?하는 느낌?으로 기록해봤다.

특별한 테크닉 없이, 최소 세그트리와 최대 세그트리 2개 만들어서 답을 구해줬다.



## 트리와 경로의 길이 - [백준 12928](https://www.acmicpc.net/problem/12928)

> 냅색, 트리, 구성적?

```Python
n, m = map(int, input().split())
if n <= 2:
    print(0 if m else 1)
else:
    M = ((n - 1) * (n - 2)) // 2
    if M < m:
        print(0)
    else:
        # checker[num of cases][used degree] = 1 if available else 0
        # Maximum degree use : n - 2      
        checker = [[0] * (n - 1) for _ in range(m + 1)]
        for used in range(n - 1):
            temp = (used * used + used) // 2
            if temp > m:
                break
            checker[temp][used] = 1
        for _ in range(n - 1):
            for score in range(m, -1, -1):
                for used in range(n - 2, -1, -1):
                    for new in range(used + 1):
                        temp = (new * new + new) // 2
                        if temp > score:
                            break
                        if checker[score - temp][used - new]:
                            checker[score][used] = 1
                            if score == m and used == n - 2:
                                print(1)
                                exit()
                            break
        print(0)
```

오늘 아침 출근 지하철에서 본 문제다. 굉장히 완전 탐색스러운 풀이가 생각나서 이걸 어떻게 줄이지 생각하다가... n이 최대 50인 걸 확인했다. 그리고 n^5 냅색 풀이가 가능해서 퇴근 후 뚝딱 만들었더니 AC.

뭐 기본 이론은 대학교 강의서 들은 그래프 이론에서 출발하는 느낌? 트리의 모든 노드들의 deg 합은 2n-2일 거고, 최소 deg는 1이므로 n개의 노드가 n-2개의 잉여 deg를 나눠가지도록 해주도록 구성하자. 이 deg 조합을 가지는 노드들로 트리를 항상 만들 수 있다. 이때 deg 값 d가 2 이상인 노드를 중간에 오게 하는 길이 2인 경로의 갯수는 dC2가 된다. 즉 이 값을 모두 더하면 길이가 2인 경로의 전체 가짓수를 구할 수 있다.

이 다음부터는 냅색 느낌으로 해결하면 된다. 다른 냅색들과 다를 것 없이, 역순으로 갱신을 해주면 한 개의 이중 리스트만을 관리하여 답을 얻을 수 있다.

역시 부담없이 재밌게 풀기에는 골1 ~ 플4이 적당한 것 같다.



## 이동 - [백준 1067](https://www.acmicpc.net/problem/1067)

> FFT

```Python
N = 1 << 18
n = int(input())
ax = list(map(int, input().split()))
ax += ax + [0] * (N - 2 * n)
ay = list(reversed(list(map(int, input().split()))))
ay += [0] * (N - n)
fft(ax)
fft(ay)
for i in range(N):
    ax[i] *= ay[i]
fft(ax, inv=True)
ans = 0
for i in range(n):
    if ans < ax[n + i - 1]:
        ans = ax[n + i - 1]
print(ans)
```

FFT 구현은 만들어놓은 구현체 그대로 쓰니까 답 구하는 코드만 보자.

한 수열을 뒤집어서 fft 때리면, 특정 차수의 계수는 수열을 이동시켜서 곱한 값에 대응된다. 예비군 쉬는 시간에 고민하다가 쓰윽 방법이 떠올라서 집에 돌아와서 완성시켰다.



## Range GCD - [백준 12858](https://www.acmicpc.net/problem/12858)

> 레이지 세그트리, 정수론

```Python
def gcd(a, b):
    a, b = abs(a), abs(b)
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


def update(idx):
    while idx > 1:
        idx //= 2
        tree[idx] = gcd(tree[2 * idx], tree[2 * idx])


n = int(input())
arr = list(map(int, input().split()))
tree = [0] * (2 * n)
for i in range(1, n):
    tree[n + i] = arr[i] - arr[i - 1]
for i in range(n - 1, 0, -1):
    tree[i] = gcd(tree[2 * i], tree[2 * i + 1])
memo = [0] * (2 * n)
for _ in range(int(input())):
    s, x, y = map(int, input().split())
    if s:
        x, y = n + x - 1, n + y - 1
        if x != n:
            tree[x] += s
            update(x)
        if y != 2 * n - 1:
            tree[y + 1] -= s
            update(y + 1)
        while x <= y:
            if x % 2:
                memo[x] += s
                x += 1
            if not y % 2:
                memo[y] += s
                y -= 1
            x //= 2
            y //= 2
    else:
        ans = arr[x - 1]
        nx = x + n - 1
        while nx:
            ans += memo[nx]
            nx //= 2
        x, y = n + x, n + y - 1
        while x <= y:
            if x % 2:
                ans = gcd(ans, tree[x])
                x += 1
            if not y % 2:
                ans = gcd(ans, tree[y])
                y -= 1
            x //= 2
            y //= 2
        print(ans)
```

우리쥐가 개같이 멸망한 뒤 해탈한 듯 풀기 시작한 문제다. 슬슬 세그 트리도 구현체가 필요한가 싶기도 하고..

중요한 핵심 포인트는,

> gcd(a, b, c, ...) = gcd(a, a - b, b - c, ...)

하나씩 나눠서 보면 자명한 성질이다. 즉, **구간의 최대 공약수 값은 제일 앞의 값 + 증가량의 최대 공약수 값과 일치한다.**

그러면, 구간 전체에 수를 더하는 쿼리를 어떻게 처리해야할지 감이 잡힌다. 각 구간의 제일 앞의 값은 정확한 값을 알아야 하므로, 느리게 갱신되는 세그 트리로 정확한 값을 관리한다. 각 미소 구간 별 증가량은 어떤 구간에 일정한 수를 더했을 때 구간의 처음과 끝에서만 값이 바뀐다. 그러므로, 미소 구간 별 증가량의 최대 공약수 세그 트리를 만들고, update를 앞 뒤에서만 해준다. 말로 풀어쓰니 어려운데, 코드 보면 이해할 수 있을 거다. 아마도.

제곱근 분할법이 아닌 일반적인 세그 트리로 플1 문제를 푼적이 있던가? 캬~



## 초콜릿과 친구들의 습격 - [백준 25798](https://www.acmicpc.net/problem/25798)

> 애드 혹

```Python
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    b, w = 0, 0
    crack = []
    for _ in range(k):
        x, y = map(int, input().split())
        crack.append((x, y))
        if (x + y) % 2:
            b += 1
        else:
            w += 1
    if (1, 1) not in crack and (1, 2) in crack and (2, 1) in crack:
        w += 1
    if (n, 1) not in crack and (n - 1, 1) in crack and (n, 2) in crack:
        b += 1
    if (1, m) not in crack and (2, m) in crack and (1, m - 1) in crack:
        b += 1
    if (n, m) not in crack and (n - 1, m) in crack and (n, m - 1) in crack:
        w += 1
    print((n * m) // 2 - max(b, w))
```

*Proof by AC*

어디 내놓기엔 너무 부끄러운 코드긴 하지만... 일단 써본다.

체스판 흑백 기준으로 나눴을 떄, 문제에서 구해야 하는 답은 흑과 백 중 더 적은 갯수보다 작거나 같다.

이제 여기서 '작거나'라는 부분을 무시하고 문제를 풀었다. 구석탱이에 초콜릿 2개 먹는 경우는 테케에 나와있어서 걸러주고. 암튼 증명도 안 하고 대충 풀어서 냈는데, 맞아버렸다. 증명하기엔 너무 감이 안 잡힌다...



## 씽크스몰 - [백준 11385](https://www.acmicpc.net/problem/11385)

> FFT, CRT

[백준 14707 그림 그리기](https://www.acmicpc.net/problem/14707) 과 풀이의 결이 비슷하다. 아니, 오히려 아이디어를 떠올릴 것도 없어 더 쉽다. CRT만 할 줄 알면 됐던 문제.


## 종이, 펜, 삼각형 - [백준 22356](https://www.acmicpc.net/problem/22356)

> FFT, 누적합

```Python
n, m = map(int, input().split())
N = 1 << 19
lx = [0] * N
ly = [0] * N
lz = [0] * N
lx[0] = 1
ly[0] = 1
lz[0] = 1
for _ in range(m):
    deg, d = map(int, input().split())
    if deg == 0:
        lx[d] += 1
    elif deg == 60:
        ly[d] += 1
    elif deg == 120:
        lz[n - d] += 1
mx = [0] * N
my = [0] * N
mz = [0] * N
mx[0] = 1
my[0] = 1
mz[0] = 1
for i in range(1, n):
    mx[i] = mx[i - 1] + lx[i]
    my[i] = my[i - 1] + ly[i]
    mz[i] = mz[i - 1] + lz[i]
ans = mx[n // 2] * my[n // 2] * mz[n // 2]
for i in range(n // 2 + 1, n):
    if lx[i]:
        ans += my[n - i] * mz[n - i]
    if ly[i]:
        ans += mz[n - i] * mx[n - i]
    if lz[i]:
        ans += mx[n - i] * my[n - i]
fft(lx)
fft(ly)
for i in range(N):
    lx[i] *= ly[i]
fft(lx, inv=True)
for i in range(n + 1):
    ans -= lx[i] * lz[n - i]
print(ans)
```

문제에서 멋대로 정삼각형 좌표계를 도입했다. 0도를 x, 60도를 y, 120도를 z라 하자. z축까지 원점에서 만나는 형태가 아닌, 세 축의 교점이 한 변의 길이가 m인 정삼각형 이루는 형태로 생각하자. 그러면, 세 직선이 이 정삼각형 안에서 정삼각형을 이룬다는 것은, 각 세 직선 중 가능한 두 직선 쌍의 교점이 모두 이 정삼각형 안에 있다는 뜻이 된다. 이제 각 평행한 축으로부터 떨어진 거리를 각각 a, b, c라 하면 재밌는 성질을 알 수 있다. (c는 120 k 로 입력값이 주어지면 m - k로 구하면 된다)

> 0 < a + b < m 일 때 두 직선이 정삼각형 안에서 만난다.

즉, a + b, b + c, a + c가 범위 안에 있는 세 쌍을 체크해서 다 더 해주면 끝! 이건 누적합으로 해결해주면 된다.

...로 끝났으면 다이아가 아니다. 반례가 있었다. 바로 세 직선이 한 점에서 만날 때이다. 이건 또 어떨 때인지 그림을 보면서 생각해보면 또다시 재밌는 성질을 찾을 수 있다.

> a + b + c = m 이면 (위의 조건을 만족하면서) 한 점에서 만난다.

그러면 이제 한 점에서 만나는 경우의 수를 빼줘야 하는데, 이를 구하기 위해 FFT를 사용해주었다. x와 y 축 평행한 직선의 위치를 각각 마킹해주고, 서로 곱한 뒤 z축 값을 확인하면서 답을 갱신해주면 끝.


이게 문제지 ㅋㅋ 재밌게 푼 문제는 기록을 안 할 수가 없다.

