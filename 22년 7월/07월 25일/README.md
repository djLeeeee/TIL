# 0725

풀다보니 어느새 다이아3이 코앞이다. 2350점에서 점수 안 오른다고 찡찡거린게 엊그제 같은데...



## :diamond_shape_with_a_dot_inside: 룩, 비숍, 킹, 나이트, 궁전 게임 - [백준 16880](https://www.acmicpc.net/problem/16880)

스프라그 그런디

```Python
from sys import stdin

input = stdin.readline

gn = 0
for _ in range(int(input())):
    x, y, s = input().strip().split()
    x, y = int(x), int(y)
    z = min(x, y)
    if s == 'R':
        ex = x ^ y
    elif s == 'B':
        ex = z
    elif s == 'K':
        if (x - y) % 2:
            if z % 2:
                ex = 3
            else:
                ex = 1
        else:
            if z % 2:
                ex = 2
            else:
                ex = 0
    elif s == 'N':
        if z % 3 == 0:
            ex = 0
        elif z % 3 == 1:
            ex = 1 if x != y else 0
        else:
            ex = 2 if abs(x - y) > 1 else 1
    else:
        dx, dy = x // 3, y // 3
        ex = 3 * (dx ^ dy) + (x + y) % 3
    gn ^= ex
print("koosaga" if gn else "cubelover")
```

[궁전 게임](https://www.acmicpc.net/problem/16879) 문제를 이미 풀어봤더라면 비교적 쉽게 해결할 수 있는 문제였다. 이미 궁전 게임의 그런디 수 구하는 방법을 알고 있으니 난 편하게 했다.

문제 조건에 **각 말은 겹쳐도 된다**라는 말이 있다. 덕분에 모든 말이 독립적인 게임으로 생각할 수 있고, 각 말의 그런디 수를 구해 XOR 연산만 해주면 된다. 겹치면 안 된다라는 조건이 있다면... 끔찍하다. DP 문제가 되려나?

룩은 세로, 가로 이동이 독립적이다. 그러니 단순하게 `X^Y`. 비숍은 대각선 왼쪽 아래로만 이동할 수 있고 최대 `Z` 칸 만큼이다. 이 때 `Z=min(X,Y)`이다. 

킹부터는 조금 복잡해진다. 킹은 쉬는 시간에 손으로 그런디 수 테이블을 쓰윽 그려봤다. 대각선 기준으로 반복되는 걸 쉽게 찾을 수 있드라.

나이트 때문에 이 문제가 플레1에서 다이아가 된 거 같은데, 사실 이 친구도 그려보면 별 거 없다. 작은 수 기준으로 0, 1, 2가 대강 반복되는 걸 확인할 수 있고, 약간의 예외 처리만 해주면 끝.

궁전은 그런디 수 테이블을 그려보니 예전에 눈알 빠지도록 규칙 찾았던 그 테이블이 나와서 금방 알아차렸다. 이제 모든 말의 그런디 수를 구할 수 있으니 다 구해서 전체 그런디 수만 구하면 끝!

![image](https://user-images.githubusercontent.com/97663863/180824412-97809d9c-96bb-4e1b-b029-59ae019250ed.png)

쉬는 시간 틈틈히 설계해 집에 와서 다이아 문제 풀기... 꽤 기분 좋다.
