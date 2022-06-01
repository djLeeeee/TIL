# 0531



## 쿨한 물건 구매 - [백준 1214](https://www.acmicpc.net/problem/1214)

수학

```python
from sys import stdin

input = stdin.readline

d, p, q = map(int, input().split())
if p == q:
    if d % p:
        print((d // p + 1) * p)
    else:
        print(d)
elif d % p and d % q:
    p, q = min(p, q), max(p, q)
    ans = (d // q + 1) * q
    for i in range(d // q, max(-1, d // q - p), -1):
        remain = d - q * i
        if remain % p == 0:
            ans = d
            break
        else:
            if q * i + (remain // p + 1) * p < ans:
                ans = q * i + (remain // p + 1) * p
    print(ans)
else:
    print(d)
```

플레 문제이긴 한데, 그리 어려운 수학 개념을 사용하진 않았다.

나누고, 나눠떨어지면 반환 아니면 계속 탐색을 진행한다. 이걸 왜 안 풀고 있었을까