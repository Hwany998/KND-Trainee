temp = [35, 36, 37, 38]     #int 리스트
float_temps = [36.4, 36.5, 36.6, 36.7]   #float 리스트
str_temps = ["펌프", "압축기", "세절기", "모터"]    #string 리스트
mixed_temps = ["펌프", 78, 36.5, True]    #리스트는 여러 자료형 한 번에 가능
empty = []    #빈 리스트

# 리스트의 자료형
print(f'temp: {temp}')
print(f'type(temp): {type(temp)}')      # <class 'list'>

print(f'temp[0]: {temp[0]}')
print(f'type(temp[0]): {type(temp[0])}')  # <class 'int'>
#이후 flaot, str, mix temp 각각의 타입은 동일

#list 슬라이싱 간격 step [시작:끝:간격]
print(temp[1:3])    # [36, 37] 리스트로 출력
print(temp[1:2])    # [36] 값이 하나라도 리스트로 출력
print(temp[1::2])   # [36, 38] 2간격으로 출력
print(temp[100:999])  # [] 범위 초과 시 빈 리스트 출력

#in 존재 확인 (주의점: .이나 ()없이 순수 in 키워드 사용)
print("펌프" in str_temps)      #True
print("펌프" not in str_temps)  #Fals  

#append(추가할값)로 리스트 끝에 값 추가

#insert(위치, 값)으로 지정 위치에 끼워 넣고 뒤 값 밀림
temps3 = [23, 26, 27, 25]
print(temps3.insert(0, 222))   #None 반환값이 없어서 일단 변수에 할당하는게 첫번째
temps3.insert(2, 38)
print(temps3)   #[23, 26, 38, 27, 25] 2번 인덱스에 38 삽입

#append 겸 얉은 복사 개념
nums = [1,2,3,4,5]
print(nums.append(222))   #None 반환값이 없어서 일단 변수에 할당하는게 첫번째
nums.append(222)
new_num = nums  #얉은 복사 - nums와 공유하는 것으로 C언어의 포인터와 비슷함
new_num.append(111)
print(nums)     #[1, 2, 3, 4, 5, 222, 111]  #nums와 new_num은 같은 리스트를 참조
print(new_num)  #[1, 2, 3, 4, 5, 222, 111]  #new_num에 append하면 nums도 같이 변경

#깊은 복사 - copy() 사용
new_num2 = nums.copy()  #깊은 복사 - nums와 주소 공유하지 않음
new_num2.append(333)
print(nums)     #[1, 2, 3, 4, 5, 222, 111]  #nums와 new_num은 같은 리스트를 참조
print(new_num2)  #[1, 2, 3, 4, 5, 222, 111, 333]  #new_num에 append하면 nums도 같이 변경

#extend(리스트) 리스트 연결
data = [1,2,3]
data2 = [4,5,6]
print(data.extend(data2))   #None 반환값이 없어서 일단 변수에 할당하는게 첫번째
data.extend(data2)
print(data)

#remove() - 제거 / 위치모르고 값만 알 때 사용하는 요소 삭제 / 값 없으면 오류
list1 = [1,2,3,4,5,6]
list1.remove(5)   #값으로 제거
print(list1)    #[1, 2, 3, 4, 6]  #5 제거

#pop - 위치로 꺼내며 제거 / 인덱스 넘기면 오류
print(list1.pop(2)) #3 출력 -> 제거한 3번 인덱스의 값을 출력
print(list1)     #[1, 2, 4, 6]  #2번 인덱스 제거

#del - 인덱스로 삭제, 값을 돌려주지 않음 / 인덱스 넘기면 오류
del list1[:]
print(list1)    #[] #[:]로 전체 삭제

#del - 건너뛰기 / 인덱스 넘기면 오류
list2 = ["빨강", "노랑", "초록", "파랑", "남색", "보랑"]
del list2[::2]
print(list2)    #['노랑', '파랑', '보람']  #0,2,4번 인덱스 제거

#reverse - 순서 뒤집기 (리스트 뒤집기)
#sort - 오른차순 정렬 
n = [ 4, 5, 9, 1, 3, 6, 2]
n.sort()
print("오름차순 결과: ", n)
n.sort(reverse=True)
print("내림차순 결과: ", n)

f = ["텀블러", "일회용컵", "일회용컵", "텀블러", "텀블러", "일회용컵"]
print(f.count("일회용컵"))
print(f)

#특정 값의 위치 찾기 .index(위치를찾을값)
print(f.index("일회용컵"))