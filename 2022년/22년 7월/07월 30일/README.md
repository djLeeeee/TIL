# 0730

주말은 점수 올리기 좋은 날~

## 제곱 ㄴㄴ - [백준 1557](https://www.acmicpc.net/problem/1557)

이분 탐색, 포함 배제

```Python
n = int(input())
start = 1
end = 2 * 10 ** 9
sq = int(end ** 0.5)
check = [1] * (sq + 1)
pr = [4]
for i in range(3, sq + 1, 2):
    if check[i]:
        pr.append(i * i)
        for j in range(i * i, sq + 1, 2 * i):
            check[j] = 0
l = len(pr)
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = mid
    for p1 in range(l):
        q1 = pr[p1]
        if q1 > mid:
            break
        cnt -= mid // q1
        for p2 in range(p1 + 1, l):
            q2 = q1 * pr[p2]
            if q2 > mid:
                break
            cnt += mid // q2
            for p3 in range(p2 + 1, l):
                q3 = q2 * pr[p3]
                if q3 > mid:
                    break
                cnt -= mid // q3
                for p4 in range(p3 + 1, l):
                    q4 = q3 * pr[p4]
                    if q4 > mid:
                        break
                    cnt += mid // q4
                    for p5 in range(p4 + 1, l):
                        q5 = q4 * pr[p5]
                        if q5 > mid:
                            break
                        cnt -= mid // q5
                        for p6 in range(p5 + 1, l):
                            q6 = q5 * pr[p6]
                            if q6 > mid:
                                break
                            cnt += mid // q6
    if cnt > n:
        end = mid - 1
    elif cnt < n:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1
print(ans)
```

이게 왜 다이아?

소수 제곱들을 확인해야 하는 건 자명하다. 답이 나오는 걸 보니 k번째 제곱 ㄴㄴ 수는 2k 이하인 듯 했다. 그래서 그 이하의 가능한 소수 제곱을 모두 찾아줬다. 그 다음 4 * 9 * 25 * 49 * 121 * 169 * 289 가 범위를 넘어가는 걸 보고 6중 for 문을 짜줬다. DFS로 짜려다가, 포함 배제를 쓰기에는 그냥 6중 for문 쓰는 게 나은 것 같아 관뒀다. 이분 탐색에서 주의할 점은, mid를 찾은 순간이 끝이 아니라, mid-1도 체크해야 한다는 점? mid가 제곱수일 수도 있으니까 ㅇㅇ

아무리 들여다봐도 다이아 정도 문제가 아니다. 일단 기여에 플2 제출했다.
