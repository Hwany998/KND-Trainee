# 여러 줄 문자열
notice = """설비 점검 안내
1. 전원 확인
2. 센서 점검"""

print(notice)
#설비 점검 안내
#1. 전원 확인
#2. 센서 점검

notice = """
설비 점검 안내
1. 전원 확인
2. 센서 점검
"""
print(notice)
#
#설비 점검 안내
#1. 전원 확인
#2. 센서 점검
#
#""" """ 3중 따옴표 사용 시 그 내부 모든 줄바꿈, 탭 등이 모두 반영됨

#이스케이프 문자(역슬레시) \n 줄바꿈, \t 띄어쓰기탭, \.:'\등 특수기호 뒤로 추가
notice = "설비 점검 안내\n1. 전원 확인\n2. 센서 점검\n"
print(notice)           #설비 점검 안내
                        #1. 전원 확인
                        #2. 센서 점검
                        #
tap = "이름\t상태"
print(tap)              #이름   상태

backslash = "이름\\상태" 
print(backslash)        #이름\상태

quotes = "It\'s me"
print(quotes)           #It's me

#빈 문자열과 공백 문자열 차이: ""따옴표로 감싸졌지만 아무것도 작성안된거면 빈 문자열 0자
#" "따옴표 안에 공백(띄어쓰기)있으면 "공백 문자열" 1자 이상
print("" == " ")        #False

#==================================
#인덱스 개념 - 문자열 위치에 따른 숫자 지정 (리스트 개념의 시작)

word = "PYTHON"
print(word[1],word[2],word[0])  #Y T P
abc = "난뒤로안돌아가돌아버려미쳤어뒤죽박죽피카소곰이된돈시간벌어빚갚어"
print(abc[10], abc[8], abc[3])  #려 아 안
korean = "김아무개제한토환경이갖춰진곳"
print(korean[0]+korean[4]+korean[7])    #김제환
#print(korean[100])             #korean 100번 인덱스 없어서 IndexError오류

#슬라이싱 문법 [start:end]
print(word[0:2])                #PY     0~1번 인덱스
print(word[1:5])                #YTHO   1~4번 인덱스
print(word[:])                  #PYTHON 시작번~끝번 인덱스 [0:6]기능
#슬라이싱 문법 중 스킵
print(word[:6:2])               #PTO    0~5번 인덱스를 2자리씩 스킵
print(word[::2])                #PTO    0번자리에서 2자리씩 스킵
print(word[1::2])               #YHN    1번자리에서 2자리씩 스킵
print(word[::-1])               #NOHTYP 

#========================
#여러 변수 문자열 연결
#구분자 \ - len() 활용

print(len("Hello, World!"))     #13
print(len(""))                  #0

var = "여러분~ 한 시간만 힘내보죠."
print(len(var))                 #16
print(len("술래잡기")+len("고무줄놀이"))    #9 int반환이라 가능

#in, not in 등 포함 여부 
print("고장" in "설비 고장")       #True
print("정상" in "설비 고장")       #False
print(" " in "설비 고장")         #True

#count 개수 세기    
fruit = "apple"
print(fruit.count('a'))         #1 
print("banana".count('a'))      #3  

#find() 위치 찾기 특정 글자 첫 위치(번호)
print("진태진".find("진"))        #0 (인덱스 기준이니 첫번째 0자리)
email = "hong@gamil.com"
at = email.find("@")            #@위치의 인덱스를 추출
user_id = email[:at]            #email 할당값의 @위치 인덱스까지
print(user_id)                  #hong

sqe = "SQE-00Q8"
print(sqe[:sqe.find("-")])

#index() 위치(인덱스번호) 찾기 (find와 짝, 없으면 오류) 상황따라 사용
print("===index() ===")
email = "wpghks1998@naver.com"
at = email.index("@")         # 5
print(email[:at])             # wpghks1998

print(sqe[:sqe.index("-")])

#==========================
print("===count()===")
str = "a, b, c, d, e,a, a"
print(str.count("a"))       #3
print(str.count(","))       #6
print(str.count(", "))      #5  (정확한 문자열을 가져오기 때문에 5가 반환)

#startswith() - 특정 단어로 !시작!하는 참과 거짓
print("===startswith()===")         #bool타입
print("APD-002".startswith("APD"))  #True (APD를 변수로 만들어서 출력시켜도 됨)

#endswith() - 끝 확인, 특정 단어로 !끝!나는 참과 거짓
print("===endswith()===")         #bool타입
str2 = "월요일이야! 우리 모두 파이팅!"
print("APD-002".endswith("!"))      #True
print("APD-002".endswith("야!"))     #True
print("APD-002".endswith("엄"))     #False
print("APD-002".endswith("월요일이야! 우리 모두 파이팅!"))      #True
print("APD-002".endswith("월요일이야!     우리 모두 파이팅!"))  #False
print("APD-002".endswith("월요일이야! 우리 모두 파이팅!   "))   #False

#in은 어디든 !포함!

print("===값은 객체다===")
print(type("잊어먹으면 안돼!"))      #<class 'str'>
#endswith()과 len의 차이는? endswith()은 .으로 연결 
#. 연결은 "매서드" / 문자열이나 int, float처럼 특정 자료형(객체) 내부에 포함된 기능
#startswith(), endswith()은 int 자료형에선 사용 불가
#print(len(123))       #len 내장함수 또한 'int' 사용 불가
#len은 . 사용 안함
#() 는 함수
#len과 같이 기본 제공 함수 "내장함수"

str3 = "abcdefg"

str3.upper
print(str3)         #abcdefg str.upper를 재할당하지 않아서 abcdefg가 출력

#lower() - 소문자 변환
print("===lower()===") #이하 동일

#capitalize() - 첫 글자만 대문자 변환, title() - 각 단어 첫 글자만 대문자 변환 (띄어쓰기, ' 기준)
user_name = "shinosuke jjangu"
print(user_name.capitalize())   #Shinosuke jjangu
print(user_name.title())        #Shinosuke Jjangu
print("i'm full".title())       #I'M Full
print("i\'m full".title())       #I'M Full

#strip() - 문자열 양쪽 공백 제거, lstrip() - 왼쪽 공백 제거, rstrip() - 오른쪽 공백 제거
text = ' 정   상 '
text = text.strip()
text1 = text.rstrip()
text2 = text.lstrip()
print(text)             # 정   상
print(text1)            # 정   상
print(text2)            #정   상

#strip("") - 문자열 양쪽 문자 제거, lstrip("") - 왼쪽 글자 제거, rstrip("") - 오른쪽 글자 제거
str4 = "===정===상==="
print(str4.strip("="))    #정===상

#=========체이닝========
raw = "     NORMAL     "
step1 = raw.strip()             #NORMAL 
step2 = step1.lower()           #normal
chain = raw.strip().lower()     #normal 체이닝
raw = raw.strip().lower()       #raw 재할당

#=====================
str5 = "aaab 이렇게? cd"
print(str5.strip('abcd'))   #" 이렇게? "
print(str5.strip('abcd '))  #"이렇게?"
print(str5.strip('bc'))     #"aaab 이렇게? cd"
print(str5.strip('ab'))     #" 이렇게? cd"

#=====================
phone = "010-1234-1234".replace("-", " ")   #010 1234 1234
print(phone)
print("정 상 작 동".replace(" ", ""))       #정상작동
print("정     상 가 동".replace(" ", ""))   #정상가동
print("정     상 가  동".replace("  ", ""))   #정 상 가동 (2칸 띄우기만 삭제)
#print("고장". replace)("고장", "fault")  #fault    type오류
#print("고장". replace("고", "fault"))   #fault장   type오류
str6 = "설비 정상 가동"
print(str6.replace("정상", "점검"))     #설비 점검 가동
print(str6.split())                  #['설비', '정상', '가동']  #띄어쓰기 기준으로 나눠서 리스트로 반환

fruits_list = "사과, 배, 바나나, 딸기"
print(fruits_list[1])   #배
print(fruits_list[3])   #딸기
print(fruits_list[-1])  #딸기

print("-".join(fruits_list.split(", ")))

# split 횟수 제한
num = "010-2283-1234"
print(num.split("-", 1))   #['010', '2283-1234']  #첫번째 - 기준 횟수로 나눔

print("===join()===")
#리스트의 문자열들을 구분자로 이어 붙이기
date = ['2025', '01', '15']
print("-".join(date))

print("=== print 함수의 sep, end ===")      #구분자 추가
print("2026", "07", "27")                   #2026 07 27
print("2026", "07", "27", sep = "사랑해")   #2026사랑해07사랑해27
print("안녕", "하세")                       #안녕 하세
print("안녕", "하세", end = "요")            #안녕 하세요
#print("안녕", "하세", end = "요", "ㅎㅎ")    #end, sep 이후 추가 인자 불가
print("이런식으로 쓰죠?", "근데 안보이는 기본값이 있어요", sep="", end="\n")

#f-string 기본 문법 예시 f'{변수}'
name = "홍길동"
age = 25
#print(str(age))
#print(name + "님은" + str(age) + "세 입니다.")
print(f'{name}님은 {age}세 입니다.')
code = "APD-002"
print(f'{code} 점검 완료')

#f-string 연산
hour = 8
print(f'우리는 하루에 {hour}시간 수업을 듣고, 이는 {hour*60}분에 해당합니다.')

#f-string 통한 소수점 자리 표기법
value = 25.7162712
print(f'{value:.2f}')    #25.72