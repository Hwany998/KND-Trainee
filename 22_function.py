first_name = "KIM"
last_name = "JEWHAN"

print(first_name)
print(last_name)
print(first_name + last_name)
print(f"성명: {first_name}{last_name}")

# 함수를 직접 만들어보며 익히도록하자!
# 내장함수와 사용자정의 함수를 익히자!

# 에러의 종류
# runtime error - 작동 중단
# 논리 오류 - 작동은 되는데, 결과적 문제가 있어 해결해야함
# 우리는 함수 이름에 걸맞는 동작만 잘 만들면 됨

# 간단 인사 메세지 함수 만들기 (def 활용)
def hello():
    print("안녕하세요")     # 이대로는 발동 안됨. 자판기만 만들어놓고 호출하지 않았기 때문

# 위에서 만든 함수 호출
print(hello)            # 논리 오류 - <function hello at 위치> 기능이 아닌 함수의 위치를 불러옴
hello()                 # 이렇게 해야 제대로 함수를 발동

# 함수 안에서 벌어질 일들 제작
def show_age():
    my_age = 29
    print(my_age)

# 함수 실행
show_age()
# my_age 재할당 후 함수 실행

my_age = 30
show_age()  # 그래도 기존 함수의 29가 출력 / 함수 안 my_age와 밖의 my_age는 다른 존재이기 때문

# 함수 안의 my_age 데이터가 영향 끼치는 범위를 전문용어 'scope'라고 부른다

# 실습1: 답안
def start_Checking():
    print("점검 시작")

start_Checking()

# 함수가 호출되면 그 안의 코드는 매번 새롭게 시작
def show_count():
    count = 2           # 해당 줄의 count 변수 없으면 함수 오류 발생
    count = count + 1
    print(count)
    # 함수가 종료되면 count 포함한 이 함수 안의 데이터 모두 사라짐

show_count()

# 각 함수의 이름은 이름에 걸맞는 역할을 해야만 한다.
def show_students():
    print("학생1: 짱구")
    print("학생2: 철수")
    print("학생3: 맹구")
    #print("선생님: 채송아")     # 학생 관련 함수인데 선생님이 들어가니 부조화

def show_teachers():
    print("선생님1: 채송아")
    print("선생님2: 나미리")

def show_class():           # 함수 2개를 바로 호출하는 함수 저장
    show_students()
    show_teachers()

show_students()
show_teachers()
show_class()

print("-" * 40)
# 코드 중복과 함수화 / 밑의 print 문들이 여럿 사용되어야한다면 함수화로 진행
print("압축기A 온도 확인 중")
print("결과 기록")
print("펌프1 온도 확인")
print("결과 기록")

def start_check():
    print("점검 시작")
    print("안전 장비 확인 요함")
    print("기록 준비")

start_check()

# 함수로 설비 점검 자동화
# 구분선과 점검 안내 2줄이 선비마다 반복 출력
# 1. 구분선 출력 함수 정의
# 2. 점검 안내 여러 줄 출력하는 함수 정의
# 3. 두 함수를 설비마다 순서대로 호출
# 4. 실행해 각 설비마다 같은 안내 반복 확인
# 예상결과: 구분선과 점검 안내 2줄이 설비마다 반복 출력
def print_line():
    print("=" * 40)

def print_check():
    print("점검 안내")
    print("기록 준비")

# 장비1에 대한 함수 호출
print_line()
print_check()

# 장비2에 대한 함수 호출
print_line()
print_check()