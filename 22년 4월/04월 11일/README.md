# 0411

프로젝트에 많은 시간을 투자했다.

## 장고 프로젝트

날짜 묶어서 출력 해결!

[이슈 링크](https://github.com/djLeeeee/project1/issues/8)



## 수열과 쿼리 38 - [백준 18917](https://www.acmicpc.net/problem/18917)

xor 연산?

```python
from sys import stdin

input = stdin.readline

a = 0
b = 0
for _ in range(int(input())):
    o, *n = map(int, input().split())
    if o == 1:
        a += n[0]
        b ^= n[0]
    elif o == 2:
        a -= n[0]
        b ^= n[0]
    elif o == 3:
        print(a)
    else:
        print(b)

```

다이아를 달고 나니 어려운 문제가 눈에 안 들어온다... 오랜만에 실버 문제 풀었는데 재밌다.

앞에서 뺀다 / 뒤에서 뺀다 라는 말을 신경 쓸 필요가 없다. xor 연산이나 덧셈은 교환 법칙이 성립하니까.

사실 수열과 쿼리 문제를 풀어야 solved.ac 배경 준다길래 만만한 문제를 골라 풀었다 ㅋㅋ
