# 0624

로그인 안 한 채로 비밀번호 변경을 억지로 구현했다. 진짜 하나부터 열까지 맘에 안 드는데..



## 수열과 쿼리 5 - [백준 13547](acmicpc.net/problem/13547)

mo's 알고리즘

```python
from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
querys = []
q = int(input())
for i in range(q):
    s, e = map(int, input().split())
    querys.append((s - 1, e - 1, i))
sq = n ** 0.5
querys.sort(key=lambda x: (x[1] // sq, x[0], x[2]))
ans = [0] * q
check = defaultdict(int)
used = 0
s, e, idx = querys[0]
for i in range(s, e + 1):
    check[arr[i]] += 1
    if check[arr[i]] == 1:
        used += 1
ps, pe = s, e
ans[idx] = used
for s, e, idx in querys[1:]:
    if pe < s:
        check = defaultdict(int)
        used = 0
        for i in range(s, e + 1):
            check[arr[i]] += 1
            if check[arr[i]] == 1:
                used += 1
    else:
        if s > ps:
            for i in range(ps, s):
                check[arr[i]] -= 1
                if check[arr[i]] == 0:
                    used -= 1
        else:
            for i in range(s, ps):
                check[arr[i]] += 1
                if check[arr[i]] == 1:
                    used += 1
        if e > pe:
            for i in range(pe + 1, e + 1):
                check[arr[i]] += 1
                if check[arr[i]] == 1:
                    used += 1
        else:
            for i in range(e + 1, pe + 1):
                check[arr[i]] -= 1
                if check[arr[i]] == 0:
                    used -= 1
    ps, pe = s, e
    ans[idx] = used
print(*ans, sep='\n')
```

저번 달 쯤에 mo's 알고리즘을 처음 접하고 풀었던 문제다. 그런데 시간 초과가 떴었다... 오늘 왕십리서 놀고 돌아가는 버스에서, 갑자기 번뜩였다. 제곱근 분할법이랑 비슷하게 접근해서 생각해보는 것이다. 그렇게 되면 sqrt n으로 나눈 몫에 대해 정렬하면 되겠다는 생각이 든다. 뭐 굳이 따지자면 전에 글을 읽은 적이 있으니까 이해가 금방 된 점도 있다. 각 쿼리 처리하는 부분은 그냥 단순 구현이니까 따로 설명할 건 없다.

암튼 CLASS 7이 1문제 밖에 안 남았다. 마지막 문제도 mo's 알고리즘으로 장식해볼까 한다.



## 수열과 쿼리 6 - [백준 13548](https://www.acmicpc.net/problem/13548)

mo's 알고리즘

```python
from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
querys = []
m = int(input())
for i in range(m):
    s, e = map(int, input().split())
    querys.append((s - 1, e - 1, i))
sn = n ** 0.5
querys.sort(key=lambda x: (x[0] // sn, x[1]))
ans = [0] * m
cnt = defaultdict(int)
cnt_inv = defaultdict(int)
cnt_inv[0] = n
ps, pe, _ = querys[0]
for idx in range(ps, pe + 1):
    cnt_inv[cnt[arr[idx]]] -= 1
    cnt[arr[idx]] += 1
    cnt_inv[cnt[arr[idx]]] += 1
mx = max(cnt.values())
for s, e, i in querys:
    if ps < s:
        for idx in range(ps, s):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] -= 1
            cnt_inv[cnt[arr[idx]]] += 1
            if not cnt_inv[mx]:
                mx -= 1
    elif s < ps:
        for idx in range(s, ps):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] += 1
            cnt_inv[cnt[arr[idx]]] += 1
            if not cnt_inv[mx + 1]:
                mx += 1
    if pe < e:
        for idx in range(pe + 1, e + 1):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] += 1
            cnt_inv[cnt[arr[idx]]] += 1
            if not cnt_inv[mx + 1]:
                mx += 1
    elif e < pe:
        for idx in range(e + 1, pe + 1):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] -= 1
            cnt_inv[cnt[arr[idx]]] += 1
            if not cnt_inv[mx]:
                mx -= 1
    ps, pe = s, e
    ans[i] = mx
print(*ans, sep='\n')
```

결국 CLASS 7을 찍었다! 마지막을 쿼리 문제로 할 줄이야...

모스 알고리즘을 알고 나면 금방 할 수 있는 문제였다. 쿼리를 계산하는 동안 수열의 업데이트가 없으므로 전형적인 오프라인 쿼리 문제이고, 이를 모스 알고리즘으로 최적화 해주면 된다. 주의할 점은, 처음엔 단순하게 `ans[i] = max(cnt.values())` 로 했더니 시간 초과가 났다. 뭐 당연하긴 하다. 그래서 O(1)에 처리할 수 있도록 했다. 한 칸 씩 업데이트하면서 `mx`도 같이 업데이트 해주고, 마지막에 `ans[i]`에 대입해주는 방식이다. 플1 문제 치고는 그렇게 어려운 로직은 없는? 그런 느낌이다.

클 7 찍으면서 오늘 하루동안 14점이나 올렸다. 크흐흐...
