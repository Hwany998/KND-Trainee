#실습1
hello = input("이름을 알려주세요. ")
print("안녕하세요", hello+"님")

#실습2
age = int(input("태어난 해 (ex: 2000): "))
print("귀하의 나이는 만 "+str(2026-age))

#실습3
nation, city = input("국적: "), input("거주도시: ")
print("당신은 "+nation+" 국적을 가지고 현재 "+city+"에 거주하고 계시군요.")

#실습4
a = int(input("1번값: "))
b = int(input("2번값: "))
print("더하기: "+str(a + b))
print("빼기: "+str(a - b))
print("곱하기: "+str(a * b))
print("나눗셈: "+str(round(a / b, 2)))
print("값: "+str(a // b))
print("나머지: "+str(a % b))
print("거듭제곱: "+str(a ** b))

#실습5
temp = int(input("현재 온도: "))
print("출력 결과 1: "+ str(temp > 80))
print("출력 결과 2: "+ str(temp >= 0))

#실습6
math = int(input("수학점수: "))
eng = int(input("영어점수: "))
science = int(input("과학점수: "))
print("평균 60점을 넘었는가? "+ str(((math+eng+science)/3) >= 60))