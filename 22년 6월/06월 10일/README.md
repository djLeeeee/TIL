# 0610

8일, 9일, 10일 2박 3일 간 가족 여행 가느라 TIL 쓸 새가 없었다. 하지만 매일 알고리즘을 풀긴 했다.

그래서 오늘은 오늘 푼 것 뿐만 아니라 3일간 푼 문제 모두 올릴 생각이다.

내일은 현대 오토에버, 일요일엔 SKT + 오늘의집 코테가 있으니 넘 무리하지 말자.

잠 안 오면 1시 30분에 Codeforce 가고 ㅇㅇ



## 교차하지 않는 원의 현들의 최대 집합 - [백준 2673](https://www.acmicpc.net/problem/2673)

DP

```python
from sys import stdin

input = stdin.readline

n = int(input())
line = [[0] * 101 for _ in range(101)]
for _ in range(n):
    s, e = map(int, input().split())
    line[s][e] = 1
    line[e][s] = 1
dp = [[0] * 101 for _ in range(101)]
for i in range(1, 101):
    for j in range(i, 0, -1):
        for k in range(j, i):
            if dp[j][i] < dp[j][k] + dp[k][i] + line[i][j]:
                dp[j][i] = dp[j][k] + dp[k][i] + line[i][j]
print(dp[1][100])
```

CLASS 7 문제 중 만만해 보이는 놈 골랐다.

선분이 존재하는 양 끝점에 대해서 2차원 리스트를 만들어 표시해줬다. 그 다음, dp 식을 세웠다.

수식까지 쓸 거 없이, 코드에 점화식이 그대로 나타나있다. 약간 플로이드 와샬 같은 느낌? 으로 생각하면 될 거 같다. 중간 점을 이동하면서 dp 값을 갱신해주는 형태이다. (플로이드 와샬은 중간 지점이 for 문 처음에 나오긴 하지만)

이게 2일 전에 푼 문제. 군산 내려가는 자동차에서 풀었다. 풀고 '나 정말 미친 놈인가?'란 생각이 들었다.



## 열혈강호 3 - [백준 11377](https://www.acmicpc.net/problem/11377)

이분 매칭

```python
from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    _, *a = map(int, input().split())
    graph[i] = a
match = [0] * (m + 1)
ans = 0
for i in range(1, n + 1):
    visited = [False] * (m + 1)
    ans += dfs(i)
for i in range(1, n + 1):
    if k == 0:
        break
    visited = [False] * (m + 1)
    if dfs(i):
        ans += 1
        k -= 1
print(ans)
```

이 친구도 달리는 차 안에서 풀었다. 뭔가 시간이 지나고 나니 뭐하러 그렇게까지 풀었는가 싶긴 하다.

최대 유량 냄새가 솔솔 나서 시도 안하고 있었는데, 일의 최대 제한이 2 밖에 안 돼서 단순하게 이분 매칭 한 번 더 하면 되겠다라는 생각이 들었다. 문제 풀이 순서는 아래와 같다.

1. 일반적인 이분 매칭을 진행한다. 인당 1개의 일이 배정될 때 최대 매칭이 나온다.
2. **앞에서부터 한 번씩 매칭을 또 해준다.** 두번째 이분 매칭에서 일을 받은 사람이 k가 넘어가면 그대로 종료.

이 때 조금 고민할 만한 포인트가 있었다.

> 2번 매칭에서 일을 배정받는 사람은 1번 매칭에서 이미 일을 받았는가?

조금 고민해보니 답이 나왔다. 거꾸로 생각해보면 된다. 만약 1번 매칭에서 일을 받지 않은 사람이 2번 매칭에서 일을 받았다면, 진작에 1번 매칭에서 일을 받았을 것이다. 그러므로 2번 매칭에서 일을 받은 사람은 일을 2개 배정받았음을 증명할 수 있다.

호프크로프트 카프로 해야 시간 초과를 피하는 거 같은데, 차 안에서 머리 쓰기 너무 힘들어서 그대로 디닉으로 짜고 PyPy3로 제출했다. 호프크로프트 카프 복습하긴 해야하는데... 디닉이 너무 편해...



## Plug It In!  - [백준 16056](https://www.acmicpc.net/problem/16056)

이분 매칭

```python
from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == idx:
            continue
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(k):
    s, e = map(int, input().split())
    graph[s].append(e)
match = [0] * (m + 1)
ans = 0
for i in range(n + 1):
    visited = [False] * (m + 1)
    ans += dfs(i)
ex = 0
p = 1
memo = match[:]
while p <= n and ex < 2:
    now_ex = 0
    match = memo[:]
    for _ in range(2):
        visited = [False] * (m + 1)
        now_ex += dfs(p)
    if ex < now_ex:
        ex = now_ex
    p += 1
print(ans + min(ex, 2))
```

이 친구도 달리는 차 안에서 해결했다. 어지간히 심심했었나 보다.

진작에 이분 매칭 문제인 거 눈치채고 북마크해놨던 문제다. 북마크가 너무 쌓였길래 쭉 보다가 눈에 띄어서 이 문제를 집었다.

앞에 열혈강호와 흐름이 비슷하다. 쭉 매칭을 진행하고, 앞에서부터 매칭을 다시 진행한다. 이 때, **추가로 진행한 매칭을 초기화 해주어야 한다.**

```python
memo = match[:]
while p <= n and ex < 2:
    now_ex = 0
    match = memo[:]
    ...
```

이렇게 해줘야 다시 롤백이 되면서 최대 2개 연결되는 곳을 찾을 수 있다.



## 같은 탑 - [백준 1126](https://www.acmicpc.net/problem/1126)

DP

```python
from sys import stdin

input = stdin.readline

n = int(input())
tower = [0] + list(map(int, input().split()))
m = sum(tower) // 2 + 1
dp = [-1] * (m + 1)
dp[0] = 0
for i in range(1, n + 1):
    new_dp = [-1] * (m + 1)
    h = tower[i]
    if h > m:
        continue
    new_dp[0] = 0
    if dp[h] != -1:
        new_dp[0] = dp[h]
    if dp[0] > 0:
        new_dp[0] = max(new_dp[0], dp[0])
    for j in range(1, m + 1):
        now = dp[j]
        if j >= h and dp[j - h] != -1:
            if now < dp[j - h] + h:
                now = dp[j - h] + h
        if j <= h and dp[h - j] != -1:
            if now < dp[h - j] + j:
                now = dp[h - j] + j
        if j + h <= m and dp[j + h] != -1:
            if now < dp[j + h]:
                now = dp[j + h]
        new_dp[j] = now
    dp = new_dp
if dp[0] != 0:
    print(dp[0])
else:
    print(-1)
```

> 옛날에 참고했던 글이다 : [준호 황] BOJ 1126 - 같은 탑
>
> https://junh0.tistory.com/2

요건 어제 숙소에서 푼 문제다. 잔디 심기 겸 CLASS 7 달성 용으로 풀었다. 이것도 옛날부터 눈여겨 본 문제라, 풀이 방법은 대강 알고 있었다. 한 3달 전 쯤에 위 블로그 글을 읽고 '이런 풀이가 있구나'라고 생각했었는데, 어제 다시 봤음에도 아직 풀이를 기억하고 있어, 이 정도면 내 꺼가 됐겠구나 싶어서 문제를 풀었다. 

내가 발견한 풀이는 아니라 길게 쓰긴 그렇고, 저 분 블로그에 정말 잘 정리되어 있다.



##  마법의 나무 - [백준 13441](https://www.acmicpc.net/problem/13441)

이분 매칭

```python
from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n = int(input())
graph = [[] for _ in range(n + 1)]
relation = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    line = input()
    for j in range(n):
        if line[j] == '1':
            relation[i].append(j + 1)
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    point = [i]
    while point:
        now = point.pop()
        for nei in relation[now]:
            if not visited[nei]:
                visited[nei] = True
                point.append(nei)
                graph[i].append(nei)
match = [0] * (n + 1)
ans = n
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    ans -= dfs(i)
print(ans)
```

[Algorithm Teaching](https://www.acmicpc.net/problem/18029) 문제와 같은 맥락이다. 딜워스의 정리를 활용해야 한다. 기억 잘 안 나면 6월 1일 TIL로.

일단 이분 그래프를 그려야 한다. 어떤 나무(왼쪽)가 마법의 나무 또는 보호받는 나무가 되었을 때, 그로 인해 보호받는 나무가 될 나무들(오른쪽)을 간선으로 이어준다. 주의할 점은, **바로 하위의 나무들이 아닌, 하위의 모든 나무들이 연결되어야 한다.** 왜 그래야 하는지는 문제의 예시 입력 3을 보면 알 수 있다.

이렇게 해서 그린 이분 그래프에서, 우리가 구해야 할 답이 무엇인지 생각해보자. 마법의 나무이면서 보호받지 않는 나무를 최대로 한다는 의미는, maximum anti chain를 구해야 한다는 의미인다. 우리가 그린 그래프는 DAG니까, 딜워스의 정리에 의해 minimum path cover를 구하면 된다. 그리고 이는, 이분 매칭으로 구할 수 있다.

휴... 3일간 푼 문제 정리하느라 힘들었다.