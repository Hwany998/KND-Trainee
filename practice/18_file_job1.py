# 실습1. open()으로 파일 읽기
#1) open으로 파일 읽기 모드 r, utf-8 열기
f = open("lecture/sample.txt", "r", encoding = "utf-8")
g = open("lecture/sample.txt", "r", encoding = "utf-8")

#2) read로 전체 한 문자열로 읽어 출력
textline = f.read()

#3) readlines로 줄 리스트로 읽어 출력
# textlines = f.readlines() 이미 f엔 읽은 기록이 저장되어 [] 빈 리스트가 됨
textlines = g.readlines()   # g라는 새로운 변수를 할당하여 readlines() 함수 사용

#4) 두 방식 결과 차이를 비교하고 파일 close
print(textline, textlines)
f.close()