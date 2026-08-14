import pandas as pd

# 실습 3. 두 조건 묶기
# 두 조건을 그리고(&)·또는(|)로 묶어 행을 추출
df3 = pd.read_csv('data/13_diecasting_shot.csv')
df3.info()

# · 비스킷두께 조건과 사이클타임 조건을 각각 괄호로 감싸기

# · 두 조건을 그리고 기호"&"로 묶어 모두 만족하는 행 추출
df3_sub1 = df3[ df3['비스킷두께'] >= 13 ]
print(len(df3_sub1)) # 6

df3_sub2 = df3[ df3['사이클타임'] >= 25 ]
print(len(df_sub2)) # 6

df3_both = df3[ (df3['비스킷두께'] >= 13) & (df3['사이클타임'] >= 25) ]
print(len(df3_both)) # 83

# · 같은 두 조건을 또는 기호"|"로 묶어 결과 수 비교
df3_eigher = df3[ (df3['비스킷두께'] >= 13) | (df3['사이클타임'] >= 25) ]
print(len(df3ㄴ_eigher)) # 104

# 예상 결과
# 그리고는 12건, 또는는 94건으로 개수 차이 확인 x