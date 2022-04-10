# 0410



## 알고리즘 대회 주최

생각보다 난이도 조절이 어려웠다. 문제 출제는 풀면서 재밌었던 스킬들을 사용하는 느낌? 으로 출제해봤다. 자세한 내용은 폴더 참고~



## 방 청소 - [백준 9938](https://www.acmicpc.net/problem/9938)

분리 집합

```python
from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)
    if a in full:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = list(range(m + 1))
full = set()
for _ in range(n):
    x, y = map(int, input().split())
    if find(x) != find(y):
        if find(x) in full and find(y) in full:
            print('SMECE')
        else:
            print('LADICA')
        union(x, y)
    else:
        if find(x) in full:
            print('SMECE')
        else:
            full.add(find(x))
            print('LADICA')
```

처음 플레 갈 때 푼 문제도 분리 집합이었던 거 같은데, 다이아도 분리 집합으로 도착했다

문제 지문이 상당히 이상한데, 단순한 분리 집합 문제이다. 트리 구조를 생각해보면 편할 듯? 사이클이 생기는 순간은 해당 서랍 연결 그래프? 가 꽉 찼다는 의미다. 그러면 `full` 이라는 set에 추가해준다. 이 때 `union`을 약간 변행해줘야 한다. `full`에 있는 원소를 가리키도록 parent 값을 조정해주면 된다!

이외에도 한 가지 예외 상황이 있는데 고려를 못해주어 WA를 받았다. 만일 두 집합이 `union`을 할 수 있으면 싸이클이 없는 거라고 판단했는데, 둘다 싸이클 있는 집합, 즉 포화 상태의 두 집합이었다면 `union`을 할 수 있어도 술을  보관할 수 있는 서랍이 없는 상황이다. 그래서 `find(x)`와 `find(y)`가 다를 때 약간의 예외 처리를 해주었다.

![image](https://user-images.githubusercontent.com/97663863/162628410-209c89d8-d872-4989-9fa4-72cfef707219.png)

80일간 수고했다~