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

#끝나면 실습2의 head, tail 행 개수 조절도 진행
