# 트레이스백으로 에러 읽기
# ValueError: 글자를 숫자로 변환 요구 - 당연히 실패

# 정상화
# temp = int("20")
# print(temp)

print("=" * 40)

# ZeroDivisionError : 숫자는 0으로 나눌 수 없다.
# result = 10 / 0

# NameError: 이름 없는 에러
# hello()

# 정상화
print("hello")

# try-except문은 오류가 나도 지나치고 재생시켜주는 문
temp = -1
try:
    temp = int("스물")
except:
    print("해봤는데 안됨")
    temp = 0    # 문제가 있어도 앞으로 

print(temp)

origin = input("온도: ")
print(f"입력한 온도는 {origin}")

# ValueError - TypeError 잘 구분해야함 (종류가 틀린 것과 내용이 부적절한 것 구별)
try:
    temp = int(origin)
except ValueError:  # 타입은 맞지만 값이 부적절할 때 발생 (글자를 숫자로 바꿀 때 자주)
    print("숫자 아니면 0으로 생각함")

next_temp = temp + 10
print(f"10도만 더 높으면 {next_temp}")

# FileNotFoundError - 문제는 파일명 오타, 경로 문제, 확장자 숨김 3가지로 귀결됨
# 예외마다 다른 대처가 필요하면 except 여러 개로 설정 가능

# try - except문에 형제가 둘 있음. else, finally문
# except가 예외면 else는 성공했을 때, finally는 성공 여부 관계 없이 발동
# finally는 파일 닫기처럼 반드시 처리할 마무리 작업에 자주 사용
text = input("값: ")
try:
    temp = float(text)
    print("알맞은 값")
finally:
    print("종료")   # 무조건 실행

# 성공 경로: try 끝까지 실행한 뒤 else로 이동, 마지막 finally
# 실패 경로: try 중간 except 발동 finally 실행
# 자주 쓰는 경로: 넷을 다 쓸 필요는 없다. 초보는 finally 가장 유용
# 종료 또는 파일을 닫는 것은 매우매우 중요한 과정이며 닫지 않았을 때 문제가 심화
