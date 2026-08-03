# 변수명은 _언더바 표현 방식 snake case로 설명
# 리스트로 크루 여러분의 이름을 나열
data_class_list = ["태구", "수진", "영준"]

# 딕셔너리로 정확한 역할까지 부여하여 나열
data_class_dict = {"반장":"태구", 
                   "부반장":"수진", 
                   "당번":"영준"}

# 센서로부터 얻는 예시 데이터로 딕셔너리 제작
sensors = {"센서이름":"보일러","모터온도": 78, "진동": 0.5}

print(sensors)
print(type(sensors))    #딕셔너리 타입 확인
empty_dict = {}         #빈 딕셔너리 생성   <class 'set'>을 원하면 empty_set = set() 해야함
print(empty_dict)       #<class 'dict'>
# 딕셔너리에서 특정 키의 값만 출력
print(sensors["센서이름"])
print(sensors["모터온도"])
print(sensors["진동"])

sensors["센서이름"] = "펌프"    #센서이름 값을 펌프로 변경
sensors["펌프압력"] = 95       #딕셔너리에 펌프압력이라는 키를 새로 추가하고 값 95를 넣음

del sensors["펌프압력"]        #sensors의 펌프압력 키와 값 삭제 del문
print(sensors)

print(sensors.get("센서이름"))    #센서이름 키의 값 출력
print(sensors.get("펌프압력"))    #del로 삭제한 펌프압력 키의 값 출력, None 출력

motor_degree = sensors.get("모터온도")    #모터온도 키의 값 출력
#next_degree = motor_degree + 10 #숫자 아닌 것에 +10해서 오류 예정
print(motor_degree)              #78 출력
#print(next_degree)              #안좋은 사례 error발생

#in으로 키 존재 확인하기 // get은 안전하게 꺼낼 때, in은 존재만 확인
is_motor_degree_key = "센서이름" in sensors
print(is_motor_degree_key)    #True 출력

#2가지 방법
if is_motor_degree_key:
    print("센서이름 키 존재함")
else:
    print("센서이름 키 존재하지 않음")

if "센서이름" in sensors:
    print("센서이름 키 존재함")

#dictionary 키 되는 것 문자열, 숫자, 튜플 / 리스트는 불가함.
#keys, values로 키, 값만 꺼내기
print(sensors.keys())   #dict_keys(['센서이름', '모터온도', '진동'])
print(sensors.values()) #dict_values([펌프, 78, 0.5])
print(len(sensors))     #3 키 길이
#items는 키,값 짝으로 함께 꺼내 반복문에서 가장 많이 사용
for key, value in sensors.items():  #sensors마 하면 error뜸
    print(key, value)

#사례로 배우는 실습
#유럽: 스페인, 프랑스, 독일, 스위스, 네덜란드
#아시아: 한국, 일본, 중국, 사우디, 이란
#남미: 아르헨티나, 브라질, 칠레. 콜롬비아, 우루과이

korea = {"국가명:대한민국", "약칭:KOR"}
japan = {"국가명:일본", "약칭:JPN"}

asia = [ 
    {"국가명":"korea","약칭":"KOR"},
    {"국가명":"japan","약칭":"JPN"}]
print(asia)

for country in asia:
    print(country.get("국가명", "없음"))

#포멧몬 1,2,3단계 진화형태를 딕셔너리 제작
#배열 데이터를 화면에 print
#가능하면 그 배열 데이터들을 for-in 사용해서 하나씩 꺼내 print합니다 (선택)
data_pokemon_dict = {}

dict_pokemon_1 = {
    "진화 1단계": "이상해씨",
    "진화 2단계": "이상해풀",
    "진화 3단계": "이상해꽃",
}
dict_pokemon_2 = {
    "진화 1단계": "파이리",
    "진화 2단계": "리자드",
    "진화 3단계": "리자몽",
}
dict_pokemon_3 = {
    "진화 1단계": "꼬부기",
    "진화 2단계": "어니부기",
    "진화 3단계": "거북왕",
}
dict_pokemon_4 = {
    "진화 1단계": "브케인",
    "진화 2단계": "마그케인",
    "진화 3단계": "블레이범",
}
dict_pokemon_5 = {
    "진화 1단계": "캐터피",
    "진화 2단계": "단데기",
    "진화 3단계": "버터플",
}
dict_pokemon_6 = {
    "진화 1단계": "뿔충이",
    "진화 2단계": "딱충이",
    "진화 3단계": "독침붕",
}
dict_pokemon_7 = {
    "진화 1단계": "구구",
    "진화 2단계": "피죤",
    "진화 3단계": "피죤투",
}
dict_pokemon_8 = {
    "진화 1단계": "피츄",
    "진화 2단계": "피카츄",
    "진화 3단계": "라이츄",
}
dict_pokemon_9 = {
    "진화 1단계": "삐",
    "진화 2단계": "삐삐",
    "진화 3단계": "픽시",
}
dict_pokemon_10 = {
    "진화 1단계": "알통몬",
    "진화 2단계": "근육몬",
    "진화 3단계": "괴력몬",
}

pokemon_list = [
    dict_pokemon_1,
    dict_pokemon_2,
    dict_pokemon_3,
    dict_pokemon_4,
    dict_pokemon_5,
    dict_pokemon_6,
    dict_pokemon_7,
    dict_pokemon_8,
    dict_pokemon_9,
    dict_pokemon_10,
]

print(pokemon_list)

for pokemon in pokemon_list:
    first, second, third = pokemon.values()
    print(f"1단계: {first}, 2단계: {second}, 3단계: {third}")

#다음 두 딕셔너리는 같은 key들을 가지고 있다.
values = {"모터온도": 95, "압력": 88} # "진동": 0.5}
#임계치
limits = {"모터온도": 90, "압력": 90}   #여긴 진동값이 없어서 오류가 발생함

# for name, value in values.items():
#     print(f"{name} 값: {value}")
    
#     if values > limits:
#         print(name, "경고")

sensors = {"모터온도": 95, "압력": 88, "진동": 0.5}
new_data = {"모터온도": 90, "압력": 90, "진동": 0.5}
sensors.update(new_data)   #update로 딕셔너리 값 업데이트 가능
print(sensors)

#zip으로 두 리스트를 딕셔너리로 묶기
#dict(zip(이름,값))
name = ["모터온도", "압력", "진동"]
values = [95, 88, 0.5]
sensors = dict(zip(name,values)) #앞에서 순서대로 dict로 만들어줌

#딕셔너리 안에 리스트, 튜플 담기
my_classroom = {
    "학년":3,
    "반":1,
    "반장": "홍길동",
    "부반장": ["고길동", "둘리"]
}
my_school = {
     "학년":3,
    "반":1,
    "반장": "메시",
    "부반장": ["데폴", "라우타로"]
},
{
     "학년":3,
    "반":2,
    "반장": "손흥민",
    "부반장": ["김민재", "이재성"]
},
{
     "학년":3,
    "반":1,
    "반장": "호날두",
    "부반장": ["루니", "박지성"]
}

#딕셔너리 안에 value로 딕셔너리를 사용
kbo = {
    "삼성": {
        "마스코트": "라이온스",
        "구장": {
            "1구장": "대구라이온스파크",
            "2구장": "포항야구장"
        },
    },
    "두산": {
        "마스코트": "베어스",
        "구장": {
            "1구장": "잠실야구장",
            "2구장": "베어스파크"
        }
    }
}

#쉽게 배열 안에 딕셔너리 안에 딕셔너리 접근
print(kbo[0]["구장"]["2구장"])