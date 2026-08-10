# 실습1을 위한 참조 코드
# 미국 속도 측정(miles)를 우리가 쓰는 속도 (km)로 변환시켜주는
# numpy 배열 예제

import numpy as np

miles = np.array([94.7, 104.5, 105.5])

# 속도(km/h)=속도(mph)*1.60934
print(miles * 1.60934)