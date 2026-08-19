#실습4
import pandas as pd

df = pd.read_csv('csv/14_hydraulic.csv', encoding='utf-8')
df.info()

# 압력별 그룹으로 평균 
print(df.groupby('냉각기상태')['압력'].mean().round(2))

# 최고 압력 확인
print(df.groupby('밸브상태')['압력'].max())

# size로 측정 건수 확인
print(df.groupby('압력').size())

#실습5
df = pd.read_csv('csv/14_hydraulic.csv', encoding='utf-8')
df.info()

# 진동별 그룹으로 평균
print(df.groupby(['벨브상태'])['진동'].mean().round(2))

# 최고 압력 확인
print(df.groupby('밸브상태')['진동'].max())

# size로 측정 건수 확인
print(df.groupby('냉각기상태').size())