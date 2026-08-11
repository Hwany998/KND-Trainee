#배열의 산수 연산
#두 배열을 같은 위치끼리 한 번에 계산
import numpy as np
x = np.array([1,2,3])
y = np.array([10,20,30])
print(x+y)  #[11 12 13]
print(x*2)  #[2 4 6]
print(x*y)  #[10 40 90]
#같은 위치 값끼리 계산하며 두 배열의 사이즈(항목갯수)가 같아야함
print("=" * 40)

#스칼라 연산
#배열 크기 무관하게
celsius = np.array([20.0, 25.0, 30.0])
f = celsius * 1.8 +32
print(f)    #[68. 77. 86.]
print("=" * 40)

#브로드캐스팅
#한 줄짜리 기준값이 모든 행에 퍼져 계산
table = np.array([
    [72, 2.3],
    [95, 6.8]
])
base = np.array([70, 2.0])
print(table - base)
#모든 위치로 퍼짐
print("=" * 40)

#벡터 연산
#회전수 측정 배열 준비
rpm = np.array([1551, 1408, 1498, 1433, 1425, 2861])
#최솟값과 최댓값을 min, max로 확인
print(rpm.min())    # 1408
print(rpm.max())    # 2861
print("=" * 40)

#실습3의 예제 코드
#정규화 공식을 브로드캐스팅으로 적용해 변환
#정규화 공식: 정규화된X = (비교대상 - 최소값) / (최대값 - 최소값)
rpm_min = rpm.min()
rpm_max = rpm.max()
normalized = (rpm - rpm_min) / (rpm_max - rpm_min)
print(normalized)
print(np.round(normalized,2))

v = np.array([70, 95, 71, 88, 73])
print(v > 85)   #[False True False True False]

print("=" * 40)

#Boolean indexing
#불리언 배열로 조건에 맞는 값만 골라내기
#조건 맞는 값만 남기며 결과 크기 작아짐
print(v[v>85])  # [95 88]

#np.where
#조건 따라 값을 둘 중 하나로 바꾸기
# - 조건/참/거짓 ... 세 가지 인자
#조건이 참이면 1(위험)
#거짓이면 0(정상)
#모든 값 유지하고 바꿈, 결과 크기 그대로
print(np.where(v>85,1,0))   # [0 1 0 1 0]
print("=" * 40)

#다중 조건 결합
print(v) # [70 95 71 88 73]
v_step1 = v[v > 70]
print(v_step1)  # [95 71 88 73]
v_step2 = v_step1[v_step1 < 90]
print(v_step2)  # [71 88 73]

#조건을 괄호를 묶기, &와 같은 기호로 다중 조건에 대한 기호 
v_mixed = v[(v > 70) & (v < 90)] #이게 다중 조건 결합
print(v_mixed)  # [71 88 73]

# 참고, 조건 대신 true를 직접 준다면?
print(v[True])  # [70 95 71 88 73] 값이 있으면 그냥 다 True

print("=" * 40)
#실습4의 예제 코드
#조건 맞는 이상 센서값만 불리언 인덱싱으로 선별
#회전수와 토크 배열 준비
#비교 연산으로 회전수가 기준을 넘는 조건 생성
#다중 조건으로 회전수 과다 또는 토크 과소 위험 시점 필터링
rpm2 = np.array([1560, 1321, 1118, 1383, 1225, 2561])
torque2 = np.array([42.8, 39.9, 45.7, 33.9, 30.1, 8.8])
print(rpm2[rpm2 > 2000])    #[2561]
print((rpm2 > 2000) | (torque2 < 10))   #[False False False False False True]

print("=" * 40)

#실습5. 조건별 개수와 비율 세기
#조건을 만족하는 값의 개수와 전체 대비 비율 계산

# 토크 배열 준비
torque3 = np.array([39.8, 23.9, 50.1, 22.2, 8.1, 60.7, 57.7, 80.1])
# 비교 조건으로 참거짓 불리언 배열 생성
high5 = torque3 > 50
print(high5)                    #이런 식으로 하면 불리언 값 및 개수 유지
print(torque3[torque3 > 50])    #이런 식으로 하면 값을 출력
# 불리언 배열의 합 개수, 평균으로 비율 계산
print(sum(high5))
print(sum(high5) / len(high5))
# 예상 결과
# 조건을 만족하는 값의 개수와 비율 출력