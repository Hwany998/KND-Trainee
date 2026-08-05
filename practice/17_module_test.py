# 실습1 
#1) import 모듈명으로 통째로 가져와 모듈명.기능() 사용
import math
result1 = math.sqrt(16)
result2 = math.ceil(4.2)
print(result1, result2)

#2) from 모듈 import 기능으로 일부만 모듈명 없이 사용
from math import sqrt, ceil
result1 = sqrt(16)
result2 = ceil(4.2)
print(result1, result2)

#3) import 모듈 as 별명으로 별명.기능() 사용
import math as mt
result1 = mt.sqrt(16)    #math를 mt로 지정한 시점에서 datetime이라 쓰면 오류
result2 = mt.ceil(4.2)
print(result1, result2)

#4) 세 방식 출력 모두 같은 것 확인
print("=" * 40)

# 실습2
#1) random 모듈 import
import random

#2) randint로 무작위 센서값 만들어 출력
sensor_result = random.randint(1, 10)
print(sensor_result)

#3) math 모듈로 그 값을 가공(제곱근)
import math
print(sensor_result ** 2)

#4) 다시 실행하면 값이 달라지는지 확인 완료
print("=" * 40)

# 실습4
#1) os를 import
import os

#2) path.join으로 폴더와 파일 이름을 이어 경로 만들기
path = os.path.join("lecture", "17_press.csv")
print(path)  # data\08_press.csv

#3) path.exists로 그 경로가 있는지 참, 거짓 확인
print(os.path.exists(path))

#4) if로 있고 없음에 따라 다른 메시지 출력
if os.path.exists(path):
    print(f"파일있음: {path}")
else:
    print(f"파일없음: {path}")

print("=" * 40)

# 실습5
#1) os와 datetime을 import
import os, datetime

#2) listdir로 폴더 파일 수 구하기
file_list_len = len(os.listdir())
print(file_list_len)

#3) datetime.now로 현재 시각 담기
now = datetime.datetime.now()
print(now)

#4) f-string으로 파일 수와 시각을 한 문장으로
print(f'점검 시각 {now}, 점검할 파일 수 {file_list_len}')

print("=" * 40)

# 선택실습1 (실습3)
#1) os를 import
import os

#2) getcwd로 현재 작업 폴더 확인
current_path = os.getcwd()
print(current_path)

#3) listdir로 폴더 안 목록을 변수에 담기
file_list = os.listdir(current_path)
print(file_list)

#4) for로 목록을 하나씩 출력하고 csv만 골라 출력
for name in file_list:
    print(name)
    if name.endswith(".csv"):
        print(name)
else:
    print("경로 내 .csv파일 없음")

print("=" * 40)

# 실습2 (실습6)
#1) os를 import하고 listdir로 폴더 목록 구하기
import os
file_list2 = os.listdir("lecture")

#2) for-if로 .csv로 끝나는 이름만 빈 리스트에 모으기
csv_list = []
for name in file_list2:
    if name.endswith(".csv"):
#3) 모은 csv마다 path.join으로 전체 경로 만들기
        file_path = os.path.join(os.getcwd(), name)
        csv_list.append(file_path)

#4) 골라낸 csv 목록 출력
for path in csv_list:
    print(f'[CSV]목록 ({path})')