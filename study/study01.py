# 랜덤한 값을 csv파일로 새로 창작

import pandas as pd

# CSV 파일에 저장할 데이터 만들기
data = {
    "이름": ["김철수", "이영희", "박민수"],
    "점수": [80, 90, 85]
}

# 딕셔너리 데이터를 DataFrame으로 변환
df = pd.DataFrame(data)

# 새로운 CSV 파일 생성
# index=False : 왼쪽에 불필요한 번호 열이 저장되지 않도록 설정
df.to_csv("temp.csv", index=True, encoding="utf-8-sig")

# 저장 완료 확인
print("temp.csv 생성 완료")