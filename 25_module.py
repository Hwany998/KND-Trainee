# 실습1 에서 사용
# import로 수학 기능을 가져오기
import math

# 해당 모듈이름.함수() 식으로 호출해야한다.
result = math.sqrt(16)
print(result)

# 수학 관련 모듈에서 sqrt 기능만 불러오기
from math import sqrt
result = sqrt(16)
print(result)

# ===================================
# math라는 모듈 이름 다 쓰기 귀찮으니 as로 줄이자
import math as mt
result = mt.sqrt(16)    #math를 mt로 지정한 시점에서 datetime이라 쓰면 오류
print(result)

# datetime 모듈 가져옴
import datetime

# datetime의 now()는 현재 지역 날짜와 시간 반환
now = datetime.datetime.now()
print(now)


# ===================================
import math
print(math.sqrt(9))     # 제곱근값
print(math.ceil(4.2))   # 올림값
print(2 ** 3)           # 거듭제곱 2의 3승

# math에서 sqrt, ceil 두 개만 사용하면 이렇게 써도 됨
from math import sqrt, ceil
print(sqrt(9), ceil(4.2))   # 2개만 쓰면 이렇게 ㄱㄱ

print("=" * 40)
# 표준 라이브러리 random 모듈
import random
print(random.randint(1, 10))    # 1 ~ 10에서 랜덤값
print(random.choice(["정상", "비정상", "위험"]))    # 셋 중 무작위

print("=" * 40)

# 표준 라이브러리의 datetime 모듈
import datetime
now = datetime.datetime.now()
print(now)

# 모듈 도움말 보기  # 현재는 참고만 하고 구글링한 웹사이트로 확인하자
# dir(math)
# help(math.sqrt)

