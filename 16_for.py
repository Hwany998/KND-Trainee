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

#무한루프 유의
count = 1
while count <= 3:
    print(count)
    count += 1  #얘 없으면 무한루프 / 멈출 땐 ctrl c / command c

goal = 7
start_num = int(input("제가 생각하는 중인 값을 1-10까지 찾아보세요:"))
while start_num != goal:
    if(start_num == goal):
        print("정답입니다.")
    else:
        print("틀렸습니다. 다시 입력하세요.")
        start_num = int(input())
print("종료")

#break 사용시 반복 바로 탈출
# input_sum = 0
# while True: #조건만 보면 무한반복하는 코드
#     input("값을 입력하세요. 값의 누적이 15 넘으면 종료")
#     input_sum += user_input

#     if(input_sum > 15):
#         print("누적합계:", input_sum, "입력 종료")
#         break
# print("break를 통해 while문 나가면 코드 실행")

#사용자 입력값을 확인만 하고 저장할 필요 없다면!
while True:
    x = input("입력 (종료는 q를 입력하세요): ")
    if x == 'q':
        break
    print("입력받은 값:", x)

# n = int(input("횟수: "))
# for i in range(n):
#     v = int(input("측정값: "))
#     if v > 80:
#         print("이상 발생")
#         print("가동 횟수:", n)
#         break
#     else:
#         print("정상 상태")
    
#실습 up down 게임
#1~50 중 하나의 숫자를 정답 저장
#사용자 입력값이 정답이 up down인지 출력
#정답이 나오면 정답, 게임 종료되었다 출력
c = 22
m = int(input("1-50 중 하나를 골라:"))
for i in range (1,50):
    if(m < c):
        print("up")
        m = int(input("재입력:"))
    elif(m > c):
        print("down")
        m = int(input("재입력:"))
    else:
        print("정답")
        break
print("종료")

#최댓값 찾기
print("====최댓값====")
first = int(input("1번째 입력값: "))
max_value = first
for i in range(4):
    v = int(input(f"{i+2}번째 입력: "))
    if v > max_value:
        max_value = v
print("최댓값:", max_value)

    #max_value에는 현 시점 최댓값
    #v에는 방금 사용자가 입력한 값

#실습: 플래그로 조건 만족값 검색
print("===플래그실습===")
check = False
first_check = int(input("1번째 입력: "))
max_value2 = first_check
for i in range(4):
    a = int(input(f"{i+2}번째 입력: "))
    if(a > 80):
        check = True
        print("발견")
        break

#조건 맞는 값 출력
temps2 = [23, 32, 30, 22, 29, 35]
for i in temps2:
    if i >= 30:
        print(f"고온: {i}")

#and로 두 조건 만족 값 출력
times = [2, 5, 6, 8, 10, 3, 4]
for t in times:
    if (t >= 5 and t <= 10):
        print(t)

#실습3 조건 맞는 값만 골라 평균 구하기
temps3 = [32, 29, 31, 36, 20, 28]
memory_temps3 = []
temps_sum = 0
temps_count = 0
for v in temps3:
    if(v > 30):
        memory_temps3.append(v)
        temps_sum += v
        temps_count += 1
print(f"({memory_temps3[:]} -> 합{temps_sum}, 개수{temps_count})")
print(f"고온평균: {temps_sum/3}")