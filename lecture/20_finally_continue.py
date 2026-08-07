
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

print("=" * 40)
# 반복문 안에서 예외처리
my_list = ["123", "456", "영크크", "32"]

problems = 0

for text in my_list:
    # 반복 도중 문제 생긴 경우 건너뛰고 이어서 진행
    try:
        my_num = int(text)
    except:
        # print("문제발생")
        problems += 1
        continue

    print(my_num)
print(f"{problems}개는 문제가 있어 건너뜀")

# bare except의 위험
# 에러정보 꺼내 쓰기, as e 문
# raise로 직접 예외 발생시키기: 잘 안씀, 주니어 개발자 테스트코드 제작용
