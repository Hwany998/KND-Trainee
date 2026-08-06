import os
import sys
import csv

csv_path = os.path.join("lecture", "17_press.csv")

# 위 경로 파일 찾지 못하면 강종
if not os.path.exists(csv_path):
    print("파일 없습니다.")
    sys.exit(1)         # 비정상 종료 시 보통 0이 아닌 값(예 1) 전달

print("파일 있습니다.")

with open(csv_path, "r", encoding = "utf-8") as f:
    # print(f.readlines())  # 이제 import csv로 전문가에게 맡기자
    reader = csv.reader(f)
    
    for row in reader:
        print(row[0])  # 각 행(row)마다 리스트에 출력
        # row[idx] 를 통해 해당 idx 행의 값만 다 출력시킬 수 있음

# 18_file3.py의 내용
import os
import sys
import csv

csv_path = os.path.join("lecture", "17_press.csv")

# 위 경로 파일 찾지 못하면 강종
if not os.path.exists(csv_path):
    print("파일 없습니다.")
    sys.exit(1)         # 비정상 종료 시 보통 0이 아닌 값(예 1) 전달

print("파일 있습니다.")

with open(csv_path, "r", encoding = "utf-8") as f:
    #pass        # 딱히 적을게 없으면 뭐라도 적어야한다면 땜빵용 pass
    reader = csv.DictReader(f)

    for row in reader:
        print(row["설비ID"], row.get("시각"))

# csv 다룰 때 흔한 오류
# 증상         원인             해결
# 한글 깨짐     = 인코딩 불일치     = utf-8 / cp949 바꿔보기
# 빈줄 끼임     = newline누락     = 쓰기 open에 newline""
# 계산 오류     = 문자열 상태       = float - int 변환
# 첫 줄 오류    = 헤더 포함        = 헤더 건너뛰기

with open(csv_path, "r", encoding = "utf-8") as f:
    #pass        # 딱히 적을게 없으면 뭐라도 적어야한다면 땜빵용 pass
    reader = csv.reader(f)
    #DictReader가 아닌 그냥 reader 사용하면 보통 csv파일의 첫줄인 헤더줄도 읽음
    #reader에서 첫줄 건너뛰고 말하려면 next(reader)로 한줄 건너뛰고 reader가 반응

    header = next(reader)
    print(header)
    #header는 따로 리스트로 챙겨짐
    #['설비id', '시각', '진동x', '진동y', '전류', '상태]

    for row in reader:
        print(row[0])