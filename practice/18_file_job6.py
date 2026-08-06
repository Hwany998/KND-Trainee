# 실습6. csv 읽어 조건 저장하기
#1) csv를 import
import csv

#2) csv.reader로 읽고 첫 줄 헤더는 건너뛰기
with open('practice/18_press.csv', 'r', encoding = 'utf-8', newline='') as f:
    reader = csv.reader(f)
    #DictReader가 아닌 그냥 reader 사용하면 보통 csv파일의 첫줄인 헤더줄도 읽음
    #reader에서 첫줄 건너뛰고 말하려면 next(reader)로 한줄 건너뛰고 reader가 반응

    header = next(reader)
    print(header)

#3) 값을 float으로 변환해 기준(90) 초과 행만 리스트에 모으기
    over_list = []
    for row in reader:
        if float(row[4]) > 90:
            over_list.append(row)
print(over_list)

#4) csv.writer로 모은 행들을 새 csv에 저장
with open('practice/18_press_copy.csv', 'w', encoding = 'utf-8', newline='') as f:
    csv_write = csv.writer(f)
    csv_write.writerow(header)
    csv_write.writerows(over_list)
print(csv_write)