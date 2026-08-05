# =====================================================================
# 종합 실습 3. 교대조 센서 경고 로그 분석
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

morning = ["TZ_11", "TZ_13", "TZ_11", "TZ_15", "TZ_13", "TZ_11", "TZ_11", "TZ_17"]
afternoon = ["TZ_13", "TZ_15", "TZ_13", "TZ_19", "TZ_15", "TZ_21", "TZ_13", "TZ_15"]

# TODO 1. 오전조 / 오후조 각각 고유 센서 종류 수 + 정렬된 목록 출력
#         (set 으로 중복 제거 > sorted 로 정렬)
set_morning = set(morning)
set_after = set(afternoon)
many_sensors = []
many_tuple = ()
list_tuple = []
triple_list = []

print("=== 교대조 센서 경고 로그 분석 ===")
print(f"오전조 고유 센서 4종: {sorted(set_morning)}")
print(f"오후조 고유 센서 4종: {sorted(set_after)}")
print("-" * 40)

# TODO 2. 교집합 (두 조 모두에서 경고 난 센서) 정렬해서 출력  ( & )
print(f"양 교대조 공통 센서 2종: {set_morning & set_after}")

# TODO 3. 차집합 (오전 전용 / 오후 전용) 각각 정렬해서 출력  ( - )
#         방향에 따라 결과 다른 것 유의
print(f"오전조 전용: {set_morning - set_after}")
print(f"오후조 전용: {set_after - set_morning}")

# TODO 4. 합집합 (전체 경고 센서) 종류 수 + 정렬된 목록 출력  ( | )
print(f"전체 공통 센서 6종: {set_morning | set_after}")
print("-" * 40)

# TODO 5. 센서마다 (오전 횟수 + 오후 횟수) 구해서
#         (횟수, 센서명) 튜플 리스트 만들고 횟수 많은 순 정렬
#         "N위: 센서명 - X회" 형태로 출력
#         힌트) morning.count("TZ_13") / sorted(리스트, reverse=True)
print("경고 발생 횟수 순위: ")
for i in (list(set_morning | set_after)):
    many_tuple = (morning.count(i) + afternoon.count(i), i)
    list_tuple.append(many_tuple)
list1 = sorted(list_tuple, reverse=True)
for idx, (i, j) in enumerate(list1):
    print(f"{idx+1}위: {j} - {i}")
print("-" * 40)

# TODO 6. 가장 경고 많았던 센서 콕 집어서 "우선 점검 필요" 출력
# print(f"최다 경고 센서: {list1[0][1]} ({list1[0][0]}회) → 우선 점검 필요")
for idx, (i, j) in enumerate(list1):
    if idx == 0:
        print(f"최다 경고 센서: {j} ({i}회) → 우선 점검 필요")
        break
# 도전) 총 3회 이상인 센서만 "집중 관리 대상" 리스트로 만들어 정렬 출력
for idx, (i, j) in enumerate(list1):
    if list1[idx][0] >= 3:
        triple_list.append(j)
print(sorted(triple_list))