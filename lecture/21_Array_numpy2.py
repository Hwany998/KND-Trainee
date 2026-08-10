#numpy의 arange
#값 범위 지정해서 나타내기
import numpy as np

#0부터 4까지 생성
under_five = np.arange(5)
print(under_five) # [0 1 2 3 4]

#0부터 8까지 2간격
gab_two = np.arange(0, 10, 2) #8보다 큰 숫자가 만들어지면 덧붙이지 않고 끝
print(gab_two) # [0 2 4 6 8]

#numpy의 linsapce (위의 import numpy as np 사용)
#개수 중심 균등 분할, 시작과 끝 구간을 지정한 개수만큼 정확히 나눔
#간격은 알아서 계산하도록 함

#0부터 1까지 5개로 균등분할
div_five = np.linspace(0,1,5)
print(div_five) # [0. 0.25 0.5 0.75 1.] 5분할, 기준의 최소/최대값 포함해서 분할

#numpy의 zeros
#값 범위 지정해서 나타내기
block_zeros = np.zeros(5)
print(block_zeros) # [0. 0. 0. 0. 0.]

#7로 채우기 / 명시적으로 float값 지정해줘야 .이 붙음
# float 타입 값으로 채워지는 배열이 만들어짐
block_seven = np.full(4, 7) #(4, 7.0)하면?
print(block_seven) #[7 7 7 7] # [7. 7. 7. 7.]