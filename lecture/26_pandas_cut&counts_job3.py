# 실습 3. 구간으로 묶어 세기
# pd.cut으로 수치형 값을 구간으로 묶어 빈도 세기
# 수치형 센서 값을 구간으로 나눠 분포 확인

# 진동 열(컬럼)의 최솟값과 최댓값으로 값의 범위 확인
import pandas as pd

df = pd.read_csv('csv/14_hydraulic.csv', encoding='utf-8')
df.info()
print(df.head(3)) # 0.577 ~ 0.640 ?
print(df['진동'].max()) # 0.779
print(df['진동'].min()) # 0.530

# pd.cut으로 경계와 이름표를 정해 세 구간으로 묶기
band = pd.cut(df['진동'], bins = [0.0, 0.4, 0.7, 10.0], labels = ['약함', '보통', '강함'])

# 묶은 구간에 value_counts로 구간별 빈도 세기
print(band.value_counts())

# round로 소수점 셋째자리까지 출력
print(band.value_counts(normalize=True).round(3))
# 구간 기준값을 0.6 -> 0.4로 변경하여 보통 값이 43에서 늘어남