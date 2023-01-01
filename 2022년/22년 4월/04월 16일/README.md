# 0416



## 제곱수 - [백준 23287](https://www.acmicpc.net/problem/23287)

수학?

```python
from sys import stdin

input = stdin.readline


def prime_list(n):
    check = [1] * (n + 1)
    check[0] = 0
    check[1] = 0
    result = set()
    for i in range(2, n + 1):
        if check[i] == 1:
            result.add(i)
            for j in range(2 * i, n + 1, i):
                check[j] = 0
    return result


prime = prime_list(10 ** 5)
m = int(input())
if m == 1:
    print(0, 0, 0, 1)
    exit()
stack = []
for p in prime:
    while m % p == 0:
        stack.append(p)
        m //= p
    if m == 1:
        break
ans = [0, 0, 0, 1]
M = max(stack)
sol = [[1] * 5 for _ in range(M + 1)]
sol[0] = []
for i in range(1, M + 1):
    j = 1
    while j * j <= i:
        if len(sol[i]) > len(sol[i - j * j]) + 1:
            sol[i] = sol[i - j * j] + [j]
        j += 1
while stack:
    a = sol[stack.pop()] + [0] * 3
    b1 = abs(+a[0] * ans[0] - a[1] * ans[2] - a[2] * ans[3] - a[3] * ans[1])
    b2 = abs(-a[0] * ans[3] + a[1] * ans[1] - a[2] * ans[0] - a[3] * ans[2])
    b3 = abs(-a[0] * ans[1] - a[1] * ans[3] + a[2] * ans[2] - a[3] * ans[0])
    b4 = abs(-a[0] * ans[2] - a[1] * ans[0] - a[2] * ans[1] + a[3] * ans[3])
    ans = [b1, b2, b3, b4]
print(*ans)
```

$$
\begin{align*}
\sum a_i^2 b_i^2
&=(a_1b_1-a_2b_3-a_3b_4-a_4b_2)^2 \\
&+(a_2b_2-a_1b_4-a_3b_1-a_4b_3)^2 \\
&+(a_3b_3-a_1b_2-a_2b_4-a_4b_1)^2	\\
&+(a_4b_4-a_1b_3-a_2b_1-a_3b_2)^2
\end{align*}
$$

랜덤 문제에서 꿀 문제가 나왔다.

합성수를 네 제곱수의 합으로 나타내는 문제였다. 10<sup>5</sup>까지의 소수를 모두 구해주고, 소인수분해를 한 뒤 각 소수를 네 제곱수의 합으로 나타내주었다. 합성수라는 데에서 힌트를 얻어, 위의 공식을 얻어냈다. 그 다음 천천히 답을 구해주면 된다.

소수에 대해서만 `sol`을 갱신해줘도 될텐데, 현재 방식은 그러기 힘들었던 점이 조금 아쉽다. 연산이 많이 낭비된 느낌? 그래도 간만에 수학 문제로 점수를 올려 기분이 좋다 ㅎ
