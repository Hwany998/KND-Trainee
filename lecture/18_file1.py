# 기본 내장함수인 open()으로 sample.txt 파일 열기
# r : 읽기모드, utf-8 : 파일형식
# w : 새로 쓰기 / 기존 삭제 후 작성
# a : 이어 쓰기 / 기존 뒤에 추가

# open() 함수 구조
# open(파일명, 모드, 인코딩) - 내장함수라 import없이 사용 가능
# open() 이후는 무조건 close() 함수를 꼭!!!!!!!!!! 써야함.

# read : 전체 한 덩어리 문자열
# readline : 한 줄 문자열
# readlines : 전체, 줄 단위 리스트 / 줄 단위 센서 로그 또는 파일 직접 반복에 어울림
f = open("lecture/sample.txt", "r", encoding = "utf-8")
print(type(f).name)   # 타입 이름 : TextIOWrapper

# 텍스트파일 파일 한 줄씩 문자열 만들어서
lines = f.readlines()
print(lines)

f.close()   # 열었다면 언제가는 꼭 닫아줍시다.

# 만약 신경써서 파일 닫기(close) 귀찮으면 with open .. as 문법 추천
with open("lecture/sample.txt", "r", encoding = "utf-8") as f:
    # 앞으로 이렇게 들여쓰기 된 코드 끝나면 파일 접근을 닫는다. 알아서 (close)

    lines = f.readlines()
    print(lines)

# 쓰기 모드로 파일을 새롭게 만들어보겠다 "w"
f = open("lecture/sample.txt", "w", encoding = "utf-8")

# 파일 쓰기에 줄바꿈 포함하려면 \n을 포함시킨다.
f.write("안녕하세요.\n")
# 파일 쓰기에 들여쓰기 포함하려면
f.write("\t반갑습니다.\n")

f.close()

# 이어 쓰기에 줄바꿈 포함하려면 \n을 포함시킨다. "a"
f = open("lecture/sample.txt", "a", encoding = "utf-8")

f.write("맛점하세요.\n")

f.close()