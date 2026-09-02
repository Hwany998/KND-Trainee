import pandas as pd

tags = pd.read_csv('csv/03-01_회전기계_신호_회전기계태그목록.csv')
df = pd.read_csv('csv/03-01_회전기계_신호_진동추세.csv')

#1번 모터에 대한 태그 목록
#tag,indicator,summary,unit,direction
print(tags.loc[tags['equipment'] == '1번 모터', ['tag','indicator','summary','unit','direction']])
'''
     tag          indicator summary  unit  direction
0    MTR01_VIB_H        속도     RMS  mm/s        수평
1    MTR01_VIB_V        속도     RMS  mm/s        수직
2    MTR01_VIB_A        속도     RMS  mm/s       축방향
3  MTR01_VIB_ACC       가속도    PEAK     g        수평
4  MTR01_CURRENT        전류     순시값    A      해당없음
5     MTR01_TEMP        온도     순시값  degC     해당없음
6      MTR01_RPM       회전수     순시값  rpm      해당없음
(.venv) gimjehwan@gimjehwan-ui-MacBookPro KND-Trainee % 
'''

#진동 정상 범위 정하기
#맨 앞 기준으로 20일 구간을 정상 기간으로 볼 것
MTR = ['MTR01_VIB_H','MTR01_VIB_V','MTR01_VIB_A','MTR01_VIB_ACC']
normalM = df.head(20)

print(normalM[MTR].agg(['min', 'max']))

#펌프 극단값 출력해보기
PMP = ['PMP01_VIB_H','PMP01_VIB_V','PMP01_VIB_A','PMP01_VIB_ACC']
normalP = df.head(20)

print(normalP[PMP].agg(['min', 'max']))
'''
     MTR01_VIB_H  MTR01_VIB_V  MTR01_VIB_A  MTR01_VIB_ACC
min          1.7          1.3          0.7           0.51
max          2.1          1.6          0.8           0.56
     PMP01_VIB_H  PMP01_VIB_V  PMP01_VIB_A  PMP01_VIB_ACC
min          2.0          1.6          0.9           0.60
max          2.2          1.7          1.0           0.63
'''

def first_over(col):
    #정상 구간 최댓값을 처음 넘어선 행의 순서 반환
    limit = normalP[col].max()
    over = df.index[df[col]>limit]
    #print(over)
    #print(over[0]) #38
    return int(over[0]) + 1 if len(over) else None

print('=' * 40)

print(df.loc[
    df["MTR01_RPM"]==1780, ["date", "MTR01_VIB_H", "MTR01_VIB_ACC", "MTR01_RPM"]
].head(4))
print(df.loc[
    df["MTR01_RPM"]==1450, ["date", "MTR01_VIB_H", "MTR01_VIB_ACC", "MTR01_RPM"]
])

print(df.loc[
    df['MTR01_RPM'] == 1780, ['date', 'MTR01_VIB_H', 'MTR01_VIB_ACC', 'MTR01_RPM']
].head(4))

print(df.loc[
    df['MTR01_RPM'] == 1450, ['date', 'MTR01_VIB_H', 'MTR01_VIB_ACC', 'MTR01_RPM']
])