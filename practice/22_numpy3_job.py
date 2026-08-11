#실습1
print("=" * 20, "실습1", "=" * 20)

import numpy as np
roll = np.array([312, 300, 268, 290, 277, 331])
print(roll[0])  #312
print(roll[-1]) #331
print(roll[::2])#[312 268 277]

print("=" * 20, "실습2", "=" * 20)

#실습2
twoD_data = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])
print(twoD_data[1])     #1행 전체
print(twoD_data[:,0])   #1열 전체

print("=" * 20, "실습3", "=" * 20)

#실습3
rpm3 = np.array([801, 908, 1102, 933, 1415, 2261])
#최솟값과 최댓값을 min, max로 확인
print(rpm3.min())    # 801
print(rpm3.max())    # 2261

rpm_min = rpm3.min()
rpm_max = rpm3.max()
normalized = (rpm3 - rpm_min) / (rpm_max - rpm_min)
print(np.round(normalized,2))

print("=" * 20, "실습4", "=" * 20)

#실습4
rpm4 = np.array([1560., 1321, 1118, 1383, 1225, 2561])
torque4 = np.array([42.8, 39.9, 45.7, 33.9, 30.1, 8.8])
print(rpm4[rpm4 > 2000])    #[2561.]
print((rpm4 > 2000) | (torque4 < 10))   #[False False False False False True]

print("=" * 20, "실습5", "=" * 20)

#실습5
torque5 = np.array([39.8, 23.9, 50.1, 22.2, 8.1, 60.7, 57.7, 80.1])
high5 = torque5 > 50
print(high5)                    #이런 식으로 하면 불리언 값 및 개수 유지
print(torque5[torque5 > 50])    #이런 식으로 하면 값을 출력
print(sum(high5))
print(sum(high5) / len(high5))

print("=" * 20, "실습6", "=" * 20)

#실습6
data3 = np.array([[1520, 42.1], [1400, 46.1], [1498, 49.2], [2800, 4.6]])
print(data3)
print(data3.mean())
print(data3.mean(axis = 0))
print(data3.mean(axis = 1))
print(np.round(data3.std(axis = 0),2))