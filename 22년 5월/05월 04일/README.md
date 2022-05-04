# 0504



## 궁전 게임 - [백준 16879](https://www.acmicpc.net/problem/16879)

스프라그-그런디 정리

```python
from sys import stdin

input = stdin.readline

n = int(input())
grundy = 0
for _ in range(n):
    x, y = map(int, input().split())
    grundy ^= ((x // 3) ^ (y // 3)) * 3 + ((x + y) % 3) % 3
print('koosaga' if grundy else 'cubelover')
```

![image-20220505031659879](README.assets/image-20220505031659879.png)

x, y의 범위가 3000까지이고, 각 그런디 넘버를 규칙을 찾지 않고 직접 구하면 3000<sup>3</sup>이라 시간 초과가 날 것이다. 그래서 규칙을 찾아보려 했는데, 생각보다 안 보여서 고생했다. 격자판을 3칸씩 짜르면 패턴을 확인할 수 있다(가운데 표). 그 다음 3 by 3의 box가 어떤 값에다가 규칙을 더했는지를 나타내주면 오른쪽 위 같이 되고, 3 씩 나눠주면 xor 연산표가 나온다. 따라서, 아래와 같은 식이 나온다.
$$
gn = ( \lfloor x /3 \rfloor \oplus \lfloor y / 3 \rfloor ) \times 3 + z \\
z \equiv x + y \mod 3 \quad (0 \le z \le 2)
$$
이제 각 그런디 수를 xor 연산해주면 게임 전체의 그런디 수를 구할 수 있다.
