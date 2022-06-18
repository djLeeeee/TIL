# 0618

랜덤 문제 드가자~



## :diamond_shape_with_a_dot_inside: 이것도 해결해 보시지 - [백준 13165]

프리발즈 알고리즘

```python
from sys import stdin
from random import randint

input = stdin.readline


def test(idx):
    for _ in range(24):
        v = [randint(0, 1) for _ in range(n)]
        v1 = [0] * n
        v2 = [0] * n
        v3 = [0] * n
        for i in range(n):
            for j in range(n):
                v1[i] += board[i][idx + n + j] * v[j]
        for i in range(n):
            for j in range(n):
                v2[i] += board[i][idx + j] * v1[j]
        for i in range(n):
            for j in range(n):
                v3[i] += board[i][idx + 2 * n + j] * v[j]
            if v2[i] != v3[i]:
                return False
    return True


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
p = 0
ans = 0
while p + 3 * n <= m:
    if test(p):
        ans += 3 * n * n
        p += 3 * n
    else:
        p += 1
print(ans)
```

> 참고글 : [레프네 약방], 탐렢, 네이버 블로그, 2017.02.19
>
> https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=sluggeryck&logNo=220938909066

랜덤 문제로 뽑은 다이아 문제 치고는 쉬워보여서 바로 집었다. 내가 원래 하던 행렬 곱은 O(n<sup>3</sup>) 이었다. 계산해보니까 무조건 시간 초과였다. 괜히 다이아겠어? 그래서 옛날에 들어봤던 행렬 곱 계산을 빨리 하는 방법을 찾아봤다. 대부분 슈트라센 알고리즘이 나왔다. 물론 빠른 알고리즘이긴 하지만, 내가 필요한 건  O(n<sup>2</sup>) 여서... 계속 찾아보다 보니, 굉장히 흥미로운 알고리즘을 찾았다. 바로 **프리발디 알고리즘** 되시겠다. 아래와 같은 순서로 작동한다.

1. 행렬 `A`, `B`를 곱했을 때 `C`가 되는지 알고 싶다고 해보자. 편의상 n by n 행렬로 정의하자. 물론 정사각 행렬이 아니어도 알고리즘의 정당성이 사라지진 않을 것이다.
2. 아래 과정을 `k`번 반복한다.
   1. 길이 n의 벡터 `v`를 생성한다. 각 원소는 0 또는 1로 랜덤 설정해준다.
   2. A * (B * v) = C * v 이면 다음 반복으로 넘어간다. 아니라면, 그대로 거짓을 반환하고 탐색 종료.
3. `k`번 동안 아무 문제가 없었다면 참을 반환.

이 과정이 위 코드의 `test` 함수다. 중간에 랜덤 벡터가 생기는 것 때문에, 정답이 아닐 수도 있다. 대신, 정답 확률이 상당히 높다. `k`번 하게 되면, 1 - 2<sup>-k</sup> 의 정답률을 보인다. 한 번 테스트할 때 1/2의 확률로 정답이니까. 만약 `k`가 20이면 정답률이 99.9999%에 달한다.

프리발디 알고리즘을 알고 나면 전혀 어려운 문제가 아니다. 그래서 답을 쉽게 구했는데 틀렸습니다가 떴다.... 시간초과도 아니고... 혹시 몰라서 `k`를 20에서 24로 늘려줬는데 정답이 됐다. 프리발디 알고리즘 자체가 랜덤성에 의존하다보니, 운이 없었나보다.



