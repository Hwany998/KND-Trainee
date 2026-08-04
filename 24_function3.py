# 07_03 함수 설계 활용

# 기본값 인자
# name과 value는 호출 때 꼭 매개변수를 지정해야하지만 
# unit은 지정/언급 안하면 "(C)" 기본값으로 정해짐
def report(name, value, unit):
    print(f'{name} : {value}{unit}')

report("압축기A", 75.3, "(C)")
#report("압축기A", 75.3)         # 인자값 부족으로 에러 발생
report("압축기A", 75.3, "(F)")

# 기본값 덮어쓰기
# 결과가 boolean 타입을 return하는 함수는 보통 is로 시작
def is_overlimit(value, limit):
    if value > limit:
        # 위험 맞음
        return True
    # 그 밖 위험 아님
    else:
        return False
    
print(f'위험한가요? {is_overlimit(95, 90)}')
print(f'위험한가요? {is_overlimit(95, 98)}')
# 다른 기준이 필요할 때만, 기준을 함께 전달해주면 된다.
print(f'위험한가요? {is_overlimit(105, limit = 90)}')

# 실습1
# 기본값 있는 매개변수를 만들고, 생략하면 기본값, 넣으면 덮어쓰기 확인
# 1. def 괄호 안 매개변수 =로 기본값 지정
# 2. 인자 생략하고 호출해 기본값 쓰이는지 확인
# 3. 인자 넣어 호출해 기본값 덮은지 확인
# 4. 필수 매개변수는 앞, 기본값 매개변수는 뒤 순서 규칙 확인

# 앞선 예제 코드들로 대체

# 02. 지역변수와 범위
# scope, 코드의 범위, 이 변수 데이터의 생존

# 바깥 동네에 변수 하나 생성
print("=" * 40)
outter = 100

def change_outter():
    # 아래 코드는 함수 내부에서 처음 언급, 새롭게 만들어진 내부 outter(지역변수)
    # 함수가 종료되면 메모리에서 제거, 함수 바깥 같은 이름 존재에는 영향 안줌
    outter = 50
change_outter()
print(outter)       # 100

print("=" * 40)

# 실습2
# 1) def 괄호 안에 매개변수 두 개를 쉼표로 정의
def sensors(machine, temp):
# 2) 함수 안에서 두 매개변수를 함께 활용
    print(f'{machine} {temp} 도')
# 3) 인자 두 개를 순서대로 전달해 호출
sensors("모터", 78)
# 4) 인자 순서를 바꾸면 결과가 어떻게 달라지는지 확인
sensors(92, "펌프")     # 순서가 바뀌어 원하는 값 출력 불가

print("=" * 40)

# 실습3
# 1) 매개변수 두 개를 가진 함수를 정의
def machine(name, temp):
# 2) 호출할 때 매개변수 이름을 지정해 값을 전달
    print(name, temp)
# 3) 키워드로 전달하면 순서를 바꿔도 같은 결과인지 확인
machine(temp = 78, name = "모터")   # 같은 결과 출력
# 4) 위치 인자와 키워드 인자를 섞을 때는 위치가 먼저임을 확인
machine("펌프", temp = 92)
# machine(temp = 92, "펌프")  # 오류 발생
print("=" * 40)

# 실습4
# 1) 값을 받아 계산하는 함수 정의
def summing(num1,num2):
    total = num1 + num2
# 2) 계산 결과를 print가 아니라 return
    return total
# 3) 호출 결과를 변수에 담기
summing_function = summing(35.0, 50)
print(summing_function)
# 4) 담은 값을 다음 계산, 출력에 이어 쓰기
print(summing_function + 5)

