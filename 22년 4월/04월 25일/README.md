# 0425



## Django Project Thunderman

어제 배포를 실패했어서, 여러가지 해봤다.

1. `favicon`를 `base.html`에 추가했다.

2. `SQLite` 에서 `PostgreSQL`로 DB를 변경했다. `Heroku`의 DB 기본값은 `PostgreSQL`이라고 한다.

3. Python 버전을 알려주는 `runtime.txt`를 추가했다.

4. `psycopg2-binary==2.9.3`를 install하고 `requirements.txt`를 갱신했다.

5. `Procfile` 파일 내용을  `meeting.wsgi`로 수정

6. `settings.py`에 아래 내용을 추가했다.

   ```python
   import dj_database_url
   db_from_env = dj_database_url.config(conn_max_age=500)
   DATABASES['default'].update(db_from_env)
   ```

6개 중 뭐가 얻어걸려서 된 줄은 모르겠는데, 암튼 성공했다. 아마도 2번이 문제였을 듯?



## JavaScript와 친해지기

#### 백준

> 참고 자료 https://overcome-the-limits.tistory.com/25

자바스크립트는 별도의 입력받는 함수가 없는 듯하다. 그래서 백준의 `input` 파일을 열어주어야 한다.

```javascript
// 1. 하나의 값만 입력받을 때
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

// 2. 공백으로 구분된 한 줄의 값들을 입력받을 때
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');

// 3. 여러 줄의 값들을 입력받을 때
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// 4. 첫 번째 줄에 자연수 n을 입력받고, 그 다음 줄에 공백으로 구분된 n개의 값들을 입력받을 때
const fs = require('fs');
const [n, ...arr] = fs.readFileSync('/dev/stdin').toString().trim().split('/\s/');

// 5. 첫 번째 줄에 자연수 n을 입력받고, 그 다음 줄부터 n개의 줄에 걸쳐 한 줄에 하나의 값을 입력받을 때
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// 6. 하나의 값 또는 공백으로 구분된 여러 값들을 여러 줄에 걸쳐 뒤죽박죽 섞여서 입력받을 때
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('/\s/ ');
const n = input[0];
const n_arr = input.slice(1, n + 1);
const [m, ...m_arr] = input.slice(n + 1);
```

몇 문제 풀어보자.

```javascript
// 백준 10998 a * b
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number);
console.log(input[0] * input[1]);
```

읽어보면서 천천히 익히자.

```javascript
// 백준 14681 사분면 고르기
const fs = require('fs');
const [x, y] = fs.readFileSync(0).toString().trim().split('\n').map(Number);
if (x>0) {
  (y>0) ? console.log("1") : console.log("4");
}
else {
  (y>0) ? console.log("2") : console.log("3");
}
```

중요한 점은, `console.log` 안에 값은 `str` 아니면 변수여야 한다. `console.log('1')` 대신 `console.log(1)`을 쓰게 되면, `1`이라는 이름의 변수를 찾는 듯 하다. 당연히 `1`에 변수 할당은 안 되니까, 오류가 발생할 것이다.

또한, `readFileSync('/dev/stdin')`을 입력하면 `EACCES` 런타임 에러가 발생한다. 대신 `readFileSync(0)`을 쓰면 정상 작동한다. 그래서 백준 10998번으로 돌아가서 다시 해봤다.

```javascript
// 백준 10998 a * b
const fs = require('fs');
const [x, y] = fs.readFileSync(0).toString().split(' ').map(Number);
console.log(x * y);
```

이건 또 된다. `/dev/stdin`이 무슨 의미인지 모르겠으니 일단 `readFileSync(0)`로 문제를 푸는 게 낫지 싶다.



## 직각삼각형 - [백준 1711](https://www.acmicpc.net/problem/1711)

기하?, 브루트포스

```python
from sys import stdin
from collections import defaultdict
from math import gcd

input = stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    x, y = points[i]
    zero_x = 0
    zero_y = 0
    ex = 0
    tan_cnt = defaultdict(int)
    for j in range(n):
        z, w = points[j]
        if x != z:
            if y != w:
                a, b = y - w, z - x
                c = gcd(a, b)
                a //= c
                b //= c
                tan_cnt[(a, b)] += 1
            else:
                zero_x += 1
        else:
            if y != w:
                zero_y += 1
    key = tan_cnt.keys()
    key = list(key)
    for x, y in key:
        ex += tan_cnt[(x, y)] * (tan_cnt[(y, -x)] + tan_cnt[(-y, x)])
    ex //= 2
    ex += zero_x * zero_y
    ans += ex
print(ans)
```

n<sup>3</sup>으로 풀면 백 퍼 시간 초과가 뜰 거라, n<sup>2</sup>의 풀이를 떠올려 풀었다. 약간 카운팅 정렬의 느낌?



## 측량사 지윤 - [백준 2778](https://www.acmicpc.net/problem/2778)

기하학

```python
from sys import stdin

input = stdin.readline


def intersection(e1, e2):
    a1, b1, c1 = e1
    a2, b2, c2 = e2
    if a1 * b2 - a2 * b1 == 0:
        return False
    return (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1), (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)


n = int(input())
for i in range(n):
    equation = [tuple(map(int, input().split())) for _ in range(3)]
    p1 = intersection(equation[0], equation[1])
    p2 = intersection(equation[1], equation[2])
    p3 = intersection(equation[2], equation[0])
    if p1 and p2 and p3:
        x1, y1 = p2[0] - p1[0], p2[1] - p1[1]
        x2, y2 = p3[0] - p1[0], p3[1] - p1[1]
        ans = abs(x1 * y2 - x2 * y1) / 2
    else:
        ans = 0
    print('{:.4f}'.format(ans))
```

세 직선이 삼각형을 이루지 않을 때는,

- 서로 다른 두 직선이 평행 또는 일치하거나,
- 세 직선이 한 점에서 만나야한다.

첫 번째 상황은 `intersection`함수에서 `False`를 반환하도록 하여 해결했다. 두 번째 상황도 고려해줘야 생각했는데, 어차피 외적으로 넓이를 구할 것이기 때문에 상관 없을 것 같아 그대로 진행해 AC.

기하학 문제들은 참 풀 때마다 느끼는 거지만 재미가 없다.
