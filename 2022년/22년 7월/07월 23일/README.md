# 0723

아침에 솔브닥 들어갔더니 998솔이었다. 와우...

1000솔을 뭐로 장식할까 고민하다가, 뉴비 시절 처음으로 나에게 절망을 줬던 문제로 하기로 했다. 999솔은 단순 골드 문제.



## 습격자 초라기 - [백준 1006](https://www.acmicpc.net/problem/1006)

DP

```Python
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(1 if arr[0][0] + arr[1][0] <= m else 2)
        continue
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0][0] = 1 if arr[0][0] + arr[1][0] <= m else 2
    dp[0][1], dp[0][2] = 1, 1
    for i in range(1, n):
        u = 1 if arr[0][i - 1] + arr[0][i] <= m else 2
        d = 1 if arr[1][i - 1] + arr[1][i] <= m else 2
        h = 1 if arr[0][i] + arr[1][i] <= m else 2
        dp[i][1] = min(dp[i - 1][2] + u, dp[i - 1][0] + 1)
        dp[i][2] = min(dp[i - 1][1] + d, dp[i - 1][0] + 1)
        dp[i][0] = min(dp[i - 1][0] + h, dp[i][1] + 1, dp[i][2] + 1, dp[i - 2][0] + u + d)
    ans = dp[-1][0]
    if arr[0][0] + arr[0][-1] <= m:
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0][1] = 1
        dp[0][0] = 2
        for i in range(1, n):
            u = 1 if arr[0][i - 1] + arr[0][i] <= m else 2
            d = 1 if arr[1][i - 1] + arr[1][i] <= m else 2
            h = 1 if arr[0][i] + arr[1][i] <= m else 2
            dp[i][1] = min(dp[i - 1][2] + u, dp[i - 1][0] + 1)
            dp[i][2] = min(dp[i - 1][1] + d, dp[i - 1][0] + 1)
            dp[i][0] = min(dp[i - 1][0] + h, dp[i][1] + 1, dp[i][2] + 1, dp[i - 2][0] + u + d)
        ans = min(ans, dp[-1][2])
    if arr[1][0] + arr[1][-1] <= m:
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0][2] = 1
        dp[0][0] = 2
        for i in range(1, n):
            u = 1 if arr[0][i - 1] + arr[0][i] <= m else 2
            d = 1 if arr[1][i - 1] + arr[1][i] <= m else 2
            h = 1 if arr[0][i] + arr[1][i] <= m else 2
            dp[i][1] = min(dp[i - 1][2] + u, dp[i - 1][0] + 1)
            dp[i][2] = min(dp[i - 1][1] + d, dp[i - 1][0] + 1)
            dp[i][0] = min(dp[i - 1][0] + h, dp[i][1] + 1, dp[i][2] + 1, dp[i - 2][0] + u + d)
        ans = min(ans, dp[-1][1])
    if arr[0][0] + arr[0][-1] <= m and arr[1][0] + arr[1][-1] <= m:
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0][0] = 2
        for i in range(1, n - 1):
            u = 1 if arr[0][i - 1] + arr[0][i] <= m else 2
            d = 1 if arr[1][i - 1] + arr[1][i] <= m else 2
            h = 1 if arr[0][i] + arr[1][i] <= m else 2
            dp[i][1] = min(dp[i - 1][2] + u, dp[i - 1][0] + 1)
            dp[i][2] = min(dp[i - 1][1] + d, dp[i - 1][0] + 1)
            dp[i][0] = min(dp[i - 1][0] + h, dp[i][1] + 1, dp[i][2] + 1, dp[i - 2][0] + u + d)
        ans = min(ans, dp[-2][0])
    print(ans)
```

**축 1000솔 달성**

단순 DP 문제이다. 원형이기 때문에 시작점 기준으로 맨 끝 점과 붙어서 특공대를 파견하는 경우를 고려해주어야 한다. 코드가 길어보이지만 절반이 DP 복붙이다. 짚고 갈만한 포인트는 없는 듯?

![캡처](https://user-images.githubusercontent.com/97663863/180616527-c20220ee-2c2e-474e-8d4c-9fc42e386875.PNG)

근 6개월 동안 수고했다!
