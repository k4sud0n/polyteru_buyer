# Polyteru Buyer

1. 필요한 패키지들 설치하기

```
pip install --upgrade pip
pip install -r requirements.txt
```


2. `config.ini` 파일을 생성하고 다음과 같이 적어주기

```
[LOGIN]
ID = 아이디
PASSWORD = 비밀번호

[ITEM]
LINK = PL23FWKNLS01PK,PL22AWMWGDG-732-786-792-793,PL22AWMWGDG-732-786-792

[KAKAOPAY]
PHONENUMBER = 01000000000
BIRTH = 생년월일6자리
```

- LINK는 폴리테루 스토어 주소에서 product/ 뒤에 있는 코드를 적어준다. 공백 있으면 안되고 붙여서 써야한다. (ex. AAAAA,BBBBB,CCCCC)


3. 실행하기

```
python main.py
```