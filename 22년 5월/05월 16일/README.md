# 0516



## :diamond_shape_with_a_dot_inside: 전령들 - [백준 3319](https://www.acmicpc.net/problem/3319)

트리 DP, CHT, DFS 

```python
from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(2 * 10 ** 5)


def dfs(now, last):
    for adj, c in graph[now]:
        if not ans[adj] and adj != 1:
            dist[adj] = dist[now] + c
            start = 0
            end = last
            while start <= end:
                mid = (start + end) // 2
                init, idx = cht[mid]
                if init < sv[adj][1]:
                    res = idx
                    start = mid + 1
                else:
                    end = mid - 1
            ans[adj] = ans[res] + (dist[adj] - dist[res]) * sv[adj][1] + sv[adj][0]
            start = 0
            end = last
            while start <= end:
                mid = (start + end) // 2
                init, idx = cht[mid]
                if ans[adj] - ans[idx] > init * (dist[adj] - dist[idx]):
                    ns = (ans[adj] - ans[idx]) / (dist[adj] - dist[idx])
                    res = mid
                    start = mid + 1
                else:
                    end = mid - 1
            memo = cht[res + 1][:]
            cht[res + 1] = [ns, adj]
            dfs(adj, res + 1)
            cht[res + 1] = memo


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y, d = map(int, input().split())
    graph[x].append((y, d))
    graph[y].append((x, d))
sv = [0, 0] + [tuple(map(int, input().split())) for _ in range(n - 1)]
dist = [0] * (n + 1)
ans = [0] * (n + 1)
cht = [[0, 0] for _ in range(n)]
cht[0][1] = 1
dfs(1, 0)
print(*ans[2:])
```

답을 구할 수 있는 코드는 진작에 짜놨다. 근데 계속 TLE, MLE가 나왔다... 그래서 별다별 난리를 다 해봤다.

> 처음 코드는 값을 while문으로 찾아주었다. CHT를 각 노드 별로 저장해주었다.

- `graph`를 `defaultdict` 대신 이중 리스트로 바꿔봤다. (고민 2일차)

- 얼마 전에 푼 [나무 자르기 문제](https://www.acmicpc.net/problem/13263)에서 이분 탐색 대신 뒤에서 `pop`을 하여 `CHT`를 갱신한 반면, 이 문제에서는 다시 이분 탐색으로 갱신해줬다. 아니, 갱신해야만 통과되는 듯 하다. 아마 문제 난이도에 따라 다른 듯? 하지만 이게 주된 시간 / 메모리 초과 요인은 아니었다. (고민 2일차)

- CHT를 각 노드 별로 저장할 필요가 없다는 걸 알아차렸다. 재귀 형식의 DFS를 해주면서, CHT를 알맞게 바꿔주었다. 두 가지 방법이 있었다. (고민 4일차)

  - **함수의 변수에 CHT를 담기** : 메모리 초과
  - **글로벌 변수 CHT를 선언 후 갱신** : 시간 초과

  둘 다 실패했지만, 이런 느낌으로 가면 되겠다는 느낌이 왔다. 

- **[! 중요 !]** CHT가 갱신될 때 항상 맨 뒤에 새로운 직선 식을 붙인다는 걸 이용할 수 있겠다는 생각이 들었다. CHT의 최대 길이는 노드의 개수 `n`일테니까 그만큼 길이의 리스트를 만들어줬다. 그 다음, CHT의 몇 번 인덱스까지가 현재 값 갱신에 유효한 데이터인지 인자 `last`로 넘겨줬다.

  ```python
  def dfs(now, last):
  	...
      start = 0
      end = last
      while start <= end:
          ...
  ```

  그 다음부턴 이분 탐색을 할 때 CHT의 길이가 아닌, `last`까지 탐색하도록 코드를 바꿨다. 이게 고민 5일차.

오늘에서야 문제 풀이가 그럴싸해졌다. 이제 CHT를 어떻게 관리할 것인지 생각해봐야 한다. 바로 생각난 것은 백트래킹 기법과 비슷하게 하는 것이었다. 어차피 `last`까지만 확인하니까, 뒤에 부분은 실시간으로 갱신되어 있을 필요가 없다. **해당 부분의 DFS가 끝났을 때 갱신했던 값을 다시 돌려주면 된다!**

```python
def dfs(now, last):
    ...
	memo = cht[res + 1][:]		# 갱신 이전 정보를 기록해놓고
    cht[res + 1] = [ns, adj]	# 그 부분을 갱신해준 뒤
    dfs(adj, res + 1)			# 그 부분까지의 CHT를 다음 DFS에서 사용
    cht[res + 1] = memo			# DFS가 끝나면 다시 돌려놓기
```

해냈다 ㅋㅋㅋㅋㅋ 어제에 이어 다이아3 문제를 또 풀어버렸다. 그것도 DP를 ㅎㅎㅎ

다른 분들 문제 리뷰를 보니 리차오 트리라는 걸 사용하면 된다고 한다. 찾아보니 세그먼트 트리 내용이었다. 세그 트리를 슬슬 공부해야 하려나...

