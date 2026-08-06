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