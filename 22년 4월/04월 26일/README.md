# 0426



## JavaScript - 회문 체크

```js
// 주어진 문자열이 회문인지 판별하는 isPalindrome 함수를 완성하시오.
// reverse할 때 deepcopy 이슈 조심!
function isPalindrome(str) {
    let answer = 'YES';
    str = str.toLowerCase().split(' ').join('').split('');
    return (str.join('') === str.reverse().join('')) ? true : false
}

// 출력
console.log(
    isPalindrome('a santa at nasa'),  // true
    isPalindrome('google')  // false
)
```

오늘 워크샵 문제였다. 효율성 신경 안 쓰고, 문장을 뒤집은 다음 같은지 체크해줬다. 근데 `Python`에서 하는 것보다 조금 까다로웠다.

1. `str`을 모두 소문자로 만들어준다. `toLowerCase()` 함수를 사용하자.

2. 띄어쓰기를 없애주어야 한다. `split(' ')`를 해주면 공백을 기준으로 나눈 단어들의 리스트가 나오게 된다. 우리는 글자 단위로 뒤집어야 하니까, `join('')`으로 합쳐준 다음, `split('')`을 해주면 글자 단위로 리스트가 나오게 된다. 이 때, `join()`이라고 쓰게 되면, 기본값이 `,`이기 때문에 합쳐진 `str` 중간마다 `,`가 들어가니까 주의하자.

3. 제일 중요한 부분이다. 

   ```javascript
   return (str === str.reverse()) ? true : false  // 항상 true를 반환한다.
   ```

   위의 코드를 보면, `str`과 `str`을 뒤집은 걸 비교하는 것으로 보이지만, 사실 `reverse` 함수는 `return` 값도 존재하면서 원래 객체도 변환한다. `Python`에서 `reversed`와 `reverse`를 합쳐놨다고 이해하면 될 듯. 그래서 앞의 `str`이 호출될 때 뒤집어진 형태로 호출되고, 뒤도 당연히 뒤집어진 형태여서 항상 `true`가 반환되더라... 우리가 원하는 상황은 이게 아니다. 어떻게 해결할 수 있냐면, `join`을 다시 사용하는 것이다. `str`을 `join`하면 더 이상 `str`이라는 객체를 확인하지 않고 새로운 객체가 생긴 것이다.

내가 잘 이해한 것인지 잘 모르겠지만, 코드를 바꿔보면서 실험해 본 결과 위와 같은 결론을 내렸다. 낼 다시 확인해보자.



## Sprague-Grundy Theorem

> 참고 자료: 탐레프의 수학문제, PS 이야기, https://tamref.github.io/Grundy1/

게임 이론의 `Grundy number`에 관련된 정리이다. 증명 과정을 아직 완전히 이해하지 못해서 자세히는 못 쓰겠지만, 핵심만 써보면
$$
G(A + B) = G(A) \oplus G(B) \\
\oplus : \text {bitwise xor operator}
$$
이 때 `G(X)`는 `X`라는 게임의 `Grundy number`이다. `A + B`는 `A` 와 `B` 게임이 동시에 진행된다고 이해하면 될 듯하다. 

#### 그래서 `Grundy number`가 뭔데?

돌무더기에서 돌을 하나 이상 가져가는 게임을 둘이서 진행한다고 하자. 승리조건은 상대방이 가져갈 돌이 없을 때이다. `Grundy number`란, **내가 행한 행동으로 갈 수 있는 `state`의 그런디 넘버의 집합에 속하지 않는, 가장 작은 음이 아닌 정수이다.** 비어있는 돌무더기 `X`를 생각해보면, `G(X)`는 0이 된다. 비어있으면 어떠한 행동도 취할 수 없고, 다르게 말하면 행동을 해서 비어있는 돌무더기 상태로 가는 것이 불가능하다. 그렇다면 돌이 `N`개 있는 돌무더기를 생각해보자. 0부터 `N - 1`개의 돌무더기는 한 번의 행동으로 만들 수 있다. 귀납적으로, `Grundy number`는 `N`이 된다!

다시 스프라그-그런디 정리로 돌아가자. `Grundy number`가 0일 때는 패배하는 조건과 같다. 이제 여러 게임판이 동시에 진행되는 상황에 대해서 승리할 플레이어가 누군지 알 수 있다.



 ## 님 게임2 - [백준 11868](https://www.acmicpc.net/problem/11868)

스프라그-그런디 정리

```python
from sys import stdin

input = stdin.readline

n = int(input())
arr = map(int, input().split())
grundy = 0
for num in arr:
    grundy ^= num
print('koosaga' if grundy else 'cubelover')
```

코드는 굉장히 간단해 보인다. 1번 플레이어의 패배 조건은 그런디 넘버를 구했을 때 0이 나오는 것이다. 각각의 돌무더기의 그런디 넘버가 돌의 갯수라고 증명했으니, 전체 그런디 넘버는 `xor` 연산을 통해 구해주면 끝.

