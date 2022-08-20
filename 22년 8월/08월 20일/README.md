# 0820

2주만인가? 오랜만에 쓰는 거 같다. 계속 맥북만 썼더니, 원래 노트북 자판이 익숙하지가 않다. 암튼 2주 동안,

- 회사 적응하기
- 알고리즘 문제 매일 1문제 씩
- solved.ac 블랙잭 이벤트
- 알고리즘 리뷰, 스터디 등등...

적당히 바빴던 거 같다. 다이아 문제는 이제 풀기 힘들 거 같고, 하루에 골플 1문제 정도? 코드포스도 이젠 더 하기 힘들 거 같다. 아무래도 자야 할 시간이니...

2주간 풀었던 문제 중 정리할 만한 문제만 꼽자면,



# 숌 언어 - [백준 1444](https://www.acmicpc.net/problem/1444)

이분 매칭

```Python
def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


target = input().upper()
l = len(target)
target = [ord(t) - 65 for t in target]
graph = [set() for _ in range(26 * 26 + 1)]
head, tail = target[0] * 26 + target[1] + 1, target[-2] * 26 + target[-1] + 1
if l % 2:
    tail *= -1
for i in range(1, l - 1):
    x, y, z = target[i - 1:i + 2]
    first, second = x * 26 + y + 1, y * 26 + z + 1
    if i % 2:
        second *= -1
    else:
        first *= -1
    if len({first, second, head, tail}) == 4 - (head == tail):
        if i % 2:
            graph[first].add(second)
        else:
            graph[second].add(first)
ans = 0
match = [0] * (26 * 26 + 1)
for i in range(1, 26 * 26 + 1):
    visited = [False] * (26 * 26 + 1)
    ans += dfs(i)
ans += 1 + (head != tail)
print(ans)
```

대문자와 소문자가 번갈아 가면서 나오고, 단어를 어디서 끊을지 정하기? 누가 봐도 이분 매칭 문제다. 맨 앞 두 글자와 맨 뒤 두 글자는 반드시 한 단어이므로 예외 처리만 해주면 된다. 이후는 별 특별한 거 없이 이분 매칭. 큰 의미는 없지만, 논리형으로 연산 표시를 해 코드 길이를 조금 줄여봤다.



# Checker Board - [백준 7003](https://www.acmicpc.net/problem/7003)

스프라그-그런디 정리

```Python
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n, m, w, b = map(int, input().split())
    white = [0] * (n + 1)
    black = [0] * (n + 1)
    for _ in range(w):
        x, y = map(int, input().split())
        white[x] = y
    for _ in range(b):
        x, y = map(int, input().split())
        black[x] = y
    gn = 0
    w, b = False, False
    for i in range(1, n + 1):
        if white[i] and black[i]:
            gn ^= abs(white[i] - black[i]) - 1
        elif white[i] and not w:
            w = True
        elif black[i] and not b:
            b = True
    if w and b:
        print('T')
    elif w:
        print('W')
    elif b:
        print('B')
    else:
        if gn:
            print('W')
        else:
            print('B')
```

두 말이 일직선에 배치되어 있을 때, 그 줄의 그런디 수를 구하는 문제다. 단순하게 두 말의 거리 차이에서 1을 빼면 그런디 수가 나온다. 한 줄에 말이 한 종류만 있을 때는 그 말만 계속 움직일 수 있으니, 예외 처리만 해주면 끝.

쉬운 편이지만 굳이 기록해놓는 이유는, 나 혼자 푼 문제다!

![image](https://user-images.githubusercontent.com/97663863/185746740-05f55074-2242-4175-aeb5-947f85251556.png)

드디어 나한테도 혼자 푼 문제가 생겼다. 난이도 평가를 하면 다른 사람들이 풀 수도 있을 거 같아서 그냥 평가하지 말까 고민도 했는데, 그건 좀 아닌 거 같아서 평가하고 왔다. 푼 사람이 1명인 문제 카테고리에 내 아이디가 올라가 있더라 ㅎㅎ



# King(Small) - [백준 12865](https://www.acmicpc.net/problem/12685)

게임 이론

```Python
from sys import stdin

input = stdin.readline


dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]


def turn(x, y):
    print(x, y)
    board[x][y] = '#'
    res = 0
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.' and not turn(nx, ny):
            res = 1
            break
    board[x][y] = '.'
    return res


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'K':
                ans = 'A' if turn(i, j) else 'B'
                break
    print(f'Case #{t}: {ans}')
```

게임판 사이즈가 4 by 4 이기 때문에, 완전 탐색에 기반한 게임 이론 코딩을 했다.

하던대로 했다. 게임판을 만들고 왕 위치에서 출발해서, 8방향 탐색을 하고, 상대가 지는 칸으로 이동할 수 있다면 승리를 반환한다. 이 때 백트래킹 느낌으로 방문 표시 후 다시 되돌려놓는 방법을 사용했다.

역시 게임 이론 문제는 풀었을 때나, 정답을 맞췄을 때 신난다! 문제를 풀다가 `n`과 `m`을 헷갈려 2트에 정답을 맞춘 건 조금 아쉽다.
