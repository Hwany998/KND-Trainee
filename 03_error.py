# print("======NameError 만들기======")   # 코드는 위에서 아래로 실행, 중간 오류 발생 시 이후 실해X
# print("NameError 만들기")     # NameError, SyntaxError 발생, 따옴표 사용

# # print("온도)        # syntaxError 발생, 따옴표 닫기
# # print("진동"        # 4line 오류가 발생하여 5line은 발동 안됨, 괄호 닫기
# print("온도")
# print("진동")

# # 실습 오류 고치기
# print("온도", 75)       # print(온도, 75) -> NameError 온도 따옴표
# print("진동", 2.5)      # print("진동", 2.3 -> SyntaxError 괄호 닫기
# print("압력", 4.0)      # print("압력": 4.0) -> SyntaxError 콜론 대신 ,쉼표

# 실습2
print("===== "+"1번","설비","점검 "+"=====")    # +와 쉼표를 통한 문자열 띄어쓰기
print("온도"+"(°C):",82)          # +와 쉼표를 통한 문자열 띄어쓰기
print("온도 상승량:", 93-82)        # 쉼표를 통한 문자열 띄어쓰기, 빼기 연산