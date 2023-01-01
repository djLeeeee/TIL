# 0529

일주일 만에 TIL이다. 프로젝트 때문에 바빠서...

프로젝트 자체는 금요일에 끝났는데, 어제는 격하게 아무것도 하기 싫드라. 야구도 보고 겜도 하고 쭉 놀았다. 이제 다시 알고리즘 풀어야지

스프링 자바 공부하는 것도 괜찮을 듯.



## 프로젝트

얘기 안 하고 넘어가기엔 섭하다. 자세한 얘기는 대외비가 많으신 분들께서 올리지 말라고 하니, 배우지 않고 직접 구현해본 기능들 정도만 기록해보려 한다.

> #### 1. 카카오 소셜 로그인
>
> 소셜 로그인 기능 자체는 배우긴 했다. 그래서 로그인 / 로그아웃까진 잘 구현했는데, 몇 가지 문제가 있었다.
>
> - 카카오 로그인 유저는 일반 유저와 토큰이 다르다.
> - **카카오 유저가 사이트와의 상호 작용을 기록할 필요가 있다. (좋아요라든지, 댓글이라든지)**
>
> 첫 번째는 카카오 토큰 유무로 조건문을 활용해서 해결하면 됐지만, 문제는 두번째였다. 여러가지 방법으로 시도했지만, 잘 안 됐다. 그러다가 카카오로 로그인한 유저를 우리가 임의로 만들어서 저장하면 되는 것 아닌가? 라는 생각이 들었다. 그래서 아이디를 `(유저 이름)fromKAKAO` 이런 식으로 저장했다. 카카오 소셜 로그인 요청 시 반환 값에 이름이 있었기 때문에 가능했다. 그러다가, 이 방법에 문제가 있음을 깨달았다. 동명이인 문제가 있었다. 그래서 또 고민을 한참하다가.... 요청 반환값에 `id`라는 이름의 카카오 계정 별 고유값이 있는 걸 확인했다. 이걸 보자마자 딱 갈피를 잡았다.
>
> 방향을 잡고 난 뒤는 단순 구현이었다. 카카오 로그인은 아래와 같은 방법으로 진행시켰다.
>
> 1. 유저가 카카오 로그인을 요청한다. 요청값이 잘못되면 카카오가 알아서 에러를 띄워준다.
> 2. `(유저 이름)(유저 로그인 id)` 를 우리 사이트 아이디로 하는 계정으로 로그인을 시도한다. 비밀번호는 일단 모든 유저가 같게 설정했다. 배포하려면 파싱을 통해 비밀번호를 계정마다 다르게 만들어 줄 필요가 있다. 유저 이름을 아이디에 넣은 이유는, 닉네임을 입력하지 않은 유저는 아이디로 활동하게 했기 때문이다. 아무래도 이름이 기본값인 게 좋을테니까.
> 3. 로그인 성공 시, 우리 사이트에 해당 카카오 계정으로 로그인한 적이 있음을 의미한다. 로그인 실패 시, 처음 로그인하는 유저이다. 알아서 회원가입 요청을 보내도록 해 계정을 만들어 저장했다. 이 때 일반 회원가입 때 설정할 수 있는 개인정보는 모두 default 값으로 처리했다.
> 4. 로그아웃 시, 카카오 토큰과 우리 사이트 토큰 모두 제거한다.
>
> 2일 간 고민한 끝에 해낸 거라 뿌듯했다. 나중에 교수님께 여쭤보니 현업에서도 비슷한 방법으로 구현한다는 듯 하여 더욱 기분이 좋았다.
>
> 
>
> #### 2. 전화번호 인증
>
> > 네이버 클라우드 공식 문서
> >
> > https://api.ncloud-docs.com/docs/common-ncpapi
> >
> > https://api.ncloud-docs.com/docs/ai-application-service-sens-smsv2
>
> 진짜 이번 프로젝트에 내가 구현한 기능 중 하이라이트라고 자신있게 말할 수 있다. 전화번호 인증은 크게 두 단계로 나뉜다. 1. 전화번호를 입력하면 그 번호로 인증번호를 전송하고, 2. 유저가 인증번호를 입력해 맞는지 체크한다.
>
> 그래서 전화번호 인증을 하려면, 일단 문자 전송 기능을 만들어야 한다. Naver Cloud에서 문자 전송 서비스를 건당 9.9원에 제공하드라. 게다가 10만원 공짜 쿠폰까지? 바로 이 플랫폼을 선택했다. 문자 전송을 위해서 발신 번호가 필요해서 일단 내 폰 번호를 입력했다. 배포하려면 고쳐야 할 듯. 
>
> ```python
> # 인증 모델
> class SMS_auth(models.Model):
>     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='smsauth') 
>     phone_number = models.CharField(primary_key=True, max_length=11)
>     time_stamp = models.IntegerField(default=0)
>     auth_number = models.IntegerField(default=0)
>     is_auth = models.BooleanField(default=False)
> 
> # 유저 모델
> class User(AbstractUser):
>     nickname = models.CharField(max_length=10)
>     phone_number = models.CharField(max_length=11, default=0)
>     profile_image = models.IntegerField(
>         default = 0,
>         validators=[
>             MaxValueValidator(24),
>             MinValueValidator(1)
>         ]
>     )
> ```
>
> ```python
> @api_view(['POST'])
> def sms_send(request, phone_number):
>     # 인증 번호 생성
>     auth_number = randint(100000, 999999)
> 
>     # 로그인 유저 확인
>     user = request.user
> 
>     # 시간을 꼭 찍어서 기록해놔야 한다. 이유는 후에 기술.
>     time_stamp = int(time.time() * 1000) // 1000
> 
>     # 해당 전화번호로 입력한 유저가 존재하는지 확인한다.
>     # 상식적으로 한 전화번호엔 한 유저만 존재해야 하니까 ㅇㅇ
>     # 만일 존재한다면 유저와 요청을 보낸 유저를 확인해 알맞게 처리한다.
>     if SMS_auth.objects.filter(phone_number=phone_number).exists():
>         auth_model = get_object_or_404(SMS_auth, phone_number=phone_number)
>         if user == auth_model.user:
>             auth_model.auth_number = auth_number
>         else:
>             return Response(status=status.HTTP_400_BAD_REQUEST)
>     # 전화번호가 없으면 새로운 인증 모델을 만들어준다.
>     else:
>         auth_model = SMS_auth(
>             phone_number=phone_number,
>             auth_number=auth_number,
>             user=user
>        	)
> 
>     # 요청이 온 시간과 인증 여부를 기록하고, 모델을 저장한다.
>     auth_model.time_stamp = time_stamp
>     auth_model.is_auth = False
>     auth_model.save()
> 
>     # 문자를 보내는 함수
>     sms_send_by_naver_cloud(auth_model.phone_number, auth_model.auth_number)
> 
>     # 인증 모델 데이터를 반환
>     serializer = AuthSerializer(auth_model)
>     return Response(serializer.data)
> ```
>
> ```python
> # 문자 보내는 함수
> def sms_send_by_naver_cloud(phone_number, auth_number):
> 
>     # 문자 수신 요청 시간을 기록한다.
>     # 문자 요청 시간과, 이후 사용할 서명과 시간이 같아야 하기 때문.
>     timestamp = str(int(time.time() * 1000))
> 
>     # 공식 문서 참고. 필수 값들 체크해서 써주기.
>     params = {
>         "type": "SMS",
>         "from": sending_phone_number,
>         "content": f'인증 번호 [{auth_number}]를 입력해주세요.',
>         "messages": [
>             {
>                 "to": phone_number,
>             }
>         ],       
>     }
> 
>     # 제일 헤맸던 부분.
>     # 시간 기록해놓고, 서명을 해당하는 시간에 만들기
>     # access key는 Naver Cloud에서 발급
>     headers = {
>         "Content-Type": "application/json; charset=utf-8",
>         "x-ncp-apigw-timestamp": timestamp,
>         "x-ncp-iam-access-key": access_key,
>         "x-ncp-apigw-signature-v2": make_signature(timestamp)        
>     }
> 
>     response = requests.post(
>         mainURL + subURL,
>         data=json.dumps(params),
>         headers=headers
>     )
> 
>     return response.json()
> 
> # 서명 만드는 함수. 공식문서 설명 잘 나와있음.
> def make_signature(timestamp):
>     method = "POST"
>     message = method + " " + subURL + "\n" + timestamp + "\n" + access_key
>     message = bytes(message, 'UTF-8')
>     signingKey = base64.b64encode(
>         hmac.new(secret_key, message, digestmod=hashlib.sha256).digest()
>     )
>     return signingKey
> ```
>
> ```python
> # 인증 번호 체크 함수
> @api_view(['POST', 'PUT'])
> def sms_auth(request, phone_number, auth_number):
>     auth_model = get_object_or_404(SMS_auth, phone_number=phone_number)
>     result = bool(int(auth_model.auth_number) == int(auth_number))
>     user = request.user
>     now = int(time.time() * 1000) // 1000
>     if request.method == 'POST':
>         if result:
>             if now - auth_model.time_stamp < 301: 
>                 user.phone_number = phone_number
>                 user.save()
>                 auth_model.is_auth = True
>                 auth_model.save()
>                 serializer = AuthSerializer(auth_model)
>                 return Response(serializer.data)
>             else:
>                 auth_model.delete()
>                 return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
>         else:
>             auth_model.delete()
>             return Response(status=status.HTTP_400_BAD_REQUEST)
>     elif request.method == 'PUT':
>         if result:
>             if now - auth_model.time_stamp < 301:
>                 auth_model.is_auth = True
>                 auth_model.save()
>                 serializer = AuthSerializer(auth_model)
>                 return Response(serializer.data)
>             else:
>                 return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
>         else:
>             return Response(status=status.HTTP_400_BAD_REQUEST)
> ```
> 인증 번호 체크는 method 별로 나눠서 체크했다. `POST`는 처음 인증할 때, `PUT`은 기존에 인증 내역이 있을 때다. 인증 성공하면 유저 모델에 전화번호를 저장한다. 이제 나중에 인증 성공 여부를 체크할 때 유저에 전화번호 저장 유무로 체크해주면 된다. 
>
> 인증 모델과 연결해놓고 `is_auth`를 왜 확인하지 않냐면, `is_auth`는 현재 인증되었는지 아닌지 여부를 체크하기 때문이다. 아무리 인증한 적 있는 유저라도 비번 변경 등을 위해 새로 인증을 받으면, `is_auth`는 `False`로 바뀐다. 즉, 인증을 체크하는 변수가 2개 있는 셈. 정리하면 아래와 같다.
>
> - `auth_model.is_auth` : 현재 인증된 번호인가? (유효시간 5분)
> - `user.phone_number` : 인증을 성공한 적이 있는가?
>
> 한 가지 실수한 건, `auth_model.phone_number`가 존재하는 모델링이라는 것이다. 아무래도 5시간 만에 완성한 기능이다 보니 모델링이 조금 아쉽다.

솔직히 우승할지는 몰랐는데... 소셜 로그인, 음성 인식, 전화번호 인증 등 안 배운 기능들을 여러 개 만들어서 가능했던 거 같다.

다음 플젝 때는 **제발 모델링 제대로 하고 시작하자**



##  박테리아 - [백준 12428](https://www.acmicpc.net/problem/12428)

이분 매칭, DFS

```python
from sys import stdin
from collections import defaultdict

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
df = [1, -1]
for t in range(int(input())):
    room = 0
    n, m, k = map(int, input().split())
    building = []
    for _ in range(k):
        floor = [list(input().strip()) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if floor[i][j] == '.':
                    room += 1
                    floor[i][j] = room
                    point = [(i, j)]
                    while point:
                        x, y = point.pop()
                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if 0 <= nx < n and 0 <= ny < m and floor[nx][ny] == '.':
                                floor[nx][ny] = room
                                point.append((nx, ny))
                elif floor[i][j] == '#':
                    floor[i][j] = 0
        building.append(floor)
    graph = defaultdict(set)
    for f in range(0, k, 2):
        for i in range(n):
            for j in range(m):
                if building[f][i][j]:
                    for d in range(2):
                        nf = f + df[d]
                        if 0 <= nf < k and building[nf][i][j]:
                            graph[building[f][i][j]].add(building[nf][i][j])
    ans = room
    match = [0] * (room + 1)
    for room_idx in graph:
        visited = [False] * (room + 1)
        ans -= dfs(room_idx)
    print(f"Case #{t + 1}: {ans}")
```

이제 다시 신나는 알고리즘 시작이다. 스타트는 상큼하게 이분 매칭으로.

인접한 방 중 하나만 선택 가능하고, 최대를 선택하고 싶다? 볼 것도 없이 최소 버텍스 커버 찾기다. 다만 구현이 조금 귀찮은 정도.

홀수 층과 짝수층의 방으로 나눠서 이분 매칭을 진행해주면 된다. 간선은 서로 붙은 방끼리 이어주자. 답은 전체 방의 수에서 최소 버텍스 커버의 크기만큼 빼주면 된다.
