
import pandas as pd

df = pd.read_csv('data/14_hydraulic.csv', encoding='utf-8')

# 라인으로 그룹을 나눠 압력 열의 평균
print(df.groupby('냉각기상태')['압력'].mean().round(2))

# 집계 함수 최고 온도 확인 max
# 벨브상태별로 최고 온도
print(df.groupby('밸브상태')['온도'].max())

# size로 교대별 측정 건수까지 확인
print(df.groupby('운전부하').size())

print("-" * 40)

# 실습 5. 그룹별 평균 비교와 정렬

# 밸브상태 그룹별로 진동의 평균
print(df.groupby('밸브상태')['진동'].mean().round(2))

# 집계 결과에 내림차순으로 정렬
print(df.groupby('밸브상태')['진동'].mean().round(2).sort_values(ascending=False))

print("-" * 40)

# 실습 6. 여러 기준 조합 그룹
# 냉각기상태, 운전부하 두 기준 잡아서 각 그룹별 평균 진동
print(df.groupby(['냉각기상태', '운전부하'])['진동'].mean().round(2))

# 같은 두 기준으로 size를 구해 조합별 측정 건수 확인
print(df.groupby(['냉각기상태', '운전부하']).size())

# 결과(null값)들이 size갯수엔 포함

print("-" * 40)

# 실습 7. 빈도와 그룹 집계 종합

# value_counts로 설비 구성과 정상·고장 비율 파악
# counts라서 결과(null값) 무시
print(df['밸브상태'].value_counts())

print(df['밸브상태'].value_counts(normalize = True).round(3))

# 고장 행만 걸러 라인별 고장 건수 집계
# 다음 세가지 방법이 있다.
print(len(df[ df['result'] == '고장' ])) # 53 - 문제가 원하는 답
print(df.groupby('result').size()) # 고장    53
print(df['result'].value_counts()) # 고장    53

# groupby로 설비별 온도·진동 평균까지 비교
print(df.groupby('냉각기상태')['온도'].mean().round(2))
print(df.groupby('냉각기상태')['진동'].mean().round(2))
# 각각 처리하지 말고 한번에!
print(df.groupby('냉각기상태')[['온도', '진동']].mean().round(2))