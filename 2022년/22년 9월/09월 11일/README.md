# 0911

추석이라고 문제를 안 풀 순 없다!

이틀간, 이동하는 차 안에서 풀만한 게임 이론 문제를 풀었다.



## 초콜릿 쪼개기 게임 - [백준 22850](https://www.acmicpc.net/problem/22850)

스프라그 그런디

```Python
def check(num):
    if num in [1, 2, 16, 36]:
        return False
    if num % 34 in [6, 10, 22, 26, 30]:
        return False
    return True


n, m = map(int, input().split())
if check(n) or check(m):
    print('sh')
else:
    print('hs')
```

2차원의 초콜릿을 자르는 상황에서 가로로 자른다고 가정하자. 그러면 새로 생긴 조각 2개는 가로 길이가 같다. 그런디 수는 계산할 때 xor 연산을 하므로, 같은 길이가 생긴 것은 알아서 상쇄될 것이다. 그러므로, 한 변이라도 그런디 수가 0이 아니라면 선공이 이긴다는 결론이 나온다.

이 후 그런디 수를 쭉 구해보니, 34주기에 약간의 예외가 있었다. 이전 문제에서 34주기를 구해본 적이 있어서 이런 기괴한 주기임에도 금방 찾아냈다. 34주기가 2번이나 나온 건 봐선 어떤 이유가 있는 거 같기도 하고...

저번처럼 이 문제도 핸드폰 파이썬 앱으로 구현했다. 이 정도 퀄리티면 결제해도 괜찮을지도?



## Wall Making Game - [백준 11717](https://www.acmicpc.net/problem/11717)

스프라그 그런디, 메모이제이션

```Python
def sol(x1, x2, y1, y2):
    state = (x1, x2, y1, y2)
    if state in dp:
        return dp[(x1, x2, y1, y2)]
    if 0 <= x1 <= x2 < n and 0 <= y1 <= y2 < m:
        now = set()
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if board[x][y] == '.':
                    s1 = sol(x1, x - 1, y1, y - 1)
                    s2 = sol(x1, x - 1, y + 1, y2)
                    s3 = sol(x + 1, x2, y1, y - 1)
                    s4 = sol(x + 1, x2, y + 1, y2)
                    now.add(s1 ^ s2 ^ s3 ^ s4)
        for gn in range(401):
            if gn not in now:
                dp[state] = gn
                return gn
    else:
        return 0


n, m = map(int, input().split())
dp = {}
board = [input() for _ in range(n)]
result = sol(0, n - 1, 0, m - 1)
print("First" if result else "Second")
```

그런디 수를 규칙에 맞게 구해주면 된다. 각 가로 세로 범위의 셀들의 그런디 수를 구해주고, 메모이제이션을 이용해 시간 초과를 피했다.

더 이상 플3을 상위 100문제에서 찾아볼 수 없게 됐다. 레이팅을 올리려면 플1 이상 문제를 풀라는 건데... 막막하다.
