# 0810

시덥잖은 얘기는 주말에 쓰고, 바로 본문으로 들어간다.



## CHT 최적화

```Python
# My original
# What a poooooooooor code,,,,,
ps = [list(map(int, input().split())) for _ in range(n)]
ps.sort()
ox, oy = ps.pop()
for i in range(n - 1):
    ps[i][0] -= ox
    ps[i][1] -= oy
ps.sort(key=lambda xy: xy[1] / (xy[0] * xy[0] + xy[1] * xy[1]) ** 0.5)
cvh = [(0, 0), (ps[0][0], ps[0][1])]
for px, py in ps[1:]:
    while True:
        fx, fy = cvh[-2]
        sx, sy = cvh[-1]
        a, b = sx - fx, sy - fy
        c, d = px - fx, py - fy
        det = a * d - b * c
        if det > 0:
            cvh.pop()
        elif det < 0:
            cvh.append((px, py))
            break
        else:
            if a * c >= 0 and b * d >= 0:
                if abs(c) >= abs(a) and abs(d) >= abs(b):
                    cvh[-1] = (px, py)
                break
            else:
                cvh.pop()
ans = len(cvh)
a, b = cvh[-2]
c, d = cvh[-1]
if not a * d - b * c:
    cvh.pop()
```

볼록 껍질 내 기존 코드다. 진짜 쓰레기 같고 이해하기도 힘들다. 그래서 언제나처럼 다른 정답 코드 뒤적였다.

```Python
# ntt source : boj handle 20210805 / https://www.acmicpc.net/user/20210805
# What a cooooooooool code!!!!!
def convex_hull(points):
    points = sorted(points)

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    lower.pop()

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    upper.pop()

    return lower + upper


def cross(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
```

캬 깔끔하다. 코드가 예쁘다 진짜.
외적을 정의하고, 조건에 맞게 볼록 껍질 윗부분/아랫부분을 찾아주셨다.
진짜 보자마자 개떡같은 내 코드보다 백번 천번 낫다고 생각했다 ㄹㅇ루

그래서 CHT 문제 소스는 아마 이걸 계속 사용하지 싶다.
