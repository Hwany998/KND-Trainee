# 실습1. CSV 불러오기 워밍업
# pip3 install pandas   (가상환경에서 설치 추천)
import pandas as pd
import os

filepath = os.path.join("csv", "12_metro_small.csv")    # = "csv/12_metro_small.csv"

try:
    df_metro_small = pd.read_csv(filepath, encoding = "utf-8", sep = ',', 
        index_col = "측정시각", nrows = 5, usecols = ["측정시각", "가동상태"])
    print(df_metro_small.shape) #(30, 7)

    print(df_metro_small.head(10))

except FileNotFoundError:
    print(f"파일이 없습니다 : {filepath}")

#실습2
#12_metro_compressor.csv
#200행 7열 - 인덱스 3번 행 오일온도가 NaN
df_metro_compressor = pd.read_csv('csv/12_metro_compressor.csv')
print(df_metro_compressor.head(3))
print(df_metro_compressor.shape)    # (200, 7)

#실습3 한글 구분자 깨짐 옵션 다루기
#sep 없이 읽으면 200행 1열, sep = ";"이면 200행 7열
df_semicolon = pd.read_csv("csv/12_metro_compressor_semicolon.csv")
print(df_semicolon.shape)
print(df_semicolon.head(4))

#실습4 
#센서 3개만 골라 불러오기 usecols=[...]
df_compressor = pd.read_csv("csv/12_metro_compressor.csv", 
    usecols = ['측정시각', '오일온도', '모터전류', '가동상태'])
print(df_compressor.shape)
print(df_compressor.head(3))

#실습5 경로 오류 고치기
df_empty = pd.read_csv('아무거나주셈.csv')  #FileNotFoundError
print(df_empty)
