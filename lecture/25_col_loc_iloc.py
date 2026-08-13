import pandas as pd

df = pd.read_csv('csv/13_diecasting_small.csv')
df.info()

df['형체력'].info() #Series
df[['형체력', '실린더압력']].info() 
#DataFrame #두 겹[[]]은 항상 DataFrame으로 출력

#열 이름 확인 print(df.columns)
#Index(['샷','실린더압력','주조압력','사이클타임' 등등]), dtype

#실습1
df1 = pd.read_csv('csv/13_diecasting_small.csv')
#shape확인
print(df1.shape)
#columns의 열 이름 출력 확인
print(df1.columns)
#실제 csv파일 열어보고 shape, columns로 출력

print("=" * 40)

#실습2 열 선택하기
#'csv/13_diecasting_small.csv' 파일 열기
df2 = pd.read_csv('csv/13_diecasting_small.csv')
#대괄호 한 겹으로 단일 열 series 선택
df2['형체력'].info()
#'형체력' 칼럼 하나만 빼오기
print(df2[['형체력']].columns)
#대괄호 두 겹으로 복수 열을 DataFrames으로 선택
#'형체력', '실린더압력' 두 개를 선택하기
print(df2[['형체력', '실린더압력']])

#선택한 열을 mean으로 평균 계산
#df['형체력'].mean() -> 소수점 이하 1자리까지만 나오게 조정
print(round(df2[['형체력', '실린더압력']].mean(),1))

print("=" * 40)

#실습3 공정 센서 열 골라내기

#주조 로그 파일 불러오기
#'csv/13_diecasting_shot.csv' 파일 열기
df3 = pd.read_csv('csv/13_diecasting_shot.csv')

#한 센서 열을 series로 선택
#형체력 선택
print(df3['형체력'].info())

#여러 feature 열을 DataFrame으로 선택해 형태 확인
print(df3[['형체력', '실린더압력', '주조압력']].shape)

df = pd.read_csv('csv/13_diecasting_small.csv')
df.info()

print("=" * 40)

s = df.loc[0]
s.info()

#loc[:], iloc[:] 차이
#loc는 끝번호까지 다, iloc는 끝번호 제외
#loc[:2] -> 0,1,2 iloc[:2] -> 0,1
#df.loc[0:2].info() #DataFrame
df_sub = df.loc[0:2]
df_sub.info()
print(df_sub)

df_sub2 = df.loc[0:2, ['품질등급', '형체력']]
df_sub2.info()
print(df_sub2)

#실습4. loc, iloc로 행 선택
#라벨 기준 loc와 번호 기준 iloc로 행 선택, 범위 차이
df = pd.read_csv('csv/13_diecasting_small.csv')

#라벨 기준 단일 행 선택
print(df.loc[0, '품질등급'])    #양품
#df.iloc[0] -> 특정 row number인 row의 Serise 추출
#['품질등급'] -> 해당 Serise에서 '품질등급' 컬럼의 내용만 추출
print(df.iloc[0, 2])

#범위 선택으로 loc 끝 포함, iloc 끝 제외 차이 확인
#다음 두 줄 결과는 각각 어떻게 나타나는지 두 결과는 동일한지 아니면 다른지 주석
print(len(df.loc[0:2]))     #3
print(len(df.iloc[0:2]))    #2

#실습5. loc, iloc로 행,열 동시 선택
#행과 열을 동시 지정해 원하는 부분만 추출
#data 'csv/13_diecasting_small.csv' 사용
df5 = pd.read_csv('csv/13_diecasting_small.csv')
#loc로 행 범위와 열 이름을 함께 지정
print(df5.loc[5, '품질등급'])
#다른 행 범위에서 세 열 선택
print(df5.loc[3, '품질등급'])
#iloc 음수 인데스로 마지막 행 선택

#실습6. 특정 구간 추출 종합
#열 선택 loc, iloc을 결합해 특정 구간을 추출하는 종합
#data 'csv/13_diecasting_shot.csv' 사용
df_shot = pd.read_csv('csv/13_diecasting_shot.csv')

#여러 feature열을 선택한 뒤 iloc로 앞구간 추출
cols = ['실린더압력','주조압력','사이클타임','비스킷두께','형체력']
print(df_shot[cols].iloc[0:10].shape)   #결과

#loc라벨 범위로 두 열 구간 추출
cols2 = ['실린더압력', '주조압력']
df_sub_shot = df_shot.loc[:10, cols2]
print(df_sub_shot)

#iloc 위치 범위로 앞쪽 열 구간 추출
cols3 = ['실린더압력', '주조압력']
df_sub_shot2 = df_shot.iloc[:11, 1:3]
print(df_sub_shot2)