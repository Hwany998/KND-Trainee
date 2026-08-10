# 2차원
import numpy as np

dim_2_list = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [2,34,6,8,10],
    [3,6,9,12,15]
]

print(dim_2_list[0][0]) #1
print(dim_2_list[1][1]) #7 

print("=" * 40)
#실습4
dim_2_list2 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [2,34,6,8,10],
    [3,6,9,12,15]
])
print(dim_2_list2.ndim)
print(dim_2_list2.shape)
print(dim_2_list2.size)

#실습5
#배열의 자료형을 확인하고 정수형으로 변환
int_list = np.array([11, 22, 33, 44, 55])
print(int_list.dtype)
print(int_list.astype(float))

#실습6
int_arange = np.arange(0, 8)
print(int_arange.reshape(2, 4))

#실습7
a_arange = np.arange(15)
print(a_arange.reshape(3, 5))

#실습8
sensors = np.array([30, 29, 27, 31, 29, 32, 27, 26])
print(sensors.shape)
print(sensors.dtype)
print(sensors.reshape(4,2))
fl_sensors = sensors.reshape(4,2).astype(float)
print(fl_sensors)