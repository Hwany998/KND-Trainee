# 실습1 - 자료형 변수
count = 3       # int
temp = 12.2     # float
name = "김제환"     # string
is_ok = True    # bool
print(count,temp,name,is_ok)

# 실습2 - 실습1의 변수를 type()을 통해 자료형 체크
print(count,"->",type(count))   # 3 -> <class 'int'>
print(temp,"->",type(temp))     # 12.2 -> <class 'float'>
print(name,"->",type(name))     # 김제환 -> <class 'str'>
print(is_ok,"->",type(is_ok))   # True -> <class 'bool'>

# 실습3 - 값을 type()을 통한 자료형 체크
print(type(100))    # <class 'int'>
print(type(100.0))  # <class 'float'>
print(type("100"))  # <class 'str'>
print(type(False))  # <class 'bool'>

# 실습4 - int, str 자료형의 덧셈 연산
print(3 + 5)        # 8 int형
print("3" + "1")    # 31 str형
print("12" + "21")  # 1221 str형

# 실습5 - bool 확인
print(3 > 2)        # True
print(5 == 5)       # True
print(type(3 > 2))  # <class 'bool'>

# 실습6 - 변수 자료형 변경
count = 3
print(count,type(count))    # 3 <class 'int'>
count = 3.0
print(count,type(count))    # 3.0 <class 'float'>
count = "3"
print(count,type(count))    # 3 <class 'str'>

# 실습7 - 변수명에 따른 자료형 지정
device_temp = 75.5      # float 기계 온도
check_count = 5         # int   검사 횟수
device_name = "열 감지 센서"    # string 기계명
is_normal = True        # bool 평소 상태