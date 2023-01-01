# 0630

거의 1주일 만에 쓰는 TIL. 1주일 간 만날 사람 만나면서 놀았다 ㅎㅎ

중간에 2 SAT 플레3 문제 풀긴 했는데, 딱히 쓸 말이 없으니 PASS.



## 배열의 힘 - [백준 8462](https://www.acmicpc.net/problem/8462)

mo's 알고리즘

```python
from sys import stdin

input = stdin.readline

n, t = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for idx in range(t):
    s, e = map(int, input().split())
    queries.append((s - 1, e - 1, idx))
sn = n ** 0.5
queries.sort(key=lambda z: (z[0] // sn, z[1]))
ans = [0] * t
ps, pe, idx = queries[0]
cnt = {}
for i in range(ps, pe + 1):
    if arr[i] not in cnt:
        cnt[arr[i]] = 1
    else:
        cnt[arr[i]] += 1
for x, y in cnt.items():
    ans[idx] += y * y * x
pa = ans[idx]
for s, e, idx in queries[1:]:
    if s < ps:
        for i in range(s, ps):
            if arr[i] not in cnt:
                cnt[arr[i]] = 1
            else:
                cnt[arr[i]] += 1
            pa += arr[i] * (2 * cnt[arr[i]] - 1)
    elif s > ps:
        for i in range(ps, s):
            if arr[i] not in cnt:
                cnt[arr[i]] = -1
            else:
                cnt[arr[i]] -= 1
            pa -= arr[i] * (2 * cnt[arr[i]] + 1)
    if e > pe:
        for i in range(pe + 1, e + 1):
            if arr[i] not in cnt:
                cnt[arr[i]] = 1
            else:
                cnt[arr[i]] += 1
            pa += arr[i] * (2 * cnt[arr[i]] - 1)
    elif e < pe:
        for i in range(e + 1, pe + 1):
            if arr[i] not in cnt:
                cnt[arr[i]] = -1
            else:
                cnt[arr[i]] -= 1
            pa -= arr[i] * (2 * cnt[arr[i]] + 1)
    ans[idx] = pa
    ps, pe = s, e
print(*ans, sep='\n')
```

누가 알았겠는가, 쿼리 문제가 점수 올리기 좋을 줄은..

구간 업데이트가 없는 걸 보고 바로 모스 알고리즘을 떠올렸다. `cnt` 변수에 전체 카운팅이 담기고, 카운팅이 변경될 때 답을 업데이트 한다. 카운팅되는 횟수가 음수가 되는 구간이 생길 수도 있다는 생각이 들어 음수도 고려해야하나... 고민하다가 상관없다는 걸 알게 됐다. 결국엔 0 됐을 때 처리될테니.