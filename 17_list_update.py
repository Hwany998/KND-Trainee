temps = [1,5,2,7,8,2,9,10]
doubled = []

for t in temps:
    doubled.append(t*3)

print(doubled)
#조건에 맞는 값으로 새 리스트 만들기
high = []
low = []
for t in temps:
    if t < 5:
        low.append(t)
    else:
        high.append(t)
print("high:", high)
print("low:", low)

print(low.sort())   #None 출력 -> 반환값이 없어서
# 오름차순 정렬된 배열을 출력하고 싶다면 아래처럼
low.sort()
print(low)

#실습 조건 맞는 새 리스트 
prac_temps = [20, 29, 24, 32, 31, 33, 35]
high_temps = []
for t in prac_temps :
    if(t > 30):
        high_temps.append(t)
print(prac_temps, high_temps)
print(f"개수 {len(high_temps)}")