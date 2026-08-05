# 인삿말 출력 함수 간단 버전
def say_hello_kjh():
    print("안녕, 제환")

def say_hello_sonny():
    print("안녕, 소니")

def say_hi(name):
    print(f"안녕, {name}")

say_hi("제환")

# 예제코드: 특정 장비 이름 알려주면 해당 장비 체크 시작 알림
def check(machine):
    print(f"{machine} 점검 시작")

check("펌프A")

# 매개변수 2개 이상 예제 - 덧셈
def calc_sum(num1, num2):
    #num1 = 1
    #num2 = 2
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")

calc_sum(20, 30)

# 매개변수 2개 이상 예제 - 장비 이름과 온도 정보 출력
def report(name, temp):
    print(f"{name}의 온도: {temp}")

report("펌프A", 85)
report("압축기B", 70)
# 매개변수가 부족하거나 넘치면 TypeError 발생

# 키워드 인자
def report_keyboard(name, temp):
    print(f"{name}의 온도: {temp}")

# 키워드 인자 없이 호출
report_keyboard("펌프A", 78)

# 키워드 인자 사용 호출
report_keyboard(name = "펌프A", temp = 78)
report_keyboard(temp = 78, name = "펌프A")  # 키워드 인자 사용하면 위치 바뀌어도 정상 작동

# =============================
# 반환값

def add(a, b):
    total = a + b
    return total    # 반환을 통해 출력으로 반환 가능

print(add(1, 2))
print(add(1, 2) + 1)
#만약 여러번 같은 결과 호출해야한다면 변수에 담아 사용 추천
result = add(1, 2)
print(result + 1)

# 평균 내는 함수 제작
def calc_average(a, b):
    return (a + b) / 2

avg = calc_average(75.3, 69.7)
print(f'평균온도: {avg}')

# 여러 값 한 번에 반환
# 다음 함수는 배열을 받아 그 안의 최소값, 최대값 동시 반환
def calc_min_max(values):
    minimum = min(values)
    maximum = max(values)
    return minimum, maximum

target_list = [1,2,3,4,5]
result = calc_min_max(target_list)
print(result)   # (1, 5)

# 반환값 언패킹
# 함수 결과 받는 순간 결과 튜플 내용 풀어서 개별 변수에 담아 사용
result_min, result_max = calc_min_max(target_list)
print("최소값", str(result_min))
print("최대값", str(result_max))

# return 반환값 없는 함수 호출
# 결과를 어디에 담겠다면 담기는 값은 None이 된다.

# 실습5 (선택)
# 내장 함수 min(), max(), sum(), len() 활용