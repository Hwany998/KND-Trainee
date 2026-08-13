#실습1. head, tail로 디지털 신호 살펴보기
import pandas as pd

df_digital = pd.read_csv('csv/12_metro_digital.csv')

#위 코드가 정상 실행되어 shape가 나오는지 부터 확인하고
#적절한 숫자들이 줄을 정해 head(),tail()을 출력
print(df_digital.shape)    # (120, 4)
print(df_digital.head(3))   # 맨 위 3줄
print(df_digital.tail(5))   # 맨 아래 5줄

#head와 tail 출력에서 NaN 위치가 보이는지도 확인

#12_metro_small.csv 파일도 같은 확인
df_small = pd.read_csv('csv/12_metro_small.csv')
print(df_small.shape)    # (30, 7)
print(df_small.head(3))   # 맨 위 3줄
print(df_small.tail(5))   # 맨 아래 5줄
print("=" * 40,'\n')

#실습2의 head, tail 행 개수 조절도 진행
df_metro_compressor = pd.read_csv('csv/12_metro_compressor.csv')
print(df_metro_compressor.head(1))   # 맨 위 1줄
print(df_metro_compressor.head(10))   # 맨 위 10줄
print(df_metro_compressor.tail(7))   # 맨 아래 5줄
print(df_metro_compressor.tail(500))   # 맨 아래 500줄

print("=" * 40,'\n')

#실습3. shape, columns, dtypes로 데이터 뼈대 읽기
#12_metro_digital.csv 읽어봐서 DataFrame에 담기
#.columns 출력 df.columns.tolist()도 출력
#DF의 .dtypes 출력
df_metro_compressor2 = pd.read_csv('csv/12_metro_compressor.csv')
print(df_metro_compressor2.shape)   # 
print(df_metro_compressor2.columns) # str, float64 * 5, str
print(df_metro_compressor2.dtypes)  # object

print("=" * 40,'\n')

#실습4 열 이름, 자료형 점검
df_metro_compressor3 = pd.read_csv('csv/12_metro_compressor.csv')
print(df_metro_compressor3.dtypes)

print("=" * 40,'\n')

#실습5. .info()로 데이터 건강검진
#.info()를 통해 전체 구조 행수, 열수, 열이름 한 번에 보기 가능
# 12_metro_digital.csv 파일을 읽어서 DF 생성
# DF의 info() 호출 출력
df_metro_compressor4 = pd.read_csv('csv/12_metro_compressor.csv')
df_metro_compressor4.info()

#실습6 describe로 이상 신호 찾기
df_metro_compressor5 = pd.read_csv('csv/12_metro_compressor.csv')

print(df_metro_compressor["오일온도"].describe())