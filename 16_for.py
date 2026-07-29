#반복문은 동일한 작업을 특정 횟수만큼 반복
#for 변수 in range(횟수):
#   반복시킬 코드 (들여쓰기 한 칸 필수)
#같은 코드를 복사 붙여넣기로 여러번 작성하는 대신
#"N번 실행하라" 의미

for i in range(3):
    print("안녕하세요")

# 0부터 10까지의 숫자 잧체가 필요하거나 출력할 때
for i in range(11):
    print(i)    #i는 증가값을 지정하지 않는 이상 반복할 때마다 자동 +1이 적용

#0부터 10까지 짝수만 출력할 시
for i in range(0, 11, 2):   #0인덱스부터 11인덱스까지 짝수번만 출력
    print(i)

#1부터 10까지 홀수만 출력
for i in range(1,10,2):
    print(i)

#역순
for i in range(10, 0, -1):
    print(i)

# 10부터 1까지 짝수만 역순으로 출력
for i in range(10, 0, -2):
    print(i)

#동작안함, 시작값인 0에서 -2를 했을 때 끝 값이 포함되지 않아서 반복문 종료
for i in range(0, 10, -2):
    print(i)     

n = int(input("몇 번 반복할까여? "))
for i in range(n):
    print("반복 중...")

#실습1
N = int(input("끝 번: "))
for i in range(1, N+1):     # N 할당값 5기준 1,2,3,4,5 출력을 위해 +1
    print(i)
for i in range(2, N, 2):
    print(i)
for i in range(N, 0, -1):
    print(i)

#실습. 3의 배수 출력
#사용자에게 범위를 입력받아 3의 배수 출력하기
goal_score = int(input("입력: "))
for i in range(1,goal_score+1):
    if(i % 3 == 0):
        print(i)
#사용자에게 숫자 입력 받고
#3, 6, 9가 들어가는 숫자
goal_score2 = input("3,6,9숫자게임: ")
for i in range(1, int(goal_score2)):
    if("3" in str(i % 10) or "6" in str(i % 10) or "9" in str(i % 10)):
        print(i)

#누적 변수
total = 0
for i in range(1,6):
    total += i  # total = total + i
print("합계: ", total)

#for문 안에 누적변수 선언 시
for i in range(1, 6):
    total2 = 0;
    print("total2 = 0 시 total2에 할당된 값:", total2)
    print("현재 i의 값:", i)
    total2 += i
    print("total2 += i 후의 total2에 할당된 값:", total2)
print("합계:", total2)

# 1~15 사이의 4의 배수만 누적
total3 = 0
for i in range(1,16):
    if i % 4 == 0:
        total3 += 3     #4의 배수만큼 +=3씩 해라.
print("1~15 사이의 4의 배수 누적 결과:", total3)

#enumerate 순서와 값 함께 (낱낱이 세다)
temps = [33, 32, 23, 45, 28]
for t in enumerate(temps):
    print(t)
for idx, t in enumerate(temps):
    print(f"idx: {idx}, t: {t}")

#리스트의 모든 요소에 접근을 해야 하는 경우가 잦음
#그래서 python이 반복문에서 이를 쉽게
#enumerate라는 내장 함수 제공
#enumerate은 리스트의 모든 요소를 앞에서부터
#순서대로 하나씩 찍어가면서 접근
#접근해서 각자의 인덱스와 그 값을 뽑아줌 -> 돌려주는 값 2개
#값을 두 개 받으니 우리도 변수를 2개 준비하면
#각 변수에 쏙쏙 값이 할당
#돌려주는 순서는 인덱스, 값
#그래서 enumerate 사용 땐 for 뒤에 변수를 두 개 전달
list = ["안녕", "hi", "안녕", "hi", "hi", "안녕"]
for index, value in enumerate(list): 
    print(value)
for i in range(len(list)):
    print(list[i])
#위의 두 개는 모두 같은 기능을 수행한다. 각자 상황, 가치관에 따라 사용 결정

#3단 출력
for i in range(1, 6):
    print("3 x", i, "=", 3 * i)
#3x1=3 ... 3x5=15

#2단 출력하기
for su in range(1, 10):
    print(f"2 x {su} = {2 * su}")

#1~5단 출력
for dan in range(1,6):
    for star in range(1,10):
        print(f"{dan} x {star} = {dan * star}") 
    print(f"{dan}단 끝")

#1~9단 사이 2의 배수 단만 구구단 출력
for dan2 in range(1, 10):       #단수 1~9
    if(dan2 % 2 == 0):          #단수 2로 나눈 나머지 값 0인 짝수
        for star2 in range(1,10):   #조건 기준으로 1~9까지 곱
            print(f"{dan2} x {star2} = {dan2 * star2}")
        print(f"{dan2}단 끝")   #1~9까지 곱한 후 해당 단수 끝