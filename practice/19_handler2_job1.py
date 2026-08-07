# 실습1. finally로 파일 안전하게 닫기
#1) try 블록에서 파일을 열어 처리 (with open 안쓰는 걸 권장)
import csv

try:
    f = open("lecture/19_student_scores.csv", "r", encoding = "utf-8")
    reader = csv.reader(f)
    header = next(reader)

#2) 처리 도중 오류가 날 수 있음 가정
except ValueError:
    header.startswith("김")
    print("잘못된 값 입력되어 0으로 처리")
else:
    print(f"{temp}, 알맞은 값")

#3) finally 블록에 close를 넣어 오류 상관없이 닫기
finally:
    print("오류 확인 과정을 종료")
    f.close()

#4) 일부러 오류 내도 finally 실행되는지 확인