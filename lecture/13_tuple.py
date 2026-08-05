tup = (
    "normal",
    "normal", 
    "warning", 
    "normal",
    "warning"
)
print(len(tup)) #5
print(tup.count("warning")) #2  warning 2개 - 없는 값 찾으면 0
print(tup.index("warning")) #2  첫 위치, 2번 인덱스 - 없는 값 찾으면 오류
#count와 index의 차이, 없는 값 찾을 시 count는 0, index는 오류

sensors = [("모터온도", 78), ("펌프압력", 95)]
for name, value in sensors:
    if value > 90:
        print(name, "경고")

now = 0
hour_13 = [
    ("모터온도", 77), 
    ("모터진동", 0.2), 
    ("모터압력", 91)
]
for name, value in hour_13:
    now += 1
    print(now, "번째 반복")
    print("name:", name, "value:", value)

temps_13 = [
    ("qox_001", 81),
    ("qox_002", 88),
    ("qox_003", 95),
    ("qox_004", 89),
]
warning = 90
for name, temp in temps_13:
    if temp >= warning:
        print("경고", name, "설비 온도 이상")

#리스트 안 튜플 갯수 늘어나면 for문에서 변수를 여러 개 작성
tup_list = [
    ("일", "one", 1, "1"),
    ("이", "two", 2, "2")
]
#for문에서도 언패킹할 때는 무조건 튜플의 값 개수와 for문의 변수 갯수 통일 (아니면 오류 발생)
for kor_str, eng_str, num, num_str in tup_list:
    print(
        "kor_str:", kor_str, 
        "eng_str", eng_str, 
        "num:", num, 
        "num_str:", num_str
    )
#============================
#튜플 리스트 정렬, sorted()를 통하여 튜플 특정 값 기준으로 리스트 정렬
hot = sorted(temps_13, reverse=True)
print(hot)

#실습1 센서를 튜플로 묶고 꺼내기
motor_temp = ("모터온도", 78)
name, value = motor_temp
print(motor_temp[0], motor_temp[1])
print(f"{name}, {value}")

#실습2 튜플 리스트 반복 처리
status = [
    ("초당회전", 91),
    ("접지온도", 88),
    ("압력", 92)
]
for i, j in status:
    print(i, j)
    if(j > 90):
        print(i, "경고")

#실습3. 중첩 튜플로 센서 위치 관리
sensors2 = [
    ("압력기", 4, (2, 5)),
    ("덮개", 3, (6, 3)),
    ("회전날", 4, (5, 3)),
    ("안전밧줄", 2, (3, 1)),
]
for c, d, e in sensors2:
    x, y = e
    print(c, "위치:", x, y)
for c, d, e in sensors2:
    x, y = e
    if x <= 5:
        print(c, "1구역")

# 리스트를 set으로 감싸면 중복 제거, 순서 없음(인덱스 못씀)
# 빈 셋은 함수를 생성한다. set()
list_ = []  #빈 리스트
tuple_ = ()    #빈 튜플