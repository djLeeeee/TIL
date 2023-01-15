# 0113

젠킨스며 도커며 grpc며 많은 걸 해봤다. 코드 보면서 얼렁뚱땅 배워나가고 있지만 ㅋㅋ

솔브닥 난이도가 매겨지지 않은 문제들을 풀고 난이도 매기기를 시작했다. 한 10문제 정도 되는 듯? 스웨덴 어로 써있어서 조금 귀찮긴 하지만 재밌긴 하다. 브론즈 문제 같은 거는 내가 매겨놓으면 하루 사이에 20명 정도 풀어버리는 걸 보는 맛도 있다. 



## 영어와 프랑스어 (Large) - [백준 12144](https://www.acmicpc.net/problem/12144)

> 최대 유량, 해싱

```Python
source = 6001
sink = N = 6002
for tc in range(1, int(input()) + 1):
    words = {}
    graph = [set() for _ in range(N + 1)]
    capacity = defaultdict(lambda: defaultdict(int))
    cnt = 0
    ls = int(input())
    english = set(input().rstrip().split())
    for w in english:
        if w not in words:
            cnt += 1
            words[w] = cnt
            makeGraph(source, words[w], N)
    french = set(input().rstrip().split())
    for w in french:
        if w not in words:
            cnt += 1
            words[w] = cnt
    lines = [list(set(input().rstrip().split())) for _ in range(ls - 2)]
    for line in lines:
        for w in line:
            if w not in words:
                cnt += 1
                words[w] = cnt
    for line in lines:
        for w in line:
            for u in line:
                makeGraph(cnt + words[u], words[w])
    for i in range(1, cnt + 1):
        makeGraph(i, cnt + i)
    for w in french:
        makeGraph(cnt + words[w], sink, N)
    print(f'Case #{tc}: {dinic(source, sink)}')
```

디닉 함수 부분은 뺐다. 평소 쓰던 디닉 그대로이다. 이중 리스트 `capacity`의 크기가 쓸데없이 큰 거 같아 `capacity = defaultdict(lambda: defaultdict(int))` 로 써봤다. 이 방법도 괜찮은 듯 ㅇㅇ

보자마자 유량으로 풀면 되겠다는 생각이 들었다. 하지만 모델 설계가 어려웠다... 그러다 [보드 색칠하기](https://www.acmicpc.net/problem/13444)와 비슷하게 접근할 수 있겠단 생각이 들었다. 나는 저 문제를 이분 매칭으로 해결했지만, 최대 유량으로 푸신 분들의 풀이를 참조해봤다.(애초에 10에 9은 유량으로 푸신 듯 하다) 사실 그래서 이 문제도 이분 매칭으로 풀어보려 했지만 잘 안 된다 ㅠ

source를 영어로, sink를 프랑스어로 생각하고 설계된 모델에서 최대 플로우를 정답으로 하게 해주고 싶은 상황이다. 각 단어들을 두 개의 노드로 쪼갤 것이다. 한 노드는 영어 담당, 다른 노드는 프랑스어 담당이다. 먼저 같은 단어의 노드들끼리 1짜리 간선으로 이어주자. 그 다음 영어와 프랑스어라고 주어진 문장들 속 단어들을 각각 source(영어) sink(프랑스어)에 연결해준다. 용량은 전체 노드의 수만큼 해주자. 그 다음 언어가 정해지지 않은 문장들 속 같은 문장에 있는 단어들 간에, 프랑스어 쪽에서 영어 쪽으로 가는 1짜리 간선을 그려주면 설계 끝!

말이 어려운데, 영어 문장 A B, 프랑스 문장 B C D, 정해지지 않은 문장 A C로 주어졌다고 했을 때 그림을 그려보면 아래와 같다.

![image](https://user-images.githubusercontent.com/97663863/212549657-d7f254ee-303b-463b-a2d8-f87302f23cdf.png)

그럼 이제 최대 유량, 즉 최소 컷이 이 모델에서 무엇을 의미하는 지 생각해보자. 처음부터 영어 문장과 프랑스어 문장에 동시에 속한 단어들은 자명하게 플로우가 1 씩 흐를 것이다. 다른 문장으로 인해 영어와 프랑스어 동시에 속하게 되는 단어가 문제인데, 이는 프랑스어에서 영어로 가는 간선들을 보면 된다. 어떤 영단어 A와 같은 문장에 속한 단어 B를 생각해보자. 이 문장이 영어 문장이라고 정하면 B는 영단어가 된다. 근데 단어 B가 프랑스어라면? 그러면 B는 영어이자 프랑스어인 우리가 찾는 친구라는 뜻이다. 그리고 이 경우 프랑스 -> 영어 간선으로 플로우가 1 흐를 것이다.

흠... 말로 하기 어렵다. 암튼 최대 유량을 구해서 출력해줬다. 문자열에 번호를 매기는 작업은 단순하게 딕셔너리를 사용해줬다.
