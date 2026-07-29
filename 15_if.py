# 조건문 if
# 조건따라 실행, 조건은 True, False로 결과가 나와야 함

# if 조건식:
#     실행할 코드 (한 칸 들여쓰기)

#if문 조건식 결과가 True일 때만 실행하라는 뜻
#들여쓰기된 것들만 실행됨

temp = 85
if temp > 80: #만약 temp변수 할당값이 80초과라면?
    print("정상 온도 80도를 초과\n!!!점검 요망!!!")
print("항상 실행1")

temp = 50
if temp > 80: #만약 temp변수 할당값이 80초과라면?
    print("정상 온도 80도를 초과\n점검 요망")
print("항상 실행2")

#temp 온도가 80보다 크면 경고, 80이하는 정상 출력
if(temp > 80):
    print("경고")
else:
    print("정상")

#if문 실습 (사용자에게 나이를 입력받아 성인인지 체크하는 조건문)
if(int(input()) > 19):
    print("성인입니다.")
else:
    print("미성년자입니다.")

#if문 실습2 (숫자 맞추기 게임 / 정답은 임의로 지정)
#정답, 오답 출력, 예시: 정답 50 / 사용자 입력값 받기, 사용자 입력값이 같다면 정답, 틀리면 오답
if(input() == 50):
    print("정답")
else:
    print("오답")
print("게임종료")

input_color = input("===신호등 색을 골라주세요. 빨, 노, 초=== : ")
if(input_color == "초" or input_color == "빨"):
    if(input_color == "초"):
        print("건너세요.")
    else:
        print("기다리세요.")
else:
    print("다시 입력하세요.")

#and 연산자 + 중첩
#체온 판단, 정상 체온 범위: 36.3 ~ 36.8
user_temp = float(input("당신의 현재 체온을 입력해주세요. (소수점 첫째자리 포함): "))
if(36.3 <= user_temp <= 36.8):
    print("정상 체온입니다.")
else:
    if(user_temp < 36.3):
        print("저체온증이 의심되니 따뜻한 곳에 머무세요.")
    else:
        print("고열이 의심되니 시원한 곳에 머무세요.")
print("체온 확인 완료.")

#위의 체온 판단 if문 안에서 열나는지 저체온인지 판단하도록 수정
if(36.3 >= user_temp or user_temp >= 36.8):
    if(user_temp >= 36.8):
        print("고열이 의심되니 시원한 곳에 머무세요.")
    else:
        print("저체온증이 의심되니 따뜻한 곳에 머무세요.")
else:
    print("정상 체온입니다.")
print("체온 확인 완료.")

# elif 탄생 (if다중첩)
score = 82
if score >= 90: print("우수")
elif score >= 70: print("보통")
elif score >= 50: print("미흡")
else: print("과락")

#not 연산자
if not (3 == 5): print("출력됩니다.")

#실습2
prac_temp = int(input("측정 온도를 입력하세요: "))
if prac_temp > 80:
 print("위험")
elif prac_temp > 60:
 print("주의")
else:
 print("정상")

#실습3
id = str("ID를 입력해주세요. (8자까지): ")
pw = str("PW를 입력해주세요. (8자까지): ")
if(id == "wpghks" & pw == "1998"):
    print("회원 정보 확인.")
else:
    print("다시 확인하세요.")

#실습4 (자료상 실습5)
prac_temp2 = int(input("현재 온도: "))
prac_vibe2 = float(input("현재 진동: "))
prac_elec2 = int(input("현재 전류: "))
if(prac_temp2 > 80 and prac_vibe2 > 4.0): print("위험: 즉시 정지")
else:
    if(prac_elec2 > 60 and prac_temp2 > 70): print("주의: 부하 점검")
    elif(prac_vibe2 > 2.5): print("주의: 진동 관찰")
    else: print("정상")