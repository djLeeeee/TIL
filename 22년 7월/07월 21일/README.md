# 0721



## All Kill - [백준 18527](https://www.acmicpc.net/problem/18527)

수학, 경우의 수

```Python
from sys import stdin

input = stdin.readline


def power(a, b):
    result = 1
    while b > 0:
        if b % 2:
            result *= a
            result %= div
        a *= a
        a %= div
        b //= 2
    return result


div = 998244353
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
ans = 1
m += 1
for x in arr[::-1]:
    m -= x - 1
    ans *= m
    ans %= div
ans *= power(m, div - 2) * (m - n)
ans %= div
print(ans)
```

.



## :diamond_shape_with_a_dot_inside: 최고인 대장장이 토르비욘 - [백준 13361](https://www.acmicpc.net/problem/13361)

분리 집합

```Python
from sys import stdin
from collections import defaultdict

input = stdin.readline


def find(target):
    if not parent[target]:
        parent[target] = target
    if parent[target] != target:
        parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    pa, pb = find(a), find(b)
    if pa == pb:
        is_cycle[pa] = True
    elif pa < pb:
        parent[pb] = pa
        if is_cycle[pb]:
            is_cycle[pa] = True
    else:
        parent[pa] = pb
        if is_cycle[pa]:
            is_cycle[pb] = True


n = int(input())
ans = 0
parent = defaultdict(int)
is_cycle = defaultdict(bool)
for _ in range(n):
    x, y = map(int, input().split())
    ans += x + y
    union(x, y)
memo = defaultdict(list)
for key in parent:
    memo[find(key)].append(key)
for key in memo:
    if is_cycle[key]:
        ans -= sum(memo[key])
    else:
        ans -= sum(memo[key]) - max(memo[key])
print(ans)
```
