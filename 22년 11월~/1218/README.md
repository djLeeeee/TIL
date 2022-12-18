# 1218

요새 시간이 너무 빨리 간다... 어째서 벌써 연말인지...

10일 사이에 백준 Class 8 을 달았다. 간만에 코포도 쳤다. 딥2가 일주일 동안 3번이나 열려 다 참가했고, 3번 다 3솔. 파이썬 억까 땜시 4솔 못한 콘테도 있었지만... 어쨌든 레이팅 망쳐놨던거 다시 블루까지 올려놨다. 8~9월에 점수 엄청 떨군 뒤 쳐다보지도 않았는데, 간만에 하니까 머리가 잘 돌아가는 느낌?

12월 25일까지 백준에서 컨테스트 검수자를 신청받는다고 한다. 조건이 코포 퍼플이거나 백준 1500문제 풀기인데, 1주일 내로 퍼플 찍는 건 실패할 확률이 있으므로(애초에 실패할 확률이 더 높지 싶다) 1500문제를 풀기로 했다. 그래서 이번 주말은 남는 시간에 계속 백준을 풀어 딱 100문제 풀었다. 이제 88문제만 더 풀면 검수자 자격 달성이다.

솔브닥에서 신규 이벤트도 시작했다. 평소에 챙겨보던 자보게동 게임을 갖고 올 줄은 몰랐는데... 이벤트에서 랜덤으로 지정해준 플레 문제들을 풀어야 보상을 받을 수 있는 덕분에 의도치 않게 랜덤 플레 문제 풀기를 했다.



## 달리기 - [백준 12963](https://www.acmicpc.net/problem/12963)

> 그리디, 분리 집합

```Python
div = 10 ** 9 + 7
n, m = map(int, input().split())
parents = list(range(n))
road = [tuple(map(int, input().split())) for _ in range(m)]
ans = 0
for i in range(m - 1, -1, -1):
    x, y = road[i]
    px, py = find(x), find(y)
    if px != py:
        if px > py:
            px, py = py, px
        if px == 0:
            if py == n - 1:
                ans += power(3, i)
                ans %= div
            else:
                parents[py] = px
        else:
            parents[px] = py
print(ans)
```

코드 전체를 다 옮기면 너무 난잡해 보이니 핵심 부분만 옮겼다. `find`와 `power` 함수는 너무 많이 써서 뭐... 마크다운 토글도 찾아봤는데, 생각보다 귀찮아서 그만 뒀다.

클래스 8 문제 치곤 수월하게 한 문제였다. **역순으로 도로를 놓을 때, 한 도로가 시작과 끝을 이었다면 그 도로를 통해 모든 플로우를 보낼 수 있다.** <- 이 한 문장을 그대로 구현해주면 된다.



## Washer - [백준 17978](https://www.acmicpc.net/problem/17978)

> 기하학, 수학(통계?)

```Python
n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
mx,my, mz, sq = 0, 0, 0, 0
for x, y, z in arr:
    sq += x * x + y * y + z * z
    mx += x
    my += y
    mz += z
ans = sq - (mx * mx + my * my + mz * mz) / n
if m == 2:
    for i in range(2, n):
        for j in range(1, i):
            x1 = arr[j][0] - arr[i][0]
            y1 = arr[j][1] - arr[i][1]
            z1 = arr[j][2] - arr[i][2]
            for k in range(j):
                x2 = arr[k][0] - arr[i][0]
                y2 = arr[k][1] - arr[i][1]
                z2 = arr[k][2] - arr[i][2]
                d1 = y1 * z2 - y2 * z1
                d2 = z1 * x2 - z2 * x1
                d3 = x1 * y2 - x2 * y1
                mr, mg, mb, cnt = 0, 0, 0, 0
                for x3, y3, z3 in arr:
                    d = (x3 - arr[i][0]) * d1 + (y3 - arr[i][1]) * d2 + (z3 - arr[i][2]) * d3
                    if d > 0:
                        mr += x3
                        mg += y3
                        mb += z3
                        cnt += 1
                pick = [i, j, k]
                for c in range(8):
                    fr, fg, fb, fc = mr, mg, mb, cnt
                    for bit in range(3):
                        if c & (1 << bit):
                            fr += arr[pick[bit]][0]
                            fg += arr[pick[bit]][1]
                            fb += arr[pick[bit]][2]
                            fc += 1
                    if 0 < fc < n:
                        temp = sq - (fr * fr + fg * fg + fb * fb) / fc
                        temp -= ((mx - fr) ** 2 + (my - fg) ** 2 + (mz - fb) ** 2) / (n - fc)
                        if temp < ans:
                            ans = temp
if n == m == 2:
    ans = 0
print(f'{ans:.6f}')
```

충분히 쉬운 부분은 다 빼고 나면, **점들을 2개의 집합으로 나누었을 때 두 집합의 분산의 합의 최솟값**을 구하면 되는 문제다. 뭐 가장 간단한건 2^n 풀이이겠지만, n < 100이므로 다른 걸 생각해봐야 한다.

갈피를 못 잡다가, 문제 조건이 눈에 띄었다. (본문은 영어로 써있지만 크롬 자동 번역을 돌려놨다 ㅋ)

> 어떠한 세 점도 한 직선 위에 있지 않으며, 어떠한 네 점도 한 평면 위에 있지 않다.

n이 100인 거에서 n^4 풀이를 계속 고민하다가 저 말을 보니 딱 떠올랐다. 분산을 최소로 만들려면 당연히 두 개의 집합이 서로 뭉쳐있어야 할 거고, 그렇다면 이 둘을 나눌 수 있는 평면이 존재할 것이다. 그리고 이 평면을 적절히 이동시키면(두 집합으로 나누는 상태에서) 세 점을 지나는 평면을 찾을 수 있을 것이다!

그러므로 이제 우리가 해야하는 건, 세 점을 고른 뒤 나머지 점(세 점 중 한 점을 임의로 원점으로 잡아주자)들과 외적을 해 +, - 로 나눠준다. 한 평면 위에 네 점이 없으므로 0은 안 나올거다. 그리고 골랐던 세 점을 두 집합 중 한 곳에 넣어준다. 8가지 케이스 모두 고려해줬다. 최적화가 가능할 거 같긴 한데...

분산을 구하는 방법은 이미 알고 있어 쉽게 했다. 매번 분산을 새로 계산하지 않고, 제곱의 평균 - 평균의 제곱을 응용해 구해줬다.

결국 이 문제로 클래스 8을 찍었다. 레이팅 2520점. 이러고 나니 백준에 별 미련이 없어져 코포를 세 번 연달아 쳤다. 덕분에 다시 블루도 달아놨다.



## ヘビの JOI 君 - [백준 14475](https://www.acmicpc.net/problem/14475)

> 데이크스트라

```Python
n, m, k = map(int, input().split())
state = [0] * (n + 1)
for i in range(1, n + 1):
    state[i] = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, d = map(int, input().split())
    graph[x].append((y, d))
    graph[y].append((x, d))
# time, now, temperature, cool time
heap = [(0, 1, 0, k)]
cost = [[[float('inf')] * 3 for _ in range(k + 1)] for _ in range(n + 1)]
cost[1][k][0] = 0
while True:
    t, idx, tp, ct = heappop(heap)
    if cost[idx][ct][tp] < t:
        continue
    if idx == n:
        print(t)
        break
    # 불편에서
    if tp != 1:
        for adj, ex in graph[idx]:
            s = state[adj]
            if s != 1:
                # 같은 상태의 불편으로
                if s == tp:
                    if cost[adj][k][s] > t + ex:
                        cost[adj][k][s] = t + ex
                        heappush(heap, (t + ex, adj, s, k))
                # 다른 상태의 불편으로
                elif ex >= ct and cost[adj][k][s] > t + ex:
                    cost[adj][k][s] = t + ex
                    heappush(heap, (t + ex, adj, s, k))
            else:
                # 쿨타임 덜 돈 상태로 편안으로
                if ct > ex:
                    if cost[adj][ct - ex][tp] > t + ex:
                        cost[adj][ct - ex][tp] = t + ex
                        heappush(heap, (t + ex, adj, tp, ct - ex))
                # 쿨타임 다 돈 상태로 편안으로
                elif cost[adj][0][1] > t + ex:
                    cost[adj][0][1] = t + ex
                    heappush(heap, (t + ex, adj, 1, 0))
    # 편안에서
    else:
        for adj, ex in graph[idx]:
            s = state[adj]
            # 불편으로
            if s != 1:
                if cost[adj][k][s] > t + ex:
                    cost[adj][k][s] = t + ex
                    heappush(heap, (t + ex, adj, s, k))
            # 편안으로
            elif cost[adj][0][1] > t + ex:
                cost[adj][0][1] = t + ex
                heappush(heap, (t + ex, adj, 1, 0))
```

솔브닥 트리 꾸미기에서 선물 문제로 나에게 지급된 문제였다. 플레 문제가 4개 지급됐는데, 플3 플3 플5 플5 이렇게 였다. 나머지 4문제는 다 골드라 별 어려움 없이 컷. 플5 두 개는 둘 다 분리 집합 문제여서 수월하게 했다. 여튼 플3 문제 + 일본어 문제라 겁 먹었는데, 번역 돌리니 어렵다기보단 구현이 귀찮은? 그런 문제였다.

3중 리스트를 활용한 데이크스트라로 풀었다. 컨트롤 해야하는 변수와 상황이 많아 오랜만에 주석을 썼다. 주석보면 이해될 듯? `cost`만 좀 설명하면, `cost[x][y][z] = d`는 `x`번 노드에 `y`초 쿨타임이 남은 `z` 상태로 `d`초에 도착했음을 의미한다.

뭐 진짜 오랜만에 데이크스트라를 써서 풀면서 재밌긴 했다.



## 이중 연결 리스트 - [백준 3045](https://www.acmicpc.net/problem/3045)

> LIS, 연결 리스트

```Python
class Node:

    def __init__(self, front, back) -> None:
        self.front = front
        self.back = back


n, m = map(int, input().split())
nodes = [Node(front=None, back=1)]
for i in range(1, n + 1):
    nodes.append(Node(front=i-1, back=i+1))
nodes.append(Node(front=n, back=None))
for _ in range(m):
    s, *xy = input().split()
    x, y = map(int, xy)
    fx, bx = nodes[x].front, nodes[x].back
    nodes[fx].back = bx
    nodes[bx].front = fx
    if s == 'A':
        fy = nodes[y].front
        nodes[y].front = x
        nodes[fy].back = x
        nodes[x].front = fy
        nodes[x].back = y
    elif s == 'B':
        by = nodes[y].back
        nodes[by].front = x
        nodes[y].back = x
        nodes[x].front = y
        nodes[x].back = by
values = []
p = nodes[0].back
while nodes[p].back:
    values.append(p)
    p = nodes[p].back
memo = [0] * n
stack = [-1]
l = 0
for i in range(n):
    value = values[i]
    if value > stack[-1]:
        l += 1
        stack.append(value)
        memo[i] = l
    else:
        left = 0
        right = l
        while left <= right:
            mid = (left + right) // 2
            if stack[mid] < value:
                left = mid + 1
            else:
                t = mid
                right = mid - 1
        stack[t] = value
        memo[i] = t
result = [0] * (l + 1)
print(n - l)
ml = l
p = n - 1
while l:
    while memo[p] != l:
        p -= 1
    result[l] = values[p]
    l -= 1
past = 1
for r in result[1:]:
    for j in range(past, r):
        print(f'A {j} {r}')
    past = r + 1
for i in range(past, n + 1):
    print(f'B {i} {i - 1}')
```

트리 만들기 이벤트의 두번째 플3 문제였다. 금요일 퇴근길 지하철에 머릿속에서 풀고 집 와서 코드 짜줬다.

클래스를 이용해 연결 리스트를 구현해줬다. 사실 간단한 구조라 튜플만 써도 됐겠지만, 한 번 써보고 싶었다.

암튼 연결 리스트를 구현한 뒤 모든 이동 연산을 처리해주고, `values` 리스트에 최종 상태를 저장해줬다. 그럼 이걸 다시 원상 복귀 시키려면 최소 몇번이 들지 생각해보자.

옮기는 전략을 어떻게 할지 생각해보면, 한 번 이동마다 이동하는 애를 맞는 위치에 옮겨야 한다. 여기서 좀 더 생각해보면, 현재 배열에서 LIS를 찾고, 걔네들은 위치를 고정하고 나머지를 채워넣으면 된다는 것을 알 수 있다. LIS를 구하는 건 굳이 쓸 필요 없을 거 같고.. LIS를 구해서 `result`에 저장해줬다. 그 다음 답 출력은,

```Python
past = 1
for r in result[1:]:
    for j in range(past, r):
        print(f'A {j} {r}')
    past = r + 1
for i in range(past, n + 1):
    print(f'B {i} {i - 1}')
```

위에서 볼 수 있듯이 앞에서 쭉 빈 칸 채우고, 맨 뒤 빈 칸을 마지막에 채워줬다. 첫날에 트리 만들기 선물 카드 30장을 바로 다 받아서, 첫날 금요일엔 이벤트 순위 7등이었는데, 오늘 보니 34등이 되어있다. 운빨망겜...
