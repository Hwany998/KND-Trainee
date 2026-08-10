#실습2 예제 코드
import numpy as np

# 0부터 숫자 6씩 증가시키다 30보다 작은 값일때만 배열에 붙임
gab_six = np.arange(0, 30, 6)
print(gab_six)  # [0 6 12 18 24]

# 0부터 30까지 6등분 나누어 배열에 붙임
div_six = np.linspace(0, 30, 6)
print(div_six)  # [0. 6. 12. 18. 24. 30.]

print("=" * 40)

#실습2
div_hund = np.linspace(0, 100, 5)
print(div_hund)

#실습3 예제 코드
#특정 시작/끝 시각 정해서 특정 간격 시간들이 지나면
#언제 체크포인트가 만들어지나를 numpy의 배열로 알아보기

#예를 들어 0~60초 사이에 5초간격으로 체크하면
#실제로 몇초마다 체크하는 지정이 생기나 알아보기
checks = np.arange(0, 60, 5)
print(checks)

#실습3
clocks = np.arange(0, 60, 10)
print(clocks)