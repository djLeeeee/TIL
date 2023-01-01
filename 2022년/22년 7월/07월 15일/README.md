# 0715

Typora가 만기 됐다. 일단 Vscode로 편집하자...

솔직히 이제 점수 올리기는 정말 힘들다. 오늘은 틀린 문제들 싹 정리하는 느낌으로 가기로 했다. 주말엔 포트 폴커슨이랑 디닉 공부하면 좋을 듯?



## Drop 7 - [백준 25331](https://www.acmicpc.net/problem/25331)

구현

```python
now = [list(map(int, input().split())) + [0] for _ in range(7)]
ans = float('inf')
ball = int(input())
for j in range(7):
    board = [line[:] for line in now]
    board[0][j] = ball
    flag = True
    while flag:
        flag = False
        for x in range(6, 0, -1):
            for y in range(7):
                if not board[x][y]:
                    for nx in range(x - 1, -1, -1):
                        if board[nx][y]:
                            board[x][y] = board[nx][y]
                            board[nx][y] = 0
                            break
        cc = [[0] * 7 for _ in range(7)]
        rc = [[0] * 7 for _ in range(7)]
        for x in range(7):
            for y in range(7):
                if board[x][y]:
                    if not cc[x][y]:
                        for nx in range(x, 7):
                            cc[nx][y] = 7 - x
                    if not rc[x][y]:
                        ny = y
                        while board[x][ny]:
                            ny += 1
                            rc[x][y] += 1
                        for yy in range(y + 1, ny):
                            rc[x][yy] = rc[x][y]
        for x in range(7):
            for y in range(7):
                if board[x][y]:
                    if board[x][y] == rc[x][y] or board[x][y] == cc[x][y]:
                        board[x][y] = 0
                        flag = True
    remain = 0
    for ii in range(7):
        for jj in range(7):
            if board[ii][jj]:
                remain += 1
    if remain < ans:
        ans = remain
print(ans)
```

단순 구현 문제다. 근데 왜 썼냐면... 원티드에서 코딩 테스트 했을 때 계속 틀렸던 문제기 때문이다. 그 때 컨디션이 안 좋기도 했지만, 너무 당연한 실수를 했었다. `flag`라는 변수로 블록이 터졌는지 안 터졌는지 판별을 해줬는데, 이 녀석이 `True`로 바뀌는 조건은 컴포넌트의 크기와 적혀있는 숫자가 같을 때이다. 근데, 0일 때, 즉 그 칸이 비어있을 때를 걸러주지 않은 듯 하다.

난 골드 구현 문제도 구현 못하는 물 다이아인가... 하면서 당일 날에는 좀 많이 그랬는데 시간 지나니까 쉽게 풀렸다. 역시 코딩할 때 멘탈도 중요하다.
