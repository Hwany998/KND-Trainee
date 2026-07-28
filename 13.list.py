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

#append()로 리스트 끝에 값 추가