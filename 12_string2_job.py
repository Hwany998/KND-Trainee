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

#재밌는? 실습퀴즈
quiz = 'python'
print(quiz[:2]+quiz[2].upper()+quiz[3:])