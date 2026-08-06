# 실습2. with open으로 파일에 쓰기
#1) with open으로 파일을 쓰기 모드 w, utf-8 열기
with open("lecture/sample.txt", "w", encoding = "utf-8") as f:
    # 앞으로 이렇게 들여쓰기 된 코드 끝나면 파일 접근을 닫는다. 알아서 (close)

#2) write로 내용을 쓰기
# 파일 쓰기에 줄바꿈 포함하려면 \n을 포함시킨다.
    f.write("안녕하세요.\n")
# 파일 쓰기에 들여쓰기 포함하려면
    f.write("\t반갑습니다.\n")

#3) with 블록이 끝나면 파일이 자동으로 닫힘

#4) r 모드로 다시 여러 쓴 내용 확인
f = open("lecture/sample.txt", "r", encoding = "utf-8")
readtxt = f.read()
print(readtxt)