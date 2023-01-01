# 0509



## :heavy_exclamation_mark: (WA) 조명등 - [백준 19943](https://www.acmicpc.net/problem/19943)

DP, CHT

```python
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    statue = []
    for _ in range(n):
        x, h = map(int, input().split())
        statue.append((x - h, x + h))
    statue.sort(reverse=True)
    real = [0, statue.pop()]
    while statue:
        s, e = statue.pop()
        if real[-1][1] < e:
            if real[-1][0] < s:
                real.append((s, e))
            else:
                real[-1] = (s, e)
    l = len(real)
    dp = [0] * l
    CHT = [(real[1][1], 0)]
    for i in range(1, l):
        start = 0
        end = len(CHT) - 1
        while start <= end:
            mid = (start + end) // 2
            if CHT[mid][0] <= real[i][1]:
                res = CHT[mid][1]
                start = mid + 1
            else:
                end = mid - 1
        dp[i] = dp[res] + (real[i][1] - real[res + 1][0]) ** 2 // 4
        if (real[i][1] - real[res + 1][0]) % 2:
            dp[i] += 0.25
        if i < l - 1:
            start = 0
            end = len(CHT) - 1
            while start <= end:
                mid = (start + end) // 2
                now = CHT[mid][1]
                s = ((real[i + 1][0] + real[now + 1][0]) + 4 * (dp[i] - dp[now]) / (real[i + 1][0] - real[now + 1][0])) / 2
                if s > CHT[mid][0]:
                    res = mid
                    ns = s
                    start = mid + 1
                else:
                    end = mid - 1
            CHT = CHT[:res + 1] + [(ns, i)]
    print('{0:.2f}'.format(dp[-1]))
```

하루 종일 이거만 붙잡고 있었는데... 어디가 틀렸는지 모르겠다...