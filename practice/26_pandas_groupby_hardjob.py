# 선택 문제 : 첨부된 CSV 파일을 통해 다음 통계들을 내는 코드를 작성해 제출해주세요.

# [문제 1] 이 학교의 전체 학생 수를 구하세요. (힌트: len 또는 shape)
import pandas as pd

df_students = pd.read_csv('csv/14_students_groupby_practice.csv', encoding='utf-8')
df_students.info()
print(len(df_students)) #학생 수 60명
print('=' * 40)

# [문제 2] 학년별 학생 수를 구하세요. (힌트: groupby + count 또는 size)
print(df_students.groupby("학년")["학년"].count())
print('=' * 40)

# [문제 3] 학년 내 각 반별 학생 수를 구하세요. (힌트: 다중 컬럼 groupby)
print(df_students.groupby(['학년', '반'])['학년'].count())
print('=' * 40)

# [문제 4] 각 반(학년, 반 조합)의 국어 점수 평균을 소수점 둘째 자리까지 구하세요.
print(df_students.groupby(['학년', '반', '국어'])['국어'].mean())
print('=' * 40)

# [문제 5] 각 학년의 영어 점수 평균을 소수점 둘째 자리까지 구하세요. 
print(df_students.groupby(['학년', '반', '영어'])['영어'].mean())
print('=' * 40)

# [문제 6] 학교 전체의 수학 점수 평균을 소수점 둘째 자리까지 구하세요.
print(df_students.groupby(['학년', '반', '수학'])['수학'].mean())
print('=' * 40)