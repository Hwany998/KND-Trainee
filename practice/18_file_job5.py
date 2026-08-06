#실습5 csv.writer로 csv쓰기
#1) csv를 import
import csv

#2) with open 으로 w-utf-8-newline 옵션으로 열기
with open('lecture/17_press.psy', 'w', encoding = 'utf-8', newline='') as f:

#3) csv.writer로 writer 객체를 만들기
    writer = csv.writer(f)

#4) writerow로 헤더와 각 데이터 행 쓰기
    writer.writerow(['시각', '설비'])
    writer.writerow(['9:00', 'PUMP-01'])

print(f)