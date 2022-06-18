# 0617

드디어 노쓸모 계절학기가 끝났다. 이제 알고리즘에 전념하자.

면접 시즌이니 CS 공부도 좀 하고.



## 직사각형 색칠 2 - [백준 18286](acmicpc.net/problem/18286)

분할 정복 거듭 제곱, 비트마스킹 DP

```python
from sys import stdin

input = stdin.readline
div = 10 ** 9 + 7


def matrix_multiple(first, second=False):
    if not second:
        second = first
    res = [[0] * s for _ in range(s)]
    for x in range(s):
        for y in range(s):
            for z in range(s):
                res[x][y] += first[x][z] * second[z][y]
            res[x][y] %= div
    return res


n, m = map(int, input().split())
s = 1 << m
mat = [[0] * s for _ in range(s)]
for i in range(s):
    c1 = [1 if (1 << bit) & i else 0 for bit in range(m)]
    for j in range(i, s):
        c2 = [1 if (1 << bit) & j else 0 for bit in range(m)]
        mat[i][j] = 1
        mat[j][i] = 1
        for k in range(m - 1):
            if c1[k] == c1[k + 1] == c2[k] == c2[k + 1]:
                mat[i][j] = 0
                mat[j][i] = 0
                break
e = [[0] * s for _ in range(s)]
for i in range(s):
    e[i][i] = 1
n -= 1
while n > 0:
    if n & 1:
        e = matrix_multiple(mat, e)
    mat = matrix_multiple(mat)
    n //= 2
ans = 0
for i in range(s):
    ans += sum(e[i])
    ans %= div
print(ans)
```

와... 얼마만에 점수를 올리는 걸까... 1점 올리기가 이렇게 힘들었던가...

돌아온 랜덤 문제 풀기다. 40분 정도 걸렸다.

핵심은 `mat` 행렬을 짜기이다. 비트 연산을 이용해 검은색인지 흰색인지 체크하고, 네모가 나오는지 체크한다. 그 다음 행렬 곱을 해주면 되는데, 10<sup>18</sup> 스케일이니 당연히 분할 정복으로 최적화해줬다.

