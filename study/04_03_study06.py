#선그래프

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csv/04-03_이상의_정의_진동데이터_130_260903_Question_1.csv")

# 가동여부가 1인 행만 사용
df_run = df[df["가동여부"] == 1]

# 선 그래프
plt.plot(df_run["일자"], df_run["진동RMS"])

# 4.5 mm/s 수평 임계선
plt.axhline(y=4.5)

# x축, y축
plt.xlabel("일자")
plt.ylabel("진동RMS")

plt.show()

#산점도

# 80일 미만 + 가동여부가 1인 데이터
df_normal = df[(df["일자"] < 80) & (df["가동여부"] == 1)]

# 산점도
plt.scatter(df_normal["부하율"], df_normal["진동RMS"])

# 축 설정
plt.xlabel("부하율")
plt.ylabel("진동RMS")

plt.show()

# 정상 기준 숫자로 확인
normal = df[(df["가동여부"] == 1) & (df["일자"] < 80)]

count = len(normal)
mean = normal["진동RMS"].mean()
std = normal["진동RMS"].std()

threshold = mean + 3 * std

print(count)
print(mean)
print(std)
print(threshold)