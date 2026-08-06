# 실습4
#1) csv 모듈을 import
import csv

#2) with open으로 csv를 읽기 모드 utf-8로 읽기
with open("lecture/sample.txt", "r", encoding = "utf-8") as f:

#3) csv.reader로 reader 객체 만들기
    csv_reader = csv.reader(f)

#4) for로 각 행(리스트)를 하나씩 꺼내 출력
    for csv_row in csv_reader:
        print(csv_row)  # 각 행(row)마다 리스트에 출력