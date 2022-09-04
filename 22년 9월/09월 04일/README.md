# 0904

8월달 TIL을 4일치 밖에 안 썼더라. 아무래도 다이아 문제를 풀기에는 시간이 모자랐기도 했고...

남는 시간엔 도커랑 리액트를 좀 공부하는게 좋을 거 같기도?



## 피보나치 수열처럼 보이지만... - [백준 13718](https://www.acmicpc.net/problem/13716)

행렬 분할정복 거듭제곱

```Python
def mul(A, B):
    l = len(A)
    res = [[0] * l for _ in range(l)]
    for x in range(l):
        for y in range(l):
            for z in range(l):
                res[x][y] += A[x][z] * B[z][y]
            res[x][y] %= div
    return res


n, k = map(int, input().split())
div = 10 ** 9 + 7
f = [1] * (k + 1)
for i in range(2, k + 1):
    f[i] = f[i - 1] * i
a = [[0] * (2 * k + 3) for _ in range(2 * k + 3)]
a[-1][-1] = 1
a[-1][-2] = 1
for i in range(k + 1):
    for j in range(i + 1):
        temp = f[i] // (f[j] * f[i - j])
        temp %= div
        a[i][j] = temp
        a[i + k + 1][j] = temp
        a[i][j + k + 1] = temp
c = [2] * (k + 1) + [1] * (k + 1) + [0]
b = [[0] * (2 * k + 3) for _ in range(2 * k + 3)]
for i in range(2 * k + 3):
    b[i][i] = 1
while n > 0:
    if n % 2:
        b = mul(a, b)
    n //= 2
    a = mul(a, a)
ans = 0
for i in range(2 * k + 3):
    ans += b[-1][i] * c[i]
ans %= div
print(ans)
```

n이 최대 10<sup>17</sup>니, 로그 스케일의 시간복잡도로 해결해야 할 것이다. 점화식을 세워보자.

$$
\begin{aligned}
A_{i + 1} &= F_{i + 1} \cdot (i + 1)^{k} \\
&= (F_i + F_{i - 1}) \cdot (i + 1)^{k} \\
&= (F_i + F_{i - 1}) \cdot \sum_{t=0}^k {{k} \choose {t}} i^t
\end{aligned}
$$

위의 식을 활용해 행렬 점화식을 구해보자. F<sub>i,j</sub>를 아래와 같은 형태로 정의하자.

$$
F_{i, j} = \big [F_i \cdot j^0, \; \dots , \; F_i \cdot j^{k} \big ]^{T}
$$

그러면, 행렬 `C`를 j <= i 에 대해 C[i][j] = <sub>i</sub>C<sub>j</sub> 로 정의 했을 때, 아래 식들이 성립하는 걸 확인 할 수 있다.

$$
F_{i + 1, i + 1} = C \cdot F_{i + 1, i}
F_{i + 2, i + 1} = C \cdot F_{i + 1, i} + C \cdot F_{i, i}
$$

F<sub>i,i</sub> 와 F<sub>i+1,i</sub> 를 이용해 F<sub>i+1,i+1</sub> 와 F<sub>i + 2,i + 1</sub> 를 유도했다. 우리가 원하는 건 F<sub>i,i</sub>의 마지막 원소의 합이니 약간의 행렬식에 조작을 해주면 된다.     

```Python
a = [[0] * (2 * k + 3) for _ in range(2 * k + 3)]
a[-1][-1] = 1
a[-1][-2] = 1
for i in range(k + 1):
    for j in range(i + 1):
        temp = f[i] // (f[j] * f[i - j])
        temp %= div
        a[i][j] = temp
        a[i + k + 1][j] = temp
        a[i][j + k + 1] = temp
```

이 과정을 통해 나오는 것이 행렬 `a`이다. 이제 이걸 n번 거듭제곱해서 답을 구하면 된다!

일주일 전에 출근길 지하철에서 처음 읽은 문제였는데, 틈틈이 고민하다가 어제 가닥이 잡혀 식을 거의 하루종일 세웠다. 특히 합을 구하도록 행렬을 설계하는 것이 잘 안 됐다. 이번에 생각해낸 방법을 자주 써먹으면 좋을 거 같다. 이런 문제 더 없나?
