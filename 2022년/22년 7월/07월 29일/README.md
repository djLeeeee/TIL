# 0729

점수 쑥쑥 오른다~



## :diamond_shape_with_a_dot_inside: 괄호 - [백준 13174](https://www.acmicpc.net/problem/13174)

조합론

```Python
def power(a, b):
    res = 1
    while b > 0:
        if b % 2:
            res *= a
            res %= div
        a *= a
        a %= div
        b //= 2
    return res


n, k = map(int, input().split())
ans = 1
div = 10 ** 9 + 7
factor = 1
for i in range(1, n + 1):
    ans *= k + 1
    if i % 2:
        if i > 1:
            r = i // 2 - 1
            factor *= k
            factor *= (4 * r + 2)
            factor *= power(r + 2, div - 2)
            factor %= div
        ans -= factor
    ans %= div
print(ans)
```

음~ 점수 달다~ 상당히 무식한 방법이지만 확실한 방법으로 풀었다. 바로 손으로 직접 점화식 풀기 ㅎ

점화식을 세워보자. k는 고정시켜놓고, A<sub>n</sub>을 구해보면,

$$
A_n = k \cdot A_{n - 1} + \sum_t^{n/2} k^t \cdot A_{n-2t}   
$$

왜 이렇게 되냐면,

- 첫번째 항은 n-1 개의 괄호를 1개의 괄호로 감싸는 경우의 수. 감싸는 괄호를 k개 중 한 개 고르면 된다.
- 두번째 항(시그마)은 양 끝에 연속된 괄호가 있는 것들의 경우의 수. 여기서 t개의 연속된 괄호란, 여는 괄호가 연속으로 t개 나온 뒤 닫는 괄호가 연속으로 t개 나오는 걸 의미.

아무래도 이 식만 보고 일반항 구하기는 힘들다. A<sub>0</sub>은 1이니까, 차례대로 구해보면,

$$
A_0 = 1 \\
A_1 = k \\
A_2 = k^2 + k \\
A_3 = k^3 + 2k^2 \\
A_4 = k^4 + 3k^3 + 2k^2 \\
A_5 = k^5 + 4k^4 + 5k^3 \\
\cdots
$$

대~충 k+1배 씩 늘어나는 걸 확인할 수 있다. k+1과의 차이를 보면,

$$
1, \ 0,\ k,\ 0,\ 2k^2,\ 0,\ 5k^3,\ 0,\ 14k^4,\ 0,\ 42k^5,\ 0,\ \cdots
$$

홀수 번째에, 지수는 1씩 늘어나는 건 알 수 있고, 문제는 계수다. 계수를 보면 1, 1, 2, 5, 14, 42 ... 처음엔 14까지만 보고 초항 제외 f(t) = 3t - 1 형태인가 했는데, 앞에 1이 2개 있는 거 보고 이상해서 다음 항까지 구해보니 아니었다. 잘 안 보여서 검색해보니, [카탈란 수](https://ko.wikipedia.org/wiki/%EC%B9%B4%ED%83%88%EB%9E%91_%EC%88%98)와 똑같았다. 뭔지는 저기에 잘 써있다. 카탈란 수 정의에 따라 계산해보니 (4n+2)/(n+2) 배 씩 늘어나는 걸 찾을 수 있었다. 그대로 코딩해줬더니 AC!
