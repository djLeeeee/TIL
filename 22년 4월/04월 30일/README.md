# 0430



## 금화 게임 - [백준 5386](https://www.acmicpc.net/problem/5386)

스프라그-그런디 정리

```python
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    if m % 2:
        if n % 2:
            print(1)
        else:
            print(0)
    else:
        n %= (m + 1)
        if n == m:
            print(m)
        elif n % 2:
            print(1)
        else:
            print(0)
```

> 그런디 넘버의 규칙을 찾기 위해 사용한 코드
>
> ```python
> n, m = map(int, input().split())
> grundy = [0] * (n + 1)
> grundy[1] = 1
> for num in range(2, n + 1):
>     sub_grundy = set()
>     if m == 1:
>         sub_grundy.add(grundy[num - 1])
>     else:
>         check = 1
>         while check <= num:
>             sub_grundy.add(grundy[num - check])
>             check *= m
>     for gn in range(num + 1):
>         if gn not in sub_grundy:
>             grundy[num] = gn
>             break
> for i in range(10):
>     print(grundy[i * 10 + 1:i * 10 + 11])
> ```

위 코드를 돌려보면 쉽게 규칙을 찾을 수 있다. 손계산도 비교적 쉬우니 직접 해봐도 될 듯.



## 크로스와 크로스 - [백준 3596](https://www.acmicpc.net/problem/3596)

스프라그-그런디 정리

```python
n = int(input())
grundy = [0] * (n + 3)
grundy[1] = 1
grundy[2] = 1
grundy[3] = 1
grundy[4] = 2
grundy[5] = 2
for num in range(6, n + 3):
    sub_grundy = set()
    for ex in range(3, 6):
        sub_grundy.add(grundy[num - ex])
    for left in range(1, (num - 5) // 2 + 1):
        right = num - 5 - left
        sub_grundy.add(grundy[left] ^ grundy[right])
    for gn in range(num + 1):
        if gn not in sub_grundy:
            grundy[num] = gn
            break
print('1' if grundy[n] else '2')
```

`x`를 그리는 행동을 좌우 인접 2칸에 더 이상 칠하지 못하게 하는 행위라 생각하면 된다. 만약 다음 플레이어가 좌우 인접 2칸을 칠한다면 현재 플레이어가 승리할 수 있다. 끝 쪽에 그리는 경우를 생각해 게임판에서 3~5칸을 지우는 행위가 가능하다. 만약 `x`를 중간에 그린다면 5칸이 지워지고 좌측과 우측이 독립적인 새로운 게임이 되어 xor 연산을 해줘 그런디 넘버를 구할 수 있다.



## JavaScript30 - Practice 02 JS AND CSS CLOCK