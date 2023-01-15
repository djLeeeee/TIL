# 0115

어제 술을 너무 마셨다. 마시러 가기 전에 보드게임컵이 있었는데, 7문제 풀면 주는 배경이 있었다. 6문제까진 무난하게 풀었는데, 7번째 문제를 풀다가 계속 WA를 받았다. 역추적하는 거에서 문제가 있었던 거 같은데, 결국 약속 시간이 되버려서 다 못 풀고 나갔다.

오늘 하루 종일 숙취 때문에 빌빌 대다가 밤에 일어나 문제를 다시 봤는데, 아무리 봐도 틀린 걸 못 찾겠어서 차라리 풀이 싹 다 지우고 처음부터 다시 써봤는데 AC를 받았다. 하...



## 벚꽃 내리는 시대에 결투를 - [백준 27163](https://www.acmicpc.net/problem/27163)

> dp

```Python
from sys import stdin

input = stdin.readline

n, a, l = map(int, input().split())
aura = [[-1] * (l + 1) for _ in range(n + 1)]
aura[0][l] = a
queries = [tuple(map(int, input().split())) for _ in range(n)]
entry = [(l, a, '')]
for turn in range(1, n + 1):
    x, y = queries[turn - 1]
    for lp in range(1, l + 1):
        if aura[turn - 1][lp] == -1:
            continue
        ap = aura[turn - 1][lp]
        if x == -1:
            if lp > y and aura[turn][lp - y] < ap:
                aura[turn][lp - y] = ap
        elif y == -1:
            t = max(ap - x, 0)
            if aura[turn][lp] < t:
                aura[turn][lp] = t
        else:
            if lp > y and aura[turn][lp - y] < ap:
                aura[turn][lp - y] = ap
            if ap >= x and aura[turn][lp] < ap - x:
                aura[turn][lp] = ap - x
for lp in range(1, l + 1):
    if aura[-1][lp] != -1:
        o = ''
        ap = aura[-1][lp]
        for turn in range(n - 1, -1, -1):
            x, y = queries[turn]
            if x == -1:
                lp += y
                o += 'L'
            elif y == -1:
                ap = aura[turn][lp]
                o += 'A'
            else:
                if lp + y <= l and aura[turn][lp + y] == ap:
                    lp += y
                    o += 'L'
                else:
                    ap += x
                    o += 'A'
        print('YES')
        print(o[::-1])
        break
else:
    print('NO')
```

문제의 7번째 문제다. 그냥 일반적인 dp다. 아직도 이전 풀이가 왜 틀렸는지 이해는 안 되지만... 그래도 코드를 다시 치니까 AC를 받았다. 흑흑 내 배경... aura[턴 수][라이프] = 오라가 되도록 설계해줬다.
