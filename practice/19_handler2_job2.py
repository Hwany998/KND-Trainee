#실습2 반복문에서 불량 줄 건너뛰기
#소숫점 이하 숫자가 포함된 숫자들을 20개 정도 만들어 리스트에 담아두기
#그 사이에 엉뚱한 글자들이 포함된 내용도 포함
#위 리스트 데이터를 사용해서 문제를 해결
dot_num = [
    12.13, 123.19, "호날두", 
    234.12, 22.10, 11.22, "메시",
    81.9, 22.21, 10.12, "손흥민",
    7.81, 99.91, "홀란", 111.11, "케인",
    11.12, 22.21, 10.16, "비니시우스"
]
normal = 0
for num in dot_num:
    try:
        normal_num = float(num)
        normal += 1
    except ValueError:
        continue
    print(num)
print(f"{normal}개는 문제가 없음")

#실습3 여러 파일 묶어 처리
#다음과 같은 식의 리스트를 만들어 반복문으로 처리
#for문으로 리스트 문자열을 꺼내어 해당 이름 파일들을 열어보기 시도
import os

file_names = ["19_press.csv", 
              "20_ict_inspection.scv", 
              "20_ict_inspection_inspection_dirty_dirty.csv",
              "18_press.csv",
              "this_file_is_none"]
normal_cnt = 0

for file in file_names:
    try:
        csv_path = os.path.join("lecture", file)
        with open(csv_path, "r", encoding = "utf-8") as f:
            normal_cnt += 1
    except FileNotFoundError:
        continue
print(normal_cnt)