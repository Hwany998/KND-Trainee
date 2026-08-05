#실습1
a = 17
b = 5
print(a + b)    # 22
print(a - b)    # 12
print(a * b)    # 85
print(a / b)    # 3.4 (소수점까지)
print(a // b)   # 3 (몫)
print(a % b)    # 2 (나머지)
print(a ** b)   # 1419857 (거듭제곱)

#실습2
a = 22
b = 20
c = 24
print((a + b + c)/3)# 22.0 (평균, 소수점 주의)
line = 8            # 변 길이
print(line ** 2)    # 64 (정사각형 넓이)
print(a * b * c)    # 10560 (직육면체 부피)

#실습3
print(3 == 3)           #True
print("안녕a" != "안녕A") #True
print(4 > 6)            #False
print(2.5 < 6)          #True
print(6 >= 6)           #True
print(4 <= 3.5)         #False

#실습4
temp = 85                   #온도 변수
temp_ok = temp >= 60 and temp <= 90
print("온도정상",temp_ok)              #온도정상 True
press = 5                   #압력 변수
press_ok = press >= 3 and press <= 7
print("압력정상",press_ok)             #압력정상 True
print("모두정상",temp_ok and press_ok) #모두정상 True

#실습5
docu = 100
print("재고",docu)      #재고 100
docu += 50
print("입고 후",docu)   #입고 후 150
docu -= 30
print("출고 후",docu)   #출고 후 120
docu += 5
print("반품 후",docu)   #반품 후 125

#실습6
all = 500
bad = 23
print("불량률",bad / all * 100,"%")  #불량률 4.6 %
run_h = 21
all_h = 24
print("가동률",run_h / all_h * 100,"%") #가동률 87.5 %

#실습7
minutes = 500
print((minutes // 60), (minutes % 60)) #8시간20분