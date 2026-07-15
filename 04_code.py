# 변수 (
# 변수 이름 규칙1  영문자, 숫자, 밑줄(_) 사용 / 숫자 시작 불가 / 공백 불가)
# 변수 이름 규칙2  예약어 불가 / 함수이름 덮어쓰기 금지 / 편집기에서 자동 색 입혀진 단어 금지
# 변수 이름 추천1  해당 변수의 기능을 적어주기 / 여러 단어는 밑줄로 잇고 소문자 통일
x = 10
print(x)    # 10
x = 20
print(x)    # 20
temp = 25
temp = 30   # temp 변수 값 재할당

x, y, z = 10, 20, 30    # x = 10, y = 20, z = 30 순서대로 할당

temp = 36   # 숫자로 저장하고 싶으면 따옴표 금지
name = "센서 A" # 글자는 무조건 따옴표 
print(temp) # 36 출력
print("temp")   # temp 출력
print(name) # 센서 A 출력

#==========================================
print("===== 변수 사용 활용 =====")
x = 5
x = x + 5 # 10 출력
print("재할당하기 전 temp:", temp)  # 재할당하기 전 temp: 36 출력
temp = 15   # 위의 temp 변수에 15 재할당
Temp = 15   # Temp 변수에 15 할당
print("temp:", temp, "Temp:", Temp) # temp: 15 Temp: 15 출력

print("===== 재할당 =====")
a = 10
b = a    # b 변수에는 10이 저장 (저장할 때의 그 순간의 a 값을 b에 복사)
a = 100  # a에 재할당 100
print(b) # b 변수에는 그대로 10이 출력

#==========================================
print("===== 여러 변수 한 번에 선언 및 할당 =====")

width, height = 10, 20  # width는 10, height는 20 할당  
print("width:", width, "height:", height) # temp: 10 Temp: 20 출력

#==========================================
print("===== 주석으로 변수 설명 =====")

temp = 25   # 온도(섭씨)
count = 3   # 센서 개수
temp = 1000000000   # 재할당
print(temp)

# 실습
print("===== 실습 =====")
temp = 25
print(temp) # 25
name = "센서A"
print(name) # 센서A

# 실습2
temp = 25
temp = 30
print(temp) # 30 출력

temperature = 30
print(temperature)  # 30 출력 및 temp 시 NameError

# 실습3
my_number = 3
print(my_number)# 3 출력
mood = "굿"
print(mood)     # 굿 출력

# 실습4
age = 29
label = "나이"
print(label)
print(age)

# 실습5
x = 10
print(x)    # 10
x = x + 5
print(x)    # 15
x = x * 2
print(x)    # 30

# 실습6
a = 100
b = a
a = 999
print(a)    # 999
print(b)    # 100 b의 값을 a가 100일 때 할당해주었기 때문에

# 실습7
#print(temp) # temp 변수가 없기에 NameError
temp = 25
print(temp) # temp 변수 할당했기에 25 출력
score = 90
#print(Score)    # 대소문자가 달라 Score 라는 변수가 없어 NameError
print(score)    # 90 출력

# 실습8
temp = 25   # 온도(섭씨)
count = 3   # 센서 개수
# temp = 100    # 줄 전체 주석화하여 실행 무시
print(temp) # 25 출력

# 실습9
x = 5
x = 10
x = x + 1
print(x)    # 11 출력

# 실습10
name = "센서A"
temp = 25
print("설비")   # 설비
print(name)    # 센서A
print(temp)    # 25

# 실습11
# a, b = 25, 3  # 변수이름이 의미불명이면 기능 인식 문제 발생
device_temp, sensor_count = 25, 3 # 기계온도 = 25, 센서개수 = 3 으로 인식
print(device_temp)
print(sensor_count)

# 실습12
x, y, z = 1, 2, 3       # x, y, z 순서대로 1, 2, 3 할당
width, height = 4, 3    # width, height에 각각 4, 3 할당
print(width)    # 4
print(height)   # 3