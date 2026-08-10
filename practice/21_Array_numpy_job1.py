# 실습1을 위한 참조 코드
# 미국 속도 측정(miles)를 우리가 쓰는 속도 (km)로 변환시켜주는
# numpy 배열 예제

import numpy as np

miles = np.array([94.7, 104.5, 105.5])

# 속도(km/h)=속도(mph)*1.60934
print(miles * 1.60934)

print("=" * 40)

#실습1
#섭씨를 센서값 리스트 배열로 화씨
np_sup = np.array([36, 29, 27, 38, 59])

print((np_sup*1.8) + 32)