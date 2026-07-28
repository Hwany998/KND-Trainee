#실습1
font = 'ready'
print(font.upper())

#실습2
font2 = 'WARNING'
print(font2.lower())

#실습3
print('kim chul soo'.capitalize())

#실습4
font3 = "Fault"
font4 = "FAULT"
print(font3.upper())

#실습5
a = 'ABC'
b = 'abc'
c = 'Abc'
print(a.isupper())
print(b.islower())
print(c.isupper())

#실습6
sensor = 'Sensor_LOG.CSV'
print(sensor.startswith('sensor'))
print(sensor.endswith('.csv'))

sensor2 = sensor.lower()
print(sensor2.startswith('sensor'))
print(sensor2.endswith('.csv'))

#실습
str = "   Warning  "
step1 = str.strip()
step2 = step1.lower()
print("["+step1+"]")
print("["+step2+"]")

#실습2
font5 = "a,b,c,d"
print(font5.split(","))

#재밌는? 실습퀴즈
quiz = 'python'
#방법1
print(quiz[:2]+quiz[2].upper()+quiz[3:])
#방법2
print(quiz[:2]+quiz.strip("py").title())
#방법3
print(quiz.split("t"))
print("T".join(quiz.split("t")))
print(quiz[2].upper().join(quiz.split("t")))

#실습3
date = ['2025', '01', '15']
print("-".join(date))

#실습4
date2 = "2026/07/27"
date2 = date2.split("/")
date3 = "-".join(date2)
print(date3)

#실습5
s = '1, NORMAL, 25.3'
s = s.split(",")
s1 = s[1].strip().lower()
print(s1)

#실습6
machine = "톱날"
temp = 65
print(f'{machine} 온도 {temp}도')

#실습7
math = 90
science = 84
eng = 87
print(f'시험 평균 점수: {(math+science+eng)/3}')

#실습8
value = 87.456
print(f'소수점 첫째자리 기준 {value:.1f}, 소수점 둘째자리 기준 {value:.2f}')

#실습9
item = ' 5, sensor_2, WARNING, 0.78912 '
item2 = item.strip().split(",")
real_sensor = item2[1].lstrip()
status = item2[2].lstrip().lower()
score = round(float(item2[3].lstrip()),2)
print(f"[센서 {real_sensor}] 상태 {status}, 측정값 {score}")