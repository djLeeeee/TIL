# 0619

네이버 코테 봤다. 4문제 나왔는데, API 명세서 수정 같은 재밌는 문제들이었다.

코드포스 치다가, 1문제만 풀고 나와버렸다. 레이팅 어떻게 되려나...



## 수열과 쿼리 22 - [백준 16978](https://www.acmicpc.net/problem/16978)

세그먼트 트리, 오프라인 쿼리

```python
from sys import stdin

input = stdin.readline

n = int(input())
tree = [0] * (2 * n)
tree[n: 2 * n] = map(int, input().split())
for i in range(n - 1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]
querys = []
q1 = 0
q2 = -1
k = int(input())
for _ in range(k):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        q1 += 1
        querys.append((q1, 1, query[1], query[2], q2))
    else:
        q2 += 1
        querys.append((query[1], 2, query[2], query[3], q2))
querys.sort()
answer = [0] * (q2 + 1)
for _, state, x, y, i in querys:
    if state == 1:
        idx = x + n - 1
        tree[idx] = y
        idx //= 2
        while idx >= 1:
            tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
            idx //= 2
    elif state == 2:
        left = x + n - 1
        right = y + n - 1
        while left <= right:
            if left % 2:
                answer[i] += tree[left]
                left += 1
            if not right % 2:
                answer[i] += tree[right]
                right -= 1
            left //= 2
            right //= 2
print(*answer, sep='\n')
```

CLASS 7 달기 프로젝트까지 4문제 남았다...

세그먼트 트리 + 전형적인 오프라인 쿼리 문제다. 특별한 건 없고, 합을 구하는 세그먼트 트리 구조체를 딱 외우고 쓸 수 있도록 더 노력해보자... 이번 건 저번 TIL 내용을 보면서 짰다. 