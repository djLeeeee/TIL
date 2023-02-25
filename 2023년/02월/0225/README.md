# 0225

오랜만의 TIL이다. 그동안,

- Kotlin
- Spring
- gRPC

등을 공부했다. 찐 개발자들이 하는 일들을 슬슬 시작하는 느낌.. 후딱 이해해서 제대로 일하고 싶은데 맘처럼 되진 않는다.

물론 백준 문제는 꼬박꼬박 풀었다. 나름 유명한 다이아 문제인 [백업](https://www.acmicpc.net/problem/1150) 문제를 풀었다. 이걸 각 잡고 푼 이유는, 아무도 안 푼 문제 중에서 굉장히 [유사한 문제](https://www.acmicpc.net/problem/26917)를 찾았기 때문이다. 그래서 정리할 내용은 백업 문제에 대해서만 정리해야지

나 혼자 푼 문제에 고 레이팅을 줄 때마다, 더 쉬운 풀이가 있는데 괜히 어렵게 푼 게 아닌가... 라는 생각이 든다. 기다리면 누군가 또 풀어주겠지

코드잼이 그만 열린다는 것 같다. 구글 티셔츠 받아보고 싶었는데 ㅜㅠ...



## 백업 - [백준 1150](https://www.acmicpc.net/problem/1150)

> 그리디, 연결 리스트, 힙

```Python
n, k = map(int, input().split())
location = [-1] + [int(input()) for _ in range(n)]
heap = []
dist = [0] * (n + 2)
for i in range(2, n + 1):
    temp = location[i] - location[i - 1]
    heappush(heap, (temp, i))
    dist[i] = temp
left = list(range(-1, n + 3))
right = list(range(1, n + 3))
dist[1] = dist[n + 1] = float('inf')
ans = 0
visited = [False] * (n + 2)
for _ in range(k):
    while heap:
        ex, idx = heappop(heap)
        if not visited[idx]:
            ans += ex
            l, r = left[idx], right[idx]
            dist[idx] = dist[l] + dist[r] - ex
            visited[l] = visited[r] = True
            left[idx] = left[l]
            right[idx] = right[r]
            left[right[r]] = idx
            right[left[l]] = idx
            heappush(heap, (dist[idx], idx))
            break
print(ans)
```

이웃한 쌍들로 이루어져야 한다는 성질은 금방 생각해낼 수 있다. 그러면 이제 (n-1) 개의 쌍을 확인해야 하는데, 당연히 작은 쌍부터 확인하는 게 좋을 것이다. 하지만 1 2 3 4에서 1-2 3-4를 고르기 전 2-3을 고른다면 문제가 꼬인다.

이를 해결하기 위해서, 2-3을 골랐다면 확인할 힙에 1-4를 추가한다. 이 친구는, 1-2, 3-4 세트를 의미한다. 이 세트의 값은 (1-2)+(3-4)-(2-3)로 해준다. 나중에 1-4를 쓰게 됐다면 0-5라는 세트도 추가되어야 한다. 이를 위해 각 사용한 구간에서 시작과 끝점이 어떻게 되는지 기록을 해놔야한다. 이는 연결 리스트로 해결 가능하다.

구현하면서 갱신해야 하는 정보를 계속 헷갈려 많이 헤맸다...
