# 0622

오늘의집 면접을 봤다. 긴장 안 했다고 생각했는데, 두뇌 회전이 급속도로 느려진 게 느껴졌다. 알게 모르게 긴장한 듯... 첫 술에 배부르랴, 첫 면접 수고했고 좋은 경험이었다.

7월 1 2 3 쭉 알고리즘 대회가 있던 걸로 기억한다. 그 때까진 알고리즘을 좀 더 깊게 파보자.



## 수열과 쿼리 21 - [백준 16975](https://www.acmicpc.net/problem/16975)

세그먼트 트리, 느리게 갱신

```python
from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tree = [0] * (2 * n + 1)
for _ in range(int(input())):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, s, e, k = query
        left = s + n - 1
        right = e + n - 1
        while left <= right:
            if left % 2:
                tree[left] += k
                left += 1
            if not right % 2:
                tree[right] += k
                right -= 1
            left //= 2
            right //= 2
    elif query[0] == 2:
        _, x = query
        ans = arr[x - 1]
        ex = 0
        idx = x + n - 1
        while idx > 0:
            ex += tree[idx]
            idx //= 2
        print(ans + ex)
```

느리게 갱신되는 세그먼트 트리가 이 때 쓰는 거구나! 싶은 문제다.

문제를 읽는 순간 어떻게 풀어야 할지 눈치챘다. 이제 좀 세그 트리가 익숙해진걸까...