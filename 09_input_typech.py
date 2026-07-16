#input - 사용자 입력

print("출력")
print(5)

#name이란 변수에 input함수로 값을 할당 (터미널에 값 입력)
#name = input("이름: ")
#print(name)

#input("이름: ","성별: ")    #input()은 하나의 매개변수만 전달받을 수 있다. 그래서 이름 입력 순서 이후 오류발생

name = input("이름: ")
age = input("나이: ")
male = input("성별: ")
print("이름: "+name,"나이: "+age, "성별: "+male)

name_age = input("이름과 나이를 입력하세요. (ex. 홍길동20)", )
print(name_age)
input("입력한 정보가 맞다면 네, 틀리면 다시 입력하세요. (ex. 홍길동20)")
print(name_age)
print(type(name_age))       #input()은 무조건 할당받는 값은 str으로 귀결된다. 숫자만 써도 str임.

#형변환 int, str등 type에 ()괄호로 묶어 사용 
age = int(input("나이(int형_변환ver): "))          #age에 input한 str값을 int로 변환한걸 할당
print("내년에", str(age + 1)+ "세가 될 예정입니다.")    #str, int를 함께 print할 수 없지만, 형변환을 통해 가능하도록함.

#===========================
height = float(input("신장: "))   
print(type(height))     #float
print(float(12.5))      #실수값을 매개변수로 넣어도 문제 없다.
print(float(12))        #12.0으로 출력 -> 정수를 실수형으로 변환하기 때문에 .0이 필수

#===========================