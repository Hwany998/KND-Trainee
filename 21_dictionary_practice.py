#실습1. 딕셔너리 만들고 다루기
print("="*40)
#1) 센서명을 키(key), 측정값을 값(value)로 하는 딕셔너리 저장
sensor = {
    "모터온도": 78,
    "진동": 0.5,
    }
# 2) 키로 값을 꺼내고 새 키로 추가, 기존 키로 수정
print(sensor["진동"])           #값 꺼내기
print(sensor.get("진동", 0))    #값 더 안전히 꺼내기

sensor["압력"] = 95          #없던 키 언급하면 추가
sensor["진동"] = 0.3         #있던 키를 언급하면 수정

print(sensor)

#3) get으로 없는 키를 기본값으로 조회, in으로 키 존재 확인
print(sensor.get("면적", -1))   #면적 key는 존재하지 않아 -1로 대체
print("진동" in sensor)         #존재key
print("면적" in sensor)         #존재않는 key

#실습2. update로 여러 값 한 번에 갱신
print("="*40)
#1) 센서, 새 데이터 딕셔너리 각각 저장
sensors = {
    "모터온도": 78,
    "진동": 0.5,
    "압력": 90
}
new_data = {
    "모터온도": 80,
    "진동": 0.3,
    "습도": 30
}
#2) update로 새 데이터 한 번에 반영(수정 or 추가)
sensors.update(new_data)   #update로 딕셔너리 값 업데이트 가능
print(sensors)

#3) del로 특정 키 삭제하고 len 개수 확인
del sensors["진동"]                     #"진동" 삭제
print(f'센서 수: {len(sensors)}')        #센서 수: 3

#실습3. 딕셔너리로 통계
print("="*40)
#1) 센서명, 측정값 딕셔너리 저장
sensors2 = {
    "모터온도": 80,
    "진동": 0.3,
    "습도": 30
}
#2) values의 합을 개수로 나눠 평균 구하기
print(f'평균: {round(sum(sensors2.values()) / len(sensors2),1)}')

#3) items로 순회하며 가장 큰 값과 그 센서명을 찾아 출력
max_value = 0
for name, value in sensors2.items():
    if max_value < value:
        max_value = value
        max_name = name
print(f'최댓값 센서: {max_name} {max_value}')

#실습4. zip으로 센서명-값 매핑
print("="*40)
#1) 센서명 리스트와 측정값 리스트 저장
sensor_names = ["온도", "진동", "압력"]
sensor_values = [78, 0.5, 95]

#2) zip으로 두 리스트 묶어 dict로 변환
sensors3 = dict(zip(sensor_names, sensor_values))
print(sensors3)

#3) items로 순회하며 이름-값 쌍 출력
for name, value in sensors3.items():
    print(f"이름: {name} - 값: {value}")

#실습5. 임계값으로 경고 센서 분류하기
print("="*40)
#1) 측정값 딕셔너리와 임계값 딕셔너리를 각각 저장
sensors5 = {
    "1번펌프": 32,
    "2번펌프": 40,
    "3번펌프": 36
}
sensor_limits = {
    "1번펌프": 34,
    "2번펌프": 44,
    "3번펌프": 33
}

#2 items로 순회하며 각 센서값 같은 이름의 임계값을 넘는지 비교
over_list = []
for name, value in sensors5.items():
    if value > sensor_limits.get(name,0):
        over_list.append(name)
#3 넘는 센서 이름을 빈 리스트에 모아 출력
print(over_list)

#실습6: 중첩 딕셔너리로 설비 관리
print("="*40)
#1) 설비명을 키로, 각 설비 정보(딕셔너리)를 값으로하는 중첩 딕셔너리 저장
sensors4 = {
    "1번펌프":{
        "온도": 32,
        "상태": "안정"
    },
    "2번펌프":{
        "온도": 95,
        "상태": "경고"
    }
}

#2) 중첩 키로 특정 설비 특정 값 꺼내기
print(sensors4["2번펌프"]["온도"])   #95

#3) items 순회로 상태가 "경고"인 설비만 찾아 출력
for name, value in sensors4.items():
    if value["상태"] == "경고":
        print(f'{name} 점검 필요')

#실습7. 표 데이터를 딕셔너리로 변환하기
print("="*40)
#1) 한 줄 "센서명, 측정값" 형태 행 문자열 리스트 저장
double_list = [
    "1번센서, 80",
    "2번센서, 75",
    "3번센서, 85",
    "4번센서, 65"
]
new_dic={}
#2) for로 각 행 쉼표로 split해 이름과 값 나누기
slice_list = []
slice_name = []
slice_value = []
for idx, i in enumerate(double_list):
    slice_list.append(i.split(", "))
    new_dic[slice_list[idx][0]] = int(slice_list[idx][1])

#3) 이름을 키, 값을 숫자로 바꿔 딕셔너리에 추가
print(new_dic)

#실습8. 센서 데이터 통합 정리
print("="*40)
#1) 센서 측정값 딕셔너리와 임계값 딕셔너리 저장
sensors6 = {
    "진동":40,
    "강도":60,
    "압력":80,
    "온도":90
}
sensors6_limit = {
    "진동":30,
    "강도":70,
    "압력":70,
    "온도":100
}

#2) values로 전체 평균 구하기
print(round(sum(sensors6.values()) / len(sensors6), 1))

#3) items 순회로 임계값 초과 센서를 셋에 모으기
sensors6_set = set()
for name, value in sensors6.items():
    if value > sensors6_limit[name]:
        sensors6_set.add(name)

#4) 셋을 정렬해 출력
print(sorted(sensors6_set))