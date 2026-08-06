# 실습3. a모드로 기록 이어붙이기
#1) with open으로 파일을 추가 모드 a로 열기
f = open("lecture/sample.txt", "a", encoding = "utf-8")

#2) write로 새 기록 문장 쓰기
f.write("이 줄은 a모드로 이어붙인거야.\n파이팅해보자")

#3) w모드와 달리 기존 내용이 보존됨을 확인 (확인합니다)
f.close()

#4) r모드로 열어 전체가 쌓였는지 확인
f = open("lecture/sample.txt", "r", encoding = "utf-8")
readline = f.read()
print(readline)