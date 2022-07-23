# 0722

알고리즘 공부를 하자~



## 분리집합에서 간선 끊기 테크닉

```Python
class DisjointSetUndo:
    def __init__(_, n):
        _.sz = [1]*(n+1)
        _.par = list(range(n+1))
        _.hist = []

    def union(_, x, y):
        xr = _.find(x); yr = _.find(y)
        if xr == yr: _.hist.append((None, None)); return
        if _.sz[xr] < _.sz[yr]: xr,yr = yr,xr
        _.hist.append((yr, _.par[yr]))
        _.sz[xr]+= _.sz[yr]
        _.par[yr] = xr

    def undo(_):
        x, p = _.hist.pop()
        if x == None: return
        _.sz[_.par[x]]-= _.sz[x]
        _.par[x] = p

    def find(_, x):
        while _.par[x] != x: x = _.par[x]
        return x

import sys;input=lambda:sys.stdin.readline().strip('\n')
MIS = lambda: map(int,input().split())

n, m, C = MIS()
edge = [tuple(MIS()) for i in range(m)]
state = [0] + list(MIS())
DS = DisjointSetUndo(n+1)
sse = {}
for a,b in edge:
    if state[a] > state[b]: a,b = b,a
    if state[a] == state[b]: DS.union(a, b)
    else: sse.setdefault((state[a], state[b]), []).append((a, b))
del edge

ssq = {}
Q = int(input())
ans = [None]*Q
for i in range(Q):
    a, b = MIS()
    if state[a] > state[b]: a,b = b,a
    ssq.setdefault((state[a], state[b]), []).append((a, b, i))

for (sa, sb), queries in ssq.items():
    for a,b in sse.get((sa,sb), []): DS.union(a, b)
    for a,b,i in queries:
        ans[i] = int(DS.find(a) == DS.find(b))
    for _ in sse.get((sa,sb), []): DS.undo()
print(*ans, sep='\n')
```

`jh05013` 님 코드다.

으에... 봐도 모르겠다...
