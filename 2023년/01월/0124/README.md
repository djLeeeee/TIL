# 0124

10일만에 쓰는 TIL이다. 마냥 알고리즘 공부 안하고 브론즈 문제만 풀진 않았다 ㅋ

![화면 캡처 2023-01-23 222332](https://user-images.githubusercontent.com/97663863/214310489-eca3bff6-c545-490b-9d72-86775bb3f8c2.png)

일단 저번 일요일에 1년 연속으로 문제 풀기를 성공했다. 그리고 [다이아2 문제](https://www.acmicpc.net/problem/4794)를 풀었는데, 이분 매칭의 argument path에 최대 유량을 접목시킨 느낌으로? 구현을 해서 풀었다. 문제를 요약하면 **Max disjoint perfect matchings of bipertite graph**라고 할 수 있겠다. 원래라면 오늘 TIL에 정리하겠는데, 순수 유량으로 만들어본 다른 풀이가 계속 오답이 나온다. 이유를 찾아보고 정리해야지.

이거 말고도 외판원 순회 + 경로 역추적으로 [아무도 안 푼 문제 하나](https://www.acmicpc.net/problem/26931) 풀었다. 역추적 코드 짜는 동안 계속 딴 짓을 했더니 굉장히 오래 걸렸다 ㅋㅋㅋ 난이도는 외판원 순회 골1에 역추적이니까 플5 주고 왔다. 나 혼자 푼 문제가 다시 생겼다 흐흐흐... 얜 좀 오래 버텼음 좋겠다.



## Needle - [백준 20176](https://www.acmicpc.net/problem/20176)

> FFT

```Python
n = 1 << 21
mx = 30000
arr_a = [0] * n
input()
for m in map(int, input().split()):
    arr_a[m + mx] += 1
input()
arr_b = tuple(map(int, input().split()))
arr_c = [0] * n
input()
for m in map(int, input().split()):
    arr_c[m + mx] += 1
fft(arr_a)
fft(arr_c)
for i in range(n):
    arr_a[i] *= arr_c[i]
fft(arr_a, inv=True)
ans = 0
for m in arr_b:
    ans += arr_a[2 * m + 2 * mx]
print(ans)
```

어레이 a, b, c에서 a<sub>i</sub>, b<sub>j</sub>, c<sub>k</sub>가 등차 수열을 이루는 쌍이 총 몇 개 있는지 구하는 문제였다. 단순하게 a랑 c를 곱하고, b의 원소 값의 2배와 비교해줬다. 곱할 때는 어레이가 많이 크므로 FFT를 써줬다. 좌표값이 음수가 가능하므로 `mx`로 보정해주면 끝. 

역시 FFT만큼 날먹이 없다. 할머니 댁 이불에서 뒹굴거리면서 풀었으니 말 다했지
