# 실습3. 구체적 예외로 입력 검증하기
#1) 입력을 int로 바꾸는 코드를 try에 넣기
value1 = 10
value2 = input("온도: ")
print(f'입력온도: {value2}')
print(f'{value1}을 {value2}로 분할과정 시작')

try:
    temp = int(value2)
    print(value1 / temp)

#2) ValueError를 except로 잡아 안내
except ValueError:
    value2 = 2
    print('입력값이 올바르지 않아, 2로 처리합니다.')

#3) 여러 except로 ZeroDivisionError도 구분해 처리
except ZeroDivisionError:
    temp = 0
    print("입력 온도가 0이기에 나눌 수 없습니다.")

print(value1 / int(value2))

#4) 잘못된 입력을 넣어 프로그램이 멈추지 않는지 확인