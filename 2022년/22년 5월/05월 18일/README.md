# 0518

본격적으로 관통 프로젝트를 시작했다. Django 서버 개발이 참 재밌긴 하지만... 한동안 알고리즘에 올인하지 못할 거 같아 좀 아쉽다.



## :diamond_shape_with_a_dot_inside: 직선 게임 - [백준 9522](https://www.acmicpc.net/problem/9522)

이분 매칭

```python
from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(2 * 10 ** 4)


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n = int(input())
x = set()
y = set()
graph = [[] for _ in range(501)]
for _ in range(n):
    a, b = map(int, input().split())
    x.add(a)
    y.add(b)
    graph[a].append(b)
if len(x) != len(y):
    print('Mirko')
    exit()
match = [0] * 501
ans = 'Slavko'
for i in x:
    visited = [False] * 501
    if not dfs(i):
        ans = 'Mirko'
        break
print(ans)
```

세로 직선, 가로 직선을 번갈아 그린다는 점애서 이분 매칭 풀이라는 걸 눈치챌 수 있다. 이분 그래프 구성을 해야하는데, 이분 그래프 G를 아래와 같이 구성했다.

- Vertex : 그릴 수 있는 모든 직선
- Edge : n개의 점 중 하나에서 만나는 두 직선 각각에 대응되는 vertex 간에 그려주기

가로 직선끼리는 만나지 않고, 세로 직선도 마찬가지이므로 이분 그래프가 됨을 쉽게 알 수 있다. 선공이 이기지 못하려면 선공이 어떤 점을 골라도 그 점에서 출발하는 경로 속 노드의 수가 짝수가 나와야 한다. 다르게 생각해보자. 선공이 이기려면 홀수 경로를 찾으면 된다. 그렇다면 홀수 경로가 없어야 한다는 것이고, 이는 이분 그래프가 완벽하게 매칭됨을 의미한다. 따라서, 양 쪽의 노드 수가 다르면 당연히 선공이 이기게 된다. 그리고 전체 점에서 이분 매칭 돌리고 매칭 안 되는 점이 하나라도 있으면 선공이 승리!