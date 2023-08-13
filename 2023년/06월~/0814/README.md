# 0814

저번 주부터, 백준에서 아레나라는 기능을 제공하고 있다.
그냥 한글 코드포스라고 생각하면 될 듯.
저번 주와 이번 주 총 2번 참가했는데, 감상평을 말하자면 현재까진 대만족이다.
코드포스를 내가 잘 안 하게 된 이유가...

1. 너무 밤 늦게 한다.
2. **영어다**

이 둘을 모두 해결해주는 갓 PS 레이팅 시스템이니, 안 좋아할 수가 없다.

결과도 썩 나쁘지 않았다.

<img width="1194" alt="스크린샷 2023-08-14 오전 1 50 45" src="https://github.com/djLeeeee/TIL/assets/97663863/22b11570-7674-47e5-9b57-2edb2014579a">

오늘 있던 대회는 그냥 뭔가 말렸다... 1번 문제부터 한 번 틀리지를 않나, 시간 복잡도를 잘못 계산하질 않나...
괜히 효율적인 풀이 찾겠다고 온갖 그리디하게 접근하다가 9번 쯤 틀리고 대회 종료 10분 전에 완전 탐색해도 된다는 걸 깨달았다.. 그래도 다행히 4분 전에 AC를 받았다. 하지만 엄청난 패널티 파티로 6솔 중엔 꼴찌...

확실히 한글 문제라 그런지, 플레 문제들도 대회에서 한 두 문제 씩 풀리고 있다.
세그트리 문제는 당연히 다 못 풀지만 ㅠ 계속 레이팅 올리려면 세그트리 특훈을 한 번 해야할 듯 하다.
그래도 2번 대회 종합해서 현재 전체 백준 내 40등이다. 언제까지 유지할 수 있을 진 모르겠지만 ㅎㅎ..

그와는 별개로 문제 해결 레이팅을 다 플레 찍는 걸 본격적으로 하고 있다.



## Manacher Algorithm 최적화

```Python
# My original
def max_palindrome(my_lst):
    length = 0
    for i in range(len(my_lst)):
        if my_lst[i - length: i + 1] == my_lst[i - length: i + 1][::-1]:
            length += 1
        elif i > length:
            if my_lst[i - length - 1: i + 1] == my_lst[i - length - 1: i + 1][::-1]:
                length += 2
    return length
```

작년 2월 18일에 문제 보고 짠 알고리즘이다. 그 떄 뭐 매너처는 커녕 kmp 같은 것도 모르는 상태로, AC를 받는 코드를 짰다.
지금 보면 그냥 테케가 좀 약했던 것 같다. 용케 AC를 받은 듯 ㄹㅇ

그래서 다른 분 매너처 소스 중 괜찮아 보이는 걸 갖고 왔다.

```Python
# Manacher's algorithm source : boj handle riroan / https://www.acmicpc.net/user/riroan
def manacher(s):
    n = len(s)
    A = [0] * n
    r = 0
    p = 0
    for i in range(n):
        if i <= r:
            A[i] = min(A[2 * p - i], r - i)
        else:
            A[i] = 0
        while i - A[i] - 1 >= 0 and i + A[i] + 1 < n and s[i - A[i] - 1] == s[i + A[i] + 1]:
            A[i] += 1
        if r < i + A[i]:
            r = i + A[i]
            p = i
    return A
```

결국엔 kmp랑 비스무리~ 한 느낌으로 돌아간다.
내 원래 코드는 문자열 자체를 뽑아서 비교를 했으니 이 쪽이 훨씬 빠를 수 밖에.

조만간 KMP 쪽이랑, 레이지 세그 쪽 소스도 찾아보려 한다. 특히 레이지 세그.
