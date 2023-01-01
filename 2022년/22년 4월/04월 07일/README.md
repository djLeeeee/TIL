## 0407

그냥 참... 뭔가 그런 하루다...

2 SAT 다이아를 푸니 시간 초과가 뜨고.... 이분 매칭 다이아를 푸니 시간 초과가 뜨고....

왜 이들은 나에게 새 알고리즘을 강요하는가.... 왜 알고리즘은 끝이 없는가.....해서 오늘은!

1. Hopcroft Karp Algorithm - 이분 매칭인데 시간 복잡도가 EV<sup>0.5</sup> ?!
2. Tarjan's Algorithm - SCC를 구하는데 DFS를 한 번만?!
3. Edmond-Karp Algorithm - 최대 유량 스킬을 아직도 안 배운 다이아(진)이 있다고?!

셋 중 하나라도 내 스킬로 만들면 성공한 하루일지도?!



## 홉크로프트 카프 Hopcroft Karp Algorithm

이분 매칭 알고리즘이다. 

```python
__import__('sys').setrecursionlimit(123123)
INF = 10**9
from collections import deque
def BFS(ssz, tsz, adj, pu, pv, dist):
    Q = deque()
    for u in range(1, ssz+1):
        if pu[u] == 0: dist[u] = 0; Q.append(u)
        else: dist[u] = INF
    dist[0] = INF
    while Q:
        u = Q.popleft()
        if dist[u] >= dist[0]: continue
        for v in adj[u]:
            if dist[pv[v]] == INF: dist[pv[v]]=dist[u]+1; Q.append(pv[v])
    return dist[0] != INF

def DFS(ssz, tsz, adj, pu, pv, dist, u):
    if u == 0: return True
    for v in adj[u]:
        if dist[pv[v]]==dist[u]+1 and DFS(ssz,tsz,adj,pu,pv,dist,pv[v]):
            pv[v] = u; pu[u] = v; return True
    dist[u] = INF; return False

def HopcroftKarp(ssz, tsz, adj):
    assert not adj[0] and not any(0 in L for L in adj)
    pu = [0]*(ssz+1); pv = [0]*(tsz+1); dist = [-1]*(ssz+1); match = 0
    while BFS(ssz, tsz, adj, pu, pv, dist):
        for u in range(1, ssz+1):
            if pu[u] == 0: match+= DFS(ssz, tsz, adj, pu, pv, dist, u)
    return match

input = __import__('sys').stdin.readline
MIS = lambda: map(int,input().split())

n, k = MIS()
black = {}
white = {}
for i in range(n):
    for j in range(n):
        if (i+j)%2 == 0: black[i,j] = len(black)
        else: white[i,j] = len(white)
ban = {tuple(MIS()) for i in range(k)}

adj = [[] for i in range(len(black)+1)]
for i in range(n):
    for j in range(n):
        if (i+j)%2 == 1 or (i+1,j+1) in ban: continue
        idx = black[i,j]
        for ni,nj in (i-2,j-1),(i-2,j+1),(i-1,j-2),(i-1,j+2),(i+2,j-1),(i+2,j+1),(i+1,j-2),(i+1,j+2):
            if (ni,nj) not in white or (ni+1,nj+1) in ban: continue
            adj[idx+1].append(white[ni,nj]+1)
print(n*n - len(ban) - HopcroftKarp(len(black), len(white), adj))
```

`jh05013`님의 코드다.

...는 공부하다가 싸피 사람들 만나서 놀았다. 내일 하자.
