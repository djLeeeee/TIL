# 0507



## Best Tree - [백준 18459](https://www.acmicpc.net/problem/18459)

트리

```python
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    t = 0
    for num in arr:
        if num > 1:
            t += 1
    if n == 2:
        print(1)
    else:
        print(min(n // 2, t))
```

이게 왜 플레?

리프 노드를 따로 빼놓고, 아닌 노드들로 그래프를 대강 완성시킨 뒤, 나중에 리프 노드들을 최소 하나씩 붙혀준다고 생각하면 된다. 예외 케이스인 n = 2일 때를 고려해주면 AC.



## :diamond_shape_with_a_dot_inside: Cow Sorting - [백준 6223](https://www.acmicpc.net/problem/6223)

그리디

```python
from sys import stdin

input = stdin.readline


def sol(idx):
    if nums[idx] == result[idx]:
        return 0
    cycle = set()
    while nums[idx] not in cycle:
        cycle.add(nums[idx])
        idx = inv[nums[idx]]
    for num in cycle:
        nums[inv[num]] = num
    m = min(cycle)
    l = len(cycle)
    return sum(cycle) + min(m + result[0] * (l + 1), (l - 2) * m)


n = int(input())
nums = [int(input()) for _ in range(n)]
result = sorted(nums)
inv = {result[i]: i for i in range(n)}
ans = 0
for j in range(n):
    ans += sol(j)
print(ans)
```

음... 새로 푼 문제가 아니다. 옛날에 [짐 정리](https://www.acmicpc.net/problem/2569) 문제랑 같은 문제길래 코드를 그대로 제출했는데 맞았다. 아무리 봐도 다이아가 아니라서 플1로 난이도 조정 제출했다. 이거 말고도 똑같은 문제가 더 있었다.

- :diamond_shape_with_a_dot_inside: **[백준 1851 추 정렬하기]** 완벽하게 똑같음
- :diamond_shape_with_a_dot_inside: **[백준 2322 아령]** Input 받는 방식만 다르고 풀이는 똑같음

뭐 가만히 있으면 다이아5를 3문제 풀고 가는 거긴 한데... 난이도가 아무리 봐도 다이아가 아니다. 다 플1로 낮춰서 제출했다.



## 카카오 코딩테스트

1번은 단순 문자열 조작 문제였다

2번은 투 포인터 문제였다. 완전 탐색은 시간 초과였을 듯?

3번은 다익스트라로 해결했다. 이게 되네 싶을 정도로 대충 짰는데 시간 내에 돌아갔다.

4번은 분리 집합을 사용했다. `parents` 의 상태를 나타내는 리스트 조작이 주요 포인트.

5번은 단순 구현 문제였는데, 최적화가 가능한 듯하다.
