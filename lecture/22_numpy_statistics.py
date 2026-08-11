import numpy as np

#합계(sum)과 평균(mean)
s = np.array([70,71,72,90,73])
print(s.sum())
print(s.mean())
#평균 약점: 유난히 크거나 작은값(이상치)에 휘둘림
#대부분 70~73인데 90하나로 평균이 75.2
#스토브리그中 백승수 단장曰: (마이클 조던 예시를 들며) 평균의 함정에 속지맙시다.
print(np.median(s))   #중앙값 72.0

print(s.max())
print(s.min())
print(s.max() - s.min()) # 범위25

print("=" * 40)

#분산
stable = np.array([70,71,71,73,72])
unstable = np.array([60,80,65,95,70])
print(stable.var())     #1.04
print(unstable.var())   #154.0

print("=" * 40)

#표준편차
s2 = np.array([70, 72, 71, 95, 73])

print(round(s2.var(),2)) #분산 89.36
print(round(s2.std(),2)) #표준편차 9.45

print("=" * 40)

#axis 개념 (형과 열의 방향)
mat = np.array([
    [70, 2.1],
    [72, 2.3]
])
print(mat.mean())   # 36.6
print(mat.mean(axis = 0))   # [71. 2.2] 70과 72의 평균 / 2.1과 2.3의 평균
print(mat.mean(axis = 1))   # [36.05. 37.15] 70과 72의 평균 / 2.1과 2.3의 평균

print("=" * 40)

#실습6 센서별 기초 통계 구하기
#표 모양 데이터에서 센서별(열별) 통계 계산
#axis(축) 옵션 문제
data3 = np.array([[1520, 42.1], [1400, 46.1], [1498, 49.2], [2800, 4.6]])
print(data3)

#여러 설비의 회전수 토크 이차원 배열 준비
#axis를 열 방향으로 지정해 센서별 평균 계산
print(data3.mean())
print(data3.mean(axis = 0))
print(data3.mean(axis = 1))
print(np.round(data3.std(axis = 0),2))
#센서별 표준편차 계산

#예상결과
#회전수 토크 각각의 평균과 표준편차가 출력

print("=" * 40)

#실습7. 파일 데이터로 기초 통계 구하기
#파일로 저장된 공정 데이터를 불러와 기초 통계 계산

#np.loadtxt로 회전수 열을 파일에서 불러오기
rp4 = np.loadtxt('practice/22_mct_tool.csv', delimiter = ',', skiprows = 1, usecols = 4)

#불러온 배열의 평균과 표준편차 계산
print(round(rp4.mean(),1))  #4212.6
print(round(rp4.std(),1))  #4212.6

#최소값과 최대값으로 갑의 범위 확인
print(rp4.min(), rp4.max())
print(rp4.max() - rp4.min())

#예상결과
#회전의 평균, 표준편차와 최솟값, 최댓값이 출력

print("=" * 40)

#실습8. 필터링과 통계 결합하기
#조건으로 값을 골라낸 뒤 그 값들의 통계 계산

#토크 배열 준비
torque8 = np.array([42.8, 46.1, 48.8, 63.9, 55.1, 41.1, 3.2, 40.3])

#불리언 인덱싱으로 기준을 넘는 값만 추출
high8 = torque8[torque8 > 50]
print(high8)    # [63.9 55.1]

#추출한 값들의 평균과 개수 계산
print(round(high8.mean(),1))

print("=" * 40)

#실습9. numpy 기초 종합 분석
#데이터 불러오기, 구조확인, 필터링, 통계를 하나의 흐름으로 수행
#np.loadtxt로 회전수와 토크 두 열 불러오기
data9 = np.loadtxt('practice/22_mct_tool.csv', delimiter = ",", skiprows=2, usecols=(4,5))
print(data9)

#shapedhk dtype으로 구조 확인
print(data9.shape, data9.dtype) # (40, 2) float64

#회전수가 기준 아래로 떨어진 이상 시점을 필터링해 개수와 평균 계산
rp9 = data9[:, 0]
print(rp9)
anomaly = rp9[rp9 < 1000]
print(anomaly)  # [58.]
print(anomaly.size, round(anomaly.mean(), 1))