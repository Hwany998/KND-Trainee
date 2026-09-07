#선그래프

import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("csv/05_03_열연압연_정비이력.csv")
df2 = pd.read_csv("csv/05_03_열연압연_운전데이터.csv")

# 선 그래프
plt.figure()
plt.plot(df2["day"], df2["roll_gap_corr_mm"], marker = "o")

# 선 그래프2
plt.figure()
plt.plot(df2["day"], df2["thickness_dev_mm"], marker = "o")
plt.axhline(y=0.09, color="red", linestyle="--")

#실습 STEP1
#그래프 분석 기록
'''
1 어느 날부터 이전과 다른 지속 변화가 보이나요? 42일
2 스파이크인가요, 누적되는 추세인가요?        누적되는 추세
3 두 그래프의 변화 시점은 비슷한가요?        변화시점 비슷함.
'''

#실습 STEP2
#변화날 기준 = 42일 / 교체일 = 67일

fig, axes = plt.subplots(2, 2, figsize = (20, 15))

roll_cols = [
    'roll_gap_corr_mm',
    'thickness_dev_mm',
    'workroll_vib_mm_s'
]

hyd_cols = [
    'hyd_pressure_bar',
    'hyd_oiltemp_c',
    'hyd_level_pct'
]

op_cols = [
    'steel_grade',
    'entry_temp_c',
    'line_speed_mpm'
]

# 1. 작업롤 마모
for col in roll_cols:
    axes[0, 0].plot(df2['day'], df2[col], label=col)

axes[0, 0].set_title("작업롤 마모")
axes[0, 0].legend()


# 2. 유압계통 이상
for col in hyd_cols:
    axes[0, 1].plot(df2['day'], df2[col], label=col)

axes[0, 1].set_title("유압계통 이상")
axes[0, 1].legend()


# 3. 운전조건 변화
for col in op_cols[1:]:
    axes[1, 0].plot(df2['day'], df2[col], label=col)

axes[1, 0].set_title("운전조건 변화")
axes[1, 0].legend()


# 4. 두께 편차
axes[1, 1].plot(
    df2['day'],
    df2['thickness_dev_mm'],
    label='thickness_dev_mm'
)

axes[1, 1].set_title("두께 편차")
axes[1, 1].legend()


plt.show()