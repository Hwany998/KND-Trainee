# set
# 자동 중복 제거
# 순서 없음. (인덱스 불가)
# 형태 중괄호{} 감쌈

# 빈 set 만들기
list_ = []  # 빈 리스트
tuple_ = () # 빈 튜플
print(type(list_), type(tuple_))    #<class 'list'> <class 'tuple'> 자료형
set_ = {}   # 빈 셋
print(type(set_))   #<class 'dict'> dictionary 자료형

# 빈 셋은 무조건 set() 내장함수를 사용
real_set = set()
print(type(real_set))   #<class 'set'> 진짜 set 자료형

#값을 포함한 셋 만들기
logs = ["SS501", "SS502", "SS501", "SS503", "SS502"]
# unique = {logs}     # set에선 리스트를 사용할 수 없어 타입 오류 발생
# print(type(unique)) 
unique_set = set(logs)
print(type(unique_set)) # set 내장 함수를 통해 <class 'set'>으로 출력
print(unique_set)       # 중복값 모두 지워지고 3개만 남고 랜덤하게 위치함
# print(unique_set[0])    # 인덱스 사용 불가로 오류 발생

#set에서 여러값 작성 방법, 
unique = set(["SS501", "SS502", "SS501", "SS503", "SS502"])
unique = {"SS501", "SS502", "SS501", "SS503", "SS502"}  # 이렇게 해도 됨. 알아서 set처리해줌
print(type(unique)) # <class 'set'>
print(unique)   # {중복 제거 후 랜덤한 위치로 01, 02, 03이 출력}
print(len(unique))  # 3 -> 중복 제거 길이기 때문에 3이 출력

#================
#set에 값 추가하기
#set.add(추가할값), 이미 있는 값을 추가할 경우 무시
alerts = {"SS501", "SS502", "SS501", "SS503", "SS502"}
alerts.add("SS505")
print(alerts)   #01, 02, 03, 05 위치 랜덤으로 출력
alerts = sorted(alerts)
print(alerts)   #오름차순으로 정렬된 값 01, 02, 03, 05가 출력
print(type(alerts)) #<class 'list'>, 정렬하자마자 리스트로 자동 형변환 발생

#S01에서 또 경고가 발생
#이미 S01은 경고가 발생한 경우가 있음, alerts라는 셋에서 경고가 발생한 센서만 저장하고 있음
#횟수 상관 없이 이럴 때 set을 쓰면 편리함 (이유: 중복되는 값은 알아서 없애주기 때문, 메모리도 적게 먹음)
#list, tuple과 같이 순서가 존재하는 애들보다 메모리 사용량이 적은건 큰 장점 (데이터 많을 수록 set이 유리)
#================
#in으로 포함 여부 확인 True/False
print('SS501' in alerts)    #True
if "SS501" in alerts:
    print("SS501기기 정비 필요")

# 실습4. 셋으로 중복 제거
# WOR_01 * 4, WOR_06 * 2, WOR_03 * 1, WOR_05 * 1
world_list = ["WOR_01", "WOR_01", "WOR_01", "WOR_01", "WOR_06", "WOR_06", "WOR_03", "WOR_05"]
print(world_list)
world_set = set(world_list)
print(world_set, len(world_set))
world_sorted = sorted(world_set)
print(world_sorted, len(world_sorted))

# union -> 두 라인의 중복없는 합집합 | 기호
# intersection -> 두 라인의 교집합 & 기호
# difference -> 두 라인의 차집합 - 기호로 표현 가능
# 집합 연산
hour_14 = {"WOR_01", "WOR_02", "WOR_06", "WOR_07"}
hour_15 = {"WOR_01", "WOR_08", "WOR_03", "WOR_09", "WOR_06", "WOR_02", "WOR_03", "WOR_05"}
print(hour_14.union(hour_15))   # 순서 랜덤인 중복값 제거된 합집합
print(hour_14)  #union은 원본 셋에 변화X
# | 연산자를 활용해 짧게 작성 가능
print(hour_14 | hour_15)    # union 연산자 |

#교집합
print(hour_14.intersection(hour_15))   # 순서 랜덤인 중복값의 교집합
print(hour_15.intersection(hour_14))   # 이와 동일
print(hour_14 & hour_15)    # intersection 연산자 &

#차집합
print(hour_14.difference(hour_15))   # 순서 랜덤인 차집합
print(hour_15.difference(hour_14))   # 위와 결과값이 다름
print(hour_14 - hour_15)    # difference 연산자 -

#실습5 두 라인의 센서 구성 비교하기
a_set = {'s01', 's03', 's05'}
b_set = {'s03', 's05', 's04'}
print(a_set | b_set) # s01, s03, s04, s05 랜덤성
print(a_set & b_set) # s03, s05 랜덤성
print(a_set - b_set) # s01
print(b_set - a_set) # s04

#실습6 두 시점 이벤트 센서 추적
today_p = {'s01', 's05', 's06'}
yester_p = {'s02', 's03', 's05'}
print(today_p - yester_p)   #s01, s06 difference (차집합)
print(today_p & yester_p)   #s05 intersection (교집합)