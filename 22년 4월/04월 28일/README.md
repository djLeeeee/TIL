# 0428



## 다각형 게임 - [백준 13034](https://www.acmicpc.net/problem/13034)

스프라그-그런디 정리

```python
n = int(input())
grundy = [0] * (n + 1)
grundy[2] = 1
for num in range(3, n + 1):
    sub_grundy = set()
    remain = num - 2
    for left in range(remain // 2 + 1):
        right = remain - left
        sub_grundy.add(grundy[left] ^ grundy[right])
    for gn in range(num + 1):
        if gn not in sub_grundy:
            grundy[num] = gn
            break
print('1' if grundy[-1] else '2')
```

스프라그-그런디 정리를 이용하여 그런디 넘버를 계산해보자.

> $$
> G(A + B) = G(A) \oplus G(B) \\\oplus : \text {bitwise xor operator}
> $$

- n이 0이면 0이다.

- n이 1이면 선분을 더 그릴 수 없으므로 0이다.

- n이 2이면 선분 하나를 반드시 그릴 수 있고, 그 다음 state는 n = 0 인 순간이다. 즉 그런디 넘버는 1이 된다.

- n > 2 일 때는, 스프라그-그런디 정리로 구해주면 된다. 선분을 하나 그리게 되면 점이 2개의 그룹으로 나뉜다. 이를 `left`와 `right`라 하고, 일반성을 잃지 않고 `left`가 `right`의 원소보다 작거나 같다고 하자. 그러면, 그 state에서의 그런디 넘버는 `left`와 `right`의 그런디 넘버를 `xor`한 값이 된다! 이후 `mex`를 찾아 그런디 넘버를 갱신해주면 된다. (`mex`: 포함되지 않는 음이 아닌 정수 중 최소값)

알다시피 초기 그런디 넘버가 0이면 선공이 패배, 아니면 선공이 승리한다. 답만 출력해주면 끝.



## 님 게임 홀짝 - [백준 11871](https://www.acmicpc.net/problem/11871)

스프라그-그런디 정리

```python
n = int(input())
arr = list(map(int, input().split()))
grundy = 0
for num in arr:
    if num % 2:
        grundy ^= num // 2 + 1
    else:
        grundy ^= num // 2 - 1
print('koosaga' if grundy else 'cubelover')
```

그런디 넘버를 다 구해주는 과정이 생략됐다. `num`의 범위가 너무 커서, 기존 방식의 O(num<sup>2</sup>) 방법은 시간 초과가 뜬다. 그래서 런타임 전처리 느낌으로 어느 정도 그런디 넘버를 구해주면 규칙을 찾을 수 있다.

>```python
>M = 20
>grundy = [0] * (M + 1)
>grundy[1] = 1
>for num in range(3, M + 1):
>    sub_grundy = set()
>    for get in range(2, num, 2):
>        sub_grundy.add(grundy[num - get])
>    for gn in range(num % 2, num + 1):
>        if gn not in sub_grundy:
>            grundy[num] = gn
>            break
>print(grundy)
>"""
>output : [0, 1, 0, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9]
>"""
>```

홀수 인덱스를 보면 [1, 2, 3, 4, 5 ...] 이고, 2부터 시작해서 짝수 인덱스를 보면 [0, 1, 2, 3, 4, ...] 가 된다. 이렇게 된다~ 라고 증명까지 하면 좋겠지만 실패. 암튼 저대로 그런디 넘버를 O(1)의 시간으로 구해주어 답을 제출해서 AC.



## 왕들의 외나무다리 게임 - [백준 18937](https://www.acmicpc.net/problem/18937)

스프라그-그런디 정리

```python
n = int(input())
arr = list(map(int, input().split()))
grundy = 0
for num in arr:
    if num % 2:
        grundy ^= num - 2
    else:
        grundy ^= num - 2
players = ['Whiteking', 'Blackking']
first = input()
for player in players:
    if player != first:
        second = player
print(first if grundy else second)
```

님 게임이랑 다를 게 없다! 아마 문제를 좀 더 어렵게 만드려고 '거리가 더 멀어지도록 이동할 수 있다'라는 조건을 추가한 것 같은데, 이 조건은 사실 **게임 승패에 아무 영향을 끼치지 않는다. 만약 어떤 플레이어가 멀어지는 선택을 했다면, 다음 플레이어는 그 칸만큼 다가가는 행동을 하면 두 턴 전의 상황과 같은 상태로 만들 수 있다.** 다르게 말하면, 멀어지는 행동은 게임의 승패를 바꿀 수 없는 것이다.

이분 매칭과 강한 연결 요소를 처음 발견했을 때처럼 새로운 꿀통을 찾아낸 기분이다 흐흐



## 님 게임 나누기 - [백준 11872](https://www.acmicpc.net/problem/11872)

스프라그-그런디 정리

```python
n = int(input())
state = 0
for num in map(int, input().split()):
    if num % 4 == 0:
        state ^= num - 1
    elif num % 4 == 3:
        state ^= num + 1
    else:
        state ^= num
print('koosaga' if state else 'cubelover')
```

마찬가지로 그런디 넘버를 일일히 구하기에는 숫자 범위가 너무 크다. 규칙이 있다는 뜻이다~

> ```python
> grundy = [0] * 21
> grundy[1] = 1
> grundy[2] = 2
> for num in range(3, 21):
>     sub_grundy = set()
>     for i in range(num):
>         sub_grundy.add(grundy[i])
>     for left in range(num // 2 + 1):
>         right = num - left
>         sub_grundy.add(grundy[left] ^ grundy[right])
>     gn = 0
>     while True:
>         if gn not in sub_grundy:
>             grundy[num] = gn
>             break
>         gn += 1
> print(grundy)
> """
> output: [0, 1, 2, 4, 3, 5, 6, 8, 7, 9, 10, 12, 11, 13, 14, 16, 15, 17, 18, 20, 19]
> """
> ```

20까지 돌려보니 별로 어렵지 않게 규칙을 찾을 수 있었다. 1, 2, (4, 3), 5, 6, (8, 7), ... 이런 느낌? 그대로 제출해서 AC.



## :diamond_shape_with_a_dot_inside: 루트 님 게임 - [백준 16887](https://www.acmicpc.net/problem/16887)

스프라그-그런디 정리, 정수론?

```python
n = int(input())
grundy = 0
for num in map(int, input().split()):
    if 0 <= num < 4 or 82 <= num < 82 * 82:
        pass
    elif 4 <= num < 16 or 15 ** 4 + 1 <= num < (15 ** 4 + 1) ** 2:
        grundy ^= 1
    elif 16 <= num < 81 or 81 ** 4 + 1 <= num:
        grundy ^= 2
    elif 82 ** 2 <= num < 15 ** 4 + 1:
        grundy ^= 3
    else:
        grundy ^= 4
print('koosaga' if grundy else 'cubelover')
```

이게 왜 다이아지? 싶긴 한데, 암튼 간만에 푼 다이아 문제다. 그런디 넘버를 구하는 과정 때문에 다이아인가 본데...  충분히 손 계산으로 구할 만하다. 각 범위의 제곱값과 네제곱값을 적당히 살펴보면서 범위를 나눠주면 된다. 길게 설명 쓸 것도 없는 듯.



## JavaScript30 - Practice 01 JS Drum Kit

오늘부터 시작해서 30일간 열심히 자바 공부를 해보자. 소스는 아래 링크 참고.

>30일간 자바스크립츠 배우기 프로젝트
>
>코드 : https://github.com/wesbos/JavaScript30
>
>영상 : https://courses.wesbos.com/account/access/626abb3dfbd6c85ff53aec9a
>
>풀코드 : https://github.com/djLeeeee/JavaScriptFor30Days/tree/master/01%20-%20JavaScript%20Drum%20Kit

```javascript
  function removePlayingClass(event) {
    const key = document.querySelector(`div[data-key="${event.keyCode}"]`);
    if (!key) return;
    key.classList.remove("playing")
  }

  function playingSound(event) {
    const key = document.querySelector(`div[data-key="${event.keyCode}"]`);
    if (!key) return;
    const audio = document.querySelector(`audio[data-key="${event.keyCode}"]`);
    audio.currentTime = 0;
    audio.play();
    key.classList.add("playing")
  }

  document.addEventListener('keydown', playingSound);
  document.addEventListener('keyup', removePlayingClass);
```

제공된 정답 코드에는 `transitionend`라는 이벤트를 사용했다. 얼추 이해했으나 지금 당장 작성하라면 못할 것 같다. 그래서 생각나는 대로 코드를 짜봤다. `keydown`과 `keyup`을 이용해서 구현했다. 

- `classList` : 객체의 `class`에 접근하는 메소드. `add`나 `remove`로 `class` 값을 추가하거나 제거할 수 있다.
- `querySelectorAll`: `querySelector`로 불러올 수 있는 모든 node들의 집합을 반환. `array`와는 다르다고 하는데, 아직 잘 모르겠다. `Array.From`을 써야 한다는 듯. 내 코드에선 사용하지 않았다.
- `currentTime`: audio 파일의 어느 지점부터 실행할 것인지 지정해준다. 0을 지정하면 처음부터 나온다. 이게 없으면 같은 값을 연타했을 때 소리가 여러 번 나오지 않는다.
- `play`: audio 파일 실행하는 커맨드.
- `keyCode` : 키보드를 사용한 이벤트에 대해서 입력값을 저장하고 있는 부분. 영어 자판에 대해서는 해당하는 영어 대문자의 아스키 코드 값을 반환한다.
- `tag[data-value="target"]`: `class`를 지정하는 것처럼, `data-` 뒤에 임의의 변수명을 써서 호출이 가능하다고 한다. 말로 풀어쓰긴 어려운데, 사용한 부분을 보면 이해할 수 있을 듯.

