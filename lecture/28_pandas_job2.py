import pandas as pd

df = pd.read_csv('csv/15_01_사출성형_공정.csv', encoding='utf-8')

# 실습 2. SECOM 첫 탐색 (사출성형_공정.csv)
# head·shape·info·describe로 결측 분위기 파악
# 처음 받은 데이터의 구조와 결측 분위기 파악
print(df.head())
print(df.shape) # (250, 22)
df.info()

print(df.describe())
# [8 rows x 21 columns]