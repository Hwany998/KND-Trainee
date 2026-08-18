# 실습1 빈도 세기
# value counts
import pandas as pd

df = pd.read_csv('csv/14_hydraulic.csv', encoding='utf-8')
df.info()
print(df.head(3))

# 이 방식도 가능하긴함.
df_old = df[ df['냉각기상태'] == '고장' ]
print(len(df_old)) # 40
# 하지만 이 방식으로 모든 상태를 찾아서 통계내는 것은 비효율적
# '고장'외에도 모든 경우를 한번에 모아서 경우마다 나타나는 갯수를 찾기
# value_counts

# 냉각기상태열 사이클 건수 세기
print(df['냉각기상태'].value_counts())
# 냉각기상태
# 고장    40
# 저하    40
# 정상    40

# results 컬럼의 정상/고장 건수 세기
print(df['result'].value_counts())
# result
# 정상    67
# 고장    53

# 실습2 
df = pd.read_csv('csv/14_hydraulic_qc.csv', encoding='utf-8')
df.info()
print(df.head(3))
# 케이스마다 비율 정규화 (normalize)
# 정규화 비율 결과를 round 처리로 3자리 반올림
print(df['검사결과'].value_counts(normalize = True).round(3))
# 합격, 불합격 비율 표시