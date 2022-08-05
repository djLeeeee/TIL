# 0803

이제부터 다이아 표시를 안 하려 한다. 뭐 딱히 할 이유는 없으니까.. 사실 Typora 대신 Vs Code에서 마크다운 작성을 하다보니 다이아몬드 이모지 찾기 귀찮다 ㅎ..



## 경비병 세우기 게임 - [백준 18939](https://www.acmicpc.net/problem/18939)

게임 이론

```Python
from sys import stdin

input = stdin.readline

ans = ''
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    if n <= 2 * k - 1 and m <= 2 * k - 1:
        ans += 'Yuto\n'
    elif not (n * m) % 2:
        ans += 'Platina\n'
    else:
        ans += 'Yuto\n'
print(ans)
```

경비병을 배치할 때, 중심에 대해 대칭으로 배치하면 필승 전략이라고 생각하고 코딩을 짰다. 즉, 선공이 이기는 상황은

1. 첫 턴에 게임 종료 가능
2. 중심이 존재, 즉 가로와 세로 모두 홀수

그걸 기반으로 제출했더니 AC. 그런데...

![image](https://user-images.githubusercontent.com/97663863/183044078-50bba80e-f841-4408-b6e7-a9ac6318adb3.png)

기여란에서 보기 좋게 논파당했다. 가로 세로가 충분히 작을 때만 저런 경우가 생기는 거 같긴 하다. 그래서 저 분이 말씀하신대로 이 대회의 [에디토리얼](https://s3-ap-northeast-1.amazonaws.com/ojuz-attach/contest/kriii4/editorial.pdf)을 찾아봤다.

풀이는 틀렸지만, 답을 구하는 로직은 어떻게 맞았다. ㅋㅋㅋㅋ 자세한 건 에디토리얼에 잘 나와 있다.
