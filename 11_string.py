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