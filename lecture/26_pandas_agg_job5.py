import pandas as pd

df = pd.read_csv('csv/14_hydraulic.csv', encoding = 'utf-8')

# 실습 5. 그룹별 통계량 종합
# 전체·그룹 통계와 진단표를 한 흐름으로
# 전체 통계부터 그룹 진단표까지 한 흐름으로 종합

# 온도 열의 전체 평균과 표준편차로 기준선 파악
print(df['온도'].mean().round(2))   # 45.34
print(df['온도'].std().round(2))    # 8.04

# 라인별(냉각기상태) 평균(mean)과 중앙값(median)을 함께 구해 치우침 확인
print(df.groupby('냉각기상태')['온도'].agg(['mean', 'median']).round(2))
#         mean  median
# 냉각기상태               
# 고장     54.67   55.45
# 저하     45.46   44.90
# 정상     35.89   35.90 -> 가장 차이가 없다 (튀는 값이 없다!)

# 설비 진단표를 온도편차 순으로 정렬해 우선 점검 대상 선정

# 예상 결과
# 전체 기준선·라인 치우침·진단표 정렬 결과 출력