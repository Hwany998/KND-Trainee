# 산술연산자
# + - * / //(몫) %(나머지) **(거듭제곱)
print(3 + 5)    # 8
print(3 - 5)    # -2
print(3 * 5)    # 15
print(3 / 5)    # 0.6 (나눗셈은 무조건 float문으로 소수 출력)
print(3 // 5)   # 0 (몫)
print(3 % 5)    # 3 (나머지)
print(3 ** 5)   # 243 (거듭제곱)

# 연산 우선순위
# **(거듭제곱) > *(곱) /(나누기) //(몫) %(나머지) > + - -> (괄호)로 묶으면 그게 우선
print(2 + 8 * 3)    #26
print((2 + 8) * 3)  #30

#===========================
#복합연산자

result = 3 * 5
print(result)   # 15
result += 10    # 15에 10을 더한 값을 재할당
print(result)   # 25
result -= 10    # 25에 10을 뺀 값을 재할당
print(result)   # 15
result *= 10    # 15에 10을 곱한 값을 재할당
print(result)   # 150
result /= 10    # 150에 10을 나눈 값을 재할당 (실수 소수점)
print(result)   # 15.0 (중요포인트)

#===========================
#문자열 연산
print("안녕"+"하세요")
print("안녕","하세요")
print("안녕 "+"하세요")
print("안녕"+" "+"하세요")

#문자열 곱하기
print("안녕" * 5)   # 안녕안녕안녕안녕안녕

#===========================

#비교연산자
print("===비교연산자===")
# <, >, <=, >=, ==, !=  (비교결과는 True 또는 False)
print(7 < 16)       # True

#비교연산자는 문자열도 가능
print("Hello" == "hello")   #False (공백 및 대소문자로 결과가 바뀜)

#=========================
#변수로 문자열 비교
hello = "hi"
print(hello == "hi")    #True
num1, num2 = 123, 456
print(num1 >= "num2")   #TypeError발생, int와 str 간의 비교 불가

#=========================
#논리연산자 and / or / not
print ( 5 == 5 and 7 == 7)
print ( 5 == 7 and 7 == 7)
print ( 5 == 5 and 7 != 7)

print ( 5 == 5 or 7 == 7)
print ( 5 == 7 or 7 == 7)   #False (처음이 False면 다음 조건을 실행하지않음.)
print ( 5 == 5 or 7 != 7)

#not문은 bool 결과값을 뒤집어 출력
print(not True)         #False
print(not 5 == 5)       #False