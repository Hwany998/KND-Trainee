# int - 정수형 (소수점 없는 수 0, 음수 포함)

count = 3
age = 20
tall = 168
temp = -30
zero = 0

# float - 실수형 (소수점 있는 수, 5.0 같은 것도 포함)

tired = 99.9999
height = 17.6

# ===================

# string - 문자열 (따옴표에 감싸진 모든 값, "12" 이런 것도 포함)

hello = "안녕하세요"
empty = ""
illit = "It's me"   # "" 큰 따옴표 안의 '작은 따옴표는 인정해줌

# bool - 참거짓형 (True, False)

ok = True
no = False

# 비교할 시 bool로 출력
print(100 < 5)  # False
print(5 == 5)   # True

# type - 자료형 확인, type(확인하려는값) -> 확인하려는값의 자료형 알려줌

type(5)     #터미널에서 확인 불가
print(type(5))          # <class 'int'>
print(type(5.2))        # <class 'float'>
print(type("센서A"))     # <class 'str'>
print(type(3 > 2))      # <class 'bool'>
print(type(True))       # <class 'bool'>
# 1. print 함수의 내부를 확인
# 2. print 함수에 또 함수가 있는 것 확인하고 type 함수 내부 확인
# 3. type 함수의 내부에 연산자 있는 것 확인하고 연산 진행
# 4. 3 > 2 연산 결과는 True이기 때문에 type(True)로 바뀜
# 5. type(True)의 결과인 <class 'bool'>이 print로 인해 터미널에 출력

print(3,type(3))       # 3 <class 'int'>

num = 123
fake_num = "123"
str = "문자열"
ok = True

# 내가 터미널에서 출력된 결과 중에서
# type()을 사용해서 출력된 자료형을 쉽게 확인할 수 있는 방법
print("num >>>",type(num))    # num <class 'int'>
print("fake_num >>>",type(fake_num))  # fake_num >>> <class 'str'>
print("str >>>",type(str))  # str >>> <class 'str'>
print("ok >>>",type(ok))    # ok >>> <class 'bool'>

# ===================

print("=== 자료형마다 동작 다른 것 확인 ===")
print(3 + 5)        # 8 int형
print("3" + "5")    # 35 str형 이어붙이기
print("안녕하"+"세요") # 안녕하세요 str형 이어붙이기

# ===================

print("=== 자주 하는 실수 ===")
print(0.1 + 0.8)    # 0.9 float형 (단, 내부 연산 과정에서 작은 오차 발생 가능)
print(round(0.11 + 0.12, 2))  # 0.23에서 작은 오차가 나올 수 있음. (round로 해결)

# str과 int/float 간 덧셈 불가
# print('123' + 456)# TypeError 발생
print(10 / 2)       # 5.0 (나눗셈은 무조건 float 실수형)
print(type(10 / 2)) # <class 'float'>