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

```css
...

.hand {
    background: black;
    position: absolute;
    top: 50%;
    transform-origin: right center;
}

.hour-hand {
    width: 50%;
    height: 6px;
}

.min-hand{
    width: 50%;
    height: 6px;
}

.second-hand {
    width: 50%;
    height: 3px;
    transition-property: all;
    transition-duration: 0.05s;
    transition-timing-function: ease;
}
```

```javascript
const hourHand = document.querySelector('.hour-hand');
const minuteHand = document.querySelector('.min-hand');
const secondHand = document.querySelector('.second-hand');

function setClockTime() {
    const now = new Date();
    const hourDegree = (90 + now.getHours() * 30 + now.getMinutes() * 0.5) % 360;
    const minuteDegree = (90 + now.getMinutes() * 6 + now.getSeconds() * 0.1) % 360;
    const secondDegree = (90 + now.getSeconds() * 6) % 360;
    hourHand.style.transform = `rotate(${hourDegree}deg)`;
    minuteHand.style.transform = `rotate(${minuteDegree}deg)`;
    secondHand.style.transform = `rotate(${secondDegree}deg)`;
}

setInterval(setClockTime, 1000);
setClockTime();
```

css style 속성 중 `transform`에 `rotate(n deg)`로 입력하면 n도 (라디안 아님!) 만큼 시계방향으로 회전한다. 중심을 설정하지 않을 경우 `center center`, 즉 중앙 지점이 기본값이다. 중심 설정은 아래와 같이 하면 된다.

```css
.hand {
	...
    transform-origin: right center;
}
```

`transition`은 `property`, `duration`, `delay`, `timing-function` 순으로 입력된다고 한다. `property`는 어떤 값에 적용할 것인지다. 현재 초침 전체에 `transition`을 걸어줄 거니까 `all`을 주었다. 1초 간격으로 움직여야 하니까 `duration`은 0.05초 정도로 주었다. `timing-function`은 `ease`를 사용했다. 처음과 끝은 느리게, 중간은 빠르게 이동하는 함수다.

> transition의 timing function에는 기본 제공하는 함수가 여러 있다. 사용자 지정도 가능하다.
>
> 자세한 얘기는 [공식 mdn](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function)를 참고하는 게 좋을 듯 하다. 

```css
.second-hand {
    width: 50%;
    height: 3px;
    transition-property: all;
    transition-duration: 0.05s;
    transition-timing-function: ease;
}
```

`JAVASCRIPT30`에서 제공한 답안 코드에는 `ease` 대신 사용자 설정 함수를 사용했다. 또한, 초침 뿐만 아니라 시침과 분침에도 해당 애니메이션을 적용했다. 사소한 문제니 고칠 필요는 없을 듯.

한 가지 문제가 있는데, **각도가 354도에서 0도가 되는 순간 `transition`이 354에서 0으로 감소하는 방향으로 들어가 초침이 해당하는 1초 구간에서 이상하게 움직인다.** 안타깝게도 제공된 답안 코드도 해당 이슈를 해결하진 않았다. 오늘은 시간이 늦었으니 다음에 해결해보자.