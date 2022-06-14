# 0614



## Python requests

```python
import requests

#### 해당 값 수정 필수 ####

nickname = ""

##########################

mainUrl = "http://13.125.222.176/quiz/"
headers = {"Accept": "application/json", "Content-Type": "application/json"}
nextUrl = "alpha/"
question = "SSAFY의 인스타그램 계정명은 무엇일까요? (영문)"
remain_question = 20
data = {
    "nickname": nickname,
    "yourAnswer": '',
}


result = '# 스무고개 \n \n '

while remain_question:

    print(question, flush=True)
    answer = input().strip()

    data = {
        "nickname": nickname,
        "yourAnswer": answer
    }

    res = requests.post(mainUrl + nextUrl, headers=headers, json=data).json()

    if res['code'] == 200:
        print(flush=True)
        remain_question -= 1
        question = res['question']
        nextUrl = res['nextUrl'] + '/'

        result += f'## Q{20 - remain_question} Result \n \n'
        result += '```json\n'
        result += '{\n'
        result += f'  code : 200,\n'
        result += f'  question : \"{question}\",\n'
        result += f'  nextUrl : \"{nextUrl}\",\n'
        result += '}\n'
        result += '```\n \n \n'

    elif res['code'] == 600:
        print('오답입니다\n', flush=True)
    elif res['code'] == 403:
        print('닉네임 값을 확인하세요.')
        exit()
    else:
        print('예기치 못한 에러가 발생했습니다.')
        exit()

print('결과 작성 중...')
file_path = './README.md'
f = open(file_path, 'w', encoding="UTF-8-sig")
f.write(result)
print('결과 파일이 해당 파이썬 파일의 폴더 위치에 성공적으로 생성되었습니다.')
```

흠... 올려다 되나 싶긴 한데, 열심히 했으니 올려본다.

선택 과제로 나온 거였다. 근데 일일히 값을 확인하고 새로 입력값 바꾸는게 너ㅓㅓㅓ무 귀찮았다. 그래서 자동화했다. 하는 김에 제출에 필요한 `README.md`까지 작성하도록 코드를 짰다. 사실 뭐 새롭게 안 건 없다. 그나마 신경 쓸만한 포인트는 write 모드에서 한글이 깨지지 않도록 `encoding="UTF-8-sig"` 설정하는 거 정도? 에러 케이스도 나름 신경 써주려 애썼다.

아 그리고 `flush` 기능을 써봤다. 나름 상호작용을 하는 거니까... 근데 사실 큰 의미는 없다. 어차피 `requests` 보내는데 시간이 걸려서 안 썼어도 큰 문제는 없었을 듯.

나만 쓰긴 아까운 거 같아서 이전 같은 반들 분께 코드를 공유했다. 다들 좋아해주셔서 뿌듯하다 ㅎㅎ 전체에도 공유하고 싶은데, 교육프로들한테 한 소리 들을 거 같아서 일단 참고 있다.