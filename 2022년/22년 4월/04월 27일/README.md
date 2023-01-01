# 0427



## 핌버 - [백준 16877](https://www.acmicpc.net/problem/16877)

스프라그-그런디 정리

```python
from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
M = max(arr)
fib = [1, 1]
grundy = [0] * (M + 1)
for idx in range(1, M + 1):
    sub_grundy = set()
    if fib[-1] + fib[-2] == idx:
        fib.append(idx)
    for num in fib:
        sub_grundy.add(grundy[idx - num])
    for gn in range(idx + 1):
        if gn not in sub_grundy:
            grundy[idx] = gn
            break
total_grundy = 0
for num in arr:
    total_grundy ^= grundy[num]
print('koosaga' if total_grundy else 'cubelover')
```

그런디 넘버를 이제 직접 구해야 한다. 피보나치의 수가 40개도 안 되기 때문에, 적당히 다 훑어보면서 그런디 넘버를 갱신해줬다. `in` 연산을 사용해야 해서 `set`을 사용했다.



## 님 게임 3 - [백준 16895](https://www.acmicpc.net/problem/16895)

스프라그-그런디 정리

```python
from sys import stdin

input = stdin.readline

n = int(input())
ans = 0
arr = list(map(int, input().split()))
grundy = 0
for num in arr:
    grundy ^= num
for num in arr:
    grundy ^= num
    if grundy < num:
        ans += 1
    grundy ^= num
print(ans)
```

선공이 취해야 할 행동은, 그런디 넘버가 0인 상태로 만드는 것이다. 그래서 `xor` 연산을 다시 해주면서 해당 돌무더기에서 한 개 이상의 돌을 제거하여 만들 수 있는지 확인해주었다.