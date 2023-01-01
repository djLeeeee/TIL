# 0807

내일 첫 출근이다. 오늘은 일찍 자자.



## 백설공주와 난쟁이 - [백준 2912](https://www.acmicpc.net/problem/2912)

무작위화, 이분 탐색

```Python
from sys import stdin
from random import randint

input = stdin.readline

n, c = map(int, input().split())
arr = [0] + list(map(int, input().split()))
arr_inv = [[] for _ in range(c + 1)]
for i in range(1, n + 1):
    arr_inv[arr[i]].append(i)
for _ in range(int(input())):
    s, e = map(int, input().split())
    ans = 'no'
    for _ in range(30):
        k = arr[randint(s, e)]
        start = 0
        end = len(arr_inv[k]) - 1
        rs = 0
        while start <= end:
            mid = (start + end) // 2
            if arr_inv[k][mid] < s:
                start = mid + 1
            elif arr_inv[k][mid] > s:
                rs = mid
                end = mid - 1
            else:
                rs = mid
                break
        start = 0
        end = len(arr_inv[k]) - 1
        re = end
        while start <= end:
            mid = (start + end) // 2
            if arr_inv[k][mid] < e:
                re = mid
                start = mid + 1
            elif arr_inv[k][mid] > e:
                end = mid - 1
            else:
                re = mid
                break
        if (re - rs + 1) * 2 > (e - s + 1):
            ans = f'yes {k}'
            break
    print(ans)
```

진짜 재밌는 문제였다.

`arr`와 `arr_inv`를 만들어주자. `arr_inv`는 같은 색깔을 가진 난쟁이 번호끼리 모아놓은 리스트를 저장한다. 그 다음이 핵심인데, `s`부터 `e`까지 중 랜덤으로 한 난쟁이를 뽑아 색깔을 확인한다. 그 다음 `arr_inv`를 확인해 `s`부터 `e` 사이에 같은 색깔을 가진 난쟁이가 몇 명인지 찾는다. 이건 이분 탐색으로 구현해주었다. 만약 절반 초과라면 그대로 답을 `yes`로 바꾸고, 아니라면 또다시 랜덤으로 탐색을 한다(최대 30번).

일단 답을 `no`라고 가정하고 탐색을 하고, 30번 탐색을 하는데, `yes`인데 30번 탐색 동안 맞는 번호를 못 찾을 확률은 2<sup>30</sup> 분의 1이다. 즉, 풀이가 99.999999%의 정확도를 가진다.

기여창을 보니 mo`s 알고리즘으로 해결 가능한 것 같다. 근데 이 풀이가 훨씬 쉬울 것 같다 ㅋㅋ
