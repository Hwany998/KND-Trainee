# =====================================================================
# 종합 실습 1. 설비 종합 모니터링 리포트
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
# (설비명, 온도, 진동)
# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험"
#   온도 >= 80 또는 진동 >= 3.0 > "주의"
#   그 외                      > "정상"

# TODO 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력 (for + enumerate + if/elif/else)
# for문으로 sensors 튜플 나열, if문 조건으로 상태 판정, enumerate로 번호 붙이기
# TODO 2. 위해 빈 리스트 변수 생성 후, 조건에 맞도록 추가
print("=" * 40)
print("\t설비 종합 모니터링 리포트")
print("=" * 40)
danger_sensors = []
error_sensors = []
normal_sensors = []
for idx, (name, value, x) in enumerate(sensors):
    if value > 90 or x > 5.0:
        print(f'{idx}. {name} | 온도 {value}℃ | 진동 {x}mm/s | 위험 ⛔️')
        danger_sensors.append(name)
    elif value >= 80 or x >= 3.0:
        print(f'{idx}. {name} | 온도 {value}℃ | 진동 {x}mm/s | 주의 ❌')
        error_sensors.append(name)
    else:
        print(f'{idx}. {name} | 온도 {value}℃ | 진동 {x}mm/s | 정상 ✅')
        normal_sensors.append(name)

# TODO 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 (누적변수)
# 상태에 따른 갯수를 변수에 저장해서 f-string으로 출력
print("-" * 40)
print(f'총 설비: {len(sensors)}대\n정상: {len(normal_sensors)} / 주의: {len(error_sensors)} / 위험: {len(danger_sensors)}')

# TODO 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)
print(f'이상 설비 비율: {round(((len(error_sensors)+len(danger_sensors)) / (len(normal_sensors)+len(error_sensors)+len(danger_sensors))*100),1)}%')

# TODO 4. 전체 평균 온도 출력 (round)
total_temps = 0
for idx, (name, value, x) in enumerate(sensors):
    total_temps += value
print(f'평균 온도: {round((total_temps / len(sensors)), 1)}℃')

# TODO 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)
max_value = 0
max_name = ""
for idx, (name, value, x) in enumerate(sensors):
    if(value > max_value):
        max_name = name
        max_value = value
print(f"최고 온도 설비: {max_name} ({max_value}℃)")

# TODO 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())
danger2_sensors = []
for idx, (name, value, x) in enumerate(sensors):
    if value > 90 or x > 5.0:
        danger2_sensors.append(name)
print(f'위험 설비 목록: {sorted(danger_sensors)}')
print("=" * 40)

# 도전) 위험 1대라도 있으면 "⚠ 즉시 점검 요망", 없으면 "✅ 전 설비 안정"
if(len(danger2_sensors) >= 1):
    print("⚠ 즉시 점검 요망")
else:
    print("✅ 전 설비 안정")