num = [1,2,3,4,5]

num_10 = []

for number in num:
    num_10.append(number * 10)

print(num_10)
#python에서 기본 제공하는 기능 외에 다양한 외부 라이브러리 이용하려면
#https://pypi.org/search 사이트에서 검색부터 하자

#Numpy 활용 이유
#수많은 숫자 묶음을 빠르게 게산하는 데이터 분석의 출발점
#데이터 분석 도구의 기초 (이외에도 Pandas, Matplotlib)
#특징: 같은 자료형, 정해진 형태

#터미널에서 바로 pip로 설치를 시도하면 (pip(맥은 pip3) install numpy)
#전체 시스템에 영향을 주는 설치로 생각되어 거절당함
#그래서 개별 Working Directory마다 별도 환경 구축하고
#그 안에 개별 프로젝트가 사용할 pip 라이브러리를 따로 받아 쓰게 한다
#이것이 가상환경(venv 또는 아나콘다라는 것도 있음)
#전역은 피하는 것을 추천
#이 밑의 1-3번까지 다 터미널에서 구동

#1. 현재 경로에 가상환경 생성
#맥 - python3 -m venv .venv (가상환경 만들건데 .venv라는 폴더 만들어서 넣어줘)
#윈도우 - python -m venv .venv

#2. 가상환경 활성화
#source .venv/bin/activate - 윈도우는 source(또는 cd) .venv/Scripts/activate

#3. (작업/실행 끝나고) 가상환경 종료
#deactivate

import numpy as np

num = [1,2,3,4,5]
#위 int값 리스트를 numpy의 배열 만들기
np_nums = np.array(num)
print(np_nums)

#파이썬의 리스트로부터 Numpy qoduf aksemfrl

temp = np.array([70.5, 69.8, 73.7])
print(temp) #출력 시 사이 콤마 없이 [70.5 69.8 73.7]

#일반적으로 리스트 항목마다 +5 하려면 for문으로 직접 처리해야했음
#numpy는 간단히 가능 / 이게 혁신 그 자체
print(temp + 5) #[75.5 74.8 78.7]

# 소수점 이하 없는 숫자 타입으로 가득찬 배열
print(np.array[1,2,3,4,5])

#소수점 이하 있는 숫자 타입으로 가득찬 배열
print(np.array[3.14, 6.7, 7.67])

#소수점 이하 있는 것 없는 것 함께 가득찬 배열
print(np.array[1, 2, 5, 3.14, 6.7, 4, 7.67])