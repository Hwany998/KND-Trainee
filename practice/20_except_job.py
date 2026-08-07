# 실습1단계
import csv

def read_csv():
    try:
        with open("lecture/20_ict_inspection_dirty.csv", "r", encoding = "utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)   # header 열만 따로 뺀 것
            rows = []               # 빈 열 리스트

            for row in reader:
                rows.append(row)

            print(f"헤더: {header}\n데이터 행 수: {len(rows)}")
            return header, rows
    
    except FileNotFoundError:   # 빈 결과 반환
        print("파일을 찾을 수 없음")
        return [], []           # 

# 실습2단계 조건 분류
# 딕셔너리
def group_data(rows):
    data = {}

    for row in rows:
        machine = row[1]
        
        if not row:
            continue

        if machine not in data:
            data[machine] = []

        data[machine].append(row[2:])

    for machine in data:
        print(machine, ":", len(data[machine]))

    return data

header, rows = read_csv()

print("=" * 40)

data = group_data(rows)

print("=" * 40)

# 실습3단계 통계 함수
def statistics(rows):
    numbers = []

    for row in rows:
        try:
            number = float(row[2:])
            numbers.append(number)
        except ValueError:
            continue

    if len(numbers) == 0:
        return None

    total = 0

    for number in numbers:
        total += number

    count = len(numbers)
    avg = total / count
    min_value = min(numbers)
    max_value = max(numbers)

    return count, avg, min_value, max_value

calc = statistics(rows, 5)
print(calc)