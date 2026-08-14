# 실습 2. 임계값 넘는 설비 골라내기
# 실제 제조 데이터에서 위험 임계값을 넘는 설비 추출
import pandas as pd

df2 = pd.read_csv('data/13_diecasting_small.csv')
df2.info()

# · 비스킷두께 열에 비교 연산자로 임계값 기준 조건 생성
# · 조건을 대괄호에 넣어 임계값 초과 설비만 추출
# · 결과에서 샷와 비스킷두께 열만 골라 확인

# 1. df['비스킷두께'] -> 시리즈 추출
# 2. 추출된 시리즈 내용들이 16 이상이면 True, 아니면 False -> Boolean Serise
# 3. Boolean Serise와 비교해서 df의 내용중에 True와 겹치는 행들을 추출 -> df_sub
df2_sub = df2[df2['비스킷두께'] >= 16]
df2_sub.info() # 5 row 존재 확인 - Index: 5 entries
print(len(df2_sub)) # 5 row 존재 확인

print(df2_sub.head(3))

# 위 내용이 너무 많은 컬럼을 보여니까, 샷과 비스킷두께 컬럼만 골라 출력
print(df2_sub['샷'].head(3))
print(df2_sub['비스킷두께'].head(3))
# 위에처럼 두 컬럼을 각각 가져와 출력하면 보기 힘드니까, 한번에!
print(df2_sub[['샷', '비스킷두께']].head(3))