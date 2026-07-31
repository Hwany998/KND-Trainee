# =====================================================================
# 종합 실습 2. 실시간 측정값 입력 시스템
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

# 이 실습은 사용자한테 입력받는 거라 미리 주는 데이터 없음
# while로 계속 입력받다가 q 입력하면 종료 > 통계 출력

LIMIT = 100  # 임계값 (100 초과 시 즉시 경고)

# TODO 1. while로 "측정값: " 계속 입력받기, q면 break
#         (입력값은 숫자 아니면 q 라고 가정)
#         값은 리스트에 .append() 로 모으기
temps = []
cover_temps = 0
max_value = 0
min_value = 0
avg_list = 0
big_num = 0

while True:
    x = input("측정값을 입력하세요. 종료하려면 q. ")
    if x != 'q' and x != "":
        temps.append(float(x))
        if int(x) > LIMIT:
            cover_temps += 1
            print(f"측정값: {int(x)}")
            print(f"임계값(100) 초과! 현재까지 초과 {cover_temps}회")
    else:
        if x != "":
            print("측정값: "+ x)
    if x == 'q':
        if len(temps) == 0:
            print("입력된 측정값이 없습니다.")
            break
        else:
            print("q")
            print("-" * 40)
            print(f'총 입력 개수: {len(temps)}개')
            max_value = temps[0]
            min_value = temps[0]
            for i in temps:
                if max_value < i:
                    max_value = i
                if min_value > i:
                    min_value = i
            print(f"최댓값: {max_value} / 최솟값: {min_value}")
            print(f"평균값: {round(sum(temps[:])/len(temps[:]),2)}")
            print(f"임계값 초과 개수: {cover_temps}개")
            avg_list = sum(temps[:])/len(temps[:])
            for i in temps:
                if i > avg_list:
                    big_num += 1
            print(f"평균 초과 개수: {big_num}개")
            temps.sort(reverse=True)
            print(f"상위 3개 값: {temps[:3]}")


# TODO 2. 입력값이 LIMIT 초과하면 즉시 경고 + 지금까지 초과 횟수 출력
# cover_temps = 0
# if int(x) >= LIMIT:
#     cover_temps += 1
#     print("할당량을 채웠습니다. 입력은 유지됩니다.")
#     print(cover_temps)

# TODO 3. q로 끝난 뒤:
#   - 입력값이 하나도 없으면 "입력된 측정값이 없습니다." 출력하고 끝
#   - 값이 있으면 아래 출력
#       · 총 입력 개수 (len)
#       · 최댓값 / 최솟값 (반복문으로 직접 찾기)
#       · 평균값 (round, 소수 둘째 자리)
#       · 임계값 초과 개수
#       · 평균보다 큰 값의 개수  > 평균 먼저 구한 뒤 리스트 다시 돌기
#       · 상위 3개 값 (.sort(reverse=True) 후 슬라이싱 [:3])
# else:
#             print("q")
#             print("-" * 40)
#             print(f'총 입력 개수: {len(temps)}개')
#             max_value = temps[0]
#             min_value = temps[0]
#             for i in temps:
#                 if max_value < i:
#                     max_value = i
#                 if min_value > i:
#                     min_value = i
#             print(f"최댓값: {max_value} / 최솟값: {min_value}")
#             print(f"평균값: {round(sum(temps[:])/len(temps[:]),2)}")
#             print(f"임계값 초과 개수: {cover_temps}개")
#             avg_list = sum(temps[:])/len(temps[:])
#             for i in temps:
#                 if i > avg_list:
#                     big_num += 1
#             print(f"평균 초과 개수: {big_num}개")
#             temps.sort(reverse=True)
#             print(f"상위 3개 값: {temps[:3]}")

# 도전) q 대신 그냥 Enter(빈 입력 "") 치면 무시하고 다시 받기
